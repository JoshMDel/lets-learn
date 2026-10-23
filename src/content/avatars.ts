import { useQuery } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import { AVATAR_EMOJI, avatarForId } from '../lib/avatar'

/** The emoji each child picked on their Profile screen (child_state.avatar_key),
 * falling back to the same deterministic default used everywhere else. */
export function useChildAvatars(childIds: string[]) {
  const { data } = useQuery({
    queryKey: ['childAvatars', childIds],
    enabled: childIds.length > 0,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_state')
        .select('child_id, avatar_key')
        .in('child_id', childIds)
      if (error) throw error
      return new Map((data ?? []).map((s) => [s.child_id as string, s.avatar_key as string]))
    },
  })
  return (childId: string) => {
    const key = data?.get(childId) ?? ''
    return AVATAR_EMOJI.includes(key) ? key : avatarForId(childId)
  }
}
