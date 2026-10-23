import { useQuery } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import type { GlossaryTerm, Passage, PassageSentence } from '../types/content'
import type { CheckResult, Lesson, LessonItem, LessonResponse } from '../types/lessons'

/** The lesson (if any) attached to a tier. Tiers without one are the older
 * passage-and-quiz levels and keep their existing Read -> Quiz flow. */
export function useLessonForTier(tierId: string | null) {
  return useQuery({
    queryKey: ['lessonForTier', tierId],
    enabled: !!tierId,
    queryFn: async () => {
      const { data, error } = await supabase.from('lessons').select('*').eq('tier_id', tierId as string).maybeSingle()
      if (error) throw error
      return (data as Lesson | null) ?? null
    },
  })
}

/** Lightweight lookup for the Topic screen: which of these tiers are lessons. */
export function useLessonsForTiers(tierIds: string[]) {
  return useQuery({
    queryKey: ['lessonsForTiers', tierIds],
    enabled: tierIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('lessons')
        .select('tier_id, werkkaart, title_af, skill_areas')
        .in('tier_id', tierIds)
      if (error) throw error
      return new Map(
        (data ?? []).map((l) => [
          l.tier_id as string,
          { werkkaart: l.werkkaart as number | null, title_af: l.title_af as string, skill_areas: (l.skill_areas ?? []) as string[] },
        ]),
      )
    },
  })
}

export function useLessonItems(lessonId: string | null) {
  return useQuery({
    queryKey: ['lessonItems', lessonId],
    enabled: !!lessonId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('lesson_items')
        .select('*')
        .eq('lesson_id', lessonId as string)
        .order('sort_order')
      if (error) throw error
      return data as LessonItem[]
    },
  })
}

export function useLessonResponses(childId: string | null, itemIds: string[]) {
  return useQuery({
    queryKey: ['lessonResponses', childId, itemIds],
    enabled: !!childId && itemIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('lesson_responses')
        .select('*')
        .eq('child_id', childId as string)
        .in('item_id', itemIds)
      if (error) throw error
      return new Map((data as LessonResponse[]).map((r) => [r.item_id, r]))
    },
  })
}

/** Checks (objective items) or saves (writing / short answer / discuss) one
 * response. Grading and answer keys live in the database function, never here. */
export async function checkLessonItem(childId: string, itemId: string, response: Record<string, unknown>) {
  const { data, error } = await supabase.rpc('check_lesson_item', {
    p_child_id: childId,
    p_item_id: itemId,
    p_response: response,
  })
  if (error) throw error
  return data as CheckResult
}

/** The reading text attached to a lesson's tier (not every lesson has one). */
export function useLessonPassage(tierId: string | null) {
  return useQuery({
    queryKey: ['lessonPassage', tierId],
    enabled: !!tierId,
    queryFn: async () => {
      const { data: passage, error } = await supabase
        .from('passages')
        .select('*')
        .eq('tier_id', tierId as string)
        .maybeSingle()
      if (error) throw error
      if (!passage) return null
      const [{ data: sentences, error: sErr }, { data: glossary, error: gErr }] = await Promise.all([
        supabase.from('passage_sentences').select('*').eq('passage_id', passage.id).order('sentence_index'),
        supabase.from('glossary_terms').select('*').eq('passage_id', passage.id),
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

/** Which topic a tier belongs to -- for the lesson's "back to lessons" link. */
export function useTierTopic(tierId: string | null) {
  return useQuery({
    queryKey: ['tierTopic', tierId],
    enabled: !!tierId,
    queryFn: async () => {
      const { data, error } = await supabase.from('tiers').select('topic_id').eq('id', tierId as string).maybeSingle()
      if (error) throw error
      return (data?.topic_id as string | undefined) ?? null
    },
  })
}
