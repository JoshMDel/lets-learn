import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { useQueryClient } from '@tanstack/react-query'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { addChild } from '../../lib/authApi'

const USERNAME_RE = /^[a-zA-Z0-9_]{3,20}$/
const GRADES = [3, 4, 5, 6, 7]

export default function AddChild() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  const [displayName, setDisplayName] = useState('')
  const [grade, setGrade] = useState(5)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState<Record<string, string>>({})
  const [submitting, setSubmitting] = useState(false)

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    const next: Record<string, string> = {}
    if (!displayName.trim()) next.displayName = t('common.error.generic')
    if (!USERNAME_RE.test(username)) next.username = t('parent.addChild.usernameHint')
    if (password.length < 6) next.password = t('auth.error.passwordLength')
    setErrors(next)
    if (Object.keys(next).length > 0) return

    setSubmitting(true)
    try {
      await addChild({ displayName, grade, username, password })
      await queryClient.invalidateQueries({ queryKey: ['myChildren'] })
      navigate('/parent', { replace: true })
    } catch (err) {
      const code = (err as { code?: string }).code
      if (code === 'username_taken') {
        setErrors({ username: t('parent.addChild.usernameTaken') })
      } else {
        setErrors({ form: t('common.error.generic') })
      }
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('parent.addChild.title')}</h1>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <TextField
          label={t('parent.addChild.displayName')}
          value={displayName}
          onChange={(e) => setDisplayName(e.target.value)}
          error={errors.displayName}
        />

        <div className="flex flex-col gap-1.5">
          <label className="font-heading text-sm font-semibold text-ink">
            {t('parent.addChild.grade')}
          </label>
          <div className="flex gap-2">
            {GRADES.map((g) => (
              <button
                type="button"
                key={g}
                onClick={() => setGrade(g)}
                className={`h-12 w-12 rounded-full border-2 font-heading font-bold transition-colors ${
                  grade === g ? 'border-primary bg-primary text-white' : 'border-subtle text-ink'
                }`}
              >
                {g}
              </button>
            ))}
          </div>
        </div>

        <TextField
          label={t('parent.addChild.username')}
          hint={errors.username ? undefined : t('parent.addChild.usernameHint')}
          error={errors.username}
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          autoCapitalize="none"
        />
        <TextField
          label={t('parent.addChild.password')}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          error={errors.password}
        />
        {errors.form && <p className="text-sm font-medium text-danger">{errors.form}</p>}
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : t('parent.addChild.submit')}
        </Button>
      </form>
    </ShellLayout>
  )
}
