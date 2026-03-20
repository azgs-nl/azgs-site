import type { ReactNode } from 'react'
import './globals.css'

/**
 * ROOT LAYOUT — src/app/layout.tsx
 *
 * Singurul fișier care definește <html> și <body> — conform Next.js App Router.
 * Complet static: fără async, fără headers(), fără params, fără Dynamic APIs.
 *
 * lang este omis intenționat: locale layout nu poate suprascrie atributul
 * din root layout server-side fără Dynamic APIs. SEO multilingv real
 * funcționează prin hreflang în generateMetadata — nu prin lang=.
 *
 * globals.css importat o singură dată, la nivelul corect.
 */
export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html suppressHydrationWarning>
      <body className="min-h-screen flex flex-col bg-white text-gray-900 antialiased">
        {children}
      </body>
    </html>
  )
}
