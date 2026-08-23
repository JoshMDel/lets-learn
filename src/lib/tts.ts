let voicesPromise: Promise<SpeechSynthesisVoice[]> | null = null

function loadVoices(): Promise<SpeechSynthesisVoice[]> {
  if (!('speechSynthesis' in window)) return Promise.resolve([])
  if (voicesPromise) return voicesPromise
  voicesPromise = new Promise((resolve) => {
    const existing = window.speechSynthesis.getVoices()
    if (existing.length > 0) {
      resolve(existing)
      return
    }
    window.speechSynthesis.onvoiceschanged = () => {
      resolve(window.speechSynthesis.getVoices())
    }
    // Some browsers never fire the event if there simply are none loaded yet.
    setTimeout(() => resolve(window.speechSynthesis.getVoices()), 1000)
  })
  return voicesPromise
}

function pickVoice(voices: SpeechSynthesisVoice[], lang: 'af' | 'en'): SpeechSynthesisVoice | null {
  const wanted = lang === 'af' ? 'af' : 'en'
  const exact = voices.find((v) => v.lang.toLowerCase().startsWith(`${wanted}-`))
  if (exact) return exact
  const loose = voices.find((v) => v.lang.toLowerCase().startsWith(wanted))
  return loose ?? null
}

/** Speaks a word/phrase aloud via the browser's built-in TTS. Best-effort
 * Afrikaans voice selection with a graceful fallback -- many devices simply
 * don't ship an af-ZA voice, in which case we fall back to whatever default
 * voice the browser has rather than staying silent. */
export async function speak(text: string, language: 'af' | 'en') {
  if (!('speechSynthesis' in window)) return
  window.speechSynthesis.cancel()
  const voices = await loadVoices()
  const utterance = new SpeechSynthesisUtterance(text)
  const voice = pickVoice(voices, language)
  if (voice) {
    utterance.voice = voice
    utterance.lang = voice.lang
  } else {
    utterance.lang = language === 'af' ? 'af-ZA' : 'en-ZA'
  }
  utterance.rate = 0.9
  window.speechSynthesis.speak(utterance)
}
