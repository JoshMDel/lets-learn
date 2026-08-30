import {
  createContext,
  useContext,
  useEffect,
  useState,
  useCallback,
  useRef,
  type ReactNode,
} from 'react'
import type { Session } from '@supabase/supabase-js'
import { supabase } from '../lib/supabaseClient'
import type { ChildProfile, Profile } from '../types/content'

type Role = 'parent' | 'child' | null

const ACTIVE_CHILD_KEY = 'lets-learn-active-child'

interface AuthContextValue {
  session: Session | null
  loading: boolean
  role: Role
  profile: Profile | null
  /** Set only when the signed-in Auth session itself belongs to a child. */
  selfChild: ChildProfile | null
  /** The child currently being played as -- either `selfChild`, or one of a
   *  signed-in parent's children after they tap an avatar to hand over the
   *  device. */
  activeChildId: string | null
  setActiveChildId: (id: string | null) => void
  /** Unlocked only for this in-memory session -- always re-locks on reload,
   *  by design (this gates real account/usage data, not a toy gate). */
  parentToolsUnlocked: boolean
  unlockParentTools: () => void
  lockParentTools: () => void
  refreshProfile: () => Promise<void>
  /** Logs a learner out of the app. A child logged in with their own
   * username/password gets a real sign-out (their auth session ends
   * entirely). A child being played by a parent who tapped their avatar
   * just has that hand-off cleared -- the parent's own session is left
   * alone, since they're still the one physically holding the device. */
  logoutLearner: () => Promise<void>
}

const AuthContext = createContext<AuthContextValue | null>(null)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [session, setSession] = useState<Session | null>(null)
  const [loading, setLoading] = useState(true)
  const [role, setRole] = useState<Role>(null)
  const [profile, setProfile] = useState<Profile | null>(null)
  const [selfChild, setSelfChild] = useState<ChildProfile | null>(null)
  const [activeChildId, setActiveChildIdState] = useState<string | null>(() =>
    typeof window === 'undefined' ? null : window.localStorage.getItem(ACTIVE_CHILD_KEY),
  )
  const [parentToolsUnlocked, setParentToolsUnlocked] = useState(false)

  const setActiveChildId = useCallback((id: string | null) => {
    setActiveChildIdState(id)
    if (id) window.localStorage.setItem(ACTIVE_CHILD_KEY, id)
    else window.localStorage.removeItem(ACTIVE_CHILD_KEY)
  }, [])

  const loadRoleForSession = useCallback(async (s: Session | null) => {
    if (!s) {
      setRole(null)
      setProfile(null)
      setSelfChild(null)
      return
    }
    const { data: parentProfile } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', s.user.id)
      .maybeSingle()

    if (parentProfile) {
      setRole('parent')
      setProfile(parentProfile as Profile)
      setSelfChild(null)
      return
    }

    const { data: childRow } = await supabase
      .from('child_profiles')
      .select('*')
      .eq('auth_user_id', s.user.id)
      .maybeSingle()

    if (childRow) {
      setRole('child')
      setProfile(null)
      setSelfChild(childRow as ChildProfile)
      setActiveChildId((childRow as ChildProfile).id)
    } else {
      setRole(null)
      setProfile(null)
      setSelfChild(null)
    }
  }, [setActiveChildId])

  const refreshProfile = useCallback(async () => {
    await loadRoleForSession(session)
  }, [loadRoleForSession, session])

  // Tracks whose session this is, so the re-auth on /parent-gate (which
  // itself calls signInWithPassword and so fires this same listener again)
  // doesn't immediately re-lock the parent tools it just unlocked -- only a
  // genuine change of user (a real logout, or a different account signing
  // in) should reset that gate.
  const currentUserIdRef = useRef<string | null>(null)

  useEffect(() => {
    let mounted = true
    supabase.auth.getSession().then(async ({ data }) => {
      if (!mounted) return
      currentUserIdRef.current = data.session?.user.id ?? null
      setSession(data.session)
      await loadRoleForSession(data.session)
      setLoading(false)
    })

    const { data: sub } = supabase.auth.onAuthStateChange(async (_event, newSession) => {
      const newUserId = newSession?.user.id ?? null
      if (newUserId !== currentUserIdRef.current) {
        setParentToolsUnlocked(false)
      }
      currentUserIdRef.current = newUserId
      setSession(newSession)
      await loadRoleForSession(newSession)
    })

    return () => {
      mounted = false
      sub.subscription.unsubscribe()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const unlockParentTools = useCallback(() => setParentToolsUnlocked(true), [])
  const lockParentTools = useCallback(() => setParentToolsUnlocked(false), [])

  const logoutLearner = useCallback(async () => {
    if (role === 'child') {
      // The auth session itself IS this child's -- end it for real so a
      // back-button press can't land on a still-authenticated dashboard.
      await supabase.auth.signOut()
    }
    // Either way, clear which child is "active" on this device.
    setActiveChildId(null)
  }, [role, setActiveChildId])

  return (
    <AuthContext.Provider
      value={{
        session,
        loading,
        role,
        profile,
        selfChild,
        activeChildId,
        setActiveChildId,
        parentToolsUnlocked,
        unlockParentTools,
        lockParentTools,
        refreshProfile,
        logoutLearner,
      }}
    >
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
