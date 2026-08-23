import { useQuery } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import type { SkillType } from '../types/content'

export interface RecentAttemptRow {
  id: string
  score_pct: number
  passed: boolean
  completed_at: string | null
  tier_label: string
  tier_number: number
  topic_name: string
  subject_name: string
}

export interface ChildDashboardStats {
  totalAttempts: number
  averageScore: number | null
  topicsMastered: number
  skillAccuracy: { skill: SkillType; correct: number; total: number }[]
  recentAttempts: RecentAttemptRow[]
}

const SKILLS: SkillType[] = ['literal', 'inference', 'vocabulary', 'main_idea', 'sequencing']

export function useChildDashboard(childId: string | null) {
  return useQuery({
    queryKey: ['childDashboard', childId],
    enabled: !!childId,
    queryFn: async (): Promise<ChildDashboardStats> => {
      const { data: attempts, error: attErr } = await supabase
        .from('attempts')
        .select('id, tier_id, score_pct, passed, completed_at')
        .eq('child_id', childId as string)
        .order('completed_at', { ascending: false })
      if (attErr) throw attErr

      const totalAttempts = attempts?.length ?? 0
      const averageScore =
        totalAttempts > 0
          ? Math.round(
              (attempts!.reduce((sum, a) => sum + Number(a.score_pct), 0) / totalAttempts) * 10,
            ) / 10
          : null

      // Skill-by-skill accuracy across ALL subjects -- the cross-subject
      // diagnostic view, via attempt_answers joined to the answer-safe
      // v_quiz_questions view (skill_type only, no answer key).
      const attemptIds = (attempts ?? []).map((a) => a.id)
      const skillAccuracy = SKILLS.map((skill) => ({ skill, correct: 0, total: 0 }))

      if (attemptIds.length > 0) {
        const { data: answers, error: ansErr } = await supabase
          .from('attempt_answers')
          .select('question_id, is_correct')
          .in('attempt_id', attemptIds)
        if (ansErr) throw ansErr

        const questionIds = Array.from(new Set((answers ?? []).map((a) => a.question_id)))
        const { data: questionSkills, error: qErr } = await supabase
          .from('v_quiz_questions')
          .select('id, skill_type')
          .in('id', questionIds)
        if (qErr) throw qErr

        const skillById = new Map((questionSkills ?? []).map((q) => [q.id, q.skill_type as SkillType]))
        const bySkill = new Map(skillAccuracy.map((s) => [s.skill, s]))
        for (const a of answers ?? []) {
          const skill = skillById.get(a.question_id)
          if (!skill) continue
          const bucket = bySkill.get(skill)!
          bucket.total += 1
          if (a.is_correct) bucket.correct += 1
        }
      }

      // Mastery / recent attempts need tier -> topic -> subject names.
      const { data: progress, error: progErr } = await supabase
        .from('child_tier_progress')
        .select('tier_id, mastered')
        .eq('child_id', childId as string)
        .eq('mastered', true)
      if (progErr) throw progErr

      const tierIds = Array.from(
        new Set([...(progress ?? []).map((p) => p.tier_id), ...(attempts ?? []).slice(0, 20).map((a) => a.tier_id)]),
      )

      let topicsMastered = 0
      const recentAttempts: RecentAttemptRow[] = []

      if (tierIds.length > 0) {
        const { data: tiers, error: tiersErr } = await supabase
          .from('tiers')
          .select('id, topic_id, tier_number, label')
          .in('id', tierIds)
        if (tiersErr) throw tiersErr

        const topicIds = Array.from(new Set((tiers ?? []).map((t) => t.topic_id)))
        const { data: topics, error: topicsErr } = await supabase
          .from('topics')
          .select('id, subject_id, name_en, name_af')
          .in('id', topicIds)
        if (topicsErr) throw topicsErr

        const subjectIds = Array.from(new Set((topics ?? []).map((t) => t.subject_id)))
        const { data: subjects, error: subjErr } = await supabase
          .from('subjects')
          .select('id, name_en, name_af')
          .in('id', subjectIds)
        if (subjErr) throw subjErr

        // All tiers for the involved topics, to know each topic's final tier.
        const { data: allTiersForTopics, error: allTiersErr } = await supabase
          .from('tiers')
          .select('id, topic_id, tier_number')
          .in('topic_id', topicIds)
        if (allTiersErr) throw allTiersErr

        const maxTierByTopic = new Map<string, number>()
        for (const t of allTiersForTopics ?? []) {
          maxTierByTopic.set(t.topic_id, Math.max(maxTierByTopic.get(t.topic_id) ?? 0, t.tier_number))
        }

        const tierById = new Map((tiers ?? []).map((t) => [t.id, t]))
        const topicById = new Map((topics ?? []).map((t) => [t.id, t]))
        const subjectById = new Map((subjects ?? []).map((s) => [s.id, s]))

        const masteredTopicIds = new Set<string>()
        for (const p of progress ?? []) {
          const tier = tierById.get(p.tier_id)
          if (!tier) continue
          if (tier.tier_number === maxTierByTopic.get(tier.topic_id)) {
            masteredTopicIds.add(tier.topic_id)
          }
        }
        topicsMastered = masteredTopicIds.size

        for (const a of (attempts ?? []).slice(0, 20)) {
          const tier = tierById.get(a.tier_id)
          const topic = tier ? topicById.get(tier.topic_id) : undefined
          const subject = topic ? subjectById.get(topic.subject_id) : undefined
          recentAttempts.push({
            id: a.id,
            score_pct: Number(a.score_pct),
            passed: a.passed,
            completed_at: a.completed_at,
            tier_label: tier?.label ?? '',
            tier_number: tier?.tier_number ?? 0,
            topic_name: topic?.name_en ?? '',
            subject_name: subject?.name_en ?? '',
          })
        }
      }

      return { totalAttempts, averageScore, topicsMastered, skillAccuracy, recentAttempts }
    },
  })
}
