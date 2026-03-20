import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'
import type { CanonicalHref } from './NavDropdown'

interface ServicePageTemplateProps {
  /** next-intl namespace — trebuie să existe în messages (ex: 'Plumbing', 'BathroomRenovation') */
  namespace: string
  /** Categoria vizuală — determină badge color și back-link */
  category: 'services' | 'renovation'
}

/**
 * ServicePageTemplate — Server Component reutilizabil.
 *
 * Structură obligatorie per Master Plan:
 *   1. Hero
 *   2. Problema clientului
 *   3. Ce include serviciul
 *   4. Avantaje AZGS
 *   5. Proces de lucru
 *   6. FAQ (min 5 întrebări)
 *   7. CTA secundar
 *   + Schema.org Service + FAQPage (TODO Module 3: adaugă nonce pentru CSP compliance)
 */
export default async function ServicePageTemplate({
  namespace,
  category,
}: ServicePageTemplateProps) {
  const t = await getTranslations(namespace)
  const tNav = await getTranslations('Navigation')

  const categoryHref: CanonicalHref = category === 'services' ? '/services' : '/renovation'
  const isRenovation = category === 'renovation'

  const steps = [1, 2, 3, 4] as const

  // FAQ items for Schema.org (Module 3: wrap in <script nonce={nonce}> for CSP)
  const faqItems = [1, 2, 3, 4, 5].map((i) => ({
    q: t(`faq.q${i}`),
    a: t(`faq.a${i}`),
  }))

  return (
    <>
      {/* ─── 1. HERO ──────────────────────────────────────────────────────────── */}
      <section className={`${isRenovation ? 'bg-brand-primary' : 'bg-brand-primary'} text-white`}>
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28">
          <div className="max-w-3xl">
            {/* Breadcrumb */}
            <div className="flex items-center gap-2 text-blue-300 text-sm mb-5">
              <Link href="/" className="hover:text-white transition-colors">{tNav('home')}</Link>
              <span>/</span>
              <Link href={categoryHref} className="hover:text-white transition-colors">
                {isRenovation ? tNav('renovation') : tNav('services')}
              </Link>
            </div>

            <span className="inline-block bg-brand-secondary text-white text-xs font-bold
                             px-3 py-1 rounded-full mb-5 uppercase tracking-wider">
              {t('hero.badge')}
            </span>

            <h1 className="text-4xl md:text-5xl font-extrabold leading-tight mb-5">
              {t('hero.title')}
            </h1>

            <p className="text-lg md:text-xl text-blue-200 mb-8 leading-relaxed max-w-2xl">
              {t('hero.subtitle')}
            </p>

            <div className="flex flex-wrap gap-4">
              <Link href="/contact" className="btn-primary">
                {t('hero.ctaPrimary')}
              </Link>
              <Link
                href={categoryHref}
                className="border-2 border-white/60 text-white font-semibold px-6 py-3 rounded-lg
                           hover:border-white hover:bg-white/10 transition-colors"
              >
                {t('hero.ctaSecondary')}
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ─── 2. PROBLEMA CLIENTULUI ───────────────────────────────────────────── */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-blue-50 border border-blue-100 rounded-2xl p-8 md:p-10">
            <h2 className="text-2xl md:text-3xl font-bold text-brand-primary mb-4">
              {t('problem.title')}
            </h2>
            <p className="text-gray-700 text-lg leading-relaxed">
              {t('problem.text')}
            </p>
          </div>
        </div>
      </section>

      {/* ─── 3. CE INCLUDE + 4. AVANTAJE ────────────────────────────────────── */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">

            {/* Includes */}
            <div>
              <h2 className="text-2xl font-bold text-brand-primary mb-6">
                {t('includes.title')}
              </h2>
              <ul className="space-y-3">
                {(['item1','item2','item3','item4','item5','item6'] as const).map((key) => (
                  <li key={key} className="flex items-start gap-3">
                    <span className="mt-1 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center shrink-0">
                      <svg className="w-3 h-3 text-green-600" fill="none" stroke="currentColor" strokeWidth={3} viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                    </span>
                    <span className="text-gray-700">{t(`includes.${key}`)}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Advantages */}
            <div>
              <h2 className="text-2xl font-bold text-brand-primary mb-6">
                {t('advantages.title')}
              </h2>
              <ul className="space-y-4">
                {(['item1','item2','item3','item4'] as const).map((key, i) => (
                  <li key={key} className="flex items-start gap-4">
                    <span className="w-9 h-9 rounded-xl bg-brand-secondary/10 flex items-center
                                     justify-center text-brand-secondary font-bold text-sm shrink-0">
                      {i + 1}
                    </span>
                    <span className="text-gray-700 pt-1.5">{t(`advantages.${key}`)}</span>
                  </li>
                ))}
              </ul>
            </div>

          </div>
        </div>
      </section>

      {/* ─── 5. PROCES DE LUCRU ───────────────────────────────────────────────── */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl md:text-3xl font-bold text-brand-primary text-center mb-12">
            {t('process.title')}
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {steps.map((step) => (
              <div key={step} className="relative">
                {step < 4 && (
                  <div className="hidden lg:block absolute top-7 left-full w-full h-0.5 bg-brand-secondary/20 z-0" />
                )}
                <div className="relative bg-white border border-gray-100 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow text-center">
                  <div className="w-14 h-14 rounded-full bg-brand-primary text-white font-extrabold
                                  text-xl flex items-center justify-center mx-auto mb-4">
                    {step}
                  </div>
                  <h3 className="font-bold text-brand-primary mb-2">
                    {t(`process.step${step}Title`)}
                  </h3>
                  <p className="text-sm text-gray-600 leading-relaxed">
                    {t(`process.step${step}Text`)}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── 6. FAQ ───────────────────────────────────────────────────────────── */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl md:text-3xl font-bold text-brand-primary text-center mb-10">
            {t('faq.title')}
          </h2>
          <div className="space-y-4">
            {faqItems.map((item, i) => (
              <details
                key={i}
                className="group bg-white border border-gray-100 rounded-xl shadow-sm"
              >
                <summary className="flex items-center justify-between gap-4 px-6 py-4 cursor-pointer
                                    font-semibold text-brand-primary list-none
                                    hover:bg-blue-50 rounded-xl transition-colors">
                  <span>{item.q}</span>
                  <svg
                    className="w-5 h-5 shrink-0 text-brand-secondary transition-transform group-open:rotate-180"
                    fill="none" stroke="currentColor" strokeWidth={2.5} viewBox="0 0 24 24"
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <p className="px-6 pb-5 pt-2 text-gray-700 leading-relaxed border-t border-gray-50">
                  {item.a}
                </p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* ─── 7. CTA SECUNDAR ──────────────────────────────────────────────────── */}
      <section className="py-16 bg-brand-primary text-white">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4">
            {t('cta.title')}
          </h2>
          <p className="text-blue-200 text-lg mb-8 leading-relaxed">
            {t('cta.text')}
          </p>
          <Link
            href="/contact"
            className="inline-block bg-brand-secondary text-white font-bold px-8 py-4
                       rounded-xl hover:bg-orange-600 transition-colors text-lg shadow-lg"
          >
            {t('cta.btn')}
          </Link>
        </div>
      </section>

      {/*
        TODO Module 3: Schema.org JSON-LD (Service + FAQPage)
        Implementare cu nonce pentru CSP compliance.
        Pagini cu formulare → dynamic rendering → headers() disponibil.

        <script
          type="application/ld+json"
          nonce={nonce}
          dangerouslySetInnerHTML={{ __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            mainEntity: faqItems.map(item => ({
              '@type': 'Question',
              name: item.q,
              acceptedAnswer: { '@type': 'Answer', text: item.a }
            }))
          })}}
        />
      */}
    </>
  )
}
