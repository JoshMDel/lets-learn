import { supabase, EDGE_FUNCTIONS_URL } from './supabaseClient'

export interface RegisterParentInput {
  firstName: string
  lastName: string
  email: string
  contactNumber: string
  password: string
}

// Real Supabase Auth signUp -- password hashing happens entirely server-side,
// inside Auth itself. The `role: 'parent'` metadata is read by the
// on_auth_user_created DB trigger to create the matching `profiles` row.
export async function registerParent(input: RegisterParentInput) {
  const { data, error } = await supabase.auth.signUp({
    email: input.email,
    password: input.password,
    options: {
      data: {
        role: 'parent',
        first_name: input.firstName,
        last_name: input.lastName,
        contact_number: input.contactNumber,
      },
    },
  })
  if (error) throw error
  return data
}

export async function loginParent(email: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password })
  if (error) throw error
  return data
}

export interface AddChildInput {
  displayName: string
  grade: number
  username: string
  password: string
  avatarKey?: string
}

// Calls the create-child Edge Function (service-role only, never exposed to
// the client) which mints a real auth.users identity for the child under a
// synthetic email -- see supabase/functions/create-child.
export async function addChild(input: AddChildInput) {
  const { data: sessionData } = await supabase.auth.getSession()
  const token = sessionData.session?.access_token
  if (!token) throw new Error('not_authenticated')

  const res = await fetch(`${EDGE_FUNCTIONS_URL}/create-child`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
      apikey: import.meta.env.VITE_SUPABASE_ANON_KEY as string,
    },
    body: JSON.stringify({
      displayName: input.displayName,
      grade: input.grade,
      username: input.username,
      password: input.password,
      avatarKey: input.avatarKey ?? 'mascot-1',
    }),
  })
  const body = await res.json()
  if (!res.ok) {
    const err = new Error(body.error ?? 'create_child_failed') as Error & { code?: string }
    err.code = body.error
    throw err
  }
  return body.child as { id: string; username: string; display_name: string; grade: number; avatar_key: string }
}

// child-login-lookup resolves username -> synthetic email (never a password).
// The actual credential check happens in the signInWithPassword call right
// after, inside Supabase Auth's own server-side hashing -- exactly like a
// parent login.
export async function childLogin(username: string, password: string) {
  const lookupRes = await fetch(`${EDGE_FUNCTIONS_URL}/child-login-lookup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      apikey: import.meta.env.VITE_SUPABASE_ANON_KEY as string,
    },
    body: JSON.stringify({ username }),
  })
  if (!lookupRes.ok) {
    // Same generic error whether the username doesn't exist or the password
    // is wrong later -- avoids trivially confirming which usernames exist.
    throw new Error('invalid_credentials')
  }
  const { email } = await lookupRes.json()
  const { data, error } = await supabase.auth.signInWithPassword({ email, password })
  if (error) throw new Error('invalid_credentials')
  return data
}

export async function signOut() {
  await supabase.auth.signOut()
}
