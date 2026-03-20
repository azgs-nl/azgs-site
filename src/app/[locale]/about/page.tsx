import type { Metadata } from 'next'
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
