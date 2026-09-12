import { LearningLayout } from '../../components/LearningLayout'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { ChatConversation } from '../chat/ChatConversation'

export default function Chat() {
  const { t } = useLocale()
  const { activeChildId, session } = useAuth()

  return (
    <LearningLayout title={t('chat.title')} bottomNav={{ active: 'chat' }}>
      <h1 className="mb-4 font-heading text-2xl font-bold">{t('chat.title')}</h1>
      {activeChildId && session && (
        <ChatConversation childId={activeChildId} viewerId={session.user.id} />
      )}
    </LearningLayout>
  )
}
