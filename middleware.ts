import createIntlMiddleware from 'next-intl/middleware'
import { type NextRequest, NextResponse } from 'next/server'
import { routing } from './src/i18n/routing'
import { applySecurityHeaders } from './src/lib/security-headers'

const handleI18nRouting = createIntlMiddleware(routing)

export function middleware(request: NextRequest): NextResponse {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')

  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)

  const response = handleI18nRouting({
    ...request,
    headers: requestHeaders,
  } as NextRequest)

  applySecurityHeaders(response.headers, nonce)

  return response
}

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|favicon.ico|.*\\..*).*)',
  ],
}