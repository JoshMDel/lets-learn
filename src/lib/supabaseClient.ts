import { createClient } from '@supabase/supabase-js'

const url = import.meta.env.VITE_SUPABASE_URL as string
const anonKey = import.meta.env.VITE_SUPABASE_ANON_KEY as string

if (!url || !anonKey) {
  // Fail loudly in dev rather than silently talking to nothing.
  throw new Error('Missing VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY env vars')
}

export const supabase = createClient(url, anonKey, {
  auth: {
    persistSession: true,
    autoRefreshToken: true,
    // Every signed-in session (parent OR child) lives in this one client, so
    // it's reachable across page reloads from any device that signs in --
    // the whole point of using real Supabase Auth instead of local-only state.
    storageKey: 'lets-learn-auth',
  },
})

export const EDGE_FUNCTIONS_URL = `${url}/functions/v1`
