import type { ReactNode } from 'react'
import { Navigate, useLocation } from 'react-router-dom'
import { useAuth } from './AuthContext'

function FullScreenLoading() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-app text-muted">
      Loading…
    </div>
  )
}

/** Any signed-in session (parent or child). */
export function RequireSession({ children }: { children: ReactNode }) {
  const { session, loading } = useAuth()
  if (loading) return <FullScreenLoading />
  if (!session) return <Navigate to="/" replace />
  return <>{children}</>
}

/** Parent/teacher session specifically (for /parent/* screens). */
export function RequireParent({ children }: { children: ReactNode }) {
  const { session, role, loading } = useAuth()
  if (loading) return <FullScreenLoading />
  if (!session || role !== 'parent') return <Navigate to="/" replace />
  return <>{children}</>
}

/** A learner must be "active" -- either the child is logged in as themself,
 * or a parent has tapped a child's avatar to hand over the device. */
export function RequireActiveLearner({ children }: { children: ReactNode }) {
  const { session, loading, activeChildId } = useAuth()
  if (loading) return <FullScreenLoading />
  if (!session) return <Navigate to="/" replace />
  if (!activeChildId) return <Navigate to="/switch-profile" replace />
  return <>{children}</>
}

/** Real re-auth gate for /parent/* when arriving from the child-facing app --
 * see AuthContext.parentToolsUnlocked (always relocks on reload). */
export function RequireParentToolsUnlocked({ children }: { children: ReactNode }) {
  const { role, parentToolsUnlocked, loading } = useAuth()
  const location = useLocation()
  if (loading) return <FullScreenLoading />
  if (role !== 'parent') return <Navigate to="/" replace />
  if (!parentToolsUnlocked) {
    return <Navigate to="/parent-gate" replace state={{ from: location.pathname }} />
  }
  return <>{children}</>
}
