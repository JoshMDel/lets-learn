export const AVATAR_EMOJI = ['🦊', '🐸', '🐼', '🦁', '🐨', '🦉', '🐙', '🦄']

/** Deterministic default avatar from a child's id, used before they've
 * picked one of their own on the Profile screen. */
export function avatarForId(id: string) {
  let hash = 0
  for (const c of id) hash = (hash * 31 + c.charCodeAt(0)) % AVATAR_EMOJI.length
  return AVATAR_EMOJI[Math.abs(hash) % AVATAR_EMOJI.length]
}
