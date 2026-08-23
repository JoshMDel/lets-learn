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
      const [{ data: questions, error: qErr }, { data: options, error: oErr }] = await Promise.all([
        supabase
          .from('v_quiz_questions')
          .select('*')
          .eq('tier_id', tierId as string)
          .order('sort_order'),
        supabase.from('v_quiz_options').select('*'),
      ])
      if (qErr) throw qErr
      if (oErr) throw oErr

      const questionIds = new Set((questions as QuizQuestion[]).map((q) => q.id))
      const filteredOptions = (options as QuizOption[]).filter((o) => questionIds.has(o.question_id))

      return { questions: questions as QuizQuestion[], options: filteredOptions }
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
