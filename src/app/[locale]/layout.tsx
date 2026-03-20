import type { Metadata } from 'next'
import type { ReactNode } from 'react'
import { NextIntlClientProvider } from 'next-intl'
import { getMessages, getTranslations } from 'next-intl/server'
import { notFound } from 'next/navigation'
import { routing } from '@/i18n/routing'
import { buildAlternates } from '@/lib/metadata-helpers'
import Header from '@/components/Header'
import Footer from '@/components/Footer'

/**
 * LOCALE LAYOUT — src/app/[locale]/layout.tsx
 *
 * Layout nested — fără <html>, fără <body>.
 * Root Layout deține exclusiv <html> și <body>.
 *
 * Responsabilități:
 *   - Validare locale → notFound() dacă necunoscut
 *   - generateMetadata: title, description, hreflang per pagină via buildAlternates
 *   - generateStaticParams: pre-render static toate 6 localele
 *   - NextIntlClientProvider + Header + main + Footer
 *
 * Fără Dynamic APIs (headers(), cookies(), searchParams).
 * Locale layout este static-friendly în Module 1.
 */

const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL || 'https://azgs.nl'

type Locale = (typeof routing.locales)[number]

interface Props {
  children: ReactNode
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'Metadata' })

  return {
    title: {
      default: t('title'),
      template: `%s | AZGS`,
    },
    description: t('description'),
    metadataBase: new URL(BASE_URL),
    alternates: buildAlternates(locale, '/'),
    openGraph: {
      title: t('title'),
      description: t('description'),
      url: `${BASE_URL}/${locale}`,
      siteName: 'AZGS',
      locale,
      type: 'website',
    },
    twitter: {
      card: 'summary_large_image',
      title: t('title'),
      description: t('description'),
    },
    robots: { index: true, follow: true },
  }
}

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }))
}

export default async function LocaleLayout({ children, params }: Props) {
  const { locale } = await params

  if (!routing.locales.includes(locale as Locale)) {
    notFound()
  }

  const messages = await getMessages()

  return (
    <NextIntlClientProvider messages={messages}>
      <Header />
      <main className="flex-1" id="main-content">
        {children}
      </main>
      <Footer />
    </NextIntlClientProvider>
  )
}
