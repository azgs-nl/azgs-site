import type { Metadata } from 'next'
import { routing } from '@/i18n/routing'
import { getPathname } from '@/navigation'

const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL || 'https://azgs.nl'

type Locale = (typeof routing.locales)[number]
type Href = Parameters<typeof getPathname>[0]['href']

/**
 * buildAlternates — helper reutilizabil pentru hreflang corect per pagină.
 *
 * Utilizare în fiecare page.tsx care are generateMetadata propriu:
 *   alternates: buildAlternates(locale, '/services/plumbing')
 *
 * Generează:
 *   - canonical: URL-ul localizat al paginii pentru locale curent
 *   - languages: hreflang pentru toate cele 6 locale, pointând la
 *     echivalentul localizat al ACELEI pagini (nu la homepage)
 *   - x-default: pointează la versiunea nl (default locale)
 *
 * ❌ Fără acest helper, Google vede toate paginile de servicii ca
 *    duplicate ale homepage-ului (hreflang moștenit din locale layout
 *    pointează mereu la '/').
 */
export function buildAlternates(
  locale: string,
  href: Href,
): NonNullable<Metadata['alternates']> {
  const languages = Object.fromEntries(
    routing.locales.map((loc) => {
      const localizedPath = getPathname({ locale: loc as Locale, href })
      return [loc, `${BASE_URL}/${loc}${localizedPath}`]
    }),
  )

  const canonicalPath = getPathname({ locale: locale as Locale, href })

  return {
    canonical: `${BASE_URL}/${locale}${canonicalPath}`,
    languages: {
      ...languages,
      'x-default': languages[routing.defaultLocale],
    },
  }
}
