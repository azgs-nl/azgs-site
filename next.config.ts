import type { NextConfig } from 'next'
import createNextIntlPlugin from 'next-intl/plugin'
import { API_CSP } from './src/lib/security-headers'

const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts')

const nextConfig: NextConfig = {
  // Remove X-Powered-By: Next.js header (don't advertise the stack)
  poweredByHeader: false,

  // Enable gzip/brotli compression
  compress: true,

  // Restrict which origins can invoke Server Actions (CSRF protection)
  experimental: {
    serverActions: {
      allowedOrigins: [
        process.env.NEXT_PUBLIC_BASE_URL?.replace(/^https?:\/\//, '') ?? 'azgs.nl',
        'localhost:3000',
      ],
    },
  },

  async headers() {
    return [
      {
        // API routes: apply static CSP (no nonces — JSON responses, not HTML)
        // HTML pages receive the nonce-based CSP from middleware.ts instead.
        source: '/api/:path*',
        headers: [
          { key: 'Content-Security-Policy', value: API_CSP },
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          {
            key: 'Permissions-Policy',
            value: 'camera=(), microphone=(), geolocation=(), payment=()',
          },
        ],
      },
    ]
  },
}

export default withNextIntl(nextConfig)
