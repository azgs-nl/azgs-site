import type { MetadataRoute } from 'next'
import { routing } from '@/i18n/routing'
import { getPathname } from '@/navigation'

type Locale = (typeof routing.locales)[number]
type Href = Parameters<typeof getPathname>[0]['href']

const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL || 'https://azgs.nl'

const pages: Href[] = [
  '/',
  '/about',
  '/services',
  '/services/plumbing',
  '/services/electrical',
  '/services/heating',
  '/services/ventilation',
  '/services/air-conditioning',
  '/services/underfloor-heating',
  '/services/boiler-installation',
  '/services/heat-pump',
  '/renovation',
  '/renovation/apartment-renovation',
  '/renovation/bathroom-renovation',
  '/renovation/kitchen-renovation',
  '/renovation/drywall',
  '/renovation/painting',
  '/renovation/plastering',
  '/renovation/flooring',
  '/renovation/tile-installation',
  '/emergency',
  '/projects',
  '/contact',
  '/privacy',
  '/terms',
]

export default function sitemap(): MetadataRoute.Sitemap {
  return pages.flatMap((href) =>
    routing.locales.map((locale) => {
      const localizedPath = getPathname({ locale: locale as Locale, href })
      return {
        url: `${BASE_URL}/${locale}${localizedPath}`,
        lastModified: new Date(),
        changeFrequency: href === '/' ? 'weekly' : ('monthly' as const),
        priority: href === '/' ? 1 : href.includes('/services/') || href.includes('/renovation/') ? 0.8 : 0.6,
        alternates: {
          languages: Object.fromEntries(
            routing.locales.map((loc) => [
              loc,
              `${BASE_URL}/${loc}${getPathname({ locale: loc as Locale, href })}`,
            ])
          ),
        },
      }
    })
  )
}
