'use client'

import { useState, useRef, useEffect, useId } from 'react'
import { Link } from '@/navigation'
import type { ComponentProps } from 'react'

export type CanonicalHref = ComponentProps<typeof Link>['href']

export interface DropdownItem {
  href: CanonicalHref
  label: string
}

interface NavDropdownProps {
  label: string
  href: CanonicalHref
  items: DropdownItem[]
}

export default function NavDropdown({ label, href, items }: NavDropdownProps) {
  const [open, setOpen] = useState(false)
  const containerRef = useRef<HTMLDivElement>(null)
  const menuId = useId()

  useEffect(() => {
    const handleOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setOpen(false)
      }
    }
    const handleKeydown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setOpen(false)
    }
    document.addEventListener('mousedown', handleOutside)
    document.addEventListener('keydown', handleKeydown)
    return () => {
      document.removeEventListener('mousedown', handleOutside)
      document.removeEventListener('keydown', handleKeydown)
    }
  }, [])

  return (
    <div
      ref={containerRef}
      className="relative"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
    >
      <button
        type="button"
        id={`${menuId}-btn`}
        aria-haspopup="menu"
        aria-expanded={open}
        aria-controls={menuId}
        onClick={() => setOpen((v) => !v)}
        className="flex items-center gap-1 px-3 py-2 text-sm font-medium text-gray-600
                   hover:text-brand-primary rounded-lg hover:bg-gray-50 transition-colors
                   focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary"
      >
        {label}
        <svg
          className={`w-3.5 h-3.5 mt-px transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
          fill="none" stroke="currentColor" strokeWidth={2.5} viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {open && (
        <div
          id={menuId}
          role="menu"
          aria-labelledby={`${menuId}-btn`}
          className="absolute top-full left-0 mt-1 w-64 bg-white border border-gray-100
                     rounded-xl shadow-xl py-2 z-50 animate-in fade-in slide-in-from-top-2 duration-150"
        >
          {/* Ghost bridge — prevents gap between button and menu */}
          <div className="absolute -top-2 left-0 right-0 h-2" aria-hidden="true" />

          {/* Category overview link */}
          <Link
            href={href}
            role="menuitem"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2 mx-2 px-3 py-2 text-xs font-bold uppercase
                       tracking-wider text-brand-primary rounded-lg hover:bg-blue-50 transition-colors"
          >
            {label} →
          </Link>

          <div className="mx-2 my-1 border-t border-gray-100" />

          {items.map((item) => (
            <Link
              key={String(item.href)}
              href={item.href}
              role="menuitem"
              onClick={() => setOpen(false)}
              className="flex items-center gap-2.5 mx-2 px-3 py-2 text-sm text-gray-700
                         rounded-lg hover:bg-gray-50 hover:text-brand-primary transition-colors
                         focus:outline-none focus-visible:bg-gray-50 focus-visible:text-brand-primary"
            >
              <span className="w-1.5 h-1.5 rounded-full bg-brand-secondary shrink-0" aria-hidden="true" />
              {item.label}
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}
