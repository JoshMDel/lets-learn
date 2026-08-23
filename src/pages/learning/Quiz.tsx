import { useEffect, useMemo, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { LearningLayout } from '../../components/LearningLayout'
import { Button } from '../../components/ui/Button'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { useQuizPool, useRecentMissedQuestionIds } from '../../content/queries'
import { selectQuizQuestions } from '../../quiz/selectQuizQuestions'
import { setResumeState } from '../../content/resume'
import { supabase } from '../../lib/supabaseClient'
import type { QuizOption, SubmitAttemptResult } from '../../types/content'

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

export default function Quiz() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const { tierId } = useParams<{ tierId: string }>()
  const { activeChildId } = useAuth()

  const { data: pool, isLoading: poolLoading } = useQuizPool(tierId ?? null)
  const { data: missed, isLoading: missedLoading } = useRecentMissedQuestionIds(
    activeChildId,
    tierId ?? null,
  )

  const ready = !poolLoading && !missedLoading && pool && missed !== undefined

  const questions = useMemo(() => {
    if (!ready || !pool) return []
    return selectQuizQuestions(pool.questions, missed ?? [])
    // Only recompute when the underlying data actually changes, not on
    // every render -- this is the set the child answers for this attempt.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ready])

  // Options must be shuffled per attempt too -- otherwise the correct answer
  // sits in the same authored position (usually first) every single time,
  // which a child would learn as a pattern instead of actually reading.
  const optionsByQuestion = useMemo(() => {
    if (!pool) return new Map<string, QuizOption[]>()
    const map = new Map<string, QuizOption[]>()
    for (const q of questions) {
      map.set(
        q.id,
        shuffle(pool.options.filter((o) => o.question_id === q.id)),
      )
    }
    return map
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [questions])

  const [index, setIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<string, string>>({})
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (activeChildId && tierId) {
      setResumeState(activeChildId, { tier_id: tierId, stage: 'quiz' })
    }
  }, [activeChildId, tierId])

  if (!ready || questions.length === 0) {
    return (
      <LearningLayout>
        <p className="text-muted">{t('common.loading')}</p>
      </LearningLayout>
    )
  }

  const current = questions[index]
  const options = optionsByQuestion.get(current.id) ?? []
  const selected = answers[current.id]
  const isLast = index === questions.length - 1
  const allAnswered = questions.every((q) => answers[q.id])

  function selectOption(optionId: string) {
    setAnswers((prev) => ({ ...prev, [current.id]: optionId }))
  }

  async function handleFinish() {
    if (!activeChildId || !tierId) return
    setSubmitting(true)
    setError('')
    try {
      const payload = questions.map((q) => ({ question_id: q.id, option_id: answers[q.id] }))
      const { data, error: rpcError } = await supabase.rpc('submit_attempt', {
        p_child_id: activeChildId,
        p_tier_id: tierId,
        p_answers: payload,
      })
      if (rpcError) throw rpcError
      await setResumeState(activeChildId, null)
      navigate(`/results/${(data as SubmitAttemptResult).attempt_id}`, {
        replace: true,
        state: { result: data as SubmitAttemptResult, tierId },
      })
    } catch {
      setError(t('common.error.generic'))
      setSubmitting(false)
    }
  }

  return (
    <LearningLayout>
      <p className="mb-2 text-sm font-semibold text-muted">
        {t('quiz.question', { current: index + 1, total: questions.length })}
      </p>
      <div className="mb-6 h-2 overflow-hidden rounded-full bg-surface-2">
        <div
          className="h-full rounded-full bg-primary transition-all"
          style={{ width: `${((index + 1) / questions.length) * 100}%` }}
        />
      </div>

      <h1 className="mb-6 font-heading text-xl font-bold">{current.prompt}</h1>

      <div className="flex flex-col gap-3">
        {options.map((opt) => {
          const isSelected = selected === opt.id
          return (
            <button
              key={opt.id}
              onClick={() => selectOption(opt.id)}
              aria-pressed={isSelected}
              className={`flex items-center gap-3 rounded-[var(--radius-lg)] border-2 p-4 text-left transition-colors ${
                isSelected ? 'border-primary bg-primary/10' : 'border-subtle bg-surface hover:border-primary/50'
              }`}
            >
              <span
                className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-full border-2 text-sm ${
                  isSelected ? 'border-primary bg-primary text-white' : 'border-subtle'
                }`}
                aria-hidden
              >
                {isSelected ? '✓' : ''}
              </span>
              {opt.option_text}
            </button>
          )
        })}
      </div>

      {error && <p className="mt-4 text-sm font-medium text-danger">{error}</p>}

      <div className="mt-8 flex gap-3">
        {index > 0 && (
          <Button variant="secondary" onClick={() => setIndex((i) => i - 1)}>
            {t('nav.back')}
          </Button>
        )}
        {isLast ? (
          <Button fullWidth disabled={!allAnswered || submitting} onClick={handleFinish}>
            {submitting ? t('common.loading') : t('quiz.submitAll')}
          </Button>
        ) : (
          <Button fullWidth disabled={!selected} onClick={() => setIndex((i) => i + 1)}>
            {t('quiz.next')}
          </Button>
        )}
      </div>
    </LearningLayout>
  )
}
