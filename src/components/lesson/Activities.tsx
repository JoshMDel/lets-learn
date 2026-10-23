import { useState, type ReactNode } from 'react'
import { useQueryClient } from '@tanstack/react-query'
import { Button } from '../ui/Button'
import { useLocale } from '../../i18n/LocaleContext'
import { speak } from '../../lib/tts'
import { checkLessonItem } from '../../content/lessons'
import type { CheckResult, Choice, LessonItem, LessonResponse } from '../../types/lessons'

interface ActivityProps {
  item: LessonItem
  childId: string
  saved?: LessonResponse
}

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

/** Shared plumbing: submit -> latest result -> cache refresh. */
function useActivity(childId: string, itemId: string) {
  const queryClient = useQueryClient()
  const [result, setResult] = useState<CheckResult | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState(false)

  async function submit(response: Record<string, unknown>) {
    setBusy(true)
    setError(false)
    try {
      const r = await checkLessonItem(childId, itemId, response)
      setResult(r)
      queryClient.invalidateQueries({ queryKey: ['lessonResponses'] })
      return r
    } catch {
      setError(true)
      return null
    } finally {
      setBusy(false)
    }
  }
  return { result, busy, error, submit }
}

export function ActivityCard({ item, children }: { item: LessonItem; children: ReactNode }) {
  const { t } = useLocale()
  return (
    <section className="rounded-[var(--radius-lg)] border border-subtle bg-surface p-5 shadow-sm">
      <header className="mb-3 flex flex-wrap items-center gap-2">
        {item.title_af && <h3 className="font-heading text-lg font-bold">{item.title_af}</h3>}
        <span
          className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ${
            item.source === 'workbook' ? 'bg-primary/10 text-primary' : 'bg-accent/15 text-ink'
          }`}
        >
          {item.source === 'workbook' ? t('lesson.source.workbook') : t('lesson.source.supplementary')}
        </span>
        {item.workbook_ref?.printed_page != null && (
          <span className="text-xs text-muted">
            {t('lesson.workbookPage', { page: item.workbook_ref.printed_page })}
          </span>
        )}
      </header>
      {children}
    </section>
  )
}

function AnswerStatusNote({ status }: { status: CheckResult['answer_status'] }) {
  const { t } = useLocale()
  if (!status) return null
  return (
    <p className="mt-2 text-xs text-muted">
      {status === 'official' ? t('lesson.suggested.official') : t('lesson.suggested.derived')}
    </p>
  )
}

function Feedback({ result, correctText }: { result: CheckResult; correctText?: ReactNode }) {
  const { t } = useLocale()
  if (result.correct === null) return null
  return (
    <div
      role="status"
      className={`mt-4 rounded-xl border-2 p-4 text-sm ${
        result.correct ? 'border-success/40 bg-success/5' : 'border-danger/40 bg-danger/5'
      }`}
    >
      <p className={`font-heading font-semibold ${result.correct ? 'text-success' : 'text-danger'}`}>
        {result.correct ? `✅ ${t('lesson.correct')}` : `❌ ${t('lesson.notQuite')} ${result.attempts < 2 ? t('lesson.tryAgain') : ''}`}
      </p>
      {result.message && <p className="mt-1">{result.message}</p>}
      {correctText && (
        <p className="mt-2">
          <span className="font-semibold">{t('lesson.correctAnswer')}: </span>
          {correctText}
        </p>
      )}
      {result.explanation && (
        <p className="mt-2">
          <span className="font-semibold">{t('results.why')}: </span>
          {result.explanation}
        </p>
      )}
      <AnswerStatusNote status={result.answer_status} />
    </div>
  )
}

function ErrorLine({ show }: { show: boolean }) {
  const { t } = useLocale()
  return show ? <p className="mt-3 text-sm font-medium text-danger">{t('common.error.generic')}</p> : null
}

function Prompt({ children }: { children: ReactNode }) {
  return <p className="mb-3 whitespace-pre-line text-base font-medium leading-relaxed">{children}</p>
}

/* ---------------------------------------------------------------- mcq */
export function McqActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const options = (item.payload.options ?? []) as Choice[]
  const [choice, setChoice] = useState<string | null>((saved?.response.choice as string) ?? null)
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const correctKey = (result?.correct_answer?.choice as string | undefined) ?? null

  return (
    <div>
      <Prompt>{item.payload.prompt as string}</Prompt>
      <div className="flex flex-col gap-2">
        {options.map((o, i) => {
          const selected = choice === o.key
          const isCorrect = correctKey === o.key
          const wrongPick = result && result.correct === false && selected
          return (
            <button
              key={o.key}
              type="button"
              disabled={done}
              aria-pressed={selected}
              onClick={() => setChoice(o.key)}
              className={`flex items-center gap-3 rounded-xl border-2 p-3 text-left transition-colors ${
                isCorrect
                  ? 'border-success bg-success/10'
                  : wrongPick
                    ? 'border-danger bg-danger/5'
                    : selected
                      ? 'border-primary bg-primary/10'
                      : 'border-subtle bg-surface hover:border-primary/50'
              }`}
            >
              <span
                className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full border-2 text-sm font-bold ${
                  selected ? 'border-primary bg-primary text-white' : 'border-subtle'
                }`}
                aria-hidden
              >
                {LETTERS[i]}
              </span>
              {o.text}
            </button>
          )
        })}
      </div>
      {!done && (
        <Button className="mt-4" disabled={!choice || busy} onClick={() => submit({ choice })}>
          {t('lesson.check')}
        </Button>
      )}
      {result && (
        <Feedback
          result={result}
          correctText={correctKey ? options.find((o) => o.key === correctKey)?.text : undefined}
        />
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* ---------------------------------------------------------- true/false */
export function TrueFalseActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const [value, setValue] = useState<boolean | null>(
    typeof saved?.response.value === 'boolean' ? (saved.response.value as boolean) : null,
  )
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const correctValue = result?.correct_answer?.value as boolean | undefined

  return (
    <div>
      <Prompt>{item.payload.statement as string}</Prompt>
      <div className="grid grid-cols-2 gap-3">
        {[true, false].map((v) => {
          const selected = value === v
          const isCorrect = correctValue === v
          return (
            <button
              key={String(v)}
              type="button"
              disabled={done}
              aria-pressed={selected}
              onClick={() => setValue(v)}
              className={`rounded-xl border-2 p-3 font-heading font-semibold transition-colors ${
                isCorrect
                  ? 'border-success bg-success/10'
                  : selected
                    ? 'border-primary bg-primary/10'
                    : 'border-subtle hover:border-primary/50'
              }`}
            >
              {v ? t('lesson.true') : t('lesson.false')}
            </button>
          )
        })}
      </div>
      {!done && (
        <Button className="mt-4" disabled={value === null || busy} onClick={() => submit({ value })}>
          {t('lesson.check')}
        </Button>
      )}
      {result && <Feedback result={result} />}
      <ErrorLine show={error} />
    </div>
  )
}

/* ---------------------------------------------------------- fill blank */
export function FillBlankActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const text = item.payload.text as string
  const bank = (item.payload.word_bank ?? []) as string[]
  const [answers, setAnswers] = useState<Record<string, string>>(
    ((saved?.response.answers as Record<string, string>) ?? {}),
  )
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const parts = text.split(/\{\{(\w+)\}\}/)
  const accepted = result?.correct_answer as Record<string, string[]> | undefined

  return (
    <div>
      {item.payload.prompt != null && <Prompt>{item.payload.prompt as string}</Prompt>}
      {bank.length > 0 && (
        <div className="mb-3 flex flex-wrap gap-2" aria-label={t('lesson.wordBank')}>
          {bank.map((w) => (
            <span key={w} className="rounded-full bg-surface-2 px-3 py-1 text-sm font-medium">
              {w}
            </span>
          ))}
        </div>
      )}
      <p className="whitespace-pre-line text-base leading-[2.6rem]">
        {parts.map((part, i) => {
          if (i % 2 === 0) return <span key={i}>{part}</span>
          const ok = result?.detail.blanks?.[part]
          return (
            <input
              key={i}
              value={answers[part] ?? ''}
              disabled={done}
              onChange={(e) => setAnswers((a) => ({ ...a, [part]: e.target.value }))}
              aria-label={`${t('lesson.blank')} ${part}`}
              autoCapitalize="off"
              autoCorrect="off"
              spellCheck={false}
              className={`mx-1 inline-block h-10 w-36 rounded-lg border-2 bg-surface px-2 text-center text-base outline-none ${
                ok === true ? 'border-success' : ok === false ? 'border-danger' : 'border-subtle focus:border-primary'
              }`}
            />
          )
        })}
      </p>
      {!done && (
        <Button
          className="mt-4"
          disabled={busy || Object.values(answers).every((a) => !a.trim())}
          onClick={() => submit({ answers })}
        >
          {t('lesson.check')}
        </Button>
      )}
      {result && (
        <Feedback
          result={result}
          correctText={
            accepted && result.correct === false ? (
              <span>{Object.keys(accepted).sort().map((k) => `${k}) ${accepted[k][0]}`).join('   ')}</span>
            ) : undefined
          }
        />
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* --------------------------------------------------------------- match */
export function MatchActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const left = (item.payload.left ?? []) as Choice[]
  const right = (item.payload.right ?? []) as Choice[]
  const [pairs, setPairs] = useState<Record<string, string>>(((saved?.response.pairs as Record<string, string>) ?? {}))
  const [active, setActive] = useState<string | null>(null)
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const rightLetter = (key: string) => LETTERS[right.findIndex((r) => r.key === key)]
  const leftNumber = (key: string) => left.findIndex((l) => l.key === key) + 1
  const correctPairs = (result?.correct_answer?.pairs ?? null) as Record<string, string> | null

  function pickRight(rKey: string) {
    if (done || !active) return
    setPairs((p) => {
      const next = { ...p }
      for (const k of Object.keys(next)) if (next[k] === rKey) delete next[k]
      next[active] = rKey
      return next
    })
    setActive(null)
  }

  return (
    <div>
      <Prompt>{item.payload.prompt as string}</Prompt>
      <p className="mb-3 text-sm text-muted">{t('lesson.match.hint')}</p>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-3">
        <ul className="flex flex-col gap-2">
          {left.map((l) => {
            const ok = result?.detail.pairs?.[l.key]
            return (
              <li key={l.key}>
                <button
                  type="button"
                  disabled={done}
                  onClick={() => setActive(l.key)}
                  aria-pressed={active === l.key}
                  className={`flex w-full items-center gap-2 rounded-xl border-2 p-2.5 text-left text-[13px] transition-colors sm:text-sm ${
                    ok === true
                      ? 'border-success bg-success/10'
                      : ok === false
                        ? 'border-danger bg-danger/5'
                        : active === l.key
                          ? 'border-primary bg-primary/10'
                          : 'border-subtle hover:border-primary/50'
                  }`}
                >
                  <span className="font-bold">{leftNumber(l.key)}.</span>
                  <span className="min-w-0 flex-1 break-words [hyphens:auto]" lang="af">
                    {l.text}
                  </span>
                  {pairs[l.key] && (
                    <span className="rounded-full bg-primary px-2 text-xs font-bold text-white">
                      {rightLetter(pairs[l.key])}
                    </span>
                  )}
                </button>
              </li>
            )
          })}
        </ul>
        <ul className="flex flex-col gap-2">
          {right.map((r, i) => {
            const taken = Object.entries(pairs).find(([, v]) => v === r.key)?.[0]
            return (
              <li key={r.key}>
                <button
                  type="button"
                  disabled={done || !active}
                  onClick={() => pickRight(r.key)}
                  className={`flex w-full items-center gap-2 rounded-xl border-2 p-2.5 text-left text-[13px] transition-colors sm:text-sm ${
                    taken ? 'border-primary/50 bg-primary/5' : 'border-subtle hover:border-primary/50'
                  }`}
                >
                  <span className="font-bold">{LETTERS[i]}.</span>
                  <span className="min-w-0 flex-1 break-words [hyphens:auto]" lang="af">
                    {r.text}
                  </span>
                  {taken && (
                    <span className="rounded-full bg-primary px-2 text-xs font-bold text-white">{leftNumber(taken)}</span>
                  )}
                </button>
              </li>
            )
          })}
        </ul>
      </div>
      {!done && (
        <div className="mt-4 flex gap-3">
          <Button disabled={busy || Object.keys(pairs).length < left.length} onClick={() => submit({ pairs })}>
            {t('lesson.check')}
          </Button>
          <Button variant="ghost" onClick={() => setPairs({})}>
            {t('lesson.reset')}
          </Button>
        </div>
      )}
      {result && (
        <Feedback
          result={result}
          correctText={
            correctPairs && result.correct === false ? (
              <span>
                {left.map((l) => `${leftNumber(l.key)}→${rightLetter(correctPairs[l.key])}`).join('  ')}
              </span>
            ) : undefined
          }
        />
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* --------------------------------------------------------------- order */
export function OrderActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const items = (item.payload.items ?? []) as (Choice & { image?: string })[]
  const savedSequence = saved?.response.sequence as string[] | undefined
  const [sequence, setSequence] = useState<string[]>(
    savedSequence && savedSequence.length === items.length ? savedSequence : items.map((i) => i.key),
  )
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const textOf = (key: string) => items.find((i) => i.key === key)?.text ?? key
  const imageOf = (key: string) => items.find((i) => i.key === key)?.image
  const correctSeq = (result?.correct_answer?.sequence ?? null) as string[] | null

  function move(i: number, dir: -1 | 1) {
    setSequence((s) => {
      const j = i + dir
      if (j < 0 || j >= s.length) return s
      const next = [...s]
      ;[next[i], next[j]] = [next[j], next[i]]
      return next
    })
  }

  return (
    <div>
      <Prompt>{item.payload.prompt as string}</Prompt>
      <p className="mb-3 text-sm text-muted">{t('lesson.order.hint')}</p>
      <ol className="flex flex-col gap-2">
        {sequence.map((key, i) => {
          const ok = result?.detail.positions?.[i]
          return (
            <li
              key={key}
              className={`flex items-center gap-2 rounded-xl border-2 p-2.5 text-sm ${
                ok === true ? 'border-success bg-success/10' : ok === false ? 'border-danger bg-danger/5' : 'border-subtle'
              }`}
            >
              <span className="w-6 shrink-0 text-center font-bold">{i + 1}</span>
              {imageOf(key) ? (
                <img
                  src={imageOf(key)}
                  alt={textOf(key)}
                  loading="lazy"
                  className="h-28 max-w-[60%] flex-1 rounded-lg border border-subtle object-contain"
                />
              ) : (
                <span className="flex-1">{textOf(key)}</span>
              )}
              {!done && (
                <span className="flex shrink-0 gap-1">
                  <button
                    type="button"
                    onClick={() => move(i, -1)}
                    disabled={i === 0}
                    aria-label={t('lesson.moveUp')}
                    className="flex h-9 w-9 items-center justify-center rounded-full bg-surface-2 disabled:opacity-30"
                  >
                    ↑
                  </button>
                  <button
                    type="button"
                    onClick={() => move(i, 1)}
                    disabled={i === sequence.length - 1}
                    aria-label={t('lesson.moveDown')}
                    className="flex h-9 w-9 items-center justify-center rounded-full bg-surface-2 disabled:opacity-30"
                  >
                    ↓
                  </button>
                </span>
              )}
            </li>
          )
        })}
      </ol>
      {!done && (
        <Button className="mt-4" disabled={busy} onClick={() => submit({ sequence })}>
          {t('lesson.check')}
        </Button>
      )}
      {result && (
        <Feedback
          result={result}
          correctText={
            correctSeq && result.correct === false ? (
              <ol className="mt-1 list-decimal pl-5">
                {correctSeq.map((k) => (
                  <li key={k}>{textOf(k)}</li>
                ))}
              </ol>
            ) : undefined
          }
        />
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* ------------------------------------------------------------- choices */
// A set of mini multiple-choice rows: spelling games, "tick the right column"
// tables, "choose the correct form" lists.
interface ChoiceQuestion {
  key: string
  text: string
  options: Choice[]
}

export function ChoicesActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const questions = (item.payload.questions ?? []) as ChoiceQuestion[]
  const [picked, setPicked] = useState<Record<string, string>>(
    ((saved?.response.answers as Record<string, string>) ?? {}),
  )
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = result?.correct === true
  const correct = (result?.correct_answer?.answers ?? null) as Record<string, string> | null

  return (
    <div>
      {item.payload.prompt != null && <Prompt>{item.payload.prompt as string}</Prompt>}
      <ol className="flex flex-col gap-3">
        {questions.map((qq, i) => {
          const ok = result?.detail.answers?.[qq.key]
          return (
            <li
              key={qq.key}
              className={`rounded-xl border-2 p-3 ${
                ok === true ? 'border-success/50 bg-success/5' : ok === false ? 'border-danger/50 bg-danger/5' : 'border-subtle'
              }`}
            >
              <p className="mb-2 text-base">
                <span className="mr-1 font-bold">{i + 1}.</span>
                {qq.text}
              </p>
              <div className="flex flex-wrap gap-2" role="radiogroup" aria-label={`${i + 1}`}>
                {qq.options.map((o) => {
                  const selected = picked[qq.key] === o.key
                  const isRight = correct?.[qq.key] === o.key
                  return (
                    <button
                      key={o.key}
                      type="button"
                      role="radio"
                      aria-checked={selected}
                      disabled={done}
                      onClick={() => setPicked((p) => ({ ...p, [qq.key]: o.key }))}
                      className={`min-h-[44px] rounded-full border-2 px-4 py-1.5 text-base transition-colors ${
                        isRight
                          ? 'border-success bg-success/10 font-semibold'
                          : selected
                            ? 'border-primary bg-primary/10 font-semibold'
                            : 'border-subtle hover:border-primary/50'
                      }`}
                    >
                      {o.text}
                    </button>
                  )
                })}
              </div>
            </li>
          )
        })}
      </ol>
      {!done && (
        <Button
          className="mt-4"
          disabled={busy || Object.keys(picked).length < questions.length}
          onClick={() => submit({ answers: picked })}
        >
          {t('lesson.check')}
        </Button>
      )}
      {result && <Feedback result={result} />}
      <ErrorLine show={error} />
    </div>
  )
}

/* --------------------------------------------------------- short answer */
export function ShortAnswerActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const [text, setText] = useState((saved?.response.text as string) ?? '')
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const lines = (item.payload.lines as number | undefined) ?? 2

  return (
    <div>
      <Prompt>{item.payload.prompt as string}</Prompt>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={Math.max(2, lines)}
        aria-label={t('lesson.yourAnswer')}
        className="w-full rounded-xl border-2 border-subtle bg-surface p-3 text-base outline-none focus:border-primary"
      />
      <Button className="mt-3" disabled={busy || !text.trim()} onClick={() => submit({ text })}>
        {result ? t('lesson.saveAgain') : t('lesson.save')}
      </Button>
      {result && (
        <div role="status" className="mt-4 rounded-xl border-2 border-primary/30 bg-primary/5 p-4 text-sm">
          <p className="font-heading font-semibold text-primary">✅ {t('lesson.saved')}</p>
          {result.suggested_answer && (
            <p className="mt-2">
              <span className="font-semibold">{t('lesson.suggested')}: </span>
              {result.suggested_answer}
            </p>
          )}
          {result.suggested_answer && <p className="mt-1 text-muted">{t('lesson.compareYours')}</p>}
          {result.suggested_answer && <AnswerStatusNote status={result.answer_status} />}
        </div>
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* ------------------------------------------------------------- writing */
export function WritingActivity({ item, childId, saved }: ActivityProps) {
  const { t } = useLocale()
  const checklist = (item.payload.checklist ?? []) as string[]
  const noText = item.payload.no_text === true // a pure tick-list (e.g. the workbook's “Ek kan” self-check)
  const [text, setText] = useState((saved?.response.text as string) ?? '')
  const savedTicks = saved?.response.checklist as boolean[] | undefined
  const [ticks, setTicks] = useState<boolean[]>(
    savedTicks && savedTicks.length === checklist.length ? savedTicks : checklist.map(() => false),
  )
  const { result, busy, error, submit } = useActivity(childId, item.id)

  return (
    <div>
      <Prompt>{item.payload.prompt as string}</Prompt>
      {(item.payload.tips as string[] | undefined)?.length ? (
        <ul className="mb-3 list-disc pl-5 text-sm text-muted">
          {(item.payload.tips as string[]).map((tip) => (
            <li key={tip}>{tip}</li>
          ))}
        </ul>
      ) : null}
      {!noText && (
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={(item.payload.lines as number | undefined) ?? 8}
          aria-label={t('lesson.yourWriting')}
          className="w-full rounded-xl border-2 border-subtle bg-surface p-3 text-base outline-none focus:border-primary"
        />
      )}
      {checklist.length > 0 && (
        <fieldset className="mt-4 rounded-xl bg-surface-2 p-4">
          <legend className="px-1 font-heading text-sm font-semibold">{t('lesson.writing.checklist')}</legend>
          <p className="mb-2 text-xs text-muted">{t('lesson.writing.tip')}</p>
          {checklist.map((c, i) => (
            <label key={c} className="flex min-h-[44px] items-center gap-3 text-sm">
              <input
                type="checkbox"
                checked={ticks[i] ?? false}
                onChange={(e) => setTicks((prev) => prev.map((v, j) => (j === i ? e.target.checked : v)))}
                className="h-5 w-5 accent-[var(--primary)]"
              />
              {c}
            </label>
          ))}
        </fieldset>
      )}
      <Button
        className="mt-4"
        disabled={busy || (noText ? !ticks.some(Boolean) : !text.trim())}
        onClick={() => submit({ text, checklist: ticks })}
      >
        {noText ? t('lesson.save') : t('lesson.saveWriting')}
      </Button>
      {result && (
        <p role="status" className="mt-3 font-heading text-sm font-semibold text-primary">
          ✅ {t('lesson.saved')}
        </p>
      )}
      <ErrorLine show={error} />
    </div>
  )
}

/* ------------------------------------------------------ discuss / listen */
export function DiscussActivity({
  item,
  childId,
  saved,
  passageText,
}: ActivityProps & { passageText?: string }) {
  const { t } = useLocale()
  const points = (item.payload.points ?? []) as string[]
  const speakText = item.payload.speak_passage ? passageText : (item.payload.speak as string | undefined)
  const { result, busy, error, submit } = useActivity(childId, item.id)
  const done = !!result || saved?.response.done === true

  return (
    <div>
      {item.payload.prompt != null && <Prompt>{item.payload.prompt as string}</Prompt>}
      {speakText && (
        <Button variant="secondary" className="mb-3" onClick={() => speak(speakText, 'af')}>
          🔊 {t('lesson.listen')}
        </Button>
      )}
      {points.length > 0 && (
        <ul className="mb-3 list-disc space-y-1 pl-5 text-base">
          {points.map((p) => (
            <li key={p}>{p}</li>
          ))}
        </ul>
      )}
      {done ? (
        <p role="status" className="font-heading text-sm font-semibold text-primary">
          ✅ {t('lesson.doneMark')}
        </p>
      ) : (
        <Button variant="secondary" disabled={busy} onClick={() => submit({ done: true })}>
          {t('lesson.done')}
        </Button>
      )}
      <ErrorLine show={error} />
    </div>
  )
}
