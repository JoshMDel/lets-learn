import type { ReactNode } from 'react'

// Shared pieces of the chat look: a teal wave header/footer around a body
// that takes its colours from the --chat-* tokens in index.css, so the same
// markup reads correctly in both the light learner theme and the dark shell.

const HEADER_BG = 'bg-gradient-to-br from-[#0b7f86] via-[#139b9a] to-[#58bdae]'

/** Full-bleed on phones (the bottom nav sits underneath), a rounded card on
 * larger screens. */
export function ChatCard({ children }: { children: ReactNode }) {
  return (
    <div className="flex h-[calc(100dvh-3.5rem-env(safe-area-inset-bottom))] flex-col overflow-hidden bg-[var(--chat-body)] md:h-[78vh] md:max-h-[720px] md:rounded-[2rem] md:border md:border-subtle md:shadow-2xl">
      {children}
    </div>
  )
}

export function ChatHeader({ children }: { children: ReactNode }) {
  return (
    <div className={`relative shrink-0 overflow-hidden pb-9 text-white ${HEADER_BG}`}>
      <svg
        aria-hidden
        className="pointer-events-none absolute inset-0 h-full w-full"
        viewBox="0 0 400 160"
        preserveAspectRatio="none"
      >
        <path d="M0 60 C80 20 150 90 240 50 C310 20 360 40 400 20 V0 H0 Z" fill="#fff" opacity="0.1" />
        <path d="M0 120 C90 70 170 150 260 100 C330 62 370 90 400 70 V160 H0 Z" fill="#fff" opacity="0.08" />
      </svg>
      <div className="relative px-5 pt-5">{children}</div>
      <svg
        aria-hidden
        className="absolute inset-x-0 -bottom-px block h-9 w-full"
        viewBox="0 0 400 40"
        preserveAspectRatio="none"
      >
        <path
          d="M0 40 V24 C70 4 120 4 180 20 C240 36 310 36 400 8 V40 Z"
          style={{ fill: 'var(--chat-body)' }}
        />
      </svg>
    </div>
  )
}

/** Teal bar with a wave cut into its top edge, holding the message input. */
export function ChatFooter({ children }: { children: ReactNode }) {
  return (
    <div className={`relative shrink-0 px-4 pb-4 pt-9 ${HEADER_BG}`}>
      <svg
        aria-hidden
        className="absolute inset-x-0 -top-px block h-8 w-full"
        viewBox="0 0 400 40"
        preserveAspectRatio="none"
      >
        <path
          d="M0 0 H400 V12 C330 34 260 36 190 22 C120 8 60 6 0 24 Z"
          style={{ fill: 'var(--chat-body)' }}
        />
      </svg>
      <div className="relative">{children}</div>
    </div>
  )
}

export function ChatAvatar({ children, size = 44 }: { children: ReactNode; size?: number }) {
  return (
    <span
      aria-hidden
      className="flex shrink-0 items-center justify-center rounded-full bg-white/90 font-heading font-bold text-[#0b5f63] ring-2 ring-white/60"
      style={{ width: size, height: size, fontSize: size * 0.52 }}
    >
      {children}
    </span>
  )
}

export function BackIcon() {
  return (
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M19 12H5M11 6l-6 6 6 6" />
    </svg>
  )
}

export function SendIcon() {
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M21 3 10.5 13.5M21 3l-6.5 18-4-7.5L3 9.5 21 3Z" />
    </svg>
  )
}
