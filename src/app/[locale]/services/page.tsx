import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'ServicesIndex' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/services'),
  }
}

const services = [
  { ns: 'Plumbing',          href: '/services/plumbing' },
  { ns: 'Electrical',        href: '/services/electrical' },
  { ns: 'Heating',           href: '/services/heating' },
  { ns: 'Ventilation',       href: '/services/ventilation' },
  { ns: 'AirConditioning',   href: '/services/air-conditioning' },
  { ns: 'UnderfloorHeating', href: '/services/underfloor-heating' },
  { ns: 'BoilerInstallation',href: '/services/boiler-installation' },
  { ns: 'HeatPump',          href: '/services/heat-pump' },
] as const

export default async function ServicesPage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'ServicesIndex' })
  const tNav = await getTranslations({ locale, namespace: 'Navigation' })

  // Load title for each service card
  const cards = await Promise.all(
    services.map(async (s) => {
      const st = await getTranslations({ locale, namespace: s.ns })
      return { href: s.href as Parameters<typeof Link>[0]['href'], title: st('hero.title'), badge: st('hero.badge'), subtitle: st('hero.subtitle') }
    })
  )

  return (
    <>
      <section className="bg-brand-primary text-white py-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <span className="inline-block bg-brand-secondary text-white text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            {tNav('services')}
          </span>
          <h1 className="text-4xl md:text-5xl font-extrabold mb-5">{t('title')}</h1>
          <p className="text-blue-200 text-xl max-w-2xl">{t('description')}</p>
        </div>
      </section>

      <section className="py-16 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {cards.map((card) => (
              <Link
                key={String(card.href)}
                href={card.href}
                className="group bg-white rounded-2xl p-6 border border-gray-100 shadow-sm
                           hover:shadow-md hover:border-brand-primary/20 transition-all"
              >
                <div className="w-10 h-10 rounded-xl bg-brand-secondary/10 flex items-center
                                justify-center mb-4">
                  <div className="w-5 h-5 rounded-md bg-brand-secondary" />
                </div>
                <h2 className="font-bold text-brand-primary mb-2 group-hover:text-brand-secondary transition-colors leading-snug">
                  {card.title}
                </h2>
                <p className="text-sm text-gray-500 line-clamp-2">{card.subtitle}</p>
                <div className="mt-4 text-xs font-bold text-brand-secondary uppercase tracking-wider">
                  {card.badge} →
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
