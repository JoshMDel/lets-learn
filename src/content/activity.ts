import { useEffect } from 'react'
import { supabase } from '../lib/supabaseClient'

/** Fires once per mount to record "this child did something meaningful
 * today" -- opening a subject, starting a passage. Not called from Home.tsx
 * (just loading the dashboard shouldn't count, per the brief). The RPC
 * itself is idempotent (upsert on the day) and also runs this child's own
 * daily-inactivity catch-up first, so a returning child self-heals any gap
 * regardless of the nightly cron. */
export function useRecordActivity(childId: string | null) {
  useEffect(() => {
    if (!childId) return
    supabase.rpc('record_subject_activity', { p_child_id: childId }).then(({ error }) => {
      if (error) console.error('record_subject_activity failed', error)
    })
  }, [childId])
}
