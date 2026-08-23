import { useLocale } from '../../i18n/LocaleContext'

export function LocaleToggle() {
  const { locale, setLocale, t } = useLocale()
  return (
    <div
      role="group"
      aria-label="Interface language"
      className="inline-flex rounded-full border border-subtle bg-surface-2 p-1 text-sm font-heading font-semibold"
    >
      {(['en', 'af'] as const).map((l) => (
        <button
          key={l}
          onClick={() => setLocale(l)}
          aria-pressed={locale === l}
          className={`rounded-full px-3 py-1.5 transition-colors ${
            locale === l ? 'bg-primary text-white' : 'text-muted hover:text-ink'
          }`}
        >
          {t(`locale.toggle.${l}`)}
        </button>
      ))}
    </div>
  )
}
