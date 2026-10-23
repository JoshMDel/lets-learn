import { useEffect, useRef, useState, type ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'
import { useQueryClient } from '@tanstack/react-query'
import { Lumi } from '../../components/Lumi'
import { BackIcon, ChatAvatar, ChatCard, ChatFooter, ChatHeader, SendIcon } from '../../components/chat/ChatParts'
import { useLocale } from '../../i18n/LocaleContext'
import { useConversation, useMessages, sendMessage, markConversationRead } from '../../content/chat'
import type { Message } from '../../types/content'

function dayKey(iso: string) {
  const d = new Date(iso)
  return `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`
}

/** The actual chat UI, shared by both the learner's /chat and the parent's
 * /parent/chat/:childId -- only the wrapping page (layout, who the other
 * person is, where "back" goes) differs between the two roles. */
export function ChatConversation({
  childId,
  viewerId,
  peerName,
  peerSubtitle,
  peerAvatar,
  backTo,
}: {
  childId: string
  viewerId: string
  peerName: string
  peerSubtitle?: string
  peerAvatar: ReactNode
  backTo: string
}) {
  const { t, locale } = useLocale()
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const { data: conversationId, isLoading: loadingConversation } = useConversation(childId)
  const { data: messages, isLoading: loadingMessages } = useMessages(conversationId ?? null)
  const [draft, setDraft] = useState('')
  const [sending, setSending] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ block: 'end' })
  }, [messages?.length])

  useEffect(() => {
    if (!conversationId) return
    markConversationRead(conversationId, viewerId).then(() => {
      // keep the unread dots / list badges in step with what was just read
      queryClient.invalidateQueries({ queryKey: ['unreadCount'] })
      queryClient.invalidateQueries({ queryKey: ['chatSummaries'] })
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [conversationId, viewerId, messages?.length])

  async function handleSend() {
    if (!conversationId || !draft.trim()) return
    setSending(true)
    try {
      await sendMessage(conversationId, viewerId, draft)
      setDraft('')
    } finally {
      setSending(false)
    }
  }

  function dayLabel(iso: string) {
    const now = new Date()
    const yesterday = new Date()
    yesterday.setDate(now.getDate() - 1)
    if (dayKey(iso) === dayKey(now.toISOString())) return t('chat.today')
    if (dayKey(iso) === dayKey(yesterday.toISOString())) return t('chat.yesterday')
    return new Date(iso).toLocaleDateString(locale, { day: 'numeric', month: 'long', year: 'numeric' })
  }

  const loading = loadingConversation || loadingMessages
  const list: Message[] = messages ?? []

  return (
    <ChatCard>
      <ChatHeader>
        <div className="flex items-center gap-3">
          <button
            onClick={() => navigate(backTo)}
            aria-label={t('chat.back')}
            className="-ml-2 flex h-11 w-11 shrink-0 items-center justify-center rounded-full hover:bg-white/15"
          >
            <BackIcon />
          </button>
          <ChatAvatar>{peerAvatar}</ChatAvatar>
          <div className="min-w-0">
            <h1 className="truncate font-heading text-lg font-bold leading-tight">{peerName}</h1>
            {peerSubtitle && <p className="truncate text-xs text-white/80">{peerSubtitle}</p>}
          </div>
        </div>
      </ChatHeader>

      <div className="flex-1 overflow-y-auto px-4 pb-3 pt-1">
        {loading ? (
          <p className="pt-6 text-center text-sm text-muted">{t('chat.loading')}</p>
        ) : list.length === 0 ? (
          <div className="flex flex-col items-center gap-3 pt-6 text-center">
            <Lumi pose="welcome" width={110} animation="enter" />
            <p className="text-sm text-muted">{t('chat.empty')}</p>
          </div>
        ) : (
          <div className="flex flex-col gap-2.5">
            {list.map((m, i) => {
              const mine = m.sender_id === viewerId
              const showDay = i === 0 || dayKey(list[i - 1].created_at) !== dayKey(m.created_at)
              return (
                <div key={m.id} className="contents">
                  {showDay && (
                    <p className="my-2 text-center font-heading text-sm font-semibold text-[var(--chat-in-ink)]">
                      {dayLabel(m.created_at)}
                    </p>
                  )}
                  <div className={`flex ${mine ? 'justify-end' : 'justify-start'}`}>
                    <div
                      className={`max-w-[78%] rounded-2xl px-3.5 py-2 text-sm shadow-sm ${
                        mine
                          ? 'rounded-br-md bg-[var(--chat-out-bg)] text-[var(--chat-out-ink)]'
                          : 'rounded-bl-md bg-[var(--chat-in-bg)] text-[var(--chat-in-ink)]'
                      }`}
                    >
                      <p className="whitespace-pre-wrap break-words">{m.body}</p>
                      <p className="mt-0.5 flex items-center justify-end gap-1 text-[10px] opacity-75">
                        {new Date(m.created_at).toLocaleTimeString(locale, { hour: '2-digit', minute: '2-digit' })}
                        {mine && (
                          <span aria-label={m.read_at ? t('chat.seen') : t('chat.sent')}>
                            {m.read_at ? '✓✓' : '✓'}
                          </span>
                        )}
                      </p>
                    </div>
                  </div>
                </div>
              )
            })}
            <div ref={bottomRef} />
          </div>
        )}
      </div>

      <ChatFooter>
        <div className="flex items-center gap-2">
          <input
            value={draft}
            onChange={(e) => setDraft(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault()
                handleSend()
              }
            }}
            placeholder={t('chat.placeholder')}
            aria-label={t('chat.placeholder')}
            className="min-h-[44px] flex-1 rounded-full bg-white px-4 py-2 text-base text-[#17383a] outline-none placeholder:text-[#7c8f91] focus:ring-2 focus:ring-white/70"
          />
          <button
            onClick={handleSend}
            disabled={sending || !draft.trim()}
            aria-label={t('chat.send')}
            className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full text-white hover:bg-white/15 disabled:opacity-50"
          >
            <SendIcon />
          </button>
        </div>
      </ChatFooter>
    </ChatCard>
  )
}
