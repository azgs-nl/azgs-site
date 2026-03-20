import { defineRouting } from 'next-intl/routing'

/**
 * ROUTING CONFIG — src/i18n/routing.ts
 *
 * Regulă: în cod folosești ÎNTOTDEAUNA cheia canonică (engleză).
 * next-intl generează automat URL-ul localizat corect per locale.
 *
 *   <Link href="/services/plumbing">  ← scriei asta
 *   /nl/diensten/loodgieter           ← browserul vede asta (nl)
 *   /en/services/plumbing             ← browserul vede asta (en)
 */
export const routing = defineRouting({
  locales: ['nl', 'en', 'ro', 'de', 'pl', 'ru'],
  defaultLocale: 'nl',
  localePrefix: 'always',
  pathnames: {
    '/': '/',
    '/about': { nl: '/over-ons', en: '/about', ro: '/despre-noi', de: '/ueber-uns', pl: '/o-nas', ru: '/o-nas' },
    '/services': { nl: '/diensten', en: '/services', ro: '/servicii', de: '/leistungen', pl: '/uslugi', ru: '/uslugi' },
    '/services/plumbing': { nl: '/diensten/loodgieter', en: '/services/plumbing', ro: '/servicii/instalatii-sanitare', de: '/leistungen/sanitaer', pl: '/uslugi/hydraulik', ru: '/uslugi/santehnik' },
    '/services/electrical': { nl: '/diensten/elektricien', en: '/services/electrical', ro: '/servicii/instalatii-electrice', de: '/leistungen/elektrik', pl: '/uslugi/elektryk', ru: '/uslugi/elektrik' },
    '/services/heating': { nl: '/diensten/verwarming', en: '/services/heating', ro: '/servicii/incalzire', de: '/leistungen/heizung', pl: '/uslugi/ogrzewanie', ru: '/uslugi/otoplenie' },
    '/services/ventilation': { nl: '/diensten/ventilatie', en: '/services/ventilation', ro: '/servicii/ventilatie', de: '/leistungen/lueftung', pl: '/uslugi/wentylacja', ru: '/uslugi/ventilyaciya' },
    '/services/air-conditioning': { nl: '/diensten/airconditioning', en: '/services/air-conditioning', ro: '/servicii/aer-conditionat', de: '/leistungen/klimaanlage', pl: '/uslugi/klimatyzacja', ru: '/uslugi/kondicionirovanie' },
    '/services/underfloor-heating': { nl: '/diensten/vloerverwarming', en: '/services/underfloor-heating', ro: '/servicii/incalzire-pardoseala', de: '/leistungen/fussbodenheizung', pl: '/uslugi/ogrzewanie-podlogowe', ru: '/uslugi/teplyj-pol' },
    '/services/boiler-installation': { nl: '/diensten/ketelinstallatie', en: '/services/boiler-installation', ro: '/servicii/instalare-centrala-termica', de: '/leistungen/kesselinstallation', pl: '/uslugi/instalacja-kotla', ru: '/uslugi/ustanovka-kotla' },
    '/services/heat-pump': { nl: '/diensten/warmtepomp', en: '/services/heat-pump', ro: '/servicii/pompa-de-caldura', de: '/leistungen/waermepumpe', pl: '/uslugi/pompa-ciepla', ru: '/uslugi/teplovoj-nasos' },
    '/renovation': { nl: '/renovatie', en: '/renovation', ro: '/renovare', de: '/renovierung', pl: '/renowacja', ru: '/remont' },
    '/renovation/apartment-renovation': { nl: '/renovatie/appartement-renovatie', en: '/renovation/apartment-renovation', ro: '/renovare/apartament', de: '/renovierung/wohnungsrenovierung', pl: '/renowacja/remont-mieszkania', ru: '/remont/kvartiry' },
    '/renovation/bathroom-renovation': { nl: '/renovatie/badkamer-renovatie', en: '/renovation/bathroom-renovation', ro: '/renovare/baie', de: '/renovierung/badsanierung', pl: '/renowacja/lazienka', ru: '/remont/vannoy' },
    '/renovation/kitchen-renovation': { nl: '/renovatie/keuken-renovatie', en: '/renovation/kitchen-renovation', ro: '/renovare/bucatarie', de: '/renovierung/kuechenrenovierung', pl: '/renowacja/kuchnia', ru: '/remont/kuhni' },
    '/renovation/drywall': { nl: '/renovatie/gipsplaten', en: '/renovation/drywall', ro: '/renovare/gips-carton', de: '/renovierung/trockenbau', pl: '/renowacja/zabudowa-gipsowa', ru: '/remont/gipsokarton' },
    '/renovation/painting': { nl: '/renovatie/schilderwerk', en: '/renovation/painting', ro: '/renovare/zugraveli', de: '/renovierung/malerarbeiten', pl: '/renowacja/malowanie', ru: '/remont/pokraska' },
    '/renovation/plastering': { nl: '/renovatie/stucwerk', en: '/renovation/plastering', ro: '/renovare/tencuiala', de: '/renovierung/putzarbeiten', pl: '/renowacja/tynkowanie', ru: '/remont/shtukaturka' },
    '/renovation/flooring': { nl: '/renovatie/vloeren', en: '/renovation/flooring', ro: '/renovare/pardoseli', de: '/renovierung/bodenbelaege', pl: '/renowacja/podlogi', ru: '/remont/poly' },
    '/renovation/tile-installation': { nl: '/renovatie/tegelwerk', en: '/renovation/tile-installation', ro: '/renovare/faianta-gresie', de: '/renovierung/fliesenarbeiten', pl: '/renowacja/plytkowanie', ru: '/remont/ukladka-plitki' },
    '/emergency': { nl: '/spoed', en: '/emergency', ro: '/urgente', de: '/notfall', pl: '/pogotowie', ru: '/srochnye-vyzovy' },
    '/projects': { nl: '/projecten', en: '/projects', ro: '/proiecte', de: '/projekte', pl: '/projekty', ru: '/proekty' },
    '/contact': { nl: '/contact', en: '/contact', ro: '/contact', de: '/kontakt', pl: '/kontakt', ru: '/kontakt' },
    '/privacy': { nl: '/privacybeleid', en: '/privacy-policy', ro: '/politica-de-confidentialitate', de: '/datenschutz', pl: '/polityka-prywatnosci', ru: '/politika-konfidencialnosti' },
    '/terms': { nl: '/algemene-voorwaarden', en: '/terms-and-conditions', ro: '/termeni-si-conditii', de: '/agb', pl: '/regulamin', ru: '/usloviya-ispolzovaniya' },
  },
})
