#!/usr/bin/env python3
"""Generator pagini Module 2 — toate paginile de servicii și renovare."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  ✅ {path}")

BASE = "/home/claude/azgs-nl/src/app/[locale]"

# ─── Template pentru pagini servicii cu ServicePageTemplate ──────────────────

def service_page(namespace: str, canonical: str, category: str) -> str:
    return f"""import type {{ Metadata }} from 'next'
import {{ getTranslations }} from 'next-intl/server'
import ServicePageTemplate from '@/components/ServicePageTemplate'
import {{ buildAlternates }} from '@/lib/metadata-helpers'

interface Props {{
  params: Promise<{{ locale: string }}>
}}

export async function generateMetadata({{ params }}: Props): Promise<Metadata> {{
  const {{ locale }} = await params
  const t = await getTranslations({{ locale, namespace: '{namespace}' }})
  return {{
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '{canonical}'),
  }}
}}

export default async function Page({{ params }}: Props) {{
  await params // ensure locale segment is resolved
  return <ServicePageTemplate namespace="{namespace}" category="{category}" />
}}
"""

# ─── Pagini servicii ─────────────────────────────────────────────────────────

service_pages = [
    ("Plumbing",          "/services/plumbing",           "services"),
    ("Electrical",        "/services/electrical",         "services"),
    ("Heating",           "/services/heating",            "services"),
    ("Ventilation",       "/services/ventilation",        "services"),
    ("AirConditioning",   "/services/air-conditioning",   "services"),
    ("UnderfloorHeating", "/services/underfloor-heating", "services"),
    ("BoilerInstallation","/services/boiler-installation","services"),
    ("HeatPump",          "/services/heat-pump",          "services"),
]

for ns, canonical, cat in service_pages:
    slug = canonical.replace("/services/", "")
    write(f"{BASE}/services/{slug}/page.tsx", service_page(ns, canonical, cat))

# ─── Pagini renovare ─────────────────────────────────────────────────────────

renovation_pages = [
    ("ApartmentRenovation", "/renovation/apartment-renovation", "renovation"),
    ("BathroomRenovation",  "/renovation/bathroom-renovation",  "renovation"),
    ("KitchenRenovation",   "/renovation/kitchen-renovation",   "renovation"),
    ("Drywall",             "/renovation/drywall",              "renovation"),
    ("Painting",            "/renovation/painting",             "renovation"),
    ("Plastering",          "/renovation/plastering",           "renovation"),
    ("Flooring",            "/renovation/flooring",             "renovation"),
    ("TileInstallation",    "/renovation/tile-installation",    "renovation"),
]

for ns, canonical, cat in renovation_pages:
    slug = canonical.replace("/renovation/", "")
    write(f"{BASE}/renovation/{slug}/page.tsx", service_page(ns, canonical, cat))

# ─── Index pages ─────────────────────────────────────────────────────────────

services_index = """import type { Metadata } from 'next'
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
"""

renovation_index = """import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'RenovationIndex' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/renovation'),
  }
}

const renovations = [
  { ns: 'ApartmentRenovation', href: '/renovation/apartment-renovation' },
  { ns: 'BathroomRenovation',  href: '/renovation/bathroom-renovation' },
  { ns: 'KitchenRenovation',   href: '/renovation/kitchen-renovation' },
  { ns: 'Drywall',             href: '/renovation/drywall' },
  { ns: 'Painting',            href: '/renovation/painting' },
  { ns: 'Plastering',          href: '/renovation/plastering' },
  { ns: 'Flooring',            href: '/renovation/flooring' },
  { ns: 'TileInstallation',    href: '/renovation/tile-installation' },
] as const

export default async function RenovationPage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'RenovationIndex' })
  const tNav = await getTranslations({ locale, namespace: 'Navigation' })

  const cards = await Promise.all(
    renovations.map(async (r) => {
      const rt = await getTranslations({ locale, namespace: r.ns })
      return { href: r.href as Parameters<typeof Link>[0]['href'], title: rt('hero.title'), subtitle: rt('hero.subtitle') }
    })
  )

  return (
    <>
      <section className="bg-brand-primary text-white py-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <span className="inline-block bg-brand-secondary text-white text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            {tNav('renovation')}
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
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
"""

write(f"{BASE}/services/page.tsx", services_index)
write(f"{BASE}/renovation/page.tsx", renovation_index)

# ─── About ───────────────────────────────────────────────────────────────────

about = """import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'About' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/about'),
  }
}

export default async function AboutPage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'About' })

  return (
    <>
      <section className="bg-brand-primary text-white py-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <span className="inline-block bg-brand-secondary text-white text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            {t('hero.badge')}
          </span>
          <h1 className="text-4xl md:text-5xl font-extrabold mb-5">{t('hero.title')}</h1>
          <p className="text-blue-200 text-xl max-w-2xl">{t('hero.subtitle')}</p>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-brand-primary mb-6">{t('story.title')}</h2>
          <p className="text-gray-700 text-lg leading-relaxed mb-12">{t('story.text')}</p>

          <h2 className="text-2xl font-bold text-brand-primary mb-6">{t('values.title')}</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {(['item1','item2','item3','item4'] as const).map((k) => (
              <div key={k} className="bg-blue-50 rounded-xl p-5 text-center">
                <div className="w-10 h-10 rounded-full bg-brand-secondary/20 mx-auto mb-3 flex items-center justify-center">
                  <div className="w-5 h-5 rounded-full bg-brand-secondary" />
                </div>
                <p className="font-bold text-brand-primary text-sm">{t(`values.${k}`)}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 bg-brand-secondary text-white text-center">
        <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-extrabold mb-6">{t('cta.title')}</h2>
          <Link href="/contact" className="inline-block bg-white text-brand-secondary font-bold px-8 py-4 rounded-xl hover:bg-orange-50 transition-colors">
            {t('cta.btn')}
          </Link>
        </div>
      </section>
    </>
  )
}
"""

write(f"{BASE}/about/page.tsx", about)

# ─── Contact ─────────────────────────────────────────────────────────────────

contact = """import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Contact' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/contact'),
  }
}

export default async function ContactPage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Contact' })

  return (
    <>
      <section className="bg-brand-primary text-white py-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <span className="inline-block bg-brand-secondary text-white text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            {t('hero.badge')}
          </span>
          <h1 className="text-4xl md:text-5xl font-extrabold mb-5">{t('hero.title')}</h1>
          <p className="text-blue-200 text-xl max-w-2xl">{t('hero.subtitle')}</p>
        </div>
      </section>

      <section className="py-16 bg-gray-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { icon: '📞', titleKey: 'phone.title', valueKey: 'phone.value', noteKey: 'phone.note', href: `tel:${t('phone.value').replace(/\\s/g, '')}` },
              { icon: '✉️', titleKey: 'email.title', valueKey: 'email.value', noteKey: 'email.note', href: `mailto:${t('email.value')}` },
              { icon: '📍', titleKey: 'address.title', valueKey: 'address.value', noteKey: 'address.note', href: null },
            ].map((item) => (
              <div key={item.titleKey} className="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm text-center">
                <div className="text-3xl mb-4">{item.icon}</div>
                <h2 className="font-bold text-brand-primary mb-2">{t(item.titleKey)}</h2>
                {item.href ? (
                  <a href={item.href} className="text-brand-secondary font-semibold hover:underline">
                    {t(item.valueKey)}
                  </a>
                ) : (
                  <p className="text-brand-secondary font-semibold">{t(item.valueKey)}</p>
                )}
                <p className="text-xs text-gray-400 mt-1">{t(item.noteKey)}</p>
              </div>
            ))}
          </div>

          {/* Form placeholder — Module 3 */}
          <div className="mt-12 bg-white rounded-2xl border-2 border-dashed border-gray-200 p-10 text-center">
            <p className="text-gray-400 font-medium">Contactformulier — Module 3</p>
          </div>
        </div>
      </section>
    </>
  )
}
"""

write(f"{BASE}/contact/page.tsx", contact)

# ─── Emergency ───────────────────────────────────────────────────────────────

emergency = """import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Emergency' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/emergency'),
  }
}

export default async function EmergencyPage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Emergency' })

  const faqItems = [1,2,3,4,5].map(i => ({ q: t(`faq.q${i}`), a: t(`faq.a${i}`) }))

  return (
    <>
      {/* Hero — orange urgency */}
      <section className="bg-brand-secondary text-white py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span className="inline-block bg-white/20 text-white text-xs font-bold px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
            {t('hero.badge')}
          </span>
          <h1 className="text-4xl md:text-5xl font-extrabold mb-5">{t('hero.title')}</h1>
          <p className="text-orange-100 text-xl mb-8 max-w-2xl mx-auto">{t('hero.subtitle')}</p>

          <div className="inline-flex flex-col items-center gap-2 bg-white/15 rounded-2xl px-8 py-5 mb-8">
            <span className="text-sm font-medium text-orange-100">{t('urgentTitle')}</span>
            <a href={`tel:${t('phone').replace(/\\s/g,'')}`}
               className="text-3xl font-extrabold tracking-wide hover:text-orange-200 transition-colors">
              {t('phone')}
            </a>
          </div>

          <div className="flex flex-wrap justify-center gap-4">
            <a href={`tel:${t('phone').replace(/\\s/g,'')}`}
               className="bg-white text-brand-secondary font-bold px-8 py-4 rounded-xl
                          hover:bg-orange-50 transition-colors shadow-lg">
              {t('hero.ctaPrimary')}
            </a>
            <Link href="/services"
               className="border-2 border-white/60 text-white font-semibold px-6 py-3 rounded-xl
                          hover:bg-white/10 transition-colors">
              {t('hero.ctaSecondary')}
            </Link>
          </div>
        </div>
      </section>

      {/* Services + Promise */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
              <h2 className="text-2xl font-bold text-brand-primary mb-6">{t('services.title')}</h2>
              <ul className="space-y-3">
                {(['item1','item2','item3','item4','item5'] as const).map(k => (
                  <li key={k} className="flex items-center gap-3 bg-white rounded-xl px-5 py-3 border border-gray-100">
                    <span className="w-2 h-2 rounded-full bg-brand-secondary shrink-0" />
                    <span className="font-medium text-gray-700">{t(`services.${k}`)}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h2 className="text-2xl font-bold text-brand-primary mb-6">{t('promise.title')}</h2>
              <ul className="space-y-4">
                {(['item1','item2','item3','item4'] as const).map((k, i) => (
                  <li key={k} className="flex items-start gap-4">
                    <span className="w-8 h-8 rounded-lg bg-green-100 flex items-center justify-center shrink-0">
                      <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" strokeWidth={3} viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                    </span>
                    <span className="text-gray-700 pt-0.5">{t(`promise.${k}`)}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-16 bg-white">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-brand-primary text-center mb-10">{t('faq.title')}</h2>
          <div className="space-y-4">
            {faqItems.map((item, i) => (
              <details key={i} className="group bg-gray-50 border border-gray-100 rounded-xl">
                <summary className="flex items-center justify-between gap-4 px-6 py-4 cursor-pointer font-semibold text-brand-primary list-none hover:bg-blue-50 rounded-xl transition-colors">
                  <span>{item.q}</span>
                  <svg className="w-5 h-5 shrink-0 text-brand-secondary transition-transform group-open:rotate-180"
                       fill="none" stroke="currentColor" strokeWidth={2.5} viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <p className="px-6 pb-5 pt-2 text-gray-700 border-t border-gray-100">{item.a}</p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-brand-secondary text-white text-center">
        <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-extrabold mb-4">{t('cta.title')}</h2>
          <p className="text-orange-100 mb-8">{t('cta.text')}</p>
          <a href={`tel:${t('phone').replace(/\\s/g,'')}`}
             className="inline-block bg-white text-brand-secondary font-bold px-8 py-4 rounded-xl hover:bg-orange-50 transition-colors text-lg shadow-lg">
            {t('cta.btn')}
          </a>
        </div>
      </section>
    </>
  )
}
"""

write(f"{BASE}/emergency/page.tsx", emergency)

print("\n✅ All pages generated.")
