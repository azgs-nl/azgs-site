'use client'

import { useState, useEffect, useRef } from 'react'
import { Link } from '@/navigation'
import type { CanonicalHref, DropdownItem } from './NavDropdown'

interface MobileMenuProps {
  servicesLabel: string
  renovationLabel: string
  emergencyLabel: string
  projectsLabel: string
  aboutLabel: string
  contactLabel: string
  ctaLabel: string
  servicesItems: DropdownItem[]
  renovationItems: DropdownItem[]
}

export default function MobileMenu({
  servicesLabel, renovationLabel, emergencyLabel,
  projectsLabel, aboutLabel, contactLabel, ctaLabel,
  servicesItems, renovationItems,
}: MobileMenuProps) {
  const [open, setOpen] = useState(false)
  const [expandedSection, setExpandedSection] = useState<string | null>(null)
  const firstFocusRef = useRef<HTMLButtonElement>(null)

  // Lock body scroll and manage focus when open
  useEffect(() => {
    if (open) {
      document.body.style.overflow = 'hidden'
      firstFocusRef.current?.focus()
    } else {
      document.body.style.overflow = ''
      setExpandedSection(null)
    }
    return () => { document.body.style.overflow = '' }
  }, [open])

  // Close on Escape
  useEffect(() => {
    const handler = (e: KeyboardEvent) => { if (e.key === 'Escape') setOpen(false) }
    document.addEventListener('keydown', handler)
    return () => document.removeEventListener('keydown', handler)
  }, [])

  const close = () => setOpen(false)
  const toggleSection = (section: string) => {
    setExpandedSection((prev) => (prev === section ? null : section))
  }

  return (
    <>
      {/* Hamburger */}
      <button
        type="button"
        aria-label="Menu openen"
        aria-expanded={open}
        onClick={() => setOpen(true)}
        className="lg:hidden inline-flex items-center justify-center w-10 h-10 rounded-lg
                   text-gray-600 hover:text-brand-primary hover:bg-gray-100 transition-colors
                   focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary"
      >
        <svg className="w-6 h-6" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      {/* Backdrop */}
      {open && (
        <div
          className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm lg:hidden"
          aria-hidden="true"
          onClick={close}
        />
      )}

      {/* Drawer */}
      <div
        role="dialog"
        aria-modal="true"
        aria-label="Navigatiemenu"
        className={`fixed top-0 right-0 z-50 h-full w-80 max-w-[90vw] bg-white shadow-2xl
                    flex flex-col transform transition-transform duration-300 ease-out lg:hidden
                    ${open ? 'translate-x-0' : 'translate-x-full'}`}
      >
        {/* Drawer header */}
        <div className="flex items-center justify-between px-5 h-16 border-b border-gray-100 shrink-0">
          <Link href="/" onClick={close} className="flex items-center gap-1.5">
            <span className="text-xl font-extrabold text-brand-primary">AZGS</span>
            <span className="text-xs font-semibold text-brand-secondary border border-brand-secondary/40 px-1.5 py-0.5 rounded-full">.nl</span>
          </Link>
          <button
            ref={firstFocusRef}
            type="button"
            aria-label="Menu sluiten"
            onClick={close}
            className="w-9 h-9 flex items-center justify-center rounded-lg text-gray-500
                       hover:text-gray-900 hover:bg-gray-100 transition-colors
                       focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" strokeWidth={2.5} viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Nav items */}
        <nav className="flex-1 overflow-y-auto py-4 px-4">

          {/* Emergency — always visible and prominent */}
          <Link
            href="/emergency"
            onClick={close}
            className="flex items-center gap-2 px-4 py-3 mb-3 rounded-xl bg-brand-secondary/10
                       text-brand-secondary font-bold text-sm border border-brand-secondary/30"
          >
            <span className="w-2 h-2 rounded-full bg-brand-secondary animate-pulse" />
            {emergencyLabel}
          </Link>

          {/* Installatietechniek accordion */}
          <AccordionSection
            label={servicesLabel}
            sectionKey="services"
            expanded={expandedSection === 'services'}
            onToggle={() => toggleSection('services')}
            overviewHref="/services"
            items={servicesItems}
            onClose={close}
          />

          {/* Renovatie accordion */}
          <AccordionSection
            label={renovationLabel}
            sectionKey="renovation"
            expanded={expandedSection === 'renovation'}
            onToggle={() => toggleSection('renovation')}
            overviewHref="/renovation"
            items={renovationItems}
            onClose={close}
          />

          <Divider />

          <NavLink href="/projects" label={projectsLabel} onClick={close} />
          <NavLink href="/about" label={aboutLabel} onClick={close} />
          <NavLink href="/contact" label={contactLabel} onClick={close} />
        </nav>

        {/* CTA footer */}
        <div className="px-4 py-4 border-t border-gray-100 shrink-0">
          <Link
            href="/contact"
            onClick={close}
            className="flex items-center justify-center gap-2 w-full bg-brand-primary text-white
                       font-bold text-sm px-4 py-3.5 rounded-xl hover:bg-blue-900 transition-colors"
          >
            <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            {ctaLabel}
          </Link>
        </div>
      </div>
    </>
  )
}

// ─── Sub-components ───────────────────────────────────────────────────────────

function NavLink({ href, label, onClick }: { href: CanonicalHref; label: string; onClick: () => void }) {
  return (
    <Link
      href={href}
      onClick={onClick}
      className="flex items-center px-4 py-3 text-sm font-medium text-gray-700
                 rounded-xl hover:bg-gray-50 hover:text-brand-primary transition-colors"
    >
      {label}
    </Link>
  )
}

function Divider() {
  return <div className="my-2 border-t border-gray-100" />
}

function AccordionSection({
  label, sectionKey, expanded, onToggle, overviewHref, items, onClose,
}: {
  label: string
  sectionKey: string
  expanded: boolean
  onToggle: () => void
  overviewHref: CanonicalHref
  items: DropdownItem[]
  onClose: () => void
}) {
  return (
    <div className="mb-1">
      <button
        type="button"
        aria-expanded={expanded}
        onClick={onToggle}
        className="flex items-center justify-between w-full px-4 py-3 text-sm font-semibold
                   text-gray-700 rounded-xl hover:bg-gray-50 hover:text-brand-primary transition-colors
                   focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary"
      >
        {label}
        <svg
          className={`w-4 h-4 transition-transform duration-200 ${expanded ? 'rotate-180' : ''}`}
          fill="none" stroke="currentColor" strokeWidth={2.5} viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {expanded && (
        <div className="mt-1 ml-4 border-l-2 border-brand-secondary/30 pl-3">
          <Link
            href={overviewHref}
            onClick={onClose}
            className="block py-2 px-2 text-xs font-bold uppercase tracking-wider text-brand-primary
                       hover:text-brand-secondary transition-colors"
          >
            {label} →
          </Link>
          {items.map((item) => (
            <Link
              key={String(item.href)}
              href={item.href}
              onClick={onClose}
              className="flex items-center gap-2 py-2 px-2 text-sm text-gray-600
                         hover:text-brand-primary transition-colors rounded-lg hover:bg-gray-50"
            >
              <span className="w-1.5 h-1.5 rounded-full bg-brand-secondary/60 shrink-0" />
              {item.label}
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}
