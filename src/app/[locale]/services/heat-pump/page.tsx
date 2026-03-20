import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import ServicePageTemplate from '@/components/ServicePageTemplate'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'HeatPump' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/services/heat-pump'),
  }
}

export default async function Page({ params }: Props) {
  await params // ensure locale segment is resolved
  return <ServicePageTemplate namespace="HeatPump" category="services" />
}
