import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Projects' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/projects'),
  }
}

export default async function ProjectsPage({ params }: Props) {
  await params
  const t = await getTranslations('Projects')

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

      <section className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-gray-400 font-medium">{t('placeholder')}</p>
        </div>
      </section>
    </>
  )
}
