import { useLocale } from '../../i18n/LocaleContext'

export type LoginRole = 'learner' | 'parent'

/** Segmented pill toggle, modeled on the existing LocaleToggle for visual
 * and code consistency -- larger, since this is the primary choice on the
 * welcome page rather than a secondary header control. The selected state
 * is never colour-only: it also gets a filled background, bold weight, and
 * a checkmark. */
export function RoleToggle({
  value,
  onChange,
}: {
  value: LoginRole
  onChange: (role: LoginRole) => void
}) {
  const { t } = useLocale()

  return (
    <div
      role="group"
      aria-label={t('welcome.title')}
      className="inline-flex w-full rounded-full border border-subtle bg-surface-2 p-1 font-heading text-base font-semibold"
    >
      {(['learner', 'parent'] as const).map((role) => {
        const selected = value === role
        return (
          <button
            key={role}
            type="button"
            onClick={() => onChange(role)}
            aria-pressed={selected}
            className={`flex flex-1 items-center justify-center gap-1.5 rounded-full px-4 py-3 transition-colors ${
              selected ? 'bg-primary text-white shadow-sm' : 'text-muted hover:text-ink'
            }`}
          >
            {selected && <span aria-hidden>✓</span>}
            {t(`welcome.roleToggle.${role}`)}
          </button>
        )
      })}
    </div>
  )
}
