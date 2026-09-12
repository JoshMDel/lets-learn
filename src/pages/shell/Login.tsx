import { Navigate } from 'react-router-dom'

// The standalone parent-login page was folded into the unified welcome
// screen's role toggle. Kept as a redirect so any existing link still works.
export default function Login() {
  return <Navigate to="/?role=parent" replace />
}
