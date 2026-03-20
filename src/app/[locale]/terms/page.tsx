import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Terms' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/terms'),
    robots: { index: false, follow: false },
  }
}

export default async function TermsPage({ params }: Props) {
  await params
  const t = await getTranslations('Terms')

  return (
    <section className="py-20 bg-white">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl md:text-4xl font-extrabold text-brand-primary mb-6">
          {t('hero.title')}
        </h1>
        <p className="text-gray-500 text-sm mb-10">{t('lastUpdated')}</p>
        <div className="prose prose-blue max-w-none text-gray-700 leading-relaxed space-y-6">
          <p>{t('intro')}</p>
          <h2 className="text-xl font-bold text-brand-primary">{t('section1.title')}</h2>
          <p>{t('section1.text')}</p>
          <h2 className="text-xl font-bold text-brand-primary">{t('section2.title')}</h2>
          <p>{t('section2.text')}</p>
          <h2 className="text-xl font-bold text-brand-primary">{t('section3.title')}</h2>
          <p>{t('section3.text')}</p>
          <h2 className="text-xl font-bold text-brand-primary">{t('contact.title')}</h2>
          <p>{t('contact.text')}</p>
          <a href="mailto:info@azgs.nl" className="text-brand-secondary hover:underline font-semibold">
            info@azgs.nl
          </a>
        </div>
      </div>
    </section>
  )
}
