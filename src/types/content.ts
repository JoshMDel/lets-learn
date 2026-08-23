export type SkillType =
  | 'literal'
  | 'inference'
  | 'vocabulary'
  | 'main_idea'
  | 'sequencing'

export type ContentLanguage = 'af' | 'en'

export interface Profile {
  id: string
  first_name: string
  last_name: string
  email: string
  contact_number: string | null
  bio: string | null
  created_at: string
}

export interface ChildProfile {
  id: string
  parent_id: string
  auth_user_id: string
  username: string
  display_name: string
  grade: number
  created_at: string
}

export interface ChildState {
  child_id: string
  avatar_key: string
  resume_state: ResumeState | null
  updated_at: string
}

export interface ResumeState {
  tier_id: string
  stage: 'reading' | 'quiz'
}

export interface Subject {
  id: string
  grade_id: number
  key: string
  name_af: string
  name_en: string
  language: ContentLanguage
  icon: string | null
  sort_order: number
}

export interface Topic {
  id: string
  subject_id: string
  key: string
  name_af: string
  name_en: string
  sort_order: number
}

export interface Tier {
  id: string
  topic_id: string
  tier_number: number
  label: string
}

export interface Passage {
  id: string
  tier_id: string
  language: ContentLanguage
  title: string
}

export interface PassageSentence {
  id: string
  passage_id: string
  sentence_index: number
  text: string
}

export interface GlossaryTerm {
  id: string
  passage_id: string
  term: string
  definition: string
  example_sentence_id: string | null
}

// Answer-hidden shapes, as returned by v_quiz_questions / v_quiz_options.
export interface QuizQuestion {
  id: string
  tier_id: string
  skill_type: SkillType
  prompt: string
  sort_order: number
}

export interface QuizOption {
  id: string
  question_id: string
  option_text: string
  sort_order: number
}

export interface ChildTierProgress {
  child_id: string
  tier_id: string
  best_score: number
  mastered: boolean
  mastered_at: string | null
  attempts_count: number
}

export interface Attempt {
  id: string
  child_id: string
  tier_id: string
  attempt_number: number
  score_pct: number
  passed: boolean
  started_at: string
  completed_at: string | null
}

export interface AttemptAnswer {
  id: string
  attempt_id: string
  question_id: string
  selected_option_id: string
  is_correct: boolean
}

// Shape returned by the submit_attempt() RPC.
export interface SubmitAttemptResult {
  attempt_id: string
  attempt_number: number
  score_pct: number
  passed: boolean
  correct_count: number
  total: number
  results: SubmitAttemptQuestionResult[]
}

export interface SubmitAttemptQuestionResult {
  question_id: string
  selected_option_id: string
  is_correct: boolean
  correct_option: { id: string; option_text: string }
  explanation: string
  misconception_note: string | null
  supporting_sentences: { sentence_index: number; text: string }[]
}
