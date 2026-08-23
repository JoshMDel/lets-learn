import { createContext, useContext, useMemo, useState, type ReactNode } from 'react'
import en from './en.json'
import af from './af.json'

export type Locale = 'en' | 'af'

const DICTS: Record<Locale, Record<string, string>> = { en, af }
const STORAGE_KEY = 'lets-learn-locale'

// IMPORTANT: this dictionary only ever translates UI chrome (buttons, labels,
// nav, errors). Reading passages, questions and glossary content are stored
// with their own authored `language` and are NEVER run through this — see
// content/README.md. Translating them would defeat the point of testing
// comprehension in a specific language.

interface LocaleContextValue {
  locale: Locale
  setLocale: (l: Locale) => void
  t: (key: string, vars?: Record<string, string | number>) => string
}

const LocaleContext = createContext<LocaleContextValue | null>(null)

function readInitialLocale(): Locale {
  if (typeof window === 'undefined') return 'en'
  const stored = window.localStorage.getItem(STORAGE_KEY)
  return stored === 'af' ? 'af' : 'en'
}

export function LocaleProvider({ children }: { children: ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(readInitialLocale)

  const setLocale = (l: Locale) => {
    setLocaleState(l)
    window.localStorage.setItem(STORAGE_KEY, l)
  }

  const value = useMemo<LocaleContextValue>(() => {
    const dict = DICTS[locale]
    const t = (key: string, vars?: Record<string, string | number>) => {
      let str = dict[key] ?? en[key as keyof typeof en] ?? key
      if (vars) {
        for (const [k, v] of Object.entries(vars)) {
          str = str.replace(`{${k}}`, String(v))
        }
      }
      return str
    }
    return { locale, setLocale, t }
  }, [locale])

  return <LocaleContext.Provider value={value}>{children}</LocaleContext.Provider>
}

export function useLocale() {
  const ctx = useContext(LocaleContext)
  if (!ctx) throw new Error('useLocale must be used within LocaleProvider')
  return ctx
}
