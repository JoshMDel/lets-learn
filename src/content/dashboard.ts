import { useQuery } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import type { RewardReason, SkillType } from '../types/content'

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

export interface RewardHistoryRow {
  id: string
  date: string
  topic_name: string
  score_pct: number | null
  amount: number
  reason: RewardReason
}

export interface ChildDashboardStats {
  totalAttempts: number
  averageScore: number | null
  topicsMastered: number
  skillAccuracy: { skill: SkillType; correct: number; total: number }[]
  recentAttempts: RecentAttemptRow[]
  /** Reward Points: total earned so far and how many tests that reflects. */
  rewardTotal: number
  rewardTestsPassed: number
  rewardHistory: RewardHistoryRow[]
}

function chunk<T>(items: T[], size: number): T[][] {
  const out: T[][] = []
  for (let i = 0; i < items.length; i += size) out.push(items.slice(i, i + size))
  return out
}

const SKILLS: SkillType[] =['literal', 'inference', 'vocabulary', 'main_idea', 'sequencing']

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
        // Chunk the id lists (URL length) and page the rows (the API returns at most
        // 1,000 rows per request) so the numbers stay right as a child does more quizzes.
        const answers: { question_id: string; is_correct: boolean }[] = []
        for (const ids of chunk(attemptIds, 100)) {
          for (let from = 0; ; from += 1000) {
            const { data, error: ansErr } = await supabase
              .from('attempt_answers')
              .select('question_id, is_correct')
              .in('attempt_id', ids)
              .range(from, from + 999)
            if (ansErr) throw ansErr
            answers.push(...(data ?? []))
            if ((data ?? []).length < 1000) break
          }
        }

        const questionIds = Array.from(new Set(answers.map((a) => a.question_id)))
        const questionSkills: { id: string; skill_type: string }[] = []
        for (const ids of chunk(questionIds, 100)) {
          const { data, error: qErr } = await supabase
            .from('v_quiz_questions')
            .select('id, skill_type')
            .in('id', ids)
          if (qErr) throw qErr
          questionSkills.push(...(data ?? []))
        }

        const skillById = new Map(questionSkills.map((q) => [q.id, q.skill_type as SkillType]))
        const bySkill = new Map(skillAccuracy.map((s) => [s.skill, s]))
        for (const a of answers ?? []) {
          const skill = skillById.get(a.question_id)
          if (!skill) continue
          const bucket = bySkill.get(skill)!
          bucket.total += 1
          if (a.is_correct) bucket.correct += 1
        }
      }

      // Reward summary: the one place every reward display (learner card,
      // parent card, this dashboard) reads its balance/count from.
      const { data: summary, error: summaryErr } = await supabase
        .from('v_child_reward_summary')
        .select('balance, tasks_passed')
        .eq('child_id', childId as string)
        .maybeSingle()
      if (summaryErr) throw summaryErr
      const rewardTotal = Number(summary?.balance ?? 0)
      const rewardTestsPassed = summary?.tasks_passed ?? 0

      // Full reward history (earned + deducted), for the transparency table.
      const { data: rewards, error: rewardsErr } = await supabase
        .from('reward_transactions')
        .select('id, tier_id, score_pct, amount, reason, created_at')
        .eq('child_id', childId as string)
        .order('created_at', { ascending: false })
      if (rewardsErr) throw rewardsErr

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
      const rewardHistory: RewardHistoryRow[] = []
      let tierById = new Map<string, { id: string; topic_id: string; tier_number: number; label: string }>()
      let topicById = new Map<string, { id: string; subject_id: string; name_en: string; name_af: string }>()

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

        tierById = new Map((tiers ?? []).map((t) => [t.id, t]))
        topicById = new Map((topics ?? []).map((t) => [t.id, t]))
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

      // Reward history: every tier passed for the first time earns R2 (via
      // submit_attempt()); every rewarded tier is guaranteed already
      // mastered, so it's covered by tierById/topicById above (populated
      // whenever tierIds was non-empty). Deduction rows
      // (reason='daily_inactivity') have no tier_id -- topic_name just
      // stays blank for those, the reason itself explains the row -- and
      // this runs regardless of tierIds, since a brand-new, never-mastered
      // child can still have been deducted for missed days.
      for (const r of rewards ?? []) {
        const tier = r.tier_id ? tierById.get(r.tier_id) : undefined
        const topic = tier ? topicById.get(tier.topic_id) : undefined
        rewardHistory.push({
          id: r.id,
          date: r.created_at,
          topic_name: topic?.name_en ?? '',
          score_pct: r.score_pct != null ? Number(r.score_pct) : null,
          amount: Number(r.amount),
          reason: r.reason as RewardReason,
        })
      }

      return {
        totalAttempts,
        averageScore,
        topicsMastered,
        skillAccuracy,
        recentAttempts,
        rewardTotal,
        rewardTestsPassed,
        rewardHistory,
      }
    },
  })
}
