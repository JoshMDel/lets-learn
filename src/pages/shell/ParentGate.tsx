import { useState, type FormEvent } from 'react'
import { Navigate, useLocation, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { loginParent } from '../../lib/authApi'

// Real re-authentication, not a math-sum toy gate -- this unlocks usage data
// and account management, so it re-checks the parent's actual password
// against Supabase Auth every time, and always re-locks on reload.
export default function ParentGate() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const location = useLocation()
  const from = (location.state as { from?: string } | null)?.from ?? '/parent'
  const { role, profile, loading, unlockParentTools } = useAuth()
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  if (loading) return null
  if (role !== 'parent' || !profile) return <Navigate to="/" replace />

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await loginParent(profile!.email, password)
      unlockParentTools()
      navigate(from, { replace: true })
    } catch {
      setError(t('reauth.error'))
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('reauth.title')}</h1>
      <p className="mt-2 text-muted">{t('reauth.subtitle')}</p>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <TextField
          label={t('auth.password')}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          autoComplete="current-password"
          autoFocus
        />
        {error && <p className="text-sm font-medium text-danger">{error}</p>}
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : t('reauth.submit')}
        </Button>
        <Button type="button" variant="ghost" onClick={() => navigate(-1)} fullWidth>
          {t('common.cancel')}
        </Button>
      </form>
    </ShellLayout>
  )
}
