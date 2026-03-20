import { getTranslations } from 'next-intl/server'
import { Link } from '@/navigation'

interface Props {
  params: Promise<{ locale: string }>
}

export default async function HomePage({ params }: Props) {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Home' })

  return (
    <>

      {/* Hero */}
      <section className="bg-brand-primary text-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32">
          <div className="max-w-3xl">
            <span className="inline-block bg-brand-secondary text-white text-sm font-semibold px-3 py-1 rounded-full mb-6 uppercase tracking-wide">
              {t('badge')}
            </span>
            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-6">
              {t('heroTitle')}
            </h1>
            <p className="text-lg md:text-xl text-blue-200 mb-10 leading-relaxed">
              {t('heroSubtitle')}
            </p>
            <div className="flex flex-wrap gap-4">
              <Link href="/contact" className="btn-primary">
                {t('ctaPrimary')}
              </Link>
              <Link
                href="/services"
                className="border-2 border-white text-white font-semibold px-6 py-3 rounded-lg hover:bg-white hover:text-brand-primary transition-colors duration-200"
              >
                {t('ctaSecondary')}
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl md:text-4xl font-extrabold text-brand-primary mb-4">
              {t('featuresTitle')}
            </h2>
            <p className="text-gray-600 text-lg max-w-2xl mx-auto">
              {t('featuresSubtitle')}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {(['feature1', 'feature2', 'feature3'] as const).map((key) => (
              <div
                key={key}
                className="bg-white rounded-2xl p-8 shadow-sm border border-gray-100 hover:shadow-md transition-shadow"
              >
                <div className="w-12 h-12 bg-brand-secondary/10 rounded-xl flex items-center justify-center mb-5">
                  <div className="w-6 h-6 bg-brand-secondary rounded-md" />
                </div>
                <h3 className="text-xl font-bold text-brand-primary mb-3">
                  {t(`${key}Title`)}
                </h3>
                <p className="text-gray-600 leading-relaxed">{t(`${key}Text`)}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Banner */}
      <section className="bg-brand-secondary">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center">
          <h2 className="text-3xl md:text-4xl font-extrabold text-white mb-4">
            {t('ctaBannerTitle')}
          </h2>
          <p className="text-orange-100 text-lg mb-8 max-w-xl mx-auto">
            {t('ctaBannerText')}
          </p>
          <Link
            href="/contact"
            className="bg-white text-brand-secondary font-bold px-8 py-4 rounded-xl hover:bg-orange-50 transition-colors duration-200 inline-block"
          >
            {t('ctaBannerBtn')}
          </Link>
        </div>
      </section>
    </>
  )
}
