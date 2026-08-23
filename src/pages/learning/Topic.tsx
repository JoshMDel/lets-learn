import { useParams, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { LearningLayout } from '../../components/LearningLayout'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { useTiers, useChildProgress } from '../../content/queries'
import { supabase } from '../../lib/supabaseClient'
import type { Topic as TopicRow } from '../../types/content'

export default function Topic() {
  const { t, locale } = useLocale()
  const navigate = useNavigate()
  const { topicId } = useParams<{ topicId: string }>()
  const { activeChildId } = useAuth()

  const { data: topic } = useQuery({
    queryKey: ['topic', topicId],
    enabled: !!topicId,
    queryFn: async () => {
      const { data, error } = await supabase.from('topics').select('*').eq('id', topicId as string).single()
      if (error) throw error
      return data as TopicRow
    },
  })

  const { data: tiers, isLoading } = useTiers(topicId ?? null)
  const tierIds = (tiers ?? []).map((tr) => tr.id)
  const { data: progress } = useChildProgress(activeChildId, tierIds)

  const progressByTier = new Map((progress ?? []).map((p) => [p.tier_id, p]))
  const topicName = topic ? (locale === 'af' ? topic.name_af : topic.name_en) : ''

  return (
    <LearningLayout title={topicName}>
      <h1 className="mb-6 font-heading text-2xl font-bold">{topicName || t('learning.topics')}</h1>

      {isLoading ? (
        <p className="text-muted">{t('common.loading')}</p>
      ) : (
        <div className="flex flex-col gap-3">
          {(tiers ?? []).map((tier, i) => {
            const prevMastered = i === 0 || progressByTier.get((tiers ?? [])[i - 1].id)?.mastered
            const mastered = progressByTier.get(tier.id)?.mastered
            const locked = !prevMastered
            return (
              <button
                key={tier.id}
                disabled={locked}
                onClick={() => navigate(`/read/${tier.id}`)}
                className={`flex items-center justify-between rounded-[var(--radius-lg)] border p-5 text-left transition-colors ${
                  locked
                    ? 'cursor-not-allowed border-subtle bg-surface-2 opacity-60'
                    : 'border-subtle bg-surface hover:border-primary'
                }`}
              >
                <div>
                  <div className="font-heading font-semibold">
                    {t('learning.tier')} {tier.tier_number}: {tier.label}
                  </div>
                  {mastered && <div className="text-sm text-success">{t('learning.mastered')}</div>}
                </div>
                <span className="text-2xl" aria-hidden>
                  {locked ? '🔒' : mastered ? '🏆' : '▶'}
                </span>
              </button>
            )
          })}
        </div>
      )}
    </LearningLayout>
  )
}
