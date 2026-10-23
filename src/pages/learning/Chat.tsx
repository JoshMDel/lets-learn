import { LearningLayout } from '../../components/LearningLayout'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { ChatConversation } from '../chat/ChatConversation'

export default function Chat() {
  const { t } = useLocale()
  const { activeChildId, session } = useAuth()

  return (
    <LearningLayout title={t('chat.title')} bottomNav={{ active: 'chat' }} chat>
      {activeChildId && session && (
        <ChatConversation
          childId={activeChildId}
          viewerId={session.user.id}
          peerName={t('chat.parentTeacher')}
          peerAvatar="👤"
          backTo="/home"
        />
      )}
    </LearningLayout>
  )
}
