import { useQuery } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import type {
  ChildTierProgress,
  GlossaryTerm,
  Passage,
  PassageSentence,
  QuizOption,
  QuizQuestion,
  Subject,
  Tier,
  Topic,
} from '../types/content'

/** My Rewards card on the learner's own home screen -- just the total and
 * count, not the full history (that's a parent-dashboard concern). Reads
 * v_child_reward_summary, the one place every reward display gets its
 * numbers from (balance already floors at 0; tasks_passed excludes
 * daily-inactivity deduction rows). */
export function useMyRewards(childId: string | null) {
  return useQuery({
    queryKey: ['myRewards', childId],
    enabled: !!childId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('v_child_reward_summary')
        .select('balance, tasks_passed')
        .eq('child_id', childId as string)
        .maybeSingle()
      if (error) throw error
      return {
        total: Number(data?.balance ?? 0),
        testsPassed: data?.tasks_passed ?? 0,
      }
    },
  })
}

export function useSubjects(grade: number | null) {
  return useQuery({
    queryKey: ['subjects', grade],
    enabled: grade != null,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('subjects')
        .select('*')
        .eq('grade_id', grade)
        .order('sort_order')
      if (error) throw error
      return data as Subject[]
    },
  })
}

export function useTopics(subjectId: string | null) {
  return useQuery({
    queryKey: ['topics', subjectId],
    enabled: !!subjectId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('topics')
        .select('*')
        .eq('subject_id', subjectId as string)
        .order('sort_order')
      if (error) throw error
      return data as Topic[]
    },
  })
}

export function useTiers(topicId: string | null) {
  return useQuery({
    queryKey: ['tiers', topicId],
    enabled: !!topicId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('tiers')
        .select('*')
        .eq('topic_id', topicId as string)
        .order('tier_number')
      if (error) throw error
      return data as Tier[]
    },
  })
}

export function useChildProgress(childId: string | null, tierIds: string[]) {
  return useQuery({
    queryKey: ['progress', childId, tierIds],
    enabled: !!childId && tierIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_tier_progress')
        .select('*')
        .eq('child_id', childId as string)
        .in('tier_id', tierIds)
      if (error) throw error
      return data as ChildTierProgress[]
    },
  })
}

export function usePassage(tierId: string | null) {
  return useQuery({
    queryKey: ['passage', tierId],
    enabled: !!tierId,
    queryFn: async () => {
      const { data: passage, error } = await supabase
        .from('passages')
        .select('*')
        .eq('tier_id', tierId as string)
        .single()
      if (error) throw error

      const [{ data: sentences, error: sErr }, { data: glossary, error: gErr }] = await Promise.all([
        supabase
          .from('passage_sentences')
          .select('*')
          .eq('passage_id', (passage as Passage).id)
          .order('sentence_index'),
        supabase.from('glossary_terms').select('*').eq('passage_id', (passage as Passage).id),
      ])
      if (sErr) throw sErr
      if (gErr) throw gErr

      return {
        passage: passage as Passage,
        sentences: sentences as PassageSentence[],
        glossary: glossary as GlossaryTerm[],
      }
    },
  })
}

export function useQuizPool(tierId: string | null) {
  return useQuery({
    queryKey: ['quizPool', tierId],
    enabled: !!tierId,
    queryFn: async () => {
      const { data: questions, error: qErr } = await supabase
        .from('v_quiz_questions')
        .select('*')
        .eq('tier_id', tierId as string)
        .order('sort_order')
      if (qErr) throw qErr

      // Only this tier's options -- fetching every option in the database would
      // silently hit the API's 1,000-row cap once the workbook lessons exist.
      const questionIds = (questions as QuizQuestion[]).map((q) => q.id)
      const { data: options, error: oErr } =
        questionIds.length > 0
          ? await supabase.from('v_quiz_options').select('*').in('question_id', questionIds)
          : { data: [] as QuizOption[], error: null }
      if (oErr) throw oErr

      return { questions: questions as QuizQuestion[], options: options as QuizOption[] }
    },
  })
}

export function useRecentMissedQuestionIds(childId: string | null, tierId: string | null) {
  return useQuery({
    queryKey: ['recentMisses', childId, tierId],
    enabled: !!childId && !!tierId,
    queryFn: async () => {
      const { data: attempts, error } = await supabase
        .from('attempts')
        .select('id')
        .eq('child_id', childId as string)
        .eq('tier_id', tierId as string)
        .order('completed_at', { ascending: false })
        .limit(3)
      if (error) throw error
      const attemptIds = (attempts ?? []).map((a) => a.id)
      if (attemptIds.length === 0) return [] as string[]

      const { data: answers, error: aErr } = await supabase
        .from('attempt_answers')
        .select('question_id, is_correct')
        .in('attempt_id', attemptIds)
      if (aErr) throw aErr

      const missed = new Set<string>()
      for (const a of answers ?? []) {
        if (!a.is_correct) missed.add(a.question_id)
      }
      return Array.from(missed)
    },
  })
}
