import { useEffect, useRef, useState } from 'react'
import { useLocale } from '../../i18n/LocaleContext'
import { useConversation, useMessages, sendMessage, markConversationRead } from '../../content/chat'

/** The actual chat UI, shared by both the learner's /chat and the parent's
 * /parent/chat/:childId -- only the wrapping page (layout, header, bottom
 * nav) differs between the two roles. */
export function ChatConversation({ childId, viewerId }: { childId: string; viewerId: string }) {
  const { t } = useLocale()
  const { data: conversationId, isLoading: loadingConversation } = useConversation(childId)
  const { data: messages, isLoading: loadingMessages } = useMessages(conversationId ?? null)
  const [draft, setDraft] = useState('')
  const [sending, setSending] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ block: 'end' })
  }, [messages?.length])

  useEffect(() => {
    if (conversationId) markConversationRead(conversationId, viewerId)
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

  if (loadingConversation || loadingMessages) {
    return <p className="text-muted">{t('chat.loading')}</p>
  }

  return (
    <div className="flex h-[calc(100dvh-9rem)] flex-col md:h-[70vh]">
      <div className="flex-1 overflow-y-auto rounded-[var(--radius-lg)] border border-subtle bg-surface p-4">
        {(messages ?? []).length === 0 ? (
          <p className="text-center text-sm text-muted">{t('chat.empty')}</p>
        ) : (
          <div className="flex flex-col gap-3">
            {(messages ?? []).map((m) => {
              const mine = m.sender_id === viewerId
              return (
                <div key={m.id} className={`flex ${mine ? 'justify-end' : 'justify-start'}`}>
                  <div
                    className={`max-w-[75%] rounded-2xl px-4 py-2 text-sm ${
                      mine ? 'bg-primary text-white' : 'bg-surface-2 text-ink'
                    }`}
                  >
                    <p className="whitespace-pre-wrap break-words">{m.body}</p>
                    <p className={`mt-1 text-[11px] ${mine ? 'text-white/70' : 'text-muted'}`}>
                      {new Date(m.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </p>
                  </div>
                </div>
              )
            })}
            <div ref={bottomRef} />
          </div>
        )}
      </div>

      <div className="mt-3 flex items-center gap-2">
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
          className="min-h-[44px] flex-1 rounded-full border-2 border-subtle bg-surface px-4 py-2 text-base text-ink outline-none focus:border-primary"
        />
        <button
          onClick={handleSend}
          disabled={sending || !draft.trim()}
          aria-label={t('chat.send')}
          className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-primary text-white disabled:opacity-50"
        >
          ➤
        </button>
      </div>
    </div>
  )
}
