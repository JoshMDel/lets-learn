import { Navigate } from 'react-router-dom'

// The standalone learner-login page was folded into the unified welcome
// screen's role toggle. Kept as a redirect so any existing link still works.
export default function ChildLogin() {
  return <Navigate to="/?role=learner" replace />
}
