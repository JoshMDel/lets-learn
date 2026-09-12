import { useState } from 'react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { LearningLayout } from '../../components/LearningLayout'
import { Card } from '../../components/ui/Card'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { useMyRewards } from '../../content/queries'
import { formatRands } from '../../lib/currency'
import { AVATAR_EMOJI, avatarForId } from '../../lib/avatar'
import { supabase } from '../../lib/supabaseClient'
import type { ChildProfile, ChildState } from '../../types/content'

// The first learner-facing profile screen -- read-only identity (parent-
// managed, unchanged) plus a self-serve avatar picker, which was already
// permitted by child_state's existing RLS before this phase.
export default function Profile() {
  const { t } = useLocale()
  const { activeChildId } = useAuth()
  const queryClient = useQueryClient()
  const [saved, setSaved] = useState(false)

  const { data: child } = useQuery({
    queryKey: ['activeChildProfile', activeChildId],
    enabled: !!activeChildId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_profiles')
        .select('*')
        .eq('id', activeChildId as string)
        .single()
      if (error) throw error
      return data as ChildProfile
    },
  })

  const { data: childState } = useQuery({
    queryKey: ['childState', activeChildId],
    enabled: !!activeChildId,
    queryFn: async () => {
      const { data, error } = await supabase
        .from('child_state')
        .select('*')
        .eq('child_id', activeChildId as string)
        .maybeSingle()
      if (error) throw error
      return data as ChildState | null
    },
  })

  const { data: rewards } = useMyRewards(activeChildId)

  async function chooseAvatar(emoji: string) {
    if (!activeChildId) return
    await supabase
      .from('child_state')
      .upsert({ child_id: activeChildId, avatar_key: emoji }, { onConflict: 'child_id' })
    await queryClient.invalidateQueries({ queryKey: ['childState', activeChildId] })
    setSaved(true)
    setTimeout(() => setSaved(false), 2000)
  }

  const currentAvatar =
    childState?.avatar_key && AVATAR_EMOJI.includes(childState.avatar_key)
      ? childState.avatar_key
      : activeChildId
        ? avatarForId(activeChildId)
        : AVATAR_EMOJI[0]

  return (
    <LearningLayout title={t('profile.title')} bottomNav={{ active: 'profile' }}>
      <h1 className="mb-6 font-heading text-2xl font-bold">{t('profile.title')}</h1>

      <Card className="mb-4 flex flex-col items-center gap-2 text-center">
        <span className="text-6xl">{currentAvatar}</span>
        <span className="font-heading text-xl font-bold">{child?.display_name}</span>
      </Card>

      <Card className="mb-4">
        <dl className="flex flex-col gap-3 text-sm">
          <div className="flex justify-between">
            <dt className="text-muted">{t('profile.grade')}</dt>
            <dd className="font-semibold">{child?.grade}</dd>
          </div>
          <div className="flex justify-between">
            <dt className="text-muted">{t('profile.username')}</dt>
            <dd className="font-semibold">@{child?.username}</dd>
          </div>
        </dl>
      </Card>

      <Card className="mb-4">
        <h2 className="mb-3 font-heading text-lg font-bold">🏆 {t('rewards.myRewards')}</h2>
        <div className="font-heading text-3xl font-bold text-primary">{formatRands(rewards?.total ?? 0)}</div>
        <p className="mt-1 text-sm text-muted">{t('rewards.testsPassedCount', { count: rewards?.testsPassed ?? 0 })}</p>
        <p className="mt-2 text-xs text-muted">{t('rewards.earnExplainer')} {t('rewards.dailyExplainer')}</p>
      </Card>

      <Card>
        <h2 className="mb-3 font-heading text-lg font-bold">{t('profile.avatarLabel')}</h2>
        <div className="grid grid-cols-4 gap-3">
          {AVATAR_EMOJI.map((emoji) => (
            <button
              key={emoji}
              onClick={() => chooseAvatar(emoji)}
              aria-pressed={currentAvatar === emoji}
              aria-label={emoji}
              className={`flex h-14 items-center justify-center rounded-[var(--radius-lg)] border-2 text-3xl transition-colors ${
                currentAvatar === emoji ? 'border-primary bg-primary/10' : 'border-subtle bg-surface'
              }`}
            >
              {emoji}
            </button>
          ))}
        </div>
        {saved && <p className="mt-3 text-sm font-semibold text-success">{t('profile.saved')}</p>}
      </Card>
    </LearningLayout>
  )
}
