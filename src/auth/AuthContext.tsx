import {
  createContext,
  useContext,
  useEffect,
  useState,
  useCallback,
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

  useEffect(() => {
    let mounted = true
    supabase.auth.getSession().then(async ({ data }) => {
      if (!mounted) return
      setSession(data.session)
      await loadRoleForSession(data.session)
      setLoading(false)
    })

    const { data: sub } = supabase.auth.onAuthStateChange(async (_event, newSession) => {
      setSession(newSession)
      setParentToolsUnlocked(false)
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
