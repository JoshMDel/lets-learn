import type { ReactNode } from 'react'
import { useLocale } from '../../i18n/LocaleContext'
import type { LessonItem } from '../../types/lessons'

/** Tiny inline formatter: **bold** and _italic_ only -- lesson text is authored data. */
function inline(text: string): ReactNode[] {
  return text.split(/(\*\*[^*]+\*\*|_[^_]+_)/g).map((part, i) => {
    if (part.startsWith('**') && part.endsWith('**')) return <strong key={i}>{part.slice(2, -2)}</strong>
    if (part.length > 2 && part.startsWith('_') && part.endsWith('_')) return <em key={i}>{part.slice(1, -1)}</em>
    return part
  })
}

export function LessonBlock({ item }: { item: LessonItem }) {
  const { t } = useLocale()
  const p = item.payload

  if (item.kind === 'note') {
    return (
      <aside className="rounded-xl border-2 border-accent/40 bg-accent/10 p-4 text-base leading-relaxed">
        {item.title_af && <p className="mb-1 font-heading font-bold">💡 {item.title_af}</p>}
        <p className="whitespace-pre-line">{inline(p.text as string)}</p>
      </aside>
    )
  }

  if (item.kind === 'table') {
    const headers = (p.headers ?? []) as string[]
    const rows = (p.rows ?? []) as string[][]
    return (
      <div>
        {item.title_af && <h3 className="mb-2 font-heading text-lg font-bold">{item.title_af}</h3>}
        <div className="overflow-x-auto rounded-xl border border-subtle">
          <table className="w-full min-w-[20rem] text-left text-sm">
            {headers.length > 0 && (
              <thead className="bg-surface-2 font-heading">
                <tr>
                  {headers.map((h) => (
                    <th key={h} className="px-3 py-2 font-semibold">
                      {h}
                    </th>
                  ))}
                </tr>
              </thead>
            )}
            <tbody>
              {rows.map((row, i) => (
                <tr key={i} className="border-t border-subtle">
                  {row.map((cell, j) => (
                    <td key={j} className="px-3 py-2 align-top">
                      {inline(cell)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  if (item.kind === 'image') {
    return (
      <figure>
        <img
          src={p.src as string}
          alt={(p.alt as string) ?? ''}
          loading="lazy"
          className="mx-auto max-h-[32rem] w-auto max-w-full rounded-xl border border-subtle"
        />
        {(p.caption as string | undefined) && (
          <figcaption className="mt-2 text-center text-sm text-muted">
            {p.caption as string}
            {item.workbook_ref?.printed_page != null && (
              <> · {t('lesson.workbookPage', { page: item.workbook_ref.printed_page })}</>
            )}
          </figcaption>
        )}
      </figure>
    )
  }

  // text
  const paragraphs = (p.paragraphs ?? []) as string[]
  const bullets = (p.bullets ?? []) as string[]
  return (
    <div className="text-base leading-relaxed">
      {item.title_af && <h3 className="mb-2 font-heading text-lg font-bold">{item.title_af}</h3>}
      {paragraphs.map((para, i) => (
        <p key={i} className="mb-2 whitespace-pre-line">
          {inline(para)}
        </p>
      ))}
      {bullets.length > 0 && (
        <ul className="list-disc space-y-1 pl-5">
          {bullets.map((b) => (
            <li key={b}>{inline(b)}</li>
          ))}
        </ul>
      )}
    </div>
  )
}
