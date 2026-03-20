import createIntlMiddleware from 'next-intl/middleware'
import { type NextRequest, NextResponse } from 'next/server'
import { routing } from './src/i18n/routing'
import { applySecurityHeaders } from './src/lib/security-headers'

const handleI18nRouting = createIntlMiddleware(routing)

export function middleware(request: NextRequest): NextResponse {
  // Nonce unic per request — folosit în CSP (script-src 'nonce-xxx').
  // Injectat în request headers pentru a fi disponibil în Server Components
  // care au nevoie de el în Module 2 (ex: JSON-LD, Google Analytics).
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')

  const i18nResponse = handleI18nRouting(request)

  // Redirect (ex: / → /nl/) — aplică security headers și returnează imediat
  if (i18nResponse.status >= 300 && i18nResponse.status < 400) {
    applySecurityHeaders(i18nResponse.headers, nonce)
    return i18nResponse as NextResponse
  }

  // Injectează nonce în request headers — disponibil în Module 2
  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)

  const response = NextResponse.next({ request: { headers: requestHeaders } })

  // Copiază cookie-uri și alte headers de la next-intl (ex: locale cookie)
  i18nResponse.headers.forEach((value, key) => {
    if (key.toLowerCase() === 'set-cookie') {
      response.headers.append('set-cookie', value)
    } else {
      response.headers.set(key, value)
    }
  })

  // Aplică CSP cu nonce + restul security headers pe response
  applySecurityHeaders(response.headers, nonce)

  return response
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon\\.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp|ico|xml|txt)).*)',
  ],
}
