import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'
import { useThemeScope } from './useThemeScope'
import { LocaleToggle } from './ui/LocaleToggle'
import { MobileBottomNav, type NavTab } from './MobileBottomNav'
import { useLocale } from '../i18n/LocaleContext'
import { useAuth } from '../auth/AuthContext'

export function LearningLayout({
  children,
  title,
  bottomNav,
  chat = false,
}: {
  children: ReactNode
  title?: string
  /** Adds the mobile-only Home/Chat/Profile bar. Only used on Home/Chat/
   * Profile themselves -- deliberately left off Subject/Topic/Read/Quiz/
   * Results so this phase doesn't touch that in-lesson flow's chrome. */
  bottomNav?: { active: NavTab; unreadChat?: boolean }
  /** Full-bleed chat screen: on phones the header and page padding give way
   * to the chat's own header (the bottom nav still handles navigation). */
  chat?: boolean
}) {
  useThemeScope('learning')
  const navigate = useNavigate()
  const { t } = useLocale()
  const { role, logoutLearner } = useAuth()

  async function handleLogout() {
    const wasChild = role === 'child'
    await logoutLearner()
    // A self-logged-in child has no session left to return to -- send them
    // to the device chooser. A child being played by a parent just loses
    // the hand-off, so the avatar picker (still that parent's session) is
    // the right "access-selection" screen to land back on.
    navigate(wasChild ? '/' : '/switch-profile', { replace: true })
  }

  return (
    <div className="min-h-full bg-app">
      <header
        className={`sticky top-0 z-10 border-b border-subtle bg-app/95 backdrop-blur ${chat ? 'hidden md:block' : ''}`}
      >
        <div className="mx-auto flex max-w-2xl items-center justify-between px-4 py-3">
          <button
            onClick={() => navigate('/home')}
            className="flex items-center gap-2 rounded-full px-3 py-2 font-heading font-semibold text-ink hover:bg-surface-2"
          >
            <img src="/brand/lets-learn-logo.svg" alt="" className="h-9 w-9" />
            {title && <span className="hidden sm:inline">{title}</span>}
          </button>
          <div className="flex items-center gap-2">
            <LocaleToggle />
            <button
              onClick={() => navigate('/switch-profile')}
              title={t('nav.switchLearner')}
              className="rounded-full p-2 hover:bg-surface-2"
              aria-label={t('nav.switchLearner')}
            >
              👤
            </button>
            {role === 'parent' && (
              <button
                onClick={() => navigate('/parent-gate')}
                title={t('nav.parentTools')}
                className="rounded-full p-2 hover:bg-surface-2"
                aria-label={t('nav.parentTools')}
              >
                🔒
              </button>
            )}
            <button
              onClick={handleLogout}
              className="rounded-full bg-surface-2 px-3 py-2 font-heading text-sm font-semibold text-ink hover:bg-danger/15 hover:text-danger"
            >
              {t('nav.logout')}
            </button>
          </div>
        </div>
      </header>
      <main
        className={
          chat
            ? 'mx-auto max-w-md p-0 md:px-4 md:py-6'
            : `mx-auto max-w-2xl px-4 py-6 ${bottomNav ? 'pb-24 md:pb-6' : ''}`
        }
      >
        {children}
      </main>
      {bottomNav && (
        <MobileBottomNav role="child" active={bottomNav.active} unreadChat={bottomNav.unreadChat} />
      )}
    </div>
  )
}
