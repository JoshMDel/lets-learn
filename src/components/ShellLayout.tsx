import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { useThemeScope } from './useThemeScope'
import { LocaleToggle } from './ui/LocaleToggle'
import { MobileBottomNav, type NavTab } from './MobileBottomNav'

export function ShellLayout({
  children,
  narrow = true,
  headerRight,
  bottomNav,
  chat = false,
}: {
  children: ReactNode
  narrow?: boolean
  headerRight?: ReactNode
  /** Adds the mobile-only Home/Chat/Profile bar for parent screens, with
   * `active` highlighted. Omit on screens that aren't part of that 3-tab
   * flow (e.g. auth screens). */
  bottomNav?: { active: NavTab; unreadChat?: boolean }
  /** Full-bleed chat screen: on phones the header, padding and footer give
   * way to the chat's own header (the bottom nav still handles navigation). */
  chat?: boolean
}) {
  useThemeScope('shell')
  return (
    <div className="min-h-full bg-app">
      <header className={`border-b border-subtle ${chat ? 'hidden md:block' : ''}`}>
        <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
          <Link to="/" className="flex items-center gap-2.5">
            <img src="/brand/lets-learn-logo.svg" alt="" className="h-9 w-9" />
            <span className="font-heading text-lg font-bold text-ink">Let's Learn</span>
          </Link>
          <div className="flex items-center gap-3">
            {headerRight}
            <LocaleToggle />
          </div>
        </div>
      </header>
      <main
        className={
          chat
            ? 'mx-auto max-w-md p-0 md:px-6 md:py-8'
            : `mx-auto px-6 py-10 ${narrow ? 'max-w-md' : 'max-w-5xl'} ${bottomNav ? 'pb-24 md:pb-10' : ''}`
        }
      >
        {children}
      </main>
      <footer
        className={`mx-auto max-w-5xl px-6 py-8 text-center text-xs text-muted ${chat ? 'hidden md:block' : ''}`}
      >
        Built by{' '}
        <a href="https://j92labs.co.za" target="_blank" rel="noreferrer" className="underline">
          J92 Labs
        </a>
      </footer>
      {bottomNav && (
        <MobileBottomNav role="parent" active={bottomNav.active} unreadChat={bottomNav.unreadChat} />
      )}
    </div>
  )
}
