import { useLocation, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { LearningLayout } from '../../components/LearningLayout'
import { Button } from '../../components/ui/Button'
import { moodFromPerformance } from '../../components/Mascot'
import { useLocale } from '../../i18n/LocaleContext'
import { supabase } from '../../lib/supabaseClient'
import type { SubmitAttemptResult } from '../../types/content'

interface ResultsState {
  result: SubmitAttemptResult
  tierId: string
}

export default function Results() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const location = useLocation()
  const state = location.state as ResultsState | null

  const { data: nextTier } = useQuery({
    queryKey: ['nextTier', state?.tierId],
    enabled: !!state?.result.passed && !!state?.tierId,
    queryFn: async () => {
      const { data: tier, error } = await supabase
        .from('tiers')
        .select('id, topic_id, tier_number')
        .eq('id', state!.tierId)
        .single()
      if (error) throw error
      const { data: next } = await supabase
        .from('tiers')
        .select('id')
        .eq('topic_id', tier.topic_id)
        .eq('tier_number', tier.tier_number + 1)
        .maybeSingle()
      return next?.id ?? null
    },
  })

  if (!state) {
    return (
      <LearningLayout>
        <p className="text-muted">{t('common.error.generic')}</p>
        <Button className="mt-4" onClick={() => navigate('/home')}>
          {t('nav.exitHome')}
        </Button>
      </LearningLayout>
    )
  }

  const { result, tierId } = state
  const mood = moodFromPerformance({
    justMastered: result.passed,
    recentAccuracy: result.correct_count / result.total,
  })

  return (
    <LearningLayout mood={mood}>
      <div className="mb-8 text-center">
        <h1 className="font-heading text-3xl font-bold">{t('results.title')}</h1>
        <p className="mt-2 text-lg text-muted">
          {t('results.score', { correct: result.correct_count, total: result.total })}
        </p>
        <p className={`mt-3 font-heading text-xl font-semibold ${result.passed ? 'text-success' : 'text-primary'}`}>
          {result.passed ? `🎉 ${t('results.passed')}` : t('results.tryAgain')}
        </p>
      </div>

      <div className="flex flex-col gap-4">
        {result.results.map((r, i) => (
          <div
            key={r.question_id}
            className={`rounded-[var(--radius-lg)] border-2 p-5 ${
              r.is_correct ? 'border-success/40 bg-success/5' : 'border-danger/40 bg-danger/5'
            }`}
          >
            <div className="mb-2 flex items-center gap-2 font-heading font-semibold">
              <span aria-hidden>{r.is_correct ? '✅' : '❌'}</span>
              <span>{t('quiz.question', { current: i + 1, total: result.total })}</span>
            </div>
            {!r.is_correct && (
              <p className="mb-1 text-sm">
                <span className="font-semibold">{t('results.correctAnswer')}: </span>
                {r.correct_option.option_text}
              </p>
            )}
            <p className="mb-2 text-sm">
              <span className="font-semibold">{t('results.why')}: </span>
              {r.misconception_note ?? r.explanation}
            </p>
            {r.supporting_sentences.length > 0 && (
              <p className="rounded-lg bg-surface-2 p-3 text-sm italic text-ink">
                <span className="mr-1 font-semibold not-italic">{t('results.fromThePassage')}:</span>
                "{r.supporting_sentences.map((s) => s.text).join(' ')}"
              </p>
            )}
          </div>
        ))}
      </div>

      <div className="mt-8 flex flex-col gap-3">
        {result.passed ? (
          nextTier ? (
            <Button fullWidth onClick={() => navigate(`/read/${nextTier}`)}>
              {t('learning.nextTier')}
            </Button>
          ) : (
            <Button fullWidth onClick={() => navigate('/home')}>
              🏆 {t('learning.topicComplete')}
            </Button>
          )
        ) : (
          <>
            <Button fullWidth onClick={() => navigate(`/quiz/${tierId}`)}>
              {t('results.retryNow')}
            </Button>
            <Button variant="secondary" fullWidth onClick={() => navigate(`/read/${tierId}`)}>
              {t('learning.continueReading')}
            </Button>
          </>
        )}
        <Button variant="ghost" fullWidth onClick={() => navigate('/home')}>
          {t('nav.exitHome')}
        </Button>
      </div>
    </LearningLayout>
  )
}
