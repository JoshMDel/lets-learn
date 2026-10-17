import { useQuery } from '@tanstack/react-query'
import { Link, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { Card } from '../../components/ui/Card'
import { LumiSays } from '../../components/Lumi'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { signOut } from '../../lib/authApi'
import { useUnreadCount } from '../../content/chat'
import { formatRands } from '../../lib/currency'
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

  const childIds = (children ?? []).map((c) => c.id)
  // Same v_child_reward_summary view every reward display reads from --
  // never a page-local sum/count over raw reward_transactions rows.
  const { data: rewardsByChild } = useQuery({
    queryKey: ['rewardsByChild', childIds],
    enabled: childIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('v_child_reward_summary')
        .select('child_id, balance, tasks_passed')
        .in('child_id', childIds)
      if (error) throw error
      const map = new Map<string, { total: number; count: number }>()
      for (const row of data ?? []) {
        map.set(row.child_id, { total: Number(row.balance), count: row.tasks_passed })
      }
      return map
    },
  })

  const { data: conversationIds } = useQuery({
    queryKey: ['myChildrenConversationIds', childIds],
    enabled: childIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase.from('conversations').select('id').in('child_id', childIds)
      if (error) throw error
      return (data ?? []).map((c) => c.id)
    },
  })
  const unreadChat = useUnreadCount(session?.user.id ?? null, conversationIds ?? [])

  async function handleLogout() {
    await signOut()
    navigate('/', { replace: true })
  }

  return (
    <ShellLayout
      narrow={false}
      bottomNav={{ active: 'home', unreadChat: unreadChat > 0 }}
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
        <Card className="mt-8">
          <LumiSays pose="emptyState" size={120}>
            <span className="block font-semibold">{t('lumi.parent.noLearners')}</span>
            <span className="mt-0.5 block text-muted">{t('parent.dashboard.empty')}</span>
          </LumiSays>
        </Card>
      ) : (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {children!.map((child) => {
            const reward = rewardsByChild?.get(child.id)
            return (
            <Card key={child.id} className="flex flex-col gap-3">
              <div>
                <div className="font-heading text-lg font-bold">{child.display_name}</div>
                <div className="text-sm text-muted">Grade {child.grade} · @{child.username}</div>
              </div>
              <div className="flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1.5 text-sm">
                <span aria-hidden>🏆</span>
                <span className="font-heading font-semibold text-primary">
                  {formatRands(reward?.total ?? 0)}
                </span>
                <span className="text-muted">
                  · {t('rewards.testsPassedCount', { count: reward?.count ?? 0 })}
                </span>
              </div>
              <Link
                to={`/parent/child/${child.id}`}
                className="rounded-full bg-primary/10 px-4 py-2 text-center text-sm font-semibold text-primary hover:bg-primary/20"
              >
                {t('parent.dashboard.viewChild')}
              </Link>
            </Card>
            )
          })}
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
