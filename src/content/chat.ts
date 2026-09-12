import { useEffect, useState } from 'react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { supabase } from '../lib/supabaseClient'
import type { Message } from '../types/content'

/** Gets (or creates, on first contact) the one conversation for this child.
 * RLS on conversations/get_or_create_conversation already restricts this to
 * the child themself or their own parent -- see migration 026/027. */
export function useConversation(childId: string | null) {
  return useQuery({
    queryKey: ['conversation', childId],
    enabled: !!childId,
    queryFn: async () => {
      const { data, error } = await supabase.rpc('get_or_create_conversation', {
        p_child_id: childId as string,
      })
      if (error) throw error
      return data as string
    },
  })
}

/** Message history for a conversation, plus a realtime subscription that
 * appends new rows as they arrive (Supabase enforces the same SELECT RLS on
 * postgres_changes, so this can't leak another conversation's messages). */
export function useMessages(conversationId: string | null) {
  const queryClient = useQueryClient()
  const queryKey = ['messages', conversationId]

  const query = useQuery({
    queryKey,
    enabled: !!conversationId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('messages')
        .select('*')
        .eq('conversation_id', conversationId as string)
        .order('created_at')
      if (error) throw error
      return data as Message[]
    },
  })

  useEffect(() => {
    if (!conversationId) return
    const channel = supabase
      .channel(`messages:${conversationId}`)
      .on(
        'postgres_changes',
        { event: 'INSERT', schema: 'public', table: 'messages', filter: `conversation_id=eq.${conversationId}` },
        (payload) => {
          queryClient.setQueryData<Message[]>(queryKey, (old) => {
            const next = payload.new as Message
            if (old?.some((m) => m.id === next.id)) return old
            return [...(old ?? []), next]
          })
        },
      )
      .subscribe()

    return () => {
      supabase.removeChannel(channel)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [conversationId])

  return query
}

export async function sendMessage(conversationId: string, senderId: string, body: string) {
  const trimmed = body.trim()
  if (!trimmed) return
  const { error } = await supabase
    .from('messages')
    .insert({ conversation_id: conversationId, sender_id: senderId, body: trimmed })
  if (error) throw error
}

/** Marks every message NOT sent by `myId` as read. */
export async function markConversationRead(conversationId: string, myId: string) {
  await supabase
    .from('messages')
    .update({ read_at: new Date().toISOString() })
    .eq('conversation_id', conversationId)
    .neq('sender_id', myId)
    .is('read_at', null)
}

/** Unread-message count across (for a parent) all their children's
 * conversations, or (for a child) their own one conversation -- used for the
 * Chat tab's badge. `childIds` is every child conversation this viewer can
 * see; RLS still applies underneath regardless. */
export function useUnreadCount(myId: string | null, conversationIds: string[]) {
  const [count, setCount] = useState(0)

  const query = useQuery({
    queryKey: ['unreadCount', myId, conversationIds],
    enabled: !!myId && conversationIds.length > 0,
    queryFn: async () => {
      const { count, error } = await supabase
        .from('messages')
        .select('id', { count: 'exact', head: true })
        .in('conversation_id', conversationIds)
        .neq('sender_id', myId as string)
        .is('read_at', null)
      if (error) throw error
      return count ?? 0
    },
  })

  useEffect(() => {
    setCount(query.data ?? 0)
  }, [query.data])

  useEffect(() => {
    if (!myId || conversationIds.length === 0) return
    const channel = supabase
      .channel(`unread:${myId}`)
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'messages' }, () => {
        query.refetch()
      })
      .subscribe()
    return () => {
      supabase.removeChannel(channel)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [myId, conversationIds.join(',')])

  return count
}
