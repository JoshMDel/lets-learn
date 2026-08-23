import { useState, type FormEvent } from 'react'
import { ShellLayout } from '../../components/ShellLayout'
import { Button } from '../../components/ui/Button'
import { TextField } from '../../components/ui/TextField'
import { useLocale } from '../../i18n/LocaleContext'
import { useAuth } from '../../auth/AuthContext'
import { supabase } from '../../lib/supabaseClient'

export default function ParentProfile() {
  const { t } = useLocale()
  const { profile, refreshProfile } = useAuth()
  const [firstName, setFirstName] = useState(profile?.first_name ?? '')
  const [lastName, setLastName] = useState(profile?.last_name ?? '')
  const [contactNumber, setContactNumber] = useState(profile?.contact_number ?? '')
  const [bio, setBio] = useState(profile?.bio ?? '')
  const [saved, setSaved] = useState(false)
  const [submitting, setSubmitting] = useState(false)

  if (!profile) return null

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    setSubmitting(true)
    setSaved(false)
    try {
      const { error } = await supabase
        .from('profiles')
        .update({
          first_name: firstName,
          last_name: lastName,
          contact_number: contactNumber || null,
          bio: bio || null,
        })
        .eq('id', profile!.id)
      if (error) throw error
      await refreshProfile()
      setSaved(true)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <ShellLayout>
      <h1 className="font-heading text-3xl font-bold">{t('parent.profile.title')}</h1>

      <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5">
        <div className="grid grid-cols-2 gap-4">
          <TextField label={t('auth.firstName')} value={firstName} onChange={(e) => setFirstName(e.target.value)} />
          <TextField label={t('auth.lastName')} value={lastName} onChange={(e) => setLastName(e.target.value)} />
        </div>
        <TextField label={t('auth.email')} value={profile.email} disabled hint={t('parent.profile.emailFixed')} />
        <TextField
          label={t('auth.contactNumber')}
          value={contactNumber}
          onChange={(e) => setContactNumber(e.target.value)}
        />
        <div className="flex flex-col gap-1.5">
          <label className="font-heading text-sm font-semibold text-ink">{t('parent.profile.bio')}</label>
          <textarea
            value={bio}
            onChange={(e) => setBio(e.target.value)}
            rows={3}
            className="rounded-xl border-2 border-subtle bg-surface px-4 py-3 text-base text-ink outline-none focus:border-primary"
          />
          <p className="text-sm text-muted">{t('parent.profile.bioHint')}</p>
        </div>
        <Button type="submit" disabled={submitting} fullWidth>
          {submitting ? t('common.loading') : saved ? t('common.saved') : t('common.save')}
        </Button>
      </form>
    </ShellLayout>
  )
}
