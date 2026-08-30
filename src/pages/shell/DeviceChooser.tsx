import { Navigate, Link } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { useAuth } from '../../auth/AuthContext'
import { useLocale } from '../../i18n/LocaleContext'

export default function DeviceChooser() {
  const { session, role, loading } = useAuth()
  const { t } = useLocale()

  if (loading) return null
  // A device that already has a parent/teacher signed in skips straight to
  // the avatar picker -- no password needed, the adult is already present.
  if (session && role === 'parent') return <Navigate to="/switch-profile" replace />
  if (session && role === 'child') return <Navigate to="/home" replace />

  return (
    <ShellLayout>
      <div className="mb-6 flex flex-col items-center text-center">
        <img
          src="/brand/lets-learn-logo.svg"
          alt="Let's Learn"
          className="h-24 w-24 sm:h-28 sm:w-28"
          width={112}
          height={112}
        />
      </div>
      <h1 className="mb-2 text-center font-heading text-3xl font-bold sm:text-left">{t('chooser.title')}</h1>
      <div className="mt-8 flex flex-col gap-4">
        <Link
          to="/child-login"
          className="rounded-[var(--radius-lg)] border border-subtle bg-surface p-6 transition-colors hover:border-primary"
        >
          <div className="font-heading text-xl font-semibold">{t('chooser.learner')}</div>
          <p className="mt-1 text-sm text-muted">{t('chooser.learnerHint')}</p>
        </Link>
        <Link
          to="/login"
          className="rounded-[var(--radius-lg)] border border-subtle bg-surface p-6 transition-colors hover:border-primary"
        >
          <div className="font-heading text-xl font-semibold">{t('chooser.parentTeacher')}</div>
          <p className="mt-1 text-sm text-muted">{t('chooser.parentHint')}</p>
        </Link>
      </div>
    </ShellLayout>
  )
}
