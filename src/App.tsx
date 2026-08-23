import { Routes, Route, Navigate } from 'react-router-dom'
import DeviceChooser from './pages/shell/DeviceChooser'
import Register from './pages/shell/Register'
import Login from './pages/shell/Login'
import ChildLogin from './pages/shell/ChildLogin'
import SwitchProfile from './pages/shell/SwitchProfile'
import ParentGate from './pages/shell/ParentGate'
import ParentHome from './pages/shell/ParentHome'
import AddChild from './pages/shell/AddChild'
import ParentProfile from './pages/shell/ParentProfile'
import ChildDashboard from './pages/shell/ChildDashboard'
import Home from './pages/learning/Home'
import Subject from './pages/learning/Subject'
import Topic from './pages/learning/Topic'
import Read from './pages/learning/Read'
import Quiz from './pages/learning/Quiz'
import Results from './pages/learning/Results'
import { RequireActiveLearner, RequireParentToolsUnlocked, RequireSession } from './auth/guards'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<DeviceChooser />} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route path="/child-login" element={<ChildLogin />} />
      <Route
        path="/switch-profile"
        element={
          <RequireSession>
            <SwitchProfile />
          </RequireSession>
        }
      />
      <Route
        path="/parent-gate"
        element={
          <RequireSession>
            <ParentGate />
          </RequireSession>
        }
      />
      <Route
        path="/parent/add-child"
        element={
          <RequireSession>
            <AddChild />
          </RequireSession>
        }
      />

      <Route
        path="/parent"
        element={
          <RequireParentToolsUnlocked>
            <ParentHome />
          </RequireParentToolsUnlocked>
        }
      />
      <Route
        path="/parent/profile"
        element={
          <RequireParentToolsUnlocked>
            <ParentProfile />
          </RequireParentToolsUnlocked>
        }
      />
      <Route
        path="/parent/child/:childId"
        element={
          <RequireParentToolsUnlocked>
            <ChildDashboard />
          </RequireParentToolsUnlocked>
        }
      />

      <Route
        path="/home"
        element={
          <RequireActiveLearner>
            <Home />
          </RequireActiveLearner>
        }
      />
      <Route
        path="/subject/:subjectId"
        element={
          <RequireActiveLearner>
            <Subject />
          </RequireActiveLearner>
        }
      />
      <Route
        path="/topic/:topicId"
        element={
          <RequireActiveLearner>
            <Topic />
          </RequireActiveLearner>
        }
      />
      <Route
        path="/read/:tierId"
        element={
          <RequireActiveLearner>
            <Read />
          </RequireActiveLearner>
        }
      />
      <Route
        path="/quiz/:tierId"
        element={
          <RequireActiveLearner>
            <Quiz />
          </RequireActiveLearner>
        }
      />
      <Route
        path="/results/:attemptId"
        element={
          <RequireActiveLearner>
            <Results />
          </RequireActiveLearner>
        }
      />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
