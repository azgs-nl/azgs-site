/**
 * Security Headers Utility
 *
 * Single source of truth for all HTTP security headers.
 * Used by middleware.ts (HTML pages, with nonce-based CSP)
 * and next.config.ts (API routes, with static CSP).
 */

/** Build a strict nonce-based Content Security Policy string. */
export function buildCsp(nonce: string): string {
  const directives: [string, string[]][] = [
    ['default-src', ["'self'"]],
    [
      'script-src',
      [
        "'self'",
        `'nonce-${nonce}'`,
        // 'strict-dynamic' allows scripts loaded by a trusted nonce to load further scripts
        "'strict-dynamic'",
        // Google Tag Manager / Analytics — remove if not used
        'https://www.googletagmanager.com',
        'https://www.google-analytics.com',
      ],
    ],
    [
      'style-src',
      [
        "'self'",
        // Required for Tailwind CSS utility classes injected at runtime in dev
        // In production with a proper build, this can be removed if you extract CSS
        "'unsafe-inline'",
        'https://fonts.googleapis.com',
      ],
    ],
    ['font-src', ["'self'", 'https://fonts.gstatic.com']],
    ['img-src', ["'self'", 'data:', 'https:']],
    [
      'connect-src',
      [
        "'self'",
        'https://www.google-analytics.com',
        'https://region1.google-analytics.com',
      ],
    ],
    ['media-src', ["'self'"]],
    ['object-src', ["'none'"]],
    ['frame-src', ["'none'"]],
    ['frame-ancestors', ["'none'"]],
    ['base-uri', ["'self'"]],
    ['form-action', ["'self'"]],
    // Force HTTPS for all subresources
    ['upgrade-insecure-requests', []],
  ]

  return directives
    .map(([key, values]) =>
      values.length > 0 ? `${key} ${values.join(' ')}` : key,
    )
    .join('; ')
}

/**
 * Apply all security headers to a Headers object.
 * Call this in middleware for every HTML page response.
 */
export function applySecurityHeaders(headers: Headers, nonce: string): void {
  headers.set('Content-Security-Policy', buildCsp(nonce))

  // Prevent clickjacking — already covered by frame-ancestors in CSP,
  // but X-Frame-Options is kept for legacy browsers
  headers.set('X-Frame-Options', 'DENY')

  // Prevent MIME-type sniffing
  headers.set('X-Content-Type-Options', 'nosniff')

  // Control referrer information sent with requests
  headers.set('Referrer-Policy', 'strict-origin-when-cross-origin')

  // Disable unused browser features
  headers.set(
    'Permissions-Policy',
    'camera=(), microphone=(), geolocation=(), payment=(), usb=(), magnetometer=()',
  )

  // Enable DNS prefetching for performance (safe to enable)
  headers.set('X-DNS-Prefetch-Control', 'on')

  // HSTS — only in production (localhost is HTTP)
  if (process.env.NODE_ENV === 'production') {
    headers.set(
      'Strict-Transport-Security',
      'max-age=63072000; includeSubDomains; preload',
    )
  }
}

/**
 * Static CSP for API routes (no nonce — responses are JSON, not HTML).
 * More restrictive than HTML pages: no scripts, no frames.
 */
export const API_CSP = "default-src 'none'; frame-ancestors 'none'"
