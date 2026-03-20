import type { Metadata } from 'next'
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
            <a href={`tel:${t('phone').replace(/\s/g,'')}`}
               className="text-3xl font-extrabold tracking-wide hover:text-orange-200 transition-colors">
              {t('phone')}
            </a>
          </div>

          <div className="flex flex-wrap justify-center gap-4">
            <a href={`tel:${t('phone').replace(/\s/g,'')}`}
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
          <a href={`tel:${t('phone').replace(/\s/g,'')}`}
             className="inline-block bg-white text-brand-secondary font-bold px-8 py-4 rounded-xl hover:bg-orange-50 transition-colors text-lg shadow-lg">
            {t('cta.btn')}
          </a>
        </div>
      </section>
    </>
  )
}
