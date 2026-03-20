# AZGS.nl — Module 1 Foundation

## Stack

- **Next.js 15** — App Router, static-first
- **TypeScript**
- **Tailwind CSS** — primary `#003366`, secondary `#FF8C00`
- **next-intl v3** — i18n cu pathnames localizate
- **Locales**: `nl` (default), `en`, `ro`, `de`, `pl`, `ru`

---

## Structura proiectului

```
azgs-nl/
├── middleware.ts                  # i18n routing + security headers (CSP, HSTS etc.)
├── next.config.ts                 # poweredByHeader off, CSRF serverActions
├── tailwind.config.ts
│
├── messages/
│   └── [locale]/
│       ├── common.json            # Metadata, Navigation, Footer
│       └── home.json              # Hero, Features, CTA
│
└── src/
    ├── navigation.ts              # createNavigation() — Link, useRouter, usePathname
    ├── i18n/
    │   ├── routing.ts             # defineRouting — locales, localePrefix: always, pathnames
    │   └── request.ts             # getRequestConfig — merge common + home per locale
    ├── lib/
    │   ├── security-headers.ts    # buildCsp(nonce), applySecurityHeaders(), API_CSP
    │   └── rate-limit.ts          # sliding window rate limiter (swap-ready pentru Redis)
    ├── components/
    │   ├── Header.tsx             # Server Component
    │   ├── NavDropdown.tsx        # Client Component — dropdown Installaties/Renovatie
    │   ├── Footer.tsx             # Server Component
    │   └── LanguageSwitcher.tsx   # Client Component — flags dropdown
    └── app/
        ├── globals.css            # Tailwind base + utilitare
        ├── layout.tsx             # ROOT LAYOUT — singurul cu <html> și <body>, static pur
        ├── sitemap.ts             # Native Next.js — URL-uri localizate via getPathname()
        ├── robots.ts              # Native Next.js
        └── [locale]/
            ├── layout.tsx         # LOCALE LAYOUT — nested, fără <html>/<body>
            └── page.tsx           # Homepage
```

---

## Regula fundamentală de routing

```
În cod (componente, Link, redirect)  →  rute CANONICE în engleză
În browser (URL vizibil)             →  rute LOCALIZATE generate de next-intl

Exemplu:
  <Link href="/services">   ← scrii asta întotdeauna
  /nl/diensten              ← browserul vede asta pentru locale nl
  /en/services              ← browserul vede asta pentru locale en
  /ro/servicii              ← browserul vede asta pentru locale ro
```

**Nu folosi niciodată** `href="/diensten"`, `href="/over-ons"` etc. în componente.

---

## URL structuur

| Canonical (intern) | nl | en | ro |
|---|---|---|---|
| `/` | `/nl/` | `/en/` | `/ro/` |
| `/about` | `/nl/over-ons` | `/en/about` | `/ro/despre-noi` |
| `/services` | `/nl/diensten` | `/en/services` | `/ro/servicii` |
| `/services/installations` | `/nl/diensten/installaties` | `/en/services/installations` | `/ro/servicii/instalatii` |
| `/services/renovation` | `/nl/diensten/renovatie` | `/en/services/renovation` | `/ro/servicii/renovare` |
| `/contact` | `/nl/contact` | `/en/contact` | `/ro/contact` |
| `/privacy` | `/nl/privacybeleid` | `/en/privacy-policy` | `/ro/politica-de-confidentialitate` |
| `/terms` | `/nl/algemene-voorwaarden` | `/en/terms-and-conditions` | `/ro/termeni-si-conditii` |

---

## Instalare și start

```bash
npm install
cp .env.local.example .env.local
npm run dev
```

Deschide [http://localhost:3000](http://localhost:3000) — redirecționează automat la `/nl/`.

---

## Arhitectura layout-urilor

```
src/app/layout.tsx             ← ROOT: <html> + <body> + globals.css
                                        static pur, fără headers(), fără async
  └── src/app/[locale]/layout.tsx  ← LOCALE: nested, fără <html>/<body>
                                        NextIntlClientProvider + Header + Footer
        └── src/app/[locale]/page.tsx   ← PAGE
```

---

## Cum se extinde — Module 2+

**Pagină nouă** (ex: `/services/installations`):
1. `src/app/[locale]/services/installations/page.tsx` — fișier nou
2. `messages/[locale]/installations.json` — traduceri noi
3. `src/i18n/request.ts` → adaugă `'installations'` în `MESSAGE_FILES`
4. `src/app/sitemap.ts` → decomentează `/services/installations`

**API route cu rate limiting**:
```ts
// src/app/api/contact/route.ts
import { rateLimit, rateLimitHeaders } from '@/lib/rate-limit'

const ip = request.headers.get('x-forwarded-for') ?? 'anonymous'
const result = rateLimit(ip, { windowMs: 60_000, max: 5 })
if (!result.success) {
  return new Response('Too Many Requests', {
    status: 429,
    headers: rateLimitHeaders(result),
  })
}
```

---

## Security Layer (Module 1)

| Header | Valoare |
|---|---|
| `Content-Security-Policy` | nonce-based, strict |
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | camera, mic, geolocation off |
| `Strict-Transport-Security` | `max-age=63072000` (production) |

JSON-LD (structured data) este omis în Module 1 — se reintroduce în Module 2
cu nonce CSP-compatible din locale layout.

