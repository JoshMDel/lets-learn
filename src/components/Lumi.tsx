import { useEffect, useState, type ReactNode } from 'react'

export type LumiPose = 'welcome' | 'reading' | 'celebrating' | 'thinking' | 'encouraging' | 'emptyState'

// Which artwork each pose uses. The concept sheet only has four full-body
// poses, so `reading` shares the welcome art (waving, book in hand) and
// `encouraging` shares the thinking art (hand on chin, idea bulb). When
// dedicated artwork is supplied, change the entry here -- nothing else moves.
// Files live in public/brand/lumi/ (see scripts/extract-lumi.mjs).
const ART = {
  welcome: { src: '/brand/lumi/lumi-welcome.webp', w: 579, h: 487 },
  celebrating: { src: '/brand/lumi/lumi-celebrating.webp', w: 343, h: 284 },
  thinking: { src: '/brand/lumi/lumi-thinking.webp', w: 305, h: 332 },
  pointing: { src: '/brand/lumi/lumi-pointing.webp', w: 454, h: 301 },
}

const POSE_ART: Record<LumiPose, keyof typeof ART> = {
  welcome: 'welcome',
  reading: 'welcome',
  celebrating: 'celebrating',
  thinking: 'thinking',
  encouraging: 'thinking',
  emptyState: 'pointing',
}

export type LumiAnimation = 'enter' | 'wave' | 'bounce'

/** True the first time `key` is seen in this browser session, so entrance
 * animations don't replay every time the learner navigates back to a screen.
 * With no key it is always true (used for result celebrations). */
function useFirstTime(key?: string): boolean {
  const [first] = useState(() => {
    if (!key) return true
    try {
      return !sessionStorage.getItem(`lumi-seen:${key}`)
    } catch {
      return true
    }
  })
  useEffect(() => {
    if (!key) return
    try {
      sessionStorage.setItem(`lumi-seen:${key}`, '1')
    } catch {
      // storage unavailable -- animation just may replay, which is harmless
    }
  }, [key])
  return first
}

export function Lumi({
  pose,
  width = 120,
  alt = '',
  animation,
  animateOnceKey,
  className = '',
}: {
  pose: LumiPose
  /** Rendered width in px; height follows the artwork's aspect ratio. */
  width?: number
  /** Leave empty for purely decorative use (the default). */
  alt?: string
  animation?: LumiAnimation
  /** Only play `animation` the first time this key is seen per session. */
  animateOnceKey?: string
  className?: string
}) {
  const art = ART[POSE_ART[pose]]
  const first = useFirstTime(animateOnceKey)
  const anim = animation && first ? `lumi-anim-${animation}` : ''
  return (
    <img
      src={art.src}
      width={art.w}
      height={art.h}
      alt={alt}
      aria-hidden={alt ? undefined : true}
      draggable={false}
      className={`h-auto max-w-full select-none ${anim} ${className}`}
      style={{ width }}
    />
  )
}

/** Lumi beside a short speech bubble. */
export function LumiSays({
  pose,
  children,
  size = 88,
  animation,
  animateOnceKey,
  className = '',
}: {
  pose: LumiPose
  children: ReactNode
  size?: number
  animation?: LumiAnimation
  animateOnceKey?: string
  className?: string
}) {
  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <div className="shrink-0">
        <Lumi pose={pose} width={size} animation={animation} animateOnceKey={animateOnceKey} />
      </div>
      <div className="relative rounded-[var(--radius-lg)] border border-subtle bg-surface px-4 py-3 font-heading text-sm font-medium leading-snug text-ink shadow-sm">
        <span
          aria-hidden
          className="absolute -left-1.5 top-1/2 h-3 w-3 -translate-y-1/2 rotate-45 border-b border-l border-subtle bg-surface"
        />
        {children}
      </div>
    </div>
  )
}
