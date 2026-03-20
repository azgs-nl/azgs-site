import { getTranslations } from 'next-intl/server'
import type { ComponentProps } from 'react'
import { Link } from '@/navigation'

export default async function Footer() {
  const t = await getTranslations('Footer')
  const year = new Date().getFullYear()

  return (
    <footer className="bg-brand-primary text-white">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10 mb-10">
          {/* Brand */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <span className="text-2xl font-extrabold">AZGS</span>
              <span className="text-xs font-semibold text-brand-secondary border border-brand-secondary/30 px-2 py-0.5 rounded-full">
                .nl
              </span>
            </div>
            <p className="text-blue-200 text-sm leading-relaxed max-w-xs">
              {t('tagline')}
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="font-bold text-sm uppercase tracking-wider text-blue-300 mb-4">
              {t('linksTitle')}
            </h3>
            <ul className="space-y-2">
              {([
                { href: '/',         label: t('linkHome') },
                { href: '/about',    label: t('linkAbout') },
                { href: '/services', label: t('linkServices') },
                { href: '/contact',  label: t('linkContact') },
              ] satisfies { href: ComponentProps<typeof Link>['href']; label: string }[]).map(({ href, label }) => (
                <li key={href}>
                  <Link
                    href={href}
                    className="text-blue-200 hover:text-white text-sm transition-colors"
                  >
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="font-bold text-sm uppercase tracking-wider text-blue-300 mb-4">
              {t('contactTitle')}
            </h3>
            <address className="not-italic space-y-2 text-blue-200 text-sm">
              <p>{t('serviceArea')}</p>
              <a
                href="mailto:info@azgs.nl"
                className="hover:text-white transition-colors block"
              >
                info@azgs.nl
              </a>
            </address>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="border-t border-blue-800 pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-blue-300">
          <p>© {year} AZGS. {t('allRights')}</p>
          <div className="flex gap-4">
            <Link href="/privacy" className="hover:text-white transition-colors">
              {t('privacy')}
            </Link>
            <Link href="/terms" className="hover:text-white transition-colors">
              {t('terms')}
            </Link>
          </div>
        </div>
      </div>
    </footer>
  )
}
