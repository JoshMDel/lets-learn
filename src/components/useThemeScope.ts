import { useEffect } from 'react'

/** Switches the document's `data-theme` while a route tree is mounted, so
 * shell (account/admin) screens and learning screens can live side by side
 * in one app but render as two distinct visual languages. See src/index.css. */
export function useThemeScope(theme: 'shell' | 'learning') {
  useEffect(() => {
    const prev = document.documentElement.dataset.theme
    document.documentElement.dataset.theme = theme
    return () => {
      if (prev) document.documentElement.dataset.theme = prev
    }
  }, [theme])
}
