import { useNavigate } from 'react-router-dom'
import { useLocale } from '../i18n/LocaleContext'

export type NavTab = 'home' | 'chat' | 'profile'

interface Tab {
  key: NavTab
  label: string
  icon: string
  to: string
}

/** Fixed mobile-only bottom nav (md:hidden) -- purely additive alongside the
 * existing header controls in ShellLayout/LearningLayout, not a replacement
 * for them. Desktop keeps using the existing header nav unchanged. */
export function MobileBottomNav({
  role,
  active,
  unreadChat = false,
}: {
  role: 'parent' | 'child'
  active: NavTab
  unreadChat?: boolean
}) {
  const navigate = useNavigate()
  const { t } = useLocale()

  const tabs: Tab[] =
    role === 'parent'
      ? [
          { key: 'home', label: t('nav.home'), icon: '🏠', to: '/parent' },
          { key: 'chat', label: t('nav.chat'), icon: '💬', to: '/parent/chat' },
          { key: 'profile', label: t('nav.profile'), icon: '👤', to: '/parent/profile' },
        ]
      : [
          { key: 'home', label: t('nav.home'), icon: '🏠', to: '/home' },
          { key: 'chat', label: t('nav.chat'), icon: '💬', to: '/chat' },
          { key: 'profile', label: t('nav.profile'), icon: '👤', to: '/profile' },
        ]

  return (
    <nav
      aria-label={t('nav.home')}
      className="fixed inset-x-0 bottom-0 z-20 border-t border-subtle bg-surface pb-[env(safe-area-inset-bottom)] md:hidden"
    >
      <div className="mx-auto flex max-w-2xl items-stretch">
        {tabs.map((tab) => {
          const isActive = tab.key === active
          return (
            <button
              key={tab.key}
              onClick={() => navigate(tab.to)}
              aria-current={isActive ? 'page' : undefined}
              className="relative flex min-h-[56px] flex-1 flex-col items-center justify-center gap-0.5 py-2 text-xs"
            >
              <span
                className={`text-xl transition-transform ${isActive ? 'scale-110' : 'opacity-60'}`}
                aria-hidden
              >
                {tab.icon}
              </span>
              <span
                className={`font-heading ${isActive ? 'font-bold text-primary' : 'font-medium text-muted'}`}
              >
                {tab.label}
              </span>
              {tab.key === 'chat' && unreadChat && (
                <span
                  aria-label="Unread messages"
                  className="absolute right-1/2 top-1.5 h-2.5 w-2.5 translate-x-3 rounded-full bg-danger"
                />
              )}
              {isActive && (
                <span className="absolute top-0 h-0.5 w-8 rounded-full bg-primary" aria-hidden />
              )}
            </button>
          )
        })}
      </div>
    </nav>
  )
}
