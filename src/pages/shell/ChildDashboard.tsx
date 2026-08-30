import { useParams, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { ShellLayout } from '../../components/ShellLayout'
import { Card } from '../../components/ui/Card'
import { useLocale } from '../../i18n/LocaleContext'
import { supabase } from '../../lib/supabaseClient'
import { useChildDashboard } from '../../content/dashboard'
import { formatRands } from '../../lib/currency'
import type { ChildProfile } from '../../types/content'

function StatCard({ label, value }: { label: string; value: string | number }) {
  return (
    <Card className="text-center">
      <div className="font-heading text-3xl font-bold text-primary">{value}</div>
      <div className="mt-1 text-sm text-muted">{label}</div>
    </Card>
  )
}

export default function ChildDashboard() {
  const { t } = useLocale()
  const { childId } = useParams<{ childId: string }>()

  const { data: child } = useQuery({
    queryKey: ['child', childId],
    enabled: !!childId,
    queryFn: async () => {
      const { data, error } = await supabase.from('child_profiles').select('*').eq('id', childId).single()
      if (error) throw error
      return data as ChildProfile
    },
  })

  const { data: stats, isLoading } = useChildDashboard(childId ?? null)

  return (
    <ShellLayout narrow={false}>
      <Link to="/parent" className="text-sm font-semibold text-primary">
        ← {t('parent.dashboard.title')}
      </Link>
      <h1 className="mt-2 font-heading text-3xl font-bold">
        {child ? `${child.display_name} · Grade ${child.grade}` : '…'}
      </h1>

      {isLoading || !stats ? (
        <p className="mt-8 text-muted">{t('common.loading')}</p>
      ) : (
        <>
          <div className="mt-8 grid grid-cols-3 gap-4">
            <StatCard label={t('parent.child.attempts')} value={stats.totalAttempts} />
            <StatCard
              label={t('parent.child.avgScore')}
              value={stats.averageScore != null ? `${stats.averageScore}%` : '—'}
            />
            <StatCard label={t('parent.child.topicsMastered')} value={stats.topicsMastered} />
          </div>

          <div className="mt-4 grid grid-cols-2 gap-4">
            <StatCard label={t('rewards.testsPassedLabel')} value={stats.rewardTestsPassed} />
            <StatCard label={t('rewards.rewardEarnedLabel')} value={formatRands(stats.rewardTotal)} />
          </div>
          <p className="mt-2 text-center text-xs text-muted">{t('rewards.explainer')}</p>

          <Card className="mt-6">
            <h2 className="font-heading text-lg font-bold">{t('rewards.rewardHistoryTitle')}</h2>
            {stats.rewardHistory.length === 0 ? (
              <p className="mt-3 text-sm text-muted">{t('rewards.history.empty')}</p>
            ) : (
              <div className="mt-4 overflow-x-auto">
                <table className="w-full min-w-[420px] text-left text-sm">
                  <thead>
                    <tr className="text-muted">
                      <th className="pb-2 font-medium">{t('rewards.history.date')}</th>
                      <th className="pb-2 font-medium">{t('rewards.history.achievement')}</th>
                      <th className="pb-2 font-medium">{t('rewards.history.score')}</th>
                      <th className="pb-2 text-right font-medium">{t('rewards.history.reward')}</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-subtle">
                    {stats.rewardHistory.map((r) => (
                      <tr key={r.id}>
                        <td className="py-2 text-muted">{new Date(r.date).toLocaleDateString()}</td>
                        <td className="py-2 font-medium">{r.topic_name}</td>
                        <td className="py-2 text-muted">{r.score_pct}%</td>
                        <td className="py-2 text-right font-heading font-semibold text-success">
                          +{formatRands(r.amount)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </Card>

          <Card className="mt-6">
            <h2 className="font-heading text-lg font-bold">{t('parent.child.skillBreakdown')}</h2>
            <div className="mt-4 flex flex-col gap-3">
              {stats.skillAccuracy.map(({ skill, correct, total }) => {
                const pct = total > 0 ? Math.round((correct / total) * 100) : null
                return (
                  <div key={skill}>
                    <div className="mb-1 flex justify-between text-sm">
                      <span className="font-medium">{t(`skill.${skill}`)}</span>
                      <span className="text-muted">{pct != null ? `${pct}% (${correct}/${total})` : '—'}</span>
                    </div>
                    <div className="h-2.5 overflow-hidden rounded-full bg-surface-2">
                      <div
                        className="h-full rounded-full bg-primary transition-all"
                        style={{ width: `${pct ?? 0}%` }}
                      />
                    </div>
                  </div>
                )
              })}
            </div>
          </Card>

          <Card className="mt-6">
            <h2 className="font-heading text-lg font-bold">{t('parent.child.recentAttempts')}</h2>
            {stats.recentAttempts.length === 0 ? (
              <p className="mt-3 text-sm text-muted">{t('parent.child.noAttempts')}</p>
            ) : (
              <div className="mt-4 flex flex-col divide-y divide-subtle">
                {stats.recentAttempts.map((a) => (
                  <div key={a.id} className="flex items-center justify-between py-3 text-sm">
                    <div>
                      <div className="font-medium">
                        {a.subject_name} · {a.topic_name}
                      </div>
                      <div className="text-muted">
                        {t('learning.tier')} {a.tier_number} ·{' '}
                        {a.completed_at ? new Date(a.completed_at).toLocaleDateString() : ''}
                      </div>
                    </div>
                    <span
                      className={`rounded-full px-3 py-1 font-heading font-semibold ${
                        a.passed ? 'bg-success/15 text-success' : 'bg-surface-2 text-muted'
                      }`}
                    >
                      {a.score_pct}%
                    </span>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </>
      )}
    </ShellLayout>
  )
}
