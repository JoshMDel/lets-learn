import type { ReactNode } from 'react'

export function Card({ children, className = '' }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={`rounded-[var(--radius-lg)] border border-subtle bg-surface p-6 shadow-sm ${className}`}
    >
      {children}
    </div>
  )
}
