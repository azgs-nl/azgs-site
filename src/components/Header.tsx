import { getTranslations, getLocale } from 'next-intl/server'
import { Link } from '@/navigation'
import NavDropdown from './NavDropdown'
import MobileMenu from './MobileMenu'
import LanguageSwitcher from './LanguageSwitcher'
import type { DropdownItem } from './NavDropdown'

export default async function Header() {
  const locale = await getLocale()
  const t = await getTranslations({ locale, namespace: 'Navigation' })

  const servicesItems: DropdownItem[] = [
    { href: '/services/plumbing',          label: t('plumbing') },
    { href: '/services/electrical',        label: t('electrical') },
    { href: '/services/heating',           label: t('heating') },
    { href: '/services/ventilation',       label: t('ventilation') },
    { href: '/services/air-conditioning',  label: t('airConditioning') },
    { href: '/services/underfloor-heating',label: t('underfloorHeating') },
    { href: '/services/boiler-installation',label: t('boilerInstallation') },
    { href: '/services/heat-pump',         label: t('heatPump') },
  ]

  const renovationItems: DropdownItem[] = [
    { href: '/renovation/apartment-renovation', label: t('apartmentRenovation') },
    { href: '/renovation/bathroom-renovation',  label: t('bathroomRenovation') },
    { href: '/renovation/kitchen-renovation',   label: t('kitchenRenovation') },
    { href: '/renovation/drywall',              label: t('drywall') },
    { href: '/renovation/painting',             label: t('painting') },
    { href: '/renovation/plastering',           label: t('plastering') },
    { href: '/renovation/flooring',             label: t('flooring') },
    { href: '/renovation/tile-installation',    label: t('tileInstallation') },
  ]

  return (
    <header className="sticky top-0 z-40 bg-white border-b border-gray-100 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">

          {/* Logo */}
          <Link href="/" className="flex items-center gap-1.5 shrink-0 group">
            <span className="text-2xl font-extrabold text-brand-primary tracking-tight group-hover:text-brand-secondary transition-colors">
              AZGS
            </span>
            <span className="text-xs font-semibold text-brand-secondary border border-brand-secondary/40 px-1.5 py-0.5 rounded-full">
              .nl
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden lg:flex items-center gap-1" aria-label="Hoofdnavigatie">
            <Link
              href="/"
              className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-brand-primary rounded-lg hover:bg-gray-50 transition-colors"
            >
              {t('home')}
            </Link>

            <NavDropdown
              label={t('services')}
              href="/services"
              items={servicesItems}
            />

            <NavDropdown
              label={t('renovation')}
              href="/renovation"
              items={renovationItems}
            />

            <Link
              href="/emergency"
              className="px-3 py-2 text-sm font-bold text-brand-secondary hover:text-white hover:bg-brand-secondary rounded-lg transition-colors"
            >
              {t('emergency')}
            </Link>

            <Link
              href="/projects"
              className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-brand-primary rounded-lg hover:bg-gray-50 transition-colors"
            >
              {t('projects')}
            </Link>

            <Link
              href="/about"
              className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-brand-primary rounded-lg hover:bg-gray-50 transition-colors"
            >
              {t('about')}
            </Link>

            <Link
              href="/contact"
              className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-brand-primary rounded-lg hover:bg-gray-50 transition-colors"
            >
              {t('contact')}
            </Link>
          </nav>

          {/* Right side */}
          <div className="flex items-center gap-2">
            <LanguageSwitcher />

            <Link
              href="/contact"
              className="hidden lg:inline-flex items-center gap-1.5 bg-brand-primary text-white text-sm font-semibold px-4 py-2 rounded-lg hover:bg-blue-900 transition-colors"
            >
              <span className="inline-block w-2 h-2 rounded-full bg-green-400 animate-pulse" />
              {t('cta')}
            </Link>

            {/* Mobile hamburger */}
            <MobileMenu
              servicesLabel={t('services')}
              renovationLabel={t('renovation')}
              emergencyLabel={t('emergency')}
              projectsLabel={t('projects')}
              aboutLabel={t('about')}
              contactLabel={t('contact')}
              ctaLabel={t('cta')}
              servicesItems={servicesItems}
              renovationItems={renovationItems}
            />
          </div>

        </div>
      </div>
    </header>
  )
}
