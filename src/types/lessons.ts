export type LessonSection = 'learn' | 'example' | 'activity'

export type LessonItemKind =
  | 'text'
  | 'note'
  | 'table'
  | 'image'
  | 'mcq'
  | 'true_false'
  | 'fill_blank'
  | 'match'
  | 'order'
  | 'choices'
  | 'short_answer'
  | 'writing'
  | 'discuss'
  | 'listen'

export type ContentSource = 'workbook' | 'supplementary'

export type AnswerStatus = 'official' | 'derived_from_text' | 'derived_from_rule' | 'needs_review'

export interface WorkbookRef {
  printed_page?: number
  pdf_page?: number
  item?: string
}

export interface ReferencePage {
  pdf: number
  printed: number | null
  src: string
}

export interface Lesson {
  id: string
  key: string
  tier_id: string
  workbook_key: string
  term: number | null
  tema: number | null
  tema_title: string | null
  weeks: string | null
  werkkaart: number | null
  title_af: string
  intro_af: string | null
  objectives_af: string[]
  skill_areas: string[]
  printed_page_start: number | null
  printed_page_end: number | null
  pdf_page_start: number | null
  pdf_page_end: number | null
  reference_pages: ReferencePage[]
  review_status: 'draft' | 'needs_review' | 'teacher_reviewed'
  review_notes: string[]
}

// Payload shapes by kind -- these are what the learner can see (no answers).
export interface Choice {
  key: string
  text: string
}

export interface LessonItem {
  id: string
  lesson_id: string
  key: string
  section: LessonSection
  kind: LessonItemKind
  title_af: string | null
  payload: Record<string, unknown>
  source: ContentSource
  workbook_ref: WorkbookRef | null
  sort_order: number
}

export interface LessonResponse {
  child_id: string
  item_id: string
  response: Record<string, unknown>
  is_correct: boolean | null
  attempts: number
}

/** What check_lesson_item() returns. Answers are only present once revealed. */
export interface CheckResult {
  correct: boolean | null
  attempts: number
  detail: {
    blanks?: Record<string, boolean>
    pairs?: Record<string, boolean>
    answers?: Record<string, boolean>
    positions?: boolean[]
  }
  message: string | null
  explanation: string | null
  answer_status: AnswerStatus | null
  correct_answer?: Record<string, unknown>
  suggested_answer?: string | null
}
