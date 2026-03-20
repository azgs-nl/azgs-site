import { createNavigation } from 'next-intl/navigation'
import { routing } from './i18n/routing'

/**
 * NAVIGATION HELPERS — src/navigation.ts
 *
 * Exportă versiunile locale-aware ale helpers-urilor de navigație Next.js.
 * Toate sunt type-safe față de `pathnames` definite în routing.ts.
 *
 * Folosește ÎNTOTDEAUNA aceste importuri în loc de cele din 'next/navigation':
 *   import { Link, useRouter, usePathname, redirect, getPathname } from '@/navigation'
 *
 * Exemple:
 *   <Link href="/services">  → generează /nl/diensten, /en/services etc.
 *   useRouter().push('/contact')
 *   redirect('/about')
 *   getPathname({ locale: 'nl', href: '/services' }) → '/diensten'
 */
export const { Link, redirect, useRouter, usePathname, getPathname } =
  createNavigation(routing)
