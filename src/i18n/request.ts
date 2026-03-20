import { getRequestConfig } from 'next-intl/server'
import { routing } from './routing'

type Locale = (typeof routing.locales)[number]

const MESSAGE_FILES = ['common', 'home', 'services', 'renovation', 'pages'] as const

export default getRequestConfig(async ({ requestLocale }) => {
  let locale = await requestLocale
  if (!locale || !routing.locales.includes(locale as Locale)) {
    locale = routing.defaultLocale
  }

  const parts = await Promise.all(
    MESSAGE_FILES.map((file) =>
      import(`../../messages/${locale}/${file}.json`).then((m) => m.default)
    )
  )

  const messages = Object.assign({}, ...parts)
  return { locale, messages }
})
