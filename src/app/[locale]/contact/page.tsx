import type { Metadata } from 'next'
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
              { icon: '📞', titleKey: 'phone.title', valueKey: 'phone.value', noteKey: 'phone.note', href: `tel:${t('phone.value').replace(/\s/g, '')}` },
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

          {/* Form placeholder — implemented in Module 3 */}
          <div className="mt-12 bg-white rounded-2xl border-2 border-dashed border-gray-200 p-10 text-center">
            <p className="text-gray-400 font-medium">{t('formPlaceholder')}</p>
          </div>
        </div>
      </section>
    </>
  )
}
