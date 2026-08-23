import type { QuizQuestion } from '../types/content'

const QUIZ_LENGTH = 6
const MISSED_WEIGHT = 3

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

/** Weighted, no-repeat sample from the tier's question pool. Previously-missed
 * questions are ~3x more likely to be picked, so a retry genuinely targets
 * what the child got wrong rather than just reshuffling the same set -- and
 * with a real pool, back-to-back attempts land on different combinations. */
export function selectQuizQuestions(
  pool: QuizQuestion[],
  missedQuestionIds: string[],
  quizLength: number = QUIZ_LENGTH,
): QuizQuestion[] {
  if (pool.length <= quizLength) return shuffle(pool)

  const missed = new Set(missedQuestionIds)
  const bag: QuizQuestion[] = []
  for (const q of pool) {
    bag.push(q)
    if (missed.has(q.id)) {
      for (let i = 1; i < MISSED_WEIGHT; i++) bag.push(q)
    }
  }

  const picked: QuizQuestion[] = []
  const pickedIds = new Set<string>()
  const shuffledBag = shuffle(bag)
  for (const q of shuffledBag) {
    if (picked.length >= quizLength) break
    if (pickedIds.has(q.id)) continue
    picked.push(q)
    pickedIds.add(q.id)
  }

  // Pool was large enough but weighting left gaps (all weighted copies
  // collided) -- top up with anything unused.
  if (picked.length < quizLength) {
    for (const q of shuffle(pool)) {
      if (picked.length >= quizLength) break
      if (pickedIds.has(q.id)) continue
      picked.push(q)
      pickedIds.add(q.id)
    }
  }

  return shuffle(picked)
}
