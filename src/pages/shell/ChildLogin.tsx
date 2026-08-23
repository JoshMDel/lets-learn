import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { childLogin } from '../../lib/authApi'

export default function ChildLogin() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await childLogin(username, password)
      navigate('/home', { replace: true })
    } catch {
      setError(t('childLogin.error'))
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('childLogin.title')}</h1>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <TextField
          label={t('childLogin.username')}
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          autoComplete="username"
          autoCapitalize="none"
        />
        <TextField
          label={t('childLogin.password')}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          autoComplete="current-password"
        />
        {error && <p className="text-sm font-medium text-danger">{error}</p>}
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : t('childLogin.submit')}
        </Button>
      </form>
    </ShellLayout>
  )
}
