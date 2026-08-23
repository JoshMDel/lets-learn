import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { useThemeScope } from './useThemeScope'
import { LocaleToggle } from './ui/LocaleToggle'

export function ShellLayout({
  children,
  narrow = true,
  headerRight,
}: {
  children: ReactNode
  narrow?: boolean
  headerRight?: ReactNode
}) {
  useThemeScope('shell')
  return (
    <div className="min-h-full bg-app">
      <header className="border-b border-subtle">
        <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
          <Link to="/" className="flex items-center gap-3">
            <img src="/brand/j92-logo.png" alt="J92 Labs" className="h-8 w-auto" />
            <span className="font-heading text-sm font-semibold tracking-wide text-muted">
              Let's Learn
            </span>
          </Link>
          <div className="flex items-center gap-3">
            {headerRight}
            <LocaleToggle />
          </div>
        </div>
      </header>
      <main className={`mx-auto px-6 py-10 ${narrow ? 'max-w-md' : 'max-w-5xl'}`}>{children}</main>
      <footer className="mx-auto max-w-5xl px-6 py-8 text-center text-xs text-muted">
        Built by{' '}
        <a href="https://j92labs.co.za" target="_blank" rel="noreferrer" className="underline">
          J92 Labs
        </a>
      </footer>
    </div>
  )
}
