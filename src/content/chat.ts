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

export interface ChatSummary {
  last: Pick<Message, 'sender_id' | 'body' | 'created_at'> | null
  unread: number
}

/** For the parent's "Messages" list: each child's latest message and unread
 * count, keyed by child id. Children with no conversation yet are simply
 * absent. Looks at the 500 newest messages, which is plenty for a preview. */
export function useChatSummaries(myId: string | null, childIds: string[]) {
  const queryClient = useQueryClient()

  const query = useQuery({
    queryKey: ['chatSummaries', myId, childIds],
    enabled: !!myId && childIds.length > 0,
    queryFn: async () => {
      const { data: convs, error: cErr } = await supabase
        .from('conversations')
        .select('id, child_id')
        .in('child_id', childIds)
      if (cErr) throw cErr
      const result = new Map<string, ChatSummary>()
      const childByConv = new Map((convs ?? []).map((c) => [c.id as string, c.child_id as string]))
      if (childByConv.size === 0) return result

      const { data: msgs, error: mErr } = await supabase
        .from('messages')
        .select('conversation_id, sender_id, body, created_at, read_at')
        .in('conversation_id', [...childByConv.keys()])
        .order('created_at', { ascending: false })
        .limit(500)
      if (mErr) throw mErr

      for (const childId of childByConv.values()) result.set(childId, { last: null, unread: 0 })
      for (const m of msgs ?? []) {
        const summary = result.get(childByConv.get(m.conversation_id) as string)
        if (!summary) continue
        if (!summary.last) summary.last = { sender_id: m.sender_id, body: m.body, created_at: m.created_at }
        if (m.sender_id !== myId && !m.read_at) summary.unread += 1
      }
      return result
    },
  })

  useEffect(() => {
    if (!myId || childIds.length === 0) return
    const channel = supabase
      .channel(`chatSummaries:${myId}`)
      .on('postgres_changes', { event: '*', schema: 'public', table: 'messages' }, () => {
        queryClient.invalidateQueries({ queryKey: ['chatSummaries'] })
      })
      .subscribe()
    return () => {
      supabase.removeChannel(channel)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [myId, childIds.join(',')])

  return query
}
