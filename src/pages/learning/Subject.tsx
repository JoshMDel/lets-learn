import { useParams, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { LearningLayout } from '../../components/LearningLayout'
import { LumiSays } from '../../components/Lumi'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { useTopics } from '../../content/queries'
import { useRecordActivity } from '../../content/activity'
import { supabase } from '../../lib/supabaseClient'

export default function Subject() {
  const { t, locale } = useLocale()
  const navigate = useNavigate()
  const { subjectId } = useParams<{ subjectId: string }>()
  const { activeChildId } = useAuth()

  // Opening a subject is a genuine subject interaction (unlike just loading
  // the home dashboard) -- protects the daily reward-decay requirement.
  useRecordActivity(activeChildId)

  const { data: topics, isLoading } = useTopics(subjectId ?? null)

  const topicIds = (topics ?? []).map((tp) => tp.id)
  const { data: progressByTopic } = useQuery({
    queryKey: ['topicProgress', activeChildId, topicIds],
    enabled: !!activeChildId && topicIds.length > 0,
    queryFn: async () => {
      const { data: tiers, error: tErr } = await supabase
        .from('tiers')
        .select('id, topic_id, tier_number')
        .in('topic_id', topicIds)
      if (tErr) throw tErr

      const tierIds = (tiers ?? []).map((t) => t.id)
      const { data: progress, error: pErr } =
        tierIds.length > 0
          ? await supabase
              .from('child_tier_progress')
              .select('tier_id, mastered')
              .eq('child_id', activeChildId as string)
              .in('tier_id', tierIds)
          : { data: [], error: null }
      if (pErr) throw pErr

      const maxTier = new Map<string, number>()
      for (const tier of tiers ?? []) {
        maxTier.set(tier.topic_id, Math.max(maxTier.get(tier.topic_id) ?? 0, tier.tier_number))
      }
      const masteredTierIds = new Set((progress ?? []).filter((p) => p.mastered).map((p) => p.tier_id))
      const tierById = new Map((tiers ?? []).map((tr) => [tr.id, tr]))

      const complete = new Set<string>()
      const started = new Set<string>()
      for (const tierId of masteredTierIds) {
        const tier = tierById.get(tierId)
        if (!tier) continue
        started.add(tier.topic_id)
        if (tier.tier_number === maxTier.get(tier.topic_id)) complete.add(tier.topic_id)
      }
      return { complete, started }
    },
  })

  const allDone =
    (topics ?? []).length > 0 && (topics ?? []).every((tp) => progressByTopic?.complete.has(tp.id))

  return (
    <LearningLayout>
      <h1 className="mb-4 font-heading text-2xl font-bold">{t('learning.topics')}</h1>

      {!isLoading && (topics ?? []).length > 0 && (
        <LumiSays
          pose={allDone ? 'celebrating' : 'reading'}
          size={allDone ? 72 : 64}
          animation={allDone ? 'bounce' : undefined}
          className="mb-5"
        >
          {allDone ? t('lumi.subject.allDone') : t('lumi.subject.intro')}
        </LumiSays>
      )}

      {isLoading ? (
        <p className="text-muted">{t('common.loading')}</p>
      ) : (topics ?? []).length === 0 ? (
        <LumiSays pose="emptyState" size={112}>
          {t('lumi.empty.activities')}
        </LumiSays>
      ) : (
        <div className="flex flex-col gap-3">
          {(topics ?? []).map((topic) => {
            const isComplete = progressByTopic?.complete.has(topic.id)
            const isStarted = progressByTopic?.started.has(topic.id)
            return (
              <button
                key={topic.id}
                onClick={() => navigate(`/topic/${topic.id}`)}
                className="flex items-center justify-between rounded-[var(--radius-lg)] border border-subtle bg-surface p-5 text-left transition-colors hover:border-primary"
              >
                <span className="font-heading font-semibold">
                  {locale === 'af' ? topic.name_af : topic.name_en}
                </span>
                {isComplete ? (
                  <span className="text-2xl" aria-label={t('learning.topicComplete')}>
                    🏆
                  </span>
                ) : isStarted ? (
                  <span className="text-2xl" aria-hidden>
                    ⭐
                  </span>
                ) : (
                  <span className="text-muted">→</span>
                )}
              </button>
            )
          })}
        </div>
      )}
    </LearningLayout>
  )
}
