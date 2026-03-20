import createIntlMiddleware from 'next-intl/middleware'
import { type NextRequest, NextResponse } from 'next/server'
import { routing } from './src/i18n/routing'
import { applySecurityHeaders } from './src/lib/security-headers'

const handleI18nRouting = createIntlMiddleware(routing)

export function middleware(request: NextRequest): NextResponse {
  const pathname = request.nextUrl.pathname

  // 🔥 FIX ROOT → redirect corect
  if (pathname === '/') {
    return NextResponse.redirect(new URL('/nl', request.url))
  }

  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')

  const i18nResponse = handleI18nRouting(request)

  // dacă next-intl face redirect → return direct
  if (i18nResponse.status >= 300 && i18nResponse.status < 400) {
    applySecurityHeaders(i18nResponse.headers, nonce)
    return i18nResponse as NextResponse
  }

  // inject nonce în request
  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)

  const response = NextResponse.next({
    request: { headers: requestHeaders },
  })

  // copiem headers (cookies, locale etc.)
  i18nResponse.headers.forEach((value, key) => {
    if (key.toLowerCase() === 'set-cookie') {
      response.headers.append('set-cookie', value)
    } else {
      response.headers.set(key, value)
    }
  })

  applySecurityHeaders(response.headers, nonce)

  return response
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon\\.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp|ico|xml|txt)).*)',
  ],
}