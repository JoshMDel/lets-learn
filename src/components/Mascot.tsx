export type MascotMood = 'building' | 'confident' | 'encouraging' | 'celebrating'

const MOOD_COLOR: Record<MascotMood, string> = {
  building: '#1f9c8f',
  confident: '#17b3a3',
  encouraging: '#ff8a3d',
  celebrating: '#ffb84d',
}

/** Derives a mood from recent quiz performance -- deterministic thresholds,
 * not literally "AI", but gives the adaptive-difficulty loop a visual and
 * emotional anchor the way the brief asks for. */
export function moodFromPerformance(opts: { justMastered?: boolean; recentAccuracy?: number | null }): MascotMood {
  if (opts.justMastered) return 'celebrating'
  if (opts.recentAccuracy == null) return 'building'
  if (opts.recentAccuracy < 0.5) return 'encouraging'
  if (opts.recentAccuracy >= 0.85) return 'confident'
  return 'building'
}

export function Mascot({ mood = 'building', size = 96 }: { mood?: MascotMood; size?: number }) {
  const color = MOOD_COLOR[mood]
  const bounce = mood === 'celebrating'
  const eyesClosed = mood === 'celebrating'

  return (
    <div
      className={bounce ? 'animate-bounce' : ''}
      style={{ width: size, height: size }}
      role="img"
      aria-label={`Learning buddy, feeling ${mood.replace('_', ' ')}`}
    >
      <svg viewBox="0 0 120 120" width={size} height={size} xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="60" cy="108" rx="34" ry="6" fill="#000" opacity="0.08" />
        <circle cx="60" cy="60" r="46" fill={color} style={{ transition: 'fill 0.4s ease' }} />
        <circle cx="60" cy="60" r="46" fill="url(#mascot-shine)" opacity="0.35" />
        <defs>
          <radialGradient id="mascot-shine" cx="35%" cy="30%" r="60%">
            <stop offset="0%" stopColor="#fff" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#fff" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* ears / antennae give it a friendly critter silhouette */}
        <circle cx="30" cy="26" r="9" fill={color} />
        <circle cx="90" cy="26" r="9" fill={color} />

        {eyesClosed ? (
          <>
            <path d="M42 58 Q48 52 54 58" stroke="#26313a" strokeWidth="4" fill="none" strokeLinecap="round" />
            <path d="M66 58 Q72 52 78 58" stroke="#26313a" strokeWidth="4" fill="none" strokeLinecap="round" />
          </>
        ) : (
          <>
            <circle cx="48" cy="58" r="6" fill="#26313a" />
            <circle cx="72" cy="58" r="6" fill="#26313a" />
          </>
        )}

        {mood === 'encouraging' ? (
          <path d="M46 78 Q60 72 74 78" stroke="#26313a" strokeWidth="4" fill="none" strokeLinecap="round" />
        ) : (
          <path d="M46 76 Q60 90 74 76" stroke="#26313a" strokeWidth="4" fill="none" strokeLinecap="round" />
        )}

        {mood === 'celebrating' && (
          <>
            <text x="14" y="24" fontSize="18">✨</text>
            <text x="92" y="102" fontSize="18">✨</text>
          </>
        )}
      </svg>
    </div>
  )
}
