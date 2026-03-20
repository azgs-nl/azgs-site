'use client'

import { useLocale } from 'next-intl'
import { usePathname as useNativePathname } from 'next/navigation'
import { useRouter } from '@/navigation'
import { routing } from '@/i18n/routing'
import { useState, useRef, useEffect } from 'react'

type Locale = (typeof routing.locales)[number]

const localeLabels: Record<string, { short: string; label: string; flag: string }> = {
  nl: { short: 'NL', label: 'Nederlands', flag: '🇳🇱' },
  en: { short: 'EN', label: 'English',    flag: '🇬🇧' },
  ro: { short: 'RO', label: 'Română',     flag: '🇷🇴' },
  de: { short: 'DE', label: 'Deutsch',    flag: '🇩🇪' },
  pl: { short: 'PL', label: 'Polski',     flag: '🇵🇱' },
  ru: { short: 'RU', label: 'Русский',    flag: '🇷🇺' },
}

export default function LanguageSwitcher() {
  // Read locale from URL path (/ru/...) — source of truth, no hydration lag
  const nativePathname = useNativePathname() // e.g. '/ru/servicii'
  const localeFromPath = nativePathname.split('/')[1] as Locale
  const localeFromCtx  = useLocale()
  const locale = routing.locales.includes(localeFromPath) ? localeFromPath : localeFromCtx

  const router = useRouter()
  const [open, setOpen] = useState(false)
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    function onClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false)
      }
    }
    document.addEventListener('mousedown', onClickOutside)
    return () => document.removeEventListener('mousedown', onClickOutside)
  }, [])

  function switchLocale(next: string) {
    // Strip locale prefix from native path: '/ru/servicii' → '/servicii'
    const segments = nativePathname.split('/')
    const pathWithoutLocale = '/' + segments.slice(2).join('/')
    router.replace(pathWithoutLocale || '/', { locale: next })
    setOpen(false)
  }

  const current = localeLabels[locale] ?? localeLabels['nl']

  return (
    <div ref={ref} className="relative">
      <button
        onClick={() => setOpen((v) => !v)}
        className="flex items-center gap-2 px-3 py-2 rounded-lg border border-gray-200
                   hover:border-brand-primary text-sm font-medium text-gray-700
                   hover:text-brand-primary transition-colors bg-white
                   focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary"
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label={`Taal: ${current.label}`}
      >
        <span>{current.flag}</span>
        <span>{current.short}</span>
        <svg
          className={`w-4 h-4 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
          fill="none" stroke="currentColor" viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {open && (
        <ul
          role="listbox"
          aria-label="Kies taal"
          className="absolute right-0 mt-1 w-44 bg-white border border-gray-200
                     rounded-xl shadow-lg py-1 z-50"
        >
          {routing.locales.map((loc) => {
            const info = localeLabels[loc]
            return (
              <li key={loc} role="option" aria-selected={loc === locale}>
                <button
                  onClick={() => switchLocale(loc)}
                  className={`w-full flex items-center gap-3 px-4 py-2 text-sm
                    hover:bg-gray-50 transition-colors
                    ${loc === locale
                      ? 'text-brand-primary font-semibold bg-blue-50'
                      : 'text-gray-700'
                    }`}
                >
                  <span>{info.flag}</span>
                  <span>{info.label}</span>
                  {loc === locale && (
                    <svg className="ml-auto w-4 h-4 text-brand-primary" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                </button>
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}

