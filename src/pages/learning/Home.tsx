import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { LearningLayout } from '../../components/LearningLayout'
import { LumiSays } from '../../components/Lumi'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { useSubjects, useMyRewards } from '../../content/queries'
import { useConversation, useUnreadCount } from '../../content/chat'
import { formatRands } from '../../lib/currency'
import type { ChildProfile, ChildState } from '../../types/content'

const GRADES = [3, 4, 5, 6, 7]

const SUBJECT_EMOJI: Record<string, string> = {
  language_af: '📖',
  language_en: '🗣️',
  mathematics: '🔢',
  natural_sciences: '🔬',
  social_sciences: '🌍',
  life_skills: '🌱',
}

export default function Home() {
  const { t, locale } = useLocale()
  const navigate = useNavigate()
  const { activeChildId, session } = useAuth()
  const [grade, setGrade] = useState<number | null>(null)

  const { data: child } = useQuery({
    queryKey: ['activeChildProfile', activeChildId],
    enabled: !!activeChildId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_profiles')
        .select('*')
        .eq('id', activeChildId as string)
        .single()
      if (error) throw error
      return data as ChildProfile
    },
  })

  const { data: childState } = useQuery({
    queryKey: ['childState', activeChildId],
    enabled: !!activeChildId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_state')
        .select('*')
        .eq('child_id', activeChildId as string)
        .maybeSingle()
      if (error) throw error
      return data as ChildState | null
    },
  })

  useEffect(() => {
    if (child && grade == null) setGrade(child.grade)
  }, [child, grade])

  const { data: subjects, isLoading } = useSubjects(grade)
  const { data: rewards } = useMyRewards(activeChildId)

  const { data: conversationId } = useConversation(activeChildId)
  const unreadChat = useUnreadCount(session?.user.id ?? null, conversationId ? [conversationId] : [])

  return (
    <LearningLayout
      title={child?.display_name}
      bottomNav={{ active: 'home', unreadChat: unreadChat > 0 }}
    >
      <LumiSays pose="welcome" size={96} animation="wave" animateOnceKey="home" className="mb-5">
        {t('lumi.greeting')}
      </LumiSays>

      <div className="mb-6 rounded-[var(--radius-lg)] border-2 border-accent/30 bg-gradient-to-br from-accent/15 to-primary/10 p-5 text-center">
        <div className="font-heading text-sm font-semibold text-muted">
          🏆 {t('rewards.myRewards')}
        </div>
        <div className="mt-1 font-heading text-4xl font-bold text-primary">
          {formatRands(rewards?.total ?? 0)}
        </div>
        <div className="mt-1 text-sm text-muted">
          {t('rewards.testsPassedCount', { count: rewards?.testsPassed ?? 0 })}
        </div>
      </div>

      {childState?.resume_state && (
        <button
          onClick={() => {
            const r = childState.resume_state!
            navigate(r.stage === 'quiz' ? `/quiz/${r.tier_id}` : `/read/${r.tier_id}`)
          }}
          className="mb-6 w-full rounded-[var(--radius-lg)] border-2 border-primary bg-primary/10 p-4 text-left font-heading font-semibold text-primary"
        >
          ▶ {t('learning.continueReading')}
        </button>
      )}

      <div className="mb-6 flex items-center gap-2 overflow-x-auto pb-1">
        <span className="shrink-0 font-heading text-sm font-semibold text-muted">
          {t('learning.pickGrade')}:
        </span>
        {GRADES.map((g) => (
          <button
            key={g}
            onClick={() => setGrade(g)}
            className={`h-10 shrink-0 rounded-full px-4 font-heading font-bold transition-colors ${
              grade === g ? 'bg-primary text-white' : 'bg-surface-2 text-ink'
            }`}
          >
            {g}
          </button>
        ))}
      </div>

      <h1 className="mb-4 font-heading text-2xl font-bold">{t('learning.pickSubject')}</h1>

      {isLoading ? (
        <p className="text-muted">{t('common.loading')}</p>
      ) : (
        <div className="grid grid-cols-2 gap-4">
          {(subjects ?? []).map((subject) => (
            <button
              key={subject.id}
              onClick={() => navigate(`/subject/${subject.id}`)}
              className="flex flex-col items-center gap-2 rounded-[var(--radius-lg)] border border-subtle bg-surface p-6 text-center transition-transform hover:-translate-y-0.5 hover:border-primary"
            >
              <span className="text-4xl">{SUBJECT_EMOJI[subject.key] ?? '📚'}</span>
              <span className="font-heading font-semibold leading-tight">
                {locale === 'af' ? subject.name_af : subject.name_en}
              </span>
            </button>
          ))}
        </div>
      )}
    </LearningLayout>
  )
}
