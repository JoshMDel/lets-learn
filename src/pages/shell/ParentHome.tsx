import { useQuery } from '@tanstack/react-query'
import { Link, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { Card } from '../../components/ui/Card'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { signOut } from '../../lib/authApi'
import type { ChildProfile } from '../../types/content'

export default function ParentHome() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const { session } = useAuth()

  const { data: children, isLoading } = useQuery({
    queryKey: ['myChildren', session?.user.id],
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

  async function handleLogout() {
    await signOut()
    navigate('/', { replace: true })
  }

  return (
    <ShellLayout
      narrow={false}
      headerRight={
        <Button variant="ghost" onClick={handleLogout}>
          {t('nav.logout')}
        </Button>
      }
    >
      <div className="flex items-center justify-between">
        <h1 className="font-heading text-3xl font-bold">{t('parent.dashboard.title')}</h1>
        <Link to="/parent/profile" className="text-sm font-semibold text-primary">
          {t('parent.dashboard.profile')}
        </Link>
      </div>

      {isLoading ? (
        <p className="mt-8 text-muted">{t('common.loading')}</p>
      ) : (children ?? []).length === 0 ? (
        <p className="mt-8 text-muted">{t('parent.dashboard.empty')}</p>
      ) : (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {children!.map((child) => (
            <Card key={child.id} className="flex flex-col gap-3">
              <div>
                <div className="font-heading text-lg font-bold">{child.display_name}</div>
                <div className="text-sm text-muted">Grade {child.grade} · @{child.username}</div>
              </div>
              <Link
                to={`/parent/child/${child.id}`}
                className="rounded-full bg-primary/10 px-4 py-2 text-center text-sm font-semibold text-primary hover:bg-primary/20"
              >
                {t('parent.dashboard.viewChild')}
              </Link>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-8 flex flex-wrap gap-3">
        <Button onClick={() => navigate('/parent/add-child')}>
          + {t('parent.dashboard.addChild')}
        </Button>
        <Button variant="secondary" onClick={() => navigate('/switch-profile')}>
          {t('switchProfile.title')}
        </Button>
      </div>
    </ShellLayout>
  )
}
