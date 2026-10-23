import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { LearningLayout } from '../../components/LearningLayout'
import { LumiSays } from '../../components/Lumi'
import { PassageReader } from '../../components/PassageReader'
import { Button } from '../../components/ui/Button'
import {
  DiscussActivity,
  FillBlankActivity,
  MatchActivity,
  McqActivity,
  OrderActivity,
  ShortAnswerActivity,
  TrueFalseActivity,
  WritingActivity,
  ActivityCard,
  ChoicesActivity,
} from '../../components/lesson/Activities'
import { LessonBlock } from '../../components/lesson/LessonBlocks'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { useChildProgress } from '../../content/queries'
import { useRecordActivity } from '../../content/activity'
import { setResumeState } from '../../content/resume'
import {
  useLessonForTier,
  useLessonItems,
  useLessonPassage,
  useLessonResponses,
  useTierTopic,
} from '../../content/lessons'
import type { LessonItem } from '../../types/lessons'

const INTERACTIVE = new Set(['mcq', 'true_false', 'fill_blank', 'match', 'order', 'choices', 'short_answer', 'writing', 'discuss', 'listen'])

function SectionHeading({ id, children }: { id: string; children: string }) {
  return (
    <h2 id={id} className="mb-3 mt-8 font-heading text-xl font-bold">
      {children}
    </h2>
  )
}

export default function Lesson() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const { tierId } = useParams<{ tierId: string }>()
  const { activeChildId } = useAuth()

  useRecordActivity(activeChildId)

  const { data: lesson, isLoading } = useLessonForTier(tierId ?? null)
  const { data: items } = useLessonItems(lesson?.id ?? null)
  const itemIds = (items ?? []).map((i) => i.id)
  const { data: responses } = useLessonResponses(activeChildId, itemIds)
  const { data: passage } = useLessonPassage(tierId ?? null)
  const { data: topicId } = useTierTopic(tierId ?? null)
  const { data: progress } = useChildProgress(activeChildId, tierId ? [tierId] : [])

  useEffect(() => {
    if (activeChildId && tierId) setResumeState(activeChildId, { tier_id: tierId, stage: 'reading' })
  }, [activeChildId, tierId])

  if (isLoading || !lesson) {
    return (
      <LearningLayout>
        <p className="text-muted">{isLoading ? t('common.loading') : t('common.error.generic')}</p>
      </LearningLayout>
    )
  }

  const learn = (items ?? []).filter((i) => i.section === 'learn')
  const examples = (items ?? []).filter((i) => i.section === 'example')
  const activities = (items ?? []).filter((i) => i.section === 'activity')
  const interactive = activities.filter((i) => INTERACTIVE.has(i.kind))
  const doneCount = interactive.filter((i) => {
    const r = responses?.get(i.id)
    return r && r.is_correct !== false
  }).length
  const myProgress = progress?.[0]

  function renderActivity(item: LessonItem) {
    if (!activeChildId) return null
    const props = { item, childId: activeChildId, saved: responses?.get(item.id) }
    switch (item.kind) {
      case 'mcq':
        return <McqActivity key={item.id} {...props} />
      case 'true_false':
        return <TrueFalseActivity key={item.id} {...props} />
      case 'fill_blank':
        return <FillBlankActivity key={item.id} {...props} />
      case 'match':
        return <MatchActivity key={item.id} {...props} />
      case 'order':
        return <OrderActivity key={item.id} {...props} />
      case 'choices':
        return <ChoicesActivity key={item.id} {...props} />
      case 'short_answer':
        return <ShortAnswerActivity key={item.id} {...props} />
      case 'writing':
        return <WritingActivity key={item.id} {...props} />
      case 'discuss':
      case 'listen':
        return (
          <DiscussActivity
            key={item.id}
            {...props}
            passageText={passage?.sentences.map((s) => s.text).join(' ')}
          />
        )
      default:
        return null
    }
  }

  return (
    <LearningLayout title={lesson.title_af}>
      <button
        onClick={() => navigate(topicId ? `/topic/${topicId}` : '/home')}
        className="mb-3 text-sm font-semibold text-primary"
      >
        ← {t('lesson.back')}
      </button>

      <p className="text-sm font-semibold text-muted">
        {lesson.werkkaart != null && `${t('lesson.werkkaart', { n: lesson.werkkaart })} · `}
        {lesson.term != null && `${t('lesson.term', { n: lesson.term })} · `}
        {lesson.weeks}
      </p>
      <h1 className="mt-1 font-heading text-2xl font-bold sm:text-3xl">{lesson.title_af}</h1>
      <div className="mt-3 flex flex-wrap gap-2">
        {lesson.skill_areas.map((s) => (
          <span key={s} className="rounded-full bg-primary/10 px-3 py-1 text-xs font-semibold text-primary">
            {s}
          </span>
        ))}
      </div>

      {lesson.intro_af && (
        <LumiSays pose="reading" size={80} className="mt-5">
          {lesson.intro_af}
        </LumiSays>
      )}

      {lesson.objectives_af.length > 0 && (
        <section className="mt-6 rounded-[var(--radius-lg)] border border-subtle bg-surface p-5">
          <h2 className="mb-2 font-heading text-lg font-bold">🎯 {t('lesson.objectives')}</h2>
          <ul className="space-y-1.5 text-base">
            {lesson.objectives_af.map((o) => (
              <li key={o} className="flex gap-2">
                <span aria-hidden className="text-success">
                  ✓
                </span>
                {o}
              </li>
            ))}
          </ul>
        </section>
      )}

      {learn.length > 0 && (
        <>
          <SectionHeading id="learn">{`📘 ${t('lesson.learn')}`}</SectionHeading>
          <div className="flex flex-col gap-4">
            {learn.map((i) => (
              <LessonBlock key={i.id} item={i} />
            ))}
          </div>
        </>
      )}

      {passage && (
        <>
          <SectionHeading id="read">{`📖 ${t('lesson.read')}`}</SectionHeading>
          <h3 className="mb-2 font-heading text-lg font-semibold">{passage.passage.title}</h3>
          <PassageReader sentences={passage.sentences} glossary={passage.glossary} language={passage.passage.language} />
        </>
      )}

      {examples.length > 0 && (
        <>
          <SectionHeading id="examples">{`✏️ ${t('lesson.examples')}`}</SectionHeading>
          <div className="flex flex-col gap-4">
            {examples.map((i) => (
              <LessonBlock key={i.id} item={i} />
            ))}
          </div>
        </>
      )}

      {activities.length > 0 && (
        <>
          <SectionHeading id="practise">{`🧩 ${t('lesson.practise')}`}</SectionHeading>
          {interactive.length > 0 && (
            <p className="-mt-1 mb-3 text-sm text-muted">
              {t('lesson.progress', { done: doneCount, total: interactive.length })}
            </p>
          )}
          <div className="flex flex-col gap-4">
            {activities.map((item) =>
              INTERACTIVE.has(item.kind) ? (
                <ActivityCard key={item.id} item={item}>
                  {renderActivity(item)}
                </ActivityCard>
              ) : (
                <LessonBlock key={item.id} item={item} />
              ),
            )}
          </div>
        </>
      )}

      <SectionHeading id="quiz">{`🏆 ${t('lesson.quiz')}`}</SectionHeading>
      <div className="rounded-[var(--radius-lg)] border-2 border-primary/30 bg-primary/5 p-5">
        <p className="text-base">{t('lesson.quiz.intro')}</p>
        {myProgress && (
          <p className="mt-2 text-sm font-semibold text-muted">
            {t('lesson.quiz.best', { score: Math.round(Number(myProgress.best_score)) })}
            {myProgress.mastered && ` · ${t('learning.mastered')}`}
          </p>
        )}
        <Button className="mt-4" fullWidth onClick={() => navigate(`/quiz/${tierId}`)}>
          {t('lesson.quiz.start')}
        </Button>
      </div>

      <SectionHeading id="reference">{`📎 ${t('lesson.reference')}`}</SectionHeading>
      <div className="rounded-[var(--radius-lg)] border border-subtle bg-surface p-5 text-sm">
        <p>
          {lesson.printed_page_start != null &&
            t('lesson.reference.pages', {
              printed:
                lesson.printed_page_end && lesson.printed_page_end !== lesson.printed_page_start
                  ? `${lesson.printed_page_start}–${lesson.printed_page_end}`
                  : `${lesson.printed_page_start}`,
              pdf:
                lesson.pdf_page_end && lesson.pdf_page_end !== lesson.pdf_page_start
                  ? `${lesson.pdf_page_start}–${lesson.pdf_page_end}`
                  : `${lesson.pdf_page_start}`,
            })}
        </p>
        {lesson.reference_pages.length > 0 && (
          <details className="mt-3">
            <summary className="cursor-pointer font-heading font-semibold text-primary">
              {t('lesson.reference.show')}
            </summary>
            <div className="mt-3 flex flex-col gap-4">
              {lesson.reference_pages.map((pg) => (
                <a key={pg.pdf} href={pg.src} target="_blank" rel="noreferrer">
                  <img
                    src={pg.src}
                    loading="lazy"
                    alt={t('lesson.workbookPage', { page: pg.printed ?? pg.pdf })}
                    className="w-full rounded-lg border border-subtle"
                  />
                </a>
              ))}
            </div>
          </details>
        )}
        <p className="mt-4 text-xs text-muted">{t('lesson.review.note')}</p>
      </div>
    </LearningLayout>
  )
}
