import { useState } from 'react'
import { Navigate, useSearchParams } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { RoleToggle, type LoginRole } from '../../components/ui/RoleToggle'
import { useAuth } from '../../auth/AuthContext'
import { useLocale } from '../../i18n/LocaleContext'
import { LearnerLoginForm } from './LearnerLoginForm'
import { ParentLoginForm } from './ParentLoginForm'

// The app's single public entry point: one unified welcome screen with a
// role toggle, replacing the old two-big-cards chooser. /login and
// /child-login now just redirect here with ?role= preselected, so the form
// logic lives in one place (LearnerLoginForm / ParentLoginForm).
export default function DeviceChooser() {
  const { session, role, loading } = useAuth()
  const { t } = useLocale()
  const [searchParams] = useSearchParams()
  const initialRole: LoginRole = searchParams.get('role') === 'parent' ? 'parent' : 'learner'
  const [selectedRole, setSelectedRole] = useState<LoginRole>(initialRole)

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
        <h1 className="mt-4 font-heading text-3xl font-bold">{t('welcome.title')}</h1>
        <p className="mt-1 text-muted">{t('welcome.subtitle')}</p>
      </div>

      <RoleToggle value={selectedRole} onChange={setSelectedRole} />

      <div className="mt-8">
        {selectedRole === 'learner' ? <LearnerLoginForm /> : <ParentLoginForm />}
      </div>
    </ShellLayout>
  )
}
