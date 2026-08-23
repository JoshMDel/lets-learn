import { useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { LearningLayout } from '../../components/LearningLayout'
import { PassageReader } from '../../components/PassageReader'
import { Button } from '../../components/ui/Button'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { usePassage } from '../../content/queries'
import { setResumeState } from '../../content/resume'

export default function Read() {
  const { t } = useLocale()
  const navigate = useNavigate()
  const { tierId } = useParams<{ tierId: string }>()
  const { activeChildId } = useAuth()

  const { data, isLoading } = usePassage(tierId ?? null)

  useEffect(() => {
    if (activeChildId && tierId) {
      setResumeState(activeChildId, { tier_id: tierId, stage: 'reading' })
    }
  }, [activeChildId, tierId])

  if (isLoading || !data) {
    return (
      <LearningLayout>
        <p className="text-muted">{t('common.loading')}</p>
      </LearningLayout>
    )
  }

  return (
    <LearningLayout title={data.passage.title}>
      <h1 className="mb-4 font-heading text-2xl font-bold">{data.passage.title}</h1>
      <PassageReader sentences={data.sentences} glossary={data.glossary} language={data.passage.language} />
      <div className="mt-6">
        <Button fullWidth onClick={() => navigate(`/quiz/${tierId}`)}>
          {t('read.startQuiz')}
        </Button>
      </div>
    </LearningLayout>
  )
}
