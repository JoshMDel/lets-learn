import { supabase } from '../lib/supabaseClient'
import type { ResumeState } from '../types/content'

/** Persists (or clears) exactly where a child is mid-flow, server-side, so
 * "exit to home" and even a different device pick back up in the right
 * place -- not just a localStorage flag tied to one browser. */
export async function setResumeState(childId: string, state: ResumeState | null) {
  await supabase
    .from('child_state')
    .upsert({ child_id: childId, resume_state: state, updated_at: new Date().toISOString() }, { onConflict: 'child_id' })
}
