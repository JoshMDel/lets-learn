import { useQuery } from '@tanstack/react-query'
import { Navigate, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { signOut } from '../../lib/authApi'
import { avatarForId, AVATAR_EMOJI } from '../../lib/avatar'
import type { ChildProfile, ChildState } from '../../types/content'

export default function SwitchProfile() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const { session, role, loading, setActiveChildId } = useAuth()

  const { data: children, isLoading } = useQuery({
    queryKey: ['myChildren', session?.user.id],
    enabled: role === 'parent',
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_profiles')
        .select('*')
        .eq('parent_id', session!.user.id)
        .order('created_at')
      if (error) throw error
      return data as ChildProfile[]
    },
  })

  const childIds = (children ?? []).map((c) => c.id)
  const { data: avatarByChild } = useQuery({
    queryKey: ['childAvatars', childIds],
    enabled: childIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_state')
        .select('child_id, avatar_key')
        .in('child_id', childIds)
      if (error) throw error
      return new Map((data as Pick<ChildState, 'child_id' | 'avatar_key'>[]).map((s) => [s.child_id, s.avatar_key]))
    },
  })

  if (loading) return null
  if (!session) return <Navigate to="/" replace />
  if (role === 'child') return <Navigate to="/home" replace />

  function chooseChild(id: string) {
    setActiveChildId(id)
    navigate('/home')
  }

  async function handleLogout() {
    await signOut()
    navigate('/', { replace: true })
  }

  return (
    <ShellLayout
      headerRight={
        <Button variant="ghost" onClick={handleLogout}>
          {t('nav.logout')}
        </Button>
      }
    >
      <h1 className="font-heading text-3xl font-bold">{t('switchProfile.title')}</h1>

      {isLoading ? (
        <p className="mt-8 text-muted">{t('common.loading')}</p>
      ) : (
        <div className="mt-8 grid grid-cols-2 gap-4 sm:grid-cols-3">
          {(children ?? []).map((child) => (
            <button
              key={child.id}
              onClick={() => chooseChild(child.id)}
              className="flex flex-col items-center gap-2 rounded-[var(--radius-lg)] border border-subtle bg-surface p-5 transition-colors hover:border-primary"
            >
              <span className="text-4xl">
                {AVATAR_EMOJI.includes(avatarByChild?.get(child.id) ?? '')
                  ? avatarByChild!.get(child.id)
                  : avatarForId(child.id)}
              </span>
              <span className="font-heading font-semibold">{child.display_name}</span>
              <span className="text-xs text-muted">Grade {child.grade}</span>
            </button>
          ))}
        </div>
      )}

      <div className="mt-8 flex flex-col gap-3">
        <Button variant="secondary" onClick={() => navigate('/parent/add-child')} fullWidth>
          + {t('switchProfile.addChild')}
        </Button>
        <Button variant="ghost" onClick={() => navigate('/parent-gate')} fullWidth>
          🔒 {t('switchProfile.parentTools')}
        </Button>
      </div>
    </ShellLayout>
  )
}
