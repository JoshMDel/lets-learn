# Let's Learn

A mobile-first, installable reading-comprehension PWA for Grades 3–7, built
for J92 Labs' Western Cape Afrikaans-medium CAPS school pilot. Reading
comprehension is practiced *inside* real subject content (Language, Maths
word problems, Natural Sciences, Social Sciences, Life Skills) rather than in
isolation, with an adaptive per-topic difficulty ladder and a parent/teacher
dashboard that surfaces cross-subject skill weaknesses.

See `content/README.md` for what's seeded and the educator-review caveat.

## Stack

- Vite + React + TypeScript, React Router, Tailwind CSS v4 (two themes: a
  dark J92-branded "shell" for accounts/admin, a warm playful "learning"
  theme in `Lexend` for the child-facing screens — see `src/index.css`).
- Supabase (Postgres + Auth + RLS + 2 Edge Functions) as the real backend —
  project **"Lets Learn"** in the J92Labs org, `eu-west-1`.
- `vite-plugin-pwa` for the installable app shell + offline caching.
- Browser-native `speechSynthesis` for tap-a-word pronunciation (best-effort
  Afrikaans voice, falls back gracefully where a device has none).

## Local setup

```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # production build + PWA manifest/service worker
npm run preview  # serve the production build locally
```

`.env.local` already has the anon key wired up (safe to commit — it's
protected entirely by RLS, not a secret). No other setup needed; the schema,
RLS policies, Edge Functions, and content are already live on the Supabase
project referenced there.

## Architecture notes

- **Auth**: both parents and children are real `auth.users` rows, so Supabase
  Auth does all password hashing server-side — see the "Auth model" section
  of the original build plan / `src/lib/authApi.ts` for how child
  username-login works (a synthetic email under the hood, resolved by the
  public `child-login-lookup` Edge Function, then a normal
  `signInWithPassword`). This is what makes both parent and child logins
  reachable from any device, not just the one that created them.
- **Answer-key secrecy**: `questions`/`question_options` are fully locked
  down by RLS (no policies at all for `authenticated`); the client only ever
  sees `v_quiz_questions`/`v_quiz_options` (no correct-answer flag). Grading
  happens server-side in the `submit_attempt()` RPC, which also returns the
  per-question explanation/citation for the results screen.
- **Quiz fairness**: both which questions get sampled (`selectQuizQuestions`,
  weighted toward previously-missed ones) *and* the on-screen order of each
  question's options are re-shuffled per attempt — don't remove the
  client-side option shuffle in `Quiz.tsx`, or the correct answer sits in the
  same authored position every time.

## Known gap to fix before real parent signups

Supabase's default built-in email provider (no custom SMTP configured) has a
very low send rate limit and, depending on project auth settings, may require
email confirmation before a new parent/teacher account can log in. During
testing, `supabase.auth.signUp()` hit `over_email_send_rate_limit` almost
immediately. Before onboarding real parents/teachers:

1. In the Supabase dashboard → Authentication → Providers → Email, either
   configure a custom SMTP provider, or (for an internal pilot only) disable
   "Confirm email".
2. Re-test the `/register` flow end-to-end afterward.

This doesn't affect the child-login path (children never get an email) or
anything already built — it's purely a project-settings step outside what
the available tooling could change directly in this pass.
