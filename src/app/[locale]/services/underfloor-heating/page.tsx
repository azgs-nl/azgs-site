import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import ServicePageTemplate from '@/components/ServicePageTemplate'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'UnderfloorHeating' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/services/underfloor-heating'),
  }
}

export default async function Page({ params }: Props) {
  await params // ensure locale segment is resolved
  return <ServicePageTemplate namespace="UnderfloorHeating" category="services" />
}
