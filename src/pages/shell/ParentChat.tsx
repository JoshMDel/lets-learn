import { useParams, Navigate, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { ShellLayout } from '../../components/ShellLayout'
import { Card } from '../../components/ui/Card'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'
import { ChatConversation } from '../chat/ChatConversation'
import type { ChildProfile } from '../../types/content'

/** Handles both /parent/chat (picker, or straight through if there's only
 * one child) and /parent/chat/:childId (the actual conversation) -- reuses
 * the same children-list query as ParentHome/SwitchProfile rather than a
 * new one. */
export default function ParentChat() {
  const { t } = useLocale()
  const { session } = useAuth()
  const { childId } = useParams<{ childId?: string }>()

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

  if (!childId && !isLoading && (children ?? []).length === 1) {
    return <Navigate to={`/parent/chat/${children![0].id}`} replace />
  }

  const activeChild = (children ?? []).find((c) => c.id === childId)

  return (
    <ShellLayout narrow={!!childId} bottomNav={{ active: 'chat' }}>
      <h1 className="mb-4 font-heading text-2xl font-bold">
        {activeChild ? `${t('chat.title')} · ${activeChild.display_name}` : t('chat.title')}
      </h1>

      {isLoading ? (
        <p className="text-muted">{t('common.loading')}</p>
      ) : childId && activeChild && session ? (
        <ChatConversation childId={childId} viewerId={session.user.id} />
      ) : childId ? (
        <p className="text-muted">{t('common.error.generic')}</p>
      ) : (
        <>
          <p className="mb-4 text-muted">{t('chat.pickChild')}</p>
          <div className="grid gap-3 sm:grid-cols-2">
            {(children ?? []).map((child) => (
              <Card key={child.id} className="flex items-center justify-between">
                <span className="font-heading font-semibold">{child.display_name}</span>
                <Link
                  to={`/parent/chat/${child.id}`}
                  className="rounded-full bg-primary/10 px-4 py-2 text-sm font-semibold text-primary hover:bg-primary/20"
                >
                  {t('chat.title')}
                </Link>
              </Card>
            ))}
          </div>
        </>
      )}
    </ShellLayout>
  )
}
