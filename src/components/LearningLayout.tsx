import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'
import { useThemeScope } from './useThemeScope'
import { LocaleToggle } from './ui/LocaleToggle'
import { Mascot, type MascotMood } from './Mascot'
import { useLocale } from '../i18n/LocaleContext'
import { useAuth } from '../auth/AuthContext'

export function LearningLayout({
  children,
  mood = 'building',
  title,
}: {
  children: ReactNode
  mood?: MascotMood
  title?: string
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
      <header className="sticky top-0 z-10 border-b border-subtle bg-app/95 backdrop-blur">
        <div className="mx-auto flex max-w-2xl items-center justify-between px-4 py-3">
          <button
            onClick={() => navigate('/home')}
            className="flex items-center gap-2 rounded-full px-3 py-2 font-heading font-semibold text-ink hover:bg-surface-2"
          >
            <Mascot mood={mood} size={36} />
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
      <main className="mx-auto max-w-2xl px-4 py-6">{children}</main>
    </div>
  )
}
