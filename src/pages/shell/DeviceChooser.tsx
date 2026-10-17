import { useState } from 'react'
import { Navigate, useSearchParams } from 'react-router-dom'
import { ShellLayout } from '../../components/ShellLayout'
import { Lumi } from '../../components/Lumi'
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
  const { session, role, loading, parentToolsUnlocked } = useAuth()
  const { t } = useLocale()
  const [searchParams] = useSearchParams()
  const initialRole: LoginRole = searchParams.get('role') === 'parent' ? 'parent' : 'learner'
  const [selectedRole, setSelectedRole] = useState<LoginRole>(initialRole)

  if (loading) return null
  // An already-signed-in parent/teacher never sees the login again: straight
  // to their dashboard, or -- if the device was last handed to a child, which
  // relocks the parent tools -- to the avatar picker.
  if (session && role === 'parent') {
    return <Navigate to={parentToolsUnlocked ? '/parent' : '/switch-profile'} replace />
  }
  if (session && role === 'child') return <Navigate to="/home" replace />

  return (
    <ShellLayout>
      <div className="mb-6 flex flex-col items-center text-center">
        <Lumi pose="welcome" width={132} animation="wave" animateOnceKey="welcome" />
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
