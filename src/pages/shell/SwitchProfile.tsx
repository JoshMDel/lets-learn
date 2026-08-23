import { useQuery } from '@tanstack/react-query'
import { Navigate, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import type { ChildProfile } from '../../types/content'

const AVATAR_EMOJI = ['🦊', '🐸', '🐼', '🦁', '🐨', '🦉', '🐙', '🦄']
function avatarFor(id: string) {
  let hash = 0
  for (const c of id) hash = (hash * 31 + c.charCodeAt(0)) % AVATAR_EMOJI.length
  return AVATAR_EMOJI[Math.abs(hash) % AVATAR_EMOJI.length]
}

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

  if (loading) return null
  if (!session) return <Navigate to="/" replace />
  if (role === 'child') return <Navigate to="/home" replace />

  function chooseChild(id: string) {
    setActiveChildId(id)
    navigate('/home')
  }

  return (
    <ShellLayout>
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
              <span className="text-4xl">{avatarFor(child.id)}</span>
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
