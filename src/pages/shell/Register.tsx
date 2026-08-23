import { useState, type FormEvent } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { registerParent } from '../../lib/authApi'

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

export default function Register() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [contactNumber, setContactNumber] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [errors, setErrors] = useState<Record<string, string>>({})
  const [submitting, setSubmitting] = useState(false)

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    const next: Record<string, string> = {}
    if (!firstName.trim()) next.firstName = t('common.error.generic')
    if (!lastName.trim()) next.lastName = t('common.error.generic')
    if (!EMAIL_RE.test(email)) next.email = t('auth.error.invalidEmail')
    if (password.length < 8) next.password = t('auth.error.passwordLength')
    if (password !== confirmPassword) next.confirmPassword = t('auth.error.passwordMismatch')
    setErrors(next)
    if (Object.keys(next).length > 0) return

    setSubmitting(true)
    try {
      await registerParent({ firstName, lastName, email, contactNumber, password })
      navigate('/switch-profile', { replace: true })
    } catch (err) {
      const message = err instanceof Error ? err.message : ''
      if (message.toLowerCase().includes('already registered') || message.toLowerCase().includes('exists')) {
        setErrors({ email: t('auth.error.emailInUse') })
      } else {
        setErrors({ form: t('common.error.generic') })
      }
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('auth.register.title')}</h1>
      <p className="mt-2 text-muted">{t('auth.register.subtitle')}</p>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <div className="grid grid-cols-2 gap-4">
          <TextField
            label={t('auth.firstName')}
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            error={errors.firstName}
            autoComplete="given-name"
          />
          <TextField
            label={t('auth.lastName')}
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            error={errors.lastName}
            autoComplete="family-name"
          />
        </div>
        <TextField
          label={t('auth.email')}
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          error={errors.email}
          autoComplete="email"
        />
        <TextField
          label={`${t('auth.contactNumber')} (${t('common.optional')})`}
          type="tel"
          value={contactNumber}
          onChange={(e) => setContactNumber(e.target.value)}
          autoComplete="tel"
        />
        <TextField
          label={t('auth.password')}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          error={errors.password}
          autoComplete="new-password"
        />
        <TextField
          label={t('auth.confirmPassword')}
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          error={errors.confirmPassword}
          autoComplete="new-password"
        />
        {errors.form && <p className="text-sm font-medium text-danger">{errors.form}</p>}
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : t('auth.register.submit')}
        </Button>
      </form>

      <p className="mt-6 text-center text-sm text-muted">
        {t('auth.register.haveAccount')}{' '}
        <Link to="/login" className="font-semibold text-primary">
          {t('auth.login.link')}
        </Link>
      </p>
    </ShellLayout>
  )
}
