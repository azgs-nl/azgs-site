import type { Metadata } from 'next'
import { getTranslations } from 'next-intl/server'
import ServicePageTemplate from '@/components/ServicePageTemplate'
import { buildAlternates } from '@/lib/metadata-helpers'

interface Props {
  params: Promise<{ locale: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: 'TileInstallation' })
  return {
    title: t('title'),
    description: t('description'),
    alternates: buildAlternates(locale, '/renovation/tile-installation'),
  }
}

export default async function Page({ params }: Props) {
  await params // ensure locale segment is resolved
  return <ServicePageTemplate namespace="TileInstallation" category="renovation" />
}
