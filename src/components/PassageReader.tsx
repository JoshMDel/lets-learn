import { useMemo, useState } from 'react'
import type { ContentLanguage, GlossaryTerm, PassageSentence } from '../types/content'
import { speak } from '../lib/tts'
import { useLocale } from '../i18n/LocaleContext'

function normalize(word: string) {
  return word.toLowerCase().replace(/[^\p{L}'-]/gu, '')
}

export function PassageReader({
  sentences,
  glossary,
  language,
}: {
  sentences: PassageSentence[]
  glossary: GlossaryTerm[]
  language: ContentLanguage
}) {
  const { t } = useLocale()
  const [activeTerm, setActiveTerm] = useState<GlossaryTerm | null>(null)

  const glossaryMap = useMemo(() => {
    const map = new Map<string, GlossaryTerm>()
    for (const g of glossary) map.set(normalize(g.term), g)
    return map
  }, [glossary])

  return (
    <div>
      <p className="mb-4 text-sm text-muted">{t('read.tapWordHint')}</p>
      <div className="space-y-4 rounded-[var(--radius-lg)] border border-subtle bg-surface p-6 text-lg leading-relaxed">
        {sentences.map((sentence) => (
          <p key={sentence.id}>
            {sentence.text.split(/(\s+)/).map((token, i) => {
              if (/^\s+$/.test(token)) return token
              const clean = normalize(token)
              const glossEntry = glossaryMap.get(clean)
              return (
                <button
                  key={i}
                  type="button"
                  onClick={() => {
                    speak(clean || token, language)
                    if (glossEntry) setActiveTerm(glossEntry)
                  }}
                  className={`rounded px-0.5 py-0.5 transition-colors hover:bg-primary/15 focus-visible:bg-primary/15 ${
                    glossEntry ? 'underline decoration-primary decoration-2 decoration-dotted underline-offset-4' : ''
                  }`}
                >
                  {token}
                </button>
              )
            })}
          </p>
        ))}
      </div>

      {activeTerm && (
        <div
          role="dialog"
          aria-modal="true"
          aria-labelledby="glossary-term-title"
          className="fixed inset-0 z-20 flex items-end justify-center bg-black/40 p-4 sm:items-center"
          onClick={() => setActiveTerm(null)}
        >
          <div
            className="w-full max-w-sm rounded-[var(--radius-lg)] bg-surface p-6 shadow-xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="mb-2 flex items-center justify-between">
              <h3 id="glossary-term-title" className="font-heading text-xl font-bold text-primary">
                {activeTerm.term}
              </h3>
              <button
                onClick={() => speak(activeTerm.term, language)}
                aria-label={t('read.listen')}
                className="rounded-full p-2 hover:bg-surface-2"
              >
                🔊
              </button>
            </div>
            <p className="mb-6 text-base text-ink">{activeTerm.definition}</p>
            <button
              onClick={() => setActiveTerm(null)}
              className="w-full rounded-full bg-surface-2 py-3 font-heading font-semibold text-ink hover:bg-primary/10"
            >
              {t('glossary.close')}
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
