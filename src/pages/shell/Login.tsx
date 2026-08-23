import { useState, type FormEvent } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { loginParent } from '../../lib/authApi'

export default function Login() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await loginParent(email, password)
      navigate('/switch-profile', { replace: true })
    } catch {
      setError(t('auth.error.invalidCredentials'))
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('auth.login.title')}</h1>
      <p className="mt-2 text-muted">{t('auth.login.subtitle')}</p>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <TextField
          label={t('auth.email')}
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          autoComplete="email"
        />
        <TextField
          label={t('auth.password')}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          autoComplete="current-password"
        />
        {error && <p className="text-sm font-medium text-danger">{error}</p>}
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : t('auth.login.submit')}
        </Button>
      </form>

      <p className="mt-6 text-center text-sm text-muted">
        {t('auth.login.noAccount')}{' '}
        <Link to="/register" className="font-semibold text-primary">
          {t('auth.register.link')}
        </Link>
      </p>
    </ShellLayout>
  )
}
