import { useState } from 'react'
import { useParams, Navigate, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { ShellLayout } from '../../components/ShellLayout'
import { Lumi } from '../../components/Lumi'
import { ChatAvatar, ChatCard, ChatHeader } from '../../components/chat/ChatParts'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { useChatSummaries } from '../../content/chat'
import { useChildAvatars } from '../../content/avatars'
import { ChatConversation } from '../chat/ChatConversation'
import type { ChildProfile } from '../../types/content'

/** Handles both /parent/chat (the "Messages" list, or straight through if
 * there's only one child) and /parent/chat/:childId (the conversation) --
 * reuses the same children-list query as ParentHome/SwitchProfile. */
export default function ParentChat() {
  const { t, locale } = useLocale()
  const { session, profile } = useAuth()
  const { childId } = useParams<{ childId?: string }>()
  const [search, setSearch] = useState('')

  const { data: children, isLoading } = useQuery({
    queryKey: ['myChildren', session?.user.id],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_profiles')
        .select('*')
        .eq('parent_id', session!.user.id)
        .order('created_at')
      if (error) throw error
      return data as ChildProfile[]
    },
  })

  const childIds = (children ?? []).map((c) => c.id)
  const avatarFor = useChildAvatars(childIds)
  const { data: summaries } = useChatSummaries(session?.user.id ?? null, childIds)

  if (!childId && !isLoading && (children ?? []).length === 1) {
    return <Navigate to={`/parent/chat/${children![0].id}`} replace />
  }

  const activeChild = (children ?? []).find((c) => c.id === childId)

  function formatWhen(iso: string) {
    const d = new Date(iso)
    const now = new Date()
    const days = Math.round(
      (new Date(now.toDateString()).getTime() - new Date(d.toDateString()).getTime()) / 86400000,
    )
    if (days <= 0) return d.toLocaleTimeString(locale, { hour: '2-digit', minute: '2-digit' })
    if (days === 1) return t('chat.yesterday')
    if (days < 7) return d.toLocaleDateString(locale, { weekday: 'long' })
    return d.toLocaleDateString(locale, { day: 'numeric', month: 'short', year: '2-digit' })
  }

  const needle = search.trim().toLowerCase()
  const visible = (children ?? []).filter((c) => c.display_name.toLowerCase().includes(needle))

  return (
    <ShellLayout narrow bottomNav={{ active: 'chat' }} chat>
      {isLoading ? (
        <p className="p-6 text-muted">{t('common.loading')}</p>
      ) : childId && activeChild && session ? (
        <ChatConversation
          childId={childId}
          viewerId={session.user.id}
          peerName={activeChild.display_name}
          peerSubtitle={`Grade ${activeChild.grade} · @${activeChild.username}`}
          peerAvatar={avatarFor(activeChild.id)}
          backTo={(children ?? []).length > 1 ? '/parent/chat' : '/parent'}
        />
      ) : childId ? (
        <p className="p-6 text-muted">{t('common.error.generic')}</p>
      ) : (
        <ChatCard>
          <ChatHeader>
            <div className="flex items-center justify-between">
              <h1 className="font-heading text-2xl font-bold">{t('chat.messages')}</h1>
              <ChatAvatar size={38}>{(profile?.first_name ?? '?').charAt(0).toUpperCase()}</ChatAvatar>
            </div>
            <label className="mt-4 flex items-center gap-2 rounded-lg bg-white px-3 py-2 text-[#17383a]">
              <svg
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2.2"
                strokeLinecap="round"
                aria-hidden
              >
                <circle cx="11" cy="11" r="7" />
                <path d="m20 20-3.5-3.5" />
              </svg>
              <input
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder={t('chat.search')}
                aria-label={t('chat.search')}
                className="min-h-[28px] w-full bg-transparent text-base outline-none placeholder:text-[#7c8f91]"
              />
            </label>
          </ChatHeader>

          <div className="flex-1 overflow-y-auto px-5 pb-4">
            <h2 className="mb-1 font-heading text-lg font-bold text-[var(--chat-in-ink)]">{t('chat.recent')}</h2>
            {(children ?? []).length === 0 ? (
              <div className="flex flex-col items-center gap-3 pt-6 text-center">
                <Lumi pose="emptyState" width={140} />
                <p className="text-sm text-muted">{t('lumi.parent.noLearners')}</p>
              </div>
            ) : visible.length === 0 ? (
              <p className="pt-4 text-sm text-muted">{t('chat.noResults')}</p>
            ) : (
              <ul>
                {visible.map((child) => {
                  const s = summaries?.get(child.id)
                  return (
                    <li key={child.id} className="border-b border-subtle last:border-0">
                      <Link to={`/parent/chat/${child.id}`} className="flex items-center gap-3 py-3.5">
                        <span
                          aria-hidden
                          className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[var(--chat-in-bg)] text-2xl"
                        >
                          {avatarFor(child.id)}
                        </span>
                        <span className="min-w-0 flex-1">
                          <span className="block truncate font-heading font-semibold text-[var(--chat-in-ink)]">
                            {child.display_name}
                          </span>
                          <span
                            className={`block truncate text-sm ${s?.unread ? 'font-medium text-ink' : 'text-muted'}`}
                          >
                            {s?.last ? s.last.body : t('chat.noMessagesYet')}
                          </span>
                        </span>
                        <span className="flex shrink-0 flex-col items-end gap-1">
                          <span className="text-xs text-muted">{s?.last ? formatWhen(s.last.created_at) : ''}</span>
                          {s && s.unread > 0 && (
                            <span
                              aria-label={`${s.unread} ${t('chat.unread')}`}
                              className="flex h-5 min-w-5 items-center justify-center rounded-full bg-danger px-1.5 text-[11px] font-bold text-white"
                            >
                              {s.unread}
                            </span>
                          )}
                        </span>
                      </Link>
                    </li>
                  )
                })}
              </ul>
            )}
          </div>
        </ChatCard>
      )}
    </ShellLayout>
  )
}
