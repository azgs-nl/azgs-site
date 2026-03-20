/**
 * Rate Limiter — Sliding Window Algorithm
 *
 * CURRENT: In-memory store (single-instance deployments / development).
 * PRODUCTION UPGRADE: Replace `store` with Redis or Upstash for multi-instance.
 *
 * Example upgrade path:
 *   import { Redis } from '@upstash/redis'
 *   const redis = new Redis({ url: process.env.UPSTASH_REDIS_URL!, token: process.env.UPSTASH_REDIS_TOKEN! })
 *   // Then replace store.get/set/delete with redis.get/set/del
 *
 * Usage in an API route handler:
 *   const identifier = request.ip ?? request.headers.get('x-forwarded-for') ?? 'anonymous'
 *   const result = rateLimit(identifier, { windowMs: 60_000, max: 20 })
 *   if (!result.success) {
 *     return new Response('Too Many Requests', {
 *       status: 429,
 *       headers: {
 *         'Retry-After': String(Math.ceil((result.reset - Date.now()) / 1000)),
 *         'X-RateLimit-Limit': String(result.limit),
 *         'X-RateLimit-Remaining': '0',
 *         'X-RateLimit-Reset': String(result.reset),
 *       },
 *     })
 *   }
 */

export interface RateLimitOptions {
  /** Time window in milliseconds. Default: 60 000 (1 minute) */
  windowMs?: number
  /** Maximum number of requests allowed in the window. Default: 20 */
  max?: number
}

export interface RateLimitResult {
  /** Whether the request is within the rate limit */
  success: boolean
  /** Number of requests remaining in the current window */
  remaining: number
  /** Unix timestamp (ms) when the current window resets */
  reset: number
  /** Configured maximum requests per window */
  limit: number
}

interface StoreEntry {
  count: number
  resetAt: number
}

// In-memory store — swap with Redis for production multi-instance deployments
const store = new Map<string, StoreEntry>()

// Purge expired entries every 5 minutes to prevent memory leaks
if (typeof setInterval !== 'undefined') {
  setInterval(() => {
    const now = Date.now()
    store.forEach((entry, key) => {
      if (entry.resetAt < now) store.delete(key)
    })
  }, 5 * 60 * 1_000)
}

/**
 * Check and increment rate limit for the given identifier.
 * @param identifier - Unique key per client (e.g. IP address or user ID)
 * @param options - Rate limit configuration
 */
export function rateLimit(
  identifier: string,
  options: RateLimitOptions = {},
): RateLimitResult {
  const windowMs = options.windowMs ?? 60_000
  const max = options.max ?? 20
  const now = Date.now()

  const existing = store.get(identifier)

  // Start a new window if none exists or the previous window has expired
  if (!existing || existing.resetAt < now) {
    const resetAt = now + windowMs
    store.set(identifier, { count: 1, resetAt })
    return { success: true, remaining: max - 1, reset: resetAt, limit: max }
  }

  existing.count++
  store.set(identifier, existing)

  const remaining = Math.max(0, max - existing.count)

  return {
    success: existing.count <= max,
    remaining,
    reset: existing.resetAt,
    limit: max,
  }
}

/**
 * Helper: build rate-limit response headers (RFC 6585 / IETF draft).
 * Attach these to your 429 response.
 */
export function rateLimitHeaders(result: RateLimitResult): Record<string, string> {
  return {
    'X-RateLimit-Limit': String(result.limit),
    'X-RateLimit-Remaining': String(result.remaining),
    'X-RateLimit-Reset': String(result.reset),
    ...(result.success ? {} : { 'Retry-After': String(Math.ceil((result.reset - Date.now()) / 1000)) }),
  }
}
