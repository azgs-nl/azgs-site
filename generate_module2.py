#!/usr/bin/env python3
"""Generator Module 2 — mesaje JSON pentru toate cele 6 locale."""
import json, os

def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {path}")

BASE = "/home/claude/azgs-nl/messages"

# ─── COMMON.JSON ─────────────────────────────────────────────────────────────

common = {
    "nl": {
        "Metadata": {
            "title": "AZGS — Installatietechniek & Renovatie | Amsterdam",
            "description": "Professionele loodgieter, elektricien, verwarming en renovatie in Amsterdam en omstreken. 24/7 spoedservice beschikbaar."
        },
        "Navigation": {
            "home": "Home",
            "services": "Installatietechniek",
            "renovation": "Renovatie",
            "emergency": "Spoed 24/7",
            "about": "Over Ons",
            "contact": "Contact",
            "cta": "Bel Nu",
            "plumbing": "Loodgieter",
            "electrical": "Elektricien",
            "heating": "Verwarming",
            "ventilation": "Ventilatie",
            "airConditioning": "Airconditioning",
            "underfloorHeating": "Vloerverwarming",
            "boilerInstallation": "Ketelinstallatie",
            "heatPump": "Warmtepomp",
            "apartmentRenovation": "Appartement renovatie",
            "bathroomRenovation": "Badkamer renovatie",
            "kitchenRenovation": "Keuken renovatie",
            "drywall": "Gipsplaten",
            "painting": "Schilderwerk",
            "plastering": "Stucwerk",
            "flooring": "Vloeren",
            "tileInstallation": "Tegelwerk"
        },
        "Footer": {
            "tagline": "Uw betrouwbare partner voor installaties en renovaties in Amsterdam en omstreken.",
            "linksTitle": "Navigatie",
            "contactTitle": "Contact",
            "linkHome": "Home",
            "linkAbout": "Over Ons",
            "linkServices": "Diensten",
            "linkContact": "Contact",
            "privacy": "Privacybeleid",
            "terms": "Algemene Voorwaarden",
            "allRights": "Alle rechten voorbehouden."
        }
    },
    "en": {
        "Metadata": {
            "title": "AZGS — Installation & Renovation Services | Amsterdam",
            "description": "Professional plumbing, electrical, heating and renovation in Amsterdam. 24/7 emergency service available."
        },
        "Navigation": {
            "home": "Home",
            "services": "Installation Services",
            "renovation": "Renovation",
            "emergency": "Emergency 24/7",
            "about": "About Us",
            "contact": "Contact",
            "cta": "Call Now",
            "plumbing": "Plumbing",
            "electrical": "Electrical",
            "heating": "Heating",
            "ventilation": "Ventilation",
            "airConditioning": "Air Conditioning",
            "underfloorHeating": "Underfloor Heating",
            "boilerInstallation": "Boiler Installation",
            "heatPump": "Heat Pump",
            "apartmentRenovation": "Apartment Renovation",
            "bathroomRenovation": "Bathroom Renovation",
            "kitchenRenovation": "Kitchen Renovation",
            "drywall": "Drywall",
            "painting": "Painting",
            "plastering": "Plastering",
            "flooring": "Flooring",
            "tileInstallation": "Tile Installation"
        },
        "Footer": {
            "tagline": "Your trusted partner for installations and renovations in Amsterdam.",
            "linksTitle": "Navigation",
            "contactTitle": "Contact",
            "linkHome": "Home",
            "linkAbout": "About Us",
            "linkServices": "Services",
            "linkContact": "Contact",
            "privacy": "Privacy Policy",
            "terms": "Terms & Conditions",
            "allRights": "All rights reserved."
        }
    },
    "ro": {
        "Metadata": {
            "title": "AZGS — Instalații & Renovări | Amsterdam",
            "description": "Instalații sanitare, electrice, termice și renovări în Amsterdam. Serviciu de urgență 24/7."
        },
        "Navigation": {
            "home": "Acasă",
            "services": "Instalații",
            "renovation": "Renovări",
            "emergency": "Urgențe 24/7",
            "about": "Despre Noi",
            "contact": "Contact",
            "cta": "Sună Acum",
            "plumbing": "Instalații Sanitare",
            "electrical": "Instalații Electrice",
            "heating": "Încălzire",
            "ventilation": "Ventilație",
            "airConditioning": "Aer Condiționat",
            "underfloorHeating": "Încălzire Pardoseală",
            "boilerInstallation": "Instalare Centrală",
            "heatPump": "Pompă de Căldură",
            "apartmentRenovation": "Renovare Apartament",
            "bathroomRenovation": "Renovare Baie",
            "kitchenRenovation": "Renovare Bucătărie",
            "drywall": "Gips-Carton",
            "painting": "Zugrăveli",
            "plastering": "Tencuieli",
            "flooring": "Pardoseli",
            "tileInstallation": "Faianță & Gresie"
        },
        "Footer": {
            "tagline": "Partenerul dumneavoastră de încredere pentru instalații și renovări în Amsterdam.",
            "linksTitle": "Navigație",
            "contactTitle": "Contact",
            "linkHome": "Acasă",
            "linkAbout": "Despre Noi",
            "linkServices": "Servicii",
            "linkContact": "Contact",
            "privacy": "Politică Confidențialitate",
            "terms": "Termeni și Condiții",
            "allRights": "Toate drepturile rezervate."
        }
    },
    "de": {
        "Metadata": {
            "title": "AZGS — Installation & Renovierung | Amsterdam",
            "description": "Professionelle Sanitär-, Elektro-, Heizungs- und Renovierungsarbeiten in Amsterdam. 24/7 Notdienst."
        },
        "Navigation": {
            "home": "Startseite",
            "services": "Installationstechnik",
            "renovation": "Renovierung",
            "emergency": "Notdienst 24/7",
            "about": "Über Uns",
            "contact": "Kontakt",
            "cta": "Jetzt Anrufen",
            "plumbing": "Sanitär",
            "electrical": "Elektrik",
            "heating": "Heizung",
            "ventilation": "Lüftung",
            "airConditioning": "Klimaanlage",
            "underfloorHeating": "Fußbodenheizung",
            "boilerInstallation": "Kesselinstallation",
            "heatPump": "Wärmepumpe",
            "apartmentRenovation": "Wohnungsrenovierung",
            "bathroomRenovation": "Badsanierung",
            "kitchenRenovation": "Küchenrenovierung",
            "drywall": "Trockenbau",
            "painting": "Malerarbeiten",
            "plastering": "Putzarbeiten",
            "flooring": "Bodenbeläge",
            "tileInstallation": "Fliesenarbeiten"
        },
        "Footer": {
            "tagline": "Ihr zuverlässiger Partner für Installationen und Renovierungen in Amsterdam.",
            "linksTitle": "Navigation",
            "contactTitle": "Kontakt",
            "linkHome": "Startseite",
            "linkAbout": "Über Uns",
            "linkServices": "Leistungen",
            "linkContact": "Kontakt",
            "privacy": "Datenschutz",
            "terms": "AGB",
            "allRights": "Alle Rechte vorbehalten."
        }
    },
    "pl": {
        "Metadata": {
            "title": "AZGS — Instalacje & Renowacje | Amsterdam",
            "description": "Profesjonalne usługi hydrauliczne, elektryczne, grzewcze i remontowe w Amsterdamie. Pogotowie 24/7."
        },
        "Navigation": {
            "home": "Strona Główna",
            "services": "Instalacje",
            "renovation": "Renowacje",
            "emergency": "Pogotowie 24/7",
            "about": "O Nas",
            "contact": "Kontakt",
            "cta": "Zadzwoń",
            "plumbing": "Hydraulik",
            "electrical": "Elektryk",
            "heating": "Ogrzewanie",
            "ventilation": "Wentylacja",
            "airConditioning": "Klimatyzacja",
            "underfloorHeating": "Ogrzewanie Podłogowe",
            "boilerInstallation": "Instalacja Kotła",
            "heatPump": "Pompa Ciepła",
            "apartmentRenovation": "Remont Mieszkania",
            "bathroomRenovation": "Remont Łazienki",
            "kitchenRenovation": "Remont Kuchni",
            "drywall": "Zabudowa Gipsowa",
            "painting": "Malowanie",
            "plastering": "Tynkowanie",
            "flooring": "Podłogi",
            "tileInstallation": "Układanie Płytek"
        },
        "Footer": {
            "tagline": "Twój zaufany partner w zakresie instalacji i renowacji w Amsterdamie.",
            "linksTitle": "Nawigacja",
            "contactTitle": "Kontakt",
            "linkHome": "Strona Główna",
            "linkAbout": "O Nas",
            "linkServices": "Usługi",
            "linkContact": "Kontakt",
            "privacy": "Polityka Prywatności",
            "terms": "Regulamin",
            "allRights": "Wszelkie prawa zastrzeżone."
        }
    },
    "ru": {
        "Metadata": {
            "title": "AZGS — Монтаж & Ремонт | Амстердам",
            "description": "Профессиональный сантехник, электрик, отопление и ремонт в Амстердаме. Срочный вызов 24/7."
        },
        "Navigation": {
            "home": "Главная",
            "services": "Монтажные работы",
            "renovation": "Ремонт",
            "emergency": "Срочный вызов 24/7",
            "about": "О нас",
            "contact": "Контакт",
            "cta": "Позвонить",
            "plumbing": "Сантехник",
            "electrical": "Электрик",
            "heating": "Отопление",
            "ventilation": "Вентиляция",
            "airConditioning": "Кондиционирование",
            "underfloorHeating": "Тёплый пол",
            "boilerInstallation": "Установка котла",
            "heatPump": "Тепловой насос",
            "apartmentRenovation": "Ремонт квартиры",
            "bathroomRenovation": "Ремонт ванной",
            "kitchenRenovation": "Ремонт кухни",
            "drywall": "Гипсокартон",
            "painting": "Покраска",
            "plastering": "Штукатурка",
            "flooring": "Полы",
            "tileInstallation": "Укладка плитки"
        },
        "Footer": {
            "tagline": "Ваш надёжный партнёр по монтажу и ремонту в Амстердаме.",
            "linksTitle": "Навигация",
            "contactTitle": "Контакт",
            "linkHome": "Главная",
            "linkAbout": "О нас",
            "linkServices": "Услуги",
            "linkContact": "Контакт",
            "privacy": "Политика конфиденциальности",
            "terms": "Условия использования",
            "allRights": "Все права защищены."
        }
    }
}

for loc, data in common.items():
    # merge with existing home.json (don't overwrite)
    write(f"{BASE}/{loc}/common.json", data)

print("\n--- common.json done ---\n")

# ─── SERVICES.JSON ────────────────────────────────────────────────────────────

def service_nl(key, title, badge="Installatietechniek", desc=None, dutch_term=None):
    term = dutch_term or title
    desc = desc or f"Professionele {term.lower()} in Amsterdam en omstreken. Snel, betrouwbaar en gecertificeerd."
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": desc,
        "hero": {
            "badge": badge,
            "title": f"Professionele {term}",
            "subtitle": f"Vakkundige {term.lower()} service in Amsterdam en omstreken. Snel ter plaatse, eerlijke prijs.",
            "ctaPrimary": "Bel Nu — Gratis Advies",
            "ctaSecondary": "Bekijk Onze Diensten"
        },
        "problem": {
            "title": f"Problemen met uw {term.lower()}?",
            "text": f"Een defecte of verouderde installatie kan veel overlast geven. AZGS lost uw {term.lower()} problemen snel en vakkundig op — ook bij spoedgevallen buiten kantooruren."
        },
        "includes": {
            "title": "Wat is inbegrepen?",
            "item1": "Gratis inspectie en kostenraming",
            "item2": "Gecertificeerde monteurs",
            "item3": "Gebruik van A-merk materialen",
            "item4": "Werkgarantie op alle uitgevoerde werkzaamheden",
            "item5": "Nette en stofvrije werkplek",
            "item6": "Factuur met duidelijke kostenspecificatie"
        },
        "advantages": {
            "title": "Waarom AZGS?",
            "item1": "Meer dan 10 jaar ervaring in Amsterdam",
            "item2": "Gecertificeerd en volledig verzekerd",
            "item3": "Transparante prijzen — geen verrassingen achteraf",
            "item4": "24/7 bereikbaar voor spoedgevallen"
        },
        "process": {
            "title": "Hoe werkt het?",
            "step1Title": "Contact opnemen",
            "step1Text": "Bel ons of stuur een bericht. We reageren binnen 1 uur.",
            "step2Title": "Inspectie & offerte",
            "step2Text": "Onze monteur komt langs voor een gratis inspectie en vrijblijvende offerte.",
            "step3Title": "Uitvoering",
            "step3Text": "Na akkoord voeren we het werk vakkundig en netjes uit.",
            "step4Title": "Oplevering",
            "step4Text": "We leveren op met garantie en een duidelijke factuur."
        },
        "faq": {
            "title": "Veelgestelde Vragen",
            "q1": f"Hoe snel kan AZGS ter plaatse zijn voor een spoedgeval?",
            "a1": "Bij spoed zijn we doorgaans binnen 1-2 uur ter plaatse in Amsterdam en omstreken.",
            "q2": "Geeft AZGS garantie op het werk?",
            "a2": "Ja, wij geven standaard 12 maanden garantie op alle uitgevoerde werkzaamheden en gebruikte materialen.",
            "q3": "Werkt AZGS ook buiten kantooruren?",
            "a3": "Ja, onze spoedlijn is 24/7 bereikbaar, inclusief weekenden en feestdagen.",
            "q4": "Krijg ik van tevoren een prijsopgave?",
            "a4": "Altijd. We geven een schriftelijke offerte voor akkoord. Geen verborgen kosten.",
            "q5": f"Is AZGS gecertificeerd voor {term.lower()} werkzaamheden?",
            "a5": "Ja, al onze monteurs zijn gecertificeerd en werken conform Nederlandse normen en wetgeving."
        },
        "cta": {
            "title": "Klaar om te beginnen?",
            "text": "Vraag vandaag nog een gratis offerte aan. Wij reageren binnen 1 uur.",
            "btn": "Gratis Offerte Aanvragen"
        }
    }

def service_en(key, title, badge="Installation Services"):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Professional {title.lower()} services in Amsterdam. Certified technicians, fast response.",
        "hero": {
            "badge": badge,
            "title": f"Professional {title}",
            "subtitle": f"Expert {title.lower()} services in Amsterdam. Fast, reliable and certified.",
            "ctaPrimary": "Call Now — Free Advice",
            "ctaSecondary": "View Our Services"
        },
        "problem": {
            "title": f"Issues with your {title.lower()}?",
            "text": f"AZGS resolves your {title.lower()} problems quickly and professionally — including emergencies outside office hours."
        },
        "includes": {"title": "What's included?", "item1": "Free inspection & quote", "item2": "Certified technicians", "item3": "A-brand materials", "item4": "Work guarantee", "item5": "Clean workspace", "item6": "Detailed invoice"},
        "advantages": {"title": "Why AZGS?", "item1": "10+ years in Amsterdam", "item2": "Certified & insured", "item3": "Transparent pricing", "item4": "24/7 emergency line"},
        "process": {"title": "How it works", "step1Title": "Contact us", "step1Text": "Call or message us. We respond within 1 hour.", "step2Title": "Inspection & quote", "step2Text": "Free inspection and no-obligation quote.", "step3Title": "Execution", "step3Text": "Professional and clean work.", "step4Title": "Delivery", "step4Text": "Handover with guarantee and clear invoice."},
        "faq": {"title": "Frequently Asked Questions", "q1": "How quickly can AZGS respond to an emergency?", "a1": "For emergencies we are usually on-site within 1-2 hours in Amsterdam.", "q2": "Does AZGS provide a work guarantee?", "a2": "Yes, we provide 12 months guarantee on all work and materials.", "q3": "Does AZGS work outside office hours?", "a3": "Yes, our emergency line is available 24/7 including weekends.", "q4": "Will I receive a quote in advance?", "a4": "Always. We provide a written quote before starting. No hidden costs.", "q5": "Is AZGS certified?", "a5": "Yes, all our technicians are certified and work according to Dutch standards."},
        "cta": {"title": "Ready to get started?", "text": "Request a free quote today. We respond within 1 hour.", "btn": "Request Free Quote"}
    }

def service_ro(key, title, badge="Instalații"):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Servicii profesionale de {title.lower()} în Amsterdam. Tehnicieni certificați, intervenție rapidă.",
        "hero": {"badge": badge, "title": f"{title} Profesional", "subtitle": f"Servicii de {title.lower()} în Amsterdam. Rapid, de încredere și certificat.", "ctaPrimary": "Sună Acum", "ctaSecondary": "Vezi Serviciile"},
        "problem": {"title": f"Probleme cu {title.lower()}?", "text": f"AZGS rezolvă problemele dumneavoastră rapid și profesional — inclusiv urgențe în afara orelor de program."},
        "includes": {"title": "Ce include serviciul?", "item1": "Inspecție și deviz gratuit", "item2": "Tehnicieni certificați", "item3": "Materiale de calitate", "item4": "Garanție la lucrare", "item5": "Loc de muncă curat", "item6": "Factură detaliată"},
        "advantages": {"title": "De ce AZGS?", "item1": "10+ ani experiență în Amsterdam", "item2": "Certificat și asigurat", "item3": "Prețuri transparente", "item4": "Urgențe 24/7"},
        "process": {"title": "Cum funcționează?", "step1Title": "Contactați-ne", "step1Text": "Sunați sau trimiteți un mesaj. Răspundem în 1 oră.", "step2Title": "Inspecție & deviz", "step2Text": "Inspecție gratuită și ofertă fără obligații.", "step3Title": "Execuție", "step3Text": "Lucrare profesională și curată.", "step4Title": "Predare", "step4Text": "Predare cu garanție și factură clară."},
        "faq": {"title": "Întrebări Frecvente", "q1": "Cât de repede poate interveni AZGS în urgență?", "a1": "La urgențe, ajungem de obicei în 1-2 ore în Amsterdam.", "q2": "Oferă AZGS garanție la lucrări?", "a2": "Da, oferim garanție de 12 luni pentru toate lucrările și materialele.", "q3": "Lucrați și în afara orelor de program?", "a3": "Da, linia de urgențe este disponibilă 24/7 inclusiv weekenduri.", "q4": "Voi primi un deviz în avans?", "a4": "Întotdeauna. Deviz scris înainte de începere. Fără costuri ascunse.", "q5": "Este AZGS certificat?", "a5": "Da, toți tehnicienii noștri sunt certificați și lucrează conform standardelor olandeze."},
        "cta": {"title": "Gata să începeți?", "text": "Solicitați un deviz gratuit astăzi. Răspundem în 1 oră.", "btn": "Solicitați Deviz Gratuit"}
    }

def service_de(key, title, badge="Installationstechnik"):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Professionelle {title}-Leistungen in Amsterdam. Zertifizierte Techniker, schnelle Reaktion.",
        "hero": {"badge": badge, "title": f"Professionelle {title}", "subtitle": f"Fachkundige {title}-Leistungen in Amsterdam. Schnell, zuverlässig und zertifiziert.", "ctaPrimary": "Jetzt Anrufen", "ctaSecondary": "Leistungen Ansehen"},
        "problem": {"title": f"Probleme mit {title}?", "text": f"AZGS löst Ihre {title}-Probleme schnell und professionell — auch bei Notfällen außerhalb der Geschäftszeiten."},
        "includes": {"title": "Was ist enthalten?", "item1": "Kostenlose Inspektion & Angebot", "item2": "Zertifizierte Techniker", "item3": "Markenqualität", "item4": "Arbeitsgarantie", "item5": "Saubere Baustelle", "item6": "Detaillierte Rechnung"},
        "advantages": {"title": "Warum AZGS?", "item1": "10+ Jahre in Amsterdam", "item2": "Zertifiziert & versichert", "item3": "Transparente Preise", "item4": "24/7 Notdienst"},
        "process": {"title": "Wie funktioniert es?", "step1Title": "Kontakt aufnehmen", "step1Text": "Rufen Sie an oder schreiben Sie uns. Wir antworten innerhalb 1 Stunde.", "step2Title": "Inspektion & Angebot", "step2Text": "Kostenlose Inspektion und unverbindliches Angebot.", "step3Title": "Ausführung", "step3Text": "Professionelle und saubere Arbeit.", "step4Title": "Übergabe", "step4Text": "Übergabe mit Garantie und übersichtlicher Rechnung."},
        "faq": {"title": "Häufig gestellte Fragen", "q1": "Wie schnell ist AZGS bei einem Notfall vor Ort?", "a1": "Bei Notfällen sind wir in der Regel innerhalb von 1-2 Stunden in Amsterdam.", "q2": "Gibt AZGS eine Arbeitsgarantie?", "a2": "Ja, wir geben 12 Monate Garantie auf alle Arbeiten und Materialien.", "q3": "Arbeitet AZGS auch außerhalb der Geschäftszeiten?", "a3": "Ja, unser Notdienst ist 24/7 erreichbar, auch an Wochenenden.", "q4": "Bekomme ich vorher ein Angebot?", "a4": "Immer. Schriftliches Angebot vor Beginn. Keine versteckten Kosten.", "q5": "Ist AZGS zertifiziert?", "a5": "Ja, alle unsere Techniker sind zertifiziert und arbeiten nach niederländischen Normen."},
        "cta": {"title": "Bereit loszulegen?", "text": "Fordern Sie noch heute ein kostenloses Angebot an.", "btn": "Kostenloses Angebot Anfordern"}
    }

def service_pl(key, title, badge="Usługi Instalacyjne"):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Profesjonalne usługi {title.lower()} w Amsterdamie. Certyfikowani technicy, szybka reakcja.",
        "hero": {"badge": badge, "title": f"Profesjonalny {title}", "subtitle": f"Usługi {title.lower()} w Amsterdamie. Szybko, rzetelnie i z certyfikatem.", "ctaPrimary": "Zadzwoń Teraz", "ctaSecondary": "Zobacz Usługi"},
        "problem": {"title": f"Problemy z {title.lower()}?", "text": f"AZGS rozwiązuje problemy z {title.lower()} szybko i profesjonalnie — w tym awaryjnie poza godzinami pracy."},
        "includes": {"title": "Co jest wliczone?", "item1": "Bezpłatna inspekcja i wycena", "item2": "Certyfikowani technicy", "item3": "Materiały markowe", "item4": "Gwarancja na pracę", "item5": "Czyste miejsce pracy", "item6": "Szczegółowa faktura"},
        "advantages": {"title": "Dlaczego AZGS?", "item1": "10+ lat w Amsterdamie", "item2": "Certyfikowany i ubezpieczony", "item3": "Przejrzyste ceny", "item4": "Pogotowie 24/7"},
        "process": {"title": "Jak to działa?", "step1Title": "Skontaktuj się", "step1Text": "Zadzwoń lub napisz. Odpowiadamy w ciągu 1 godziny.", "step2Title": "Inspekcja i wycena", "step2Text": "Bezpłatna inspekcja i oferta bez zobowiązań.", "step3Title": "Realizacja", "step3Text": "Profesjonalna i staranna praca.", "step4Title": "Odbiór", "step4Text": "Odbiór z gwarancją i przejrzystą fakturą."},
        "faq": {"title": "Często zadawane pytania", "q1": "Jak szybko AZGS reaguje na awarię?", "a1": "W przypadku awarii jesteśmy zazwyczaj na miejscu w ciągu 1-2 godzin w Amsterdamie.", "q2": "Czy AZGS udziela gwarancji?", "a2": "Tak, udzielamy 12 miesięcy gwarancji na wszystkie prace i materiały.", "q3": "Czy AZGS pracuje poza godzinami biurowymi?", "a3": "Tak, nasza linia awaryjna jest czynna 24/7 w tym w weekendy.", "q4": "Czy otrzymam wycenę z góry?", "a4": "Zawsze. Pisemna wycena przed rozpoczęciem. Bez ukrytych kosztów.", "q5": "Czy AZGS jest certyfikowany?", "a5": "Tak, wszyscy nasi technicy są certyfikowani i pracują zgodnie z normami holenderskimi."},
        "cta": {"title": "Gotowy do działania?", "text": "Poproś o bezpłatną wycenę już dziś.", "btn": "Poproś o Bezpłatną Wycenę"}
    }

def service_ru(key, title, badge="Монтажные работы"):
    return {
        "title": f"{title} Амстердам | AZGS",
        "description": f"Профессиональные услуги {title.lower()} в Амстердаме. Сертифицированные мастера, быстрый выезд.",
        "hero": {"badge": badge, "title": f"Профессиональный {title}", "subtitle": f"Услуги {title.lower()} в Амстердаме. Быстро, надёжно и с сертификатом.", "ctaPrimary": "Позвонить сейчас", "ctaSecondary": "Смотреть услуги"},
        "problem": {"title": f"Проблемы с {title.lower()}?", "text": f"AZGS решит ваши проблемы быстро и профессионально — включая аварийный выезд в нерабочее время."},
        "includes": {"title": "Что входит в услугу?", "item1": "Бесплатный осмотр и смета", "item2": "Сертифицированные мастера", "item3": "Фирменные материалы", "item4": "Гарантия на работы", "item5": "Чистое рабочее место", "item6": "Подробный счёт"},
        "advantages": {"title": "Почему AZGS?", "item1": "10+ лет в Амстердаме", "item2": "Сертифицирован и застрахован", "item3": "Прозрачные цены", "item4": "Экстренный вызов 24/7"},
        "process": {"title": "Как это работает?", "step1Title": "Свяжитесь с нами", "step1Text": "Позвоните или напишите. Отвечаем в течение 1 часа.", "step2Title": "Осмотр и смета", "step2Text": "Бесплатный осмотр и безобязательное предложение.", "step3Title": "Выполнение", "step3Text": "Профессиональная и аккуратная работа.", "step4Title": "Сдача", "step4Text": "Сдача с гарантией и понятным счётом."},
        "faq": {"title": "Часто задаваемые вопросы", "q1": "Как быстро AZGS приедет на аварийный вызов?", "a1": "При аварии мы обычно приезжаем в течение 1-2 часов по Амстердаму.", "q2": "Даёт ли AZGS гарантию на работы?", "a2": "Да, мы даём гарантию 12 месяцев на все работы и материалы.", "q3": "Работает ли AZGS вне рабочих часов?", "a3": "Да, наша аварийная линия работает 24/7 включая выходные.", "q4": "Получу ли я смету заранее?", "a4": "Всегда. Письменная смета до начала работ. Никаких скрытых платежей.", "q5": "Есть ли сертификаты у AZGS?", "a5": "Да, все наши мастера сертифицированы и работают по голландским нормам."},
        "cta": {"title": "Готовы начать?", "text": "Запросите бесплатную смету сегодня.", "btn": "Запросить Бесплатную Смету"}
    }

# Service definitions: (key, nl_title, nl_dutch_term, en_title, ro_title, de_title, pl_title, ru_title)
services_data = [
    ("ServicesIndex", "Installatietechniek Amsterdam", "Installatietechniek", "Installation Services", "Servicii de Instalații", "Installationstechnik", "Usługi Instalacyjne", "Монтажные работы"),
    ("Plumbing",       "Loodgieter Amsterdam",         "Loodgieter",          "Plumbing",             "Instalații Sanitare",  "Sanitärinstallation",  "Hydraulik",            "Сантехник"),
    ("Electrical",     "Elektricien Amsterdam",         "Elektricien",         "Electrical",           "Instalații Electrice",  "Elektroinstallation",  "Elektryk",             "Электрик"),
    ("Heating",        "Verwarming Amsterdam",           "Verwarming",          "Heating",              "Încălzire",            "Heizungsinstallation", "Ogrzewanie",           "Отопление"),
    ("Ventilation",    "Ventilatie Amsterdam",           "Ventilatie",          "Ventilation",          "Ventilație",           "Lüftungsinstallation", "Wentylacja",           "Вентиляция"),
    ("AirConditioning","Airconditioning Amsterdam",      "Airconditioning",     "Air Conditioning",     "Aer Condiționat",      "Klimaanlage",          "Klimatyzacja",         "Кондиционирование"),
    ("UnderfloorHeating","Vloerverwarming Amsterdam",    "Vloerverwarming",     "Underfloor Heating",   "Încălzire Pardoseală", "Fußbodenheizung",      "Ogrzewanie Podłogowe", "Тёплый пол"),
    ("BoilerInstallation","Ketelinstallatie Amsterdam",  "Ketelinstallatie",    "Boiler Installation",  "Instalare Centrală Termică","Kesselinstallation","Instalacja Kotła",  "Установка котла"),
    ("HeatPump",       "Warmtepomp Amsterdam",           "Warmtepomp",          "Heat Pump",            "Pompă de Căldură",     "Wärmepumpe",           "Pompa Ciepła",         "Тепловой насос"),
]

services_msgs = {loc: {} for loc in ['nl','en','ro','de','pl','ru']}
for d in services_data:
    key, nl_title, nl_term, en_title, ro_title, de_title, pl_title, ru_title = d
    services_msgs['nl'][key] = service_nl(key, nl_title, dutch_term=nl_term)
    services_msgs['en'][key] = service_en(key, en_title)
    services_msgs['ro'][key] = service_ro(key, ro_title)
    services_msgs['de'][key] = service_de(key, de_title)
    services_msgs['pl'][key] = service_pl(key, pl_title)
    services_msgs['ru'][key] = service_ru(key, ru_title)

for loc in ['nl','en','ro','de','pl','ru']:
    write(f"{BASE}/{loc}/services.json", services_msgs[loc])

print("\n--- services.json done ---\n")

# ─── RENOVATION.JSON ──────────────────────────────────────────────────────────

def reno_nl(key, title, dutch_term=None):
    term = dutch_term or title
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Professionele {term.lower()} in Amsterdam. Vakkundige aanpak, vaste prijs, geen verrassingen.",
        "hero": {
            "badge": "Renovatie",
            "title": f"Vakkundige {term}",
            "subtitle": f"Wij verzorgen uw {term.lower()} van A tot Z. Transparante offerte, kwaliteitsgarantie.",
            "ctaPrimary": "Vraag Gratis Offerte",
            "ctaSecondary": "Bekijk Renovatiediensten"
        },
        "problem": {"title": f"Op zoek naar een betrouwbare {term.lower()} aannemer?", "text": f"AZGS voert {term.lower()} uit met eigen vakmannen. Geen onderaannemers, geen vertragingen, geen verborgen kosten."},
        "includes": {"title": "Wat is inbegrepen?", "item1": "Gratis opname en gedetailleerde offerte", "item2": "Eigen gecertificeerde vaklieden", "item3": "Materialen van topkwaliteit", "item4": "Dagelijkse opruiming van de werkplek", "item5": "Coördinatie van alle werkzaamheden", "item6": "Opleveringsgarantie"},
        "advantages": {"title": "Voordelen van AZGS", "item1": "Alles-in-één renovatiepartner", "item2": "Vaste prijs na offerte — geen meerwerk verrassingen", "item3": "Eigen vaklieden, geen onderaannemers", "item4": "Tijdige oplevering gegarandeerd"},
        "process": {"title": "Onze Werkwijze", "step1Title": "Opname", "step1Text": "Gratis opname van uw woning of bedrijfspand.", "step2Title": "Offerte", "step2Text": "Gedetailleerde offerte met vaste prijs binnen 48 uur.", "step3Title": "Uitvoering", "step3Text": "Dagelijkse werkzaamheden met minimale overlast.", "step4Title": "Oplevering", "step4Text": "Grondige inspectie en oplevering met garantie."},
        "faq": {"title": "Veelgestelde Vragen", "q1": f"Hoe lang duurt een gemiddelde {term.lower()}?", "a1": f"De duur varieert per project. Na de opname geven wij een realistische planning.", "q2": "Werkt AZGS met vaste prijzen?", "a2": "Ja, na de offerte geldt een vaste prijs. Geen meerwerk tenzij door u verzocht.", "q3": "Kan ik tijdens de renovatie thuis blijven?", "a3": "Dat kan in de meeste gevallen. We bespreken dit bij de opname.", "q4": "Regelt AZGS ook de vergunningen?", "a4": "Ja, indien nodig verzorgen wij alle benodigde vergunningen.", "q5": "Geeft AZGS garantie op renovatiewerk?", "a5": "Ja, standaard 12 maanden garantie op alle uitgevoerde werkzaamheden."},
        "cta": {"title": "Klaar voor uw renovatie?", "text": "Vraag een gratis opname en offerte aan.", "btn": "Gratis Offerte Aanvragen"}
    }

def reno_en(key, title, badge="Renovation"):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Professional {title.lower()} in Amsterdam. Expert approach, fixed price, no surprises.",
        "hero": {"badge": badge, "title": f"Expert {title}", "subtitle": f"We handle your {title.lower()} from start to finish. Transparent quote, quality guarantee.", "ctaPrimary": "Request Free Quote", "ctaSecondary": "View Renovation Services"},
        "problem": {"title": f"Looking for a reliable {title.lower()} contractor?", "text": f"AZGS carries out {title.lower()} with our own craftsmen. No subcontractors, no delays, no hidden costs."},
        "includes": {"title": "What's included?", "item1": "Free survey & detailed quote", "item2": "Own certified craftsmen", "item3": "Top quality materials", "item4": "Daily site cleanup", "item5": "All-work coordination", "item6": "Delivery guarantee"},
        "advantages": {"title": "AZGS Advantages", "item1": "All-in-one renovation partner", "item2": "Fixed price after quote", "item3": "Own craftsmen, no subcontractors", "item4": "On-time delivery guaranteed"},
        "process": {"title": "Our Process", "step1Title": "Survey", "step1Text": "Free survey of your property.", "step2Title": "Quote", "step2Text": "Detailed fixed-price quote within 48 hours.", "step3Title": "Execution", "step3Text": "Daily work with minimal disruption.", "step4Title": "Handover", "step4Text": "Thorough inspection and handover with guarantee."},
        "faq": {"title": "FAQ", "q1": f"How long does a typical {title.lower()} take?", "a1": "Duration varies per project. After the survey we provide a realistic schedule.", "q2": "Does AZGS work with fixed prices?", "a2": "Yes, fixed price after the quote. No extras unless requested by you.", "q3": "Can I stay home during renovation?", "a3": "Usually yes. We discuss this during the survey.", "q4": "Does AZGS handle permits?", "a4": "Yes, we take care of all necessary permits.", "q5": "Does AZGS provide a guarantee?", "a5": "Yes, 12 months guarantee on all work."},
        "cta": {"title": "Ready for your renovation?", "text": "Request a free survey and quote.", "btn": "Request Free Quote"}
    }

def reno_ro(key, title):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Servicii profesionale de {title.lower()} în Amsterdam. Preț fix, fără surprize.",
        "hero": {"badge": "Renovări", "title": f"{title} Profesional", "subtitle": f"Executăm {title.lower()} de la A la Z. Deviz transparent, garanție calitate.", "ctaPrimary": "Solicită Deviz Gratuit", "ctaSecondary": "Vezi Serviciile"},
        "problem": {"title": f"Cauți un contractor de încredere?", "text": f"AZGS execută {title.lower()} cu propriii meșteri. Fără subcontractori, fără întârzieri, fără costuri ascunse."},
        "includes": {"title": "Ce include serviciul?", "item1": "Vizită gratuită și deviz detaliat", "item2": "Meșteri proprii certificați", "item3": "Materiale de calitate superioară", "item4": "Curățenie zilnică a șantierului", "item5": "Coordonarea tuturor lucrărilor", "item6": "Garanție la predare"},
        "advantages": {"title": "Avantajele AZGS", "item1": "Partener all-in-one pentru renovări", "item2": "Preț fix după deviz", "item3": "Meșteri proprii, fără subcontractori", "item4": "Predare la termen garantată"},
        "process": {"title": "Procesul nostru", "step1Title": "Vizită", "step1Text": "Vizită gratuită la proprietatea dumneavoastră.", "step2Title": "Deviz", "step2Text": "Deviz detaliat cu preț fix în 48 de ore.", "step3Title": "Execuție", "step3Text": "Lucrări zilnice cu deranj minim.", "step4Title": "Predare", "step4Text": "Inspecție amănunțită și predare cu garanție."},
        "faq": {"title": "Întrebări Frecvente", "q1": f"Cât durează o {title.lower()}?", "a1": "Durata variază per proiect. După vizită furnizăm un program realist.", "q2": "AZGS lucrează cu prețuri fixe?", "a2": "Da, preț fix după deviz. Fără extra-costuri decât la solicitarea dumneavoastră.", "q3": "Pot rămâne acasă în timpul renovării?", "a3": "De obicei da. Discutăm la vizita inițială.", "q4": "Se ocupă AZGS de autorizații?", "a4": "Da, ne ocupăm de toate autorizațiile necesare.", "q5": "Oferă AZGS garanție?", "a5": "Da, garanție 12 luni pentru toate lucrările."},
        "cta": {"title": "Gata pentru renovare?", "text": "Solicitați o vizită și deviz gratuit.", "btn": "Solicită Deviz Gratuit"}
    }

def reno_de(key, title):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Professionelle {title} in Amsterdam. Fachkundige Ausführung, Festpreis, keine Überraschungen.",
        "hero": {"badge": "Renovierung", "title": f"Fachkundige {title}", "subtitle": f"Wir führen Ihre {title} von A bis Z durch. Transparentes Angebot, Qualitätsgarantie.", "ctaPrimary": "Kostenloses Angebot", "ctaSecondary": "Leistungen Ansehen"},
        "problem": {"title": f"Suchen Sie einen zuverlässigen {title}-Auftragnehmer?", "text": f"AZGS führt {title} mit eigenen Handwerkern aus. Keine Subunternehmer, keine Verzögerungen, keine versteckten Kosten."},
        "includes": {"title": "Was ist enthalten?", "item1": "Kostenloser Besichtigungstermin & detailliertes Angebot", "item2": "Eigene zertifizierte Handwerker", "item3": "Hochwertige Materialien", "item4": "Tägliche Reinigung der Baustelle", "item5": "Koordination aller Arbeiten", "item6": "Übergabegarantie"},
        "advantages": {"title": "Vorteile von AZGS", "item1": "All-in-one Renovierungspartner", "item2": "Festpreis nach Angebot", "item3": "Eigene Handwerker, keine Subunternehmer", "item4": "Pünktliche Fertigstellung garantiert"},
        "process": {"title": "Unser Ablauf", "step1Title": "Besichtigung", "step1Text": "Kostenloser Besichtigungstermin.", "step2Title": "Angebot", "step2Text": "Detailliertes Festpreisangebot innerhalb 48 Stunden.", "step3Title": "Ausführung", "step3Text": "Tägliche Arbeiten mit minimaler Beeinträchtigung.", "step4Title": "Übergabe", "step4Text": "Gründliche Inspektion und Übergabe mit Garantie."},
        "faq": {"title": "Häufig gestellte Fragen", "q1": f"Wie lange dauert eine typische {title}?", "a1": "Die Dauer variiert je nach Projekt. Nach der Besichtigung erstellen wir einen realistischen Zeitplan.", "q2": "Arbeitet AZGS mit Festpreisen?", "a2": "Ja, Festpreis nach dem Angebot. Keine Extras, es sei denn auf Ihren Wunsch.", "q3": "Kann ich während der Renovierung zu Hause bleiben?", "a3": "Meistens ja. Wir besprechen dies bei der Besichtigung.", "q4": "Kümmert sich AZGS um Genehmigungen?", "a4": "Ja, wir übernehmen alle erforderlichen Genehmigungen.", "q5": "Gibt AZGS eine Garantie?", "a5": "Ja, 12 Monate Garantie auf alle Arbeiten."},
        "cta": {"title": "Bereit für Ihre Renovierung?", "text": "Fordern Sie eine kostenlose Besichtigung und ein Angebot an.", "btn": "Kostenloses Angebot Anfordern"}
    }

def reno_pl(key, title):
    return {
        "title": f"{title} Amsterdam | AZGS",
        "description": f"Profesjonalny {title.lower()} w Amsterdamie. Stała cena, bez niespodzianek.",
        "hero": {"badge": "Renowacje", "title": f"Profesjonalny {title}", "subtitle": f"Realizujemy {title.lower()} od A do Z. Przejrzysta wycena, gwarancja jakości.", "ctaPrimary": "Bezpłatna Wycena", "ctaSecondary": "Zobacz Usługi"},
        "problem": {"title": f"Szukasz rzetelnego wykonawcy {title.lower()}?", "text": f"AZGS realizuje {title.lower()} własnymi rzemieślnikami. Bez podwykonawców, bez opóźnień, bez ukrytych kosztów."},
        "includes": {"title": "Co jest wliczone?", "item1": "Bezpłatna wizja lokalna i szczegółowa wycena", "item2": "Własni certyfikowani rzemieślnicy", "item3": "Materiały najwyższej jakości", "item4": "Codzienne sprzątanie placu budowy", "item5": "Koordynacja wszystkich prac", "item6": "Gwarancja odbioru"},
        "advantages": {"title": "Zalety AZGS", "item1": "Kompleksowy partner renowacyjny", "item2": "Stała cena po wycenie", "item3": "Własni rzemieślnicy, bez podwykonawców", "item4": "Terminowe zakończenie gwarantowane"},
        "process": {"title": "Nasz proces", "step1Title": "Wizja lokalna", "step1Text": "Bezpłatna wizja lokalna.", "step2Title": "Wycena", "step2Text": "Szczegółowa wycena ze stałą ceną w 48 godzin.", "step3Title": "Realizacja", "step3Text": "Codzienne prace z minimalną uciążliwością.", "step4Title": "Odbiór", "step4Text": "Dokładna inspekcja i odbiór z gwarancją."},
        "faq": {"title": "FAQ", "q1": f"Jak długo trwa typowy {title.lower()}?", "a1": "Czas trwania zależy od projektu. Po wizji podamy realistyczny harmonogram.", "q2": "Czy AZGS pracuje ze stałymi cenami?", "a2": "Tak, stała cena po wycenie. Bez dodatkowych kosztów.", "q3": "Czy mogę zostać w domu podczas remontu?", "a3": "Zazwyczaj tak. Omówimy to podczas wizji.", "q4": "Czy AZGS zajmuje się pozwoleniami?", "a4": "Tak, zajmujemy się wszystkimi pozwoleniami.", "q5": "Czy AZGS udziela gwarancji?", "a5": "Tak, 12 miesięcy gwarancji na wszystkie prace."},
        "cta": {"title": "Gotowy na remont?", "text": "Poproś o bezpłatną wizję i wycenę.", "btn": "Poproś o Bezpłatną Wycenę"}
    }

def reno_ru(key, title):
    return {
        "title": f"{title} Амстердам | AZGS",
        "description": f"Профессиональный {title.lower()} в Амстердаме. Фиксированная цена, без сюрпризов.",
        "hero": {"badge": "Ремонт", "title": f"Профессиональный {title}", "subtitle": f"Выполняем {title.lower()} под ключ. Прозрачная смета, гарантия качества.", "ctaPrimary": "Бесплатная смета", "ctaSecondary": "Смотреть услуги"},
        "problem": {"title": f"Ищете надёжного подрядчика?", "text": f"AZGS выполняет {title.lower()} собственными мастерами. Без субподрядчиков, без задержек, без скрытых платежей."},
        "includes": {"title": "Что входит?", "item1": "Бесплатный выезд и подробная смета", "item2": "Собственные сертифицированные мастера", "item3": "Материалы высшего качества", "item4": "Ежедневная уборка объекта", "item5": "Координация всех работ", "item6": "Гарантия при сдаче"},
        "advantages": {"title": "Преимущества AZGS", "item1": "Комплексный партнёр по ремонту", "item2": "Фиксированная цена после сметы", "item3": "Собственные мастера, без субподрядчиков", "item4": "Сдача в срок гарантирована"},
        "process": {"title": "Наш процесс", "step1Title": "Выезд", "step1Text": "Бесплатный выезд на объект.", "step2Title": "Смета", "step2Text": "Подробная смета с фиксированной ценой за 48 часов.", "step3Title": "Выполнение", "step3Text": "Ежедневные работы с минимальным неудобством.", "step4Title": "Сдача", "step4Text": "Тщательная приёмка и сдача с гарантией."},
        "faq": {"title": "Часто задаваемые вопросы", "q1": f"Сколько занимает типичный {title.lower()}?", "a1": "Срок зависит от проекта. После выезда составим реальный график.", "q2": "Работает ли AZGS по фиксированным ценам?", "a2": "Да, фиксированная цена после сметы. Без доплат.", "q3": "Могу ли я жить дома во время ремонта?", "a3": "Обычно да. Обсудим это при выезде.", "q4": "Занимается ли AZGS разрешениями?", "a4": "Да, мы оформляем все необходимые разрешения.", "q5": "Даёт ли AZGS гарантию?", "a5": "Да, гарантия 12 месяцев на все работы."},
        "cta": {"title": "Готовы к ремонту?", "text": "Запросите бесплатный выезд и смету.", "btn": "Запросить Бесплатную Смету"}
    }

renovation_data = [
    ("RenovationIndex",        "Renovatie Amsterdam",              "Renovatie",                  "Renovation Services",        "Servicii Renovare",           "Renovierungsarbeiten",         "Usługi Renowacyjne",          "Ремонтные работы"),
    ("ApartmentRenovation",    "Appartement renovatie Amsterdam",  "Appartement renovatie",      "Apartment Renovation",       "Renovare Apartament",         "Wohnungsrenovierung",          "Remont Mieszkania",           "Ремонт квартиры"),
    ("BathroomRenovation",     "Badkamer renovatie Amsterdam",     "Badkamer renovatie",         "Bathroom Renovation",        "Renovare Baie",               "Badsanierung",                 "Remont Łazienki",             "Ремонт ванной"),
    ("KitchenRenovation",      "Keuken renovatie Amsterdam",       "Keuken renovatie",           "Kitchen Renovation",         "Renovare Bucătărie",          "Küchenrenovierung",            "Remont Kuchni",               "Ремонт кухни"),
    ("Drywall",                "Gipsplaten Amsterdam",             "Gipsplaten montage",         "Drywall",                    "Gips-Carton",                 "Trockenbau",                   "Zabudowa Gipsowa",            "Гипсокартон"),
    ("Painting",               "Schilderwerk Amsterdam",           "Schilderwerk",               "Painting",                   "Zugrăveli",                   "Malerarbeiten",                "Malowanie",                   "Покраска"),
    ("Plastering",             "Stucwerk Amsterdam",               "Stucwerk",                   "Plastering",                 "Tencuieli",                   "Putzarbeiten",                 "Tynkowanie",                  "Штукатурка"),
    ("Flooring",               "Vloeren Amsterdam",                "Vloerwerk",                  "Flooring",                   "Pardoseli",                   "Bodenbelagsarbeiten",          "Układanie Podłóg",            "Укладка полов"),
    ("TileInstallation",       "Tegelwerk Amsterdam",              "Tegelwerk",                  "Tile Installation",          "Faianță & Gresie",            "Fliesenarbeiten",              "Układanie Płytek",            "Укладка плитки"),
]

reno_msgs = {loc: {} for loc in ['nl','en','ro','de','pl','ru']}
for d in renovation_data:
    key, nl_title, nl_term, en_title, ro_title, de_title, pl_title, ru_title = d
    reno_msgs['nl'][key] = reno_nl(key, nl_title, dutch_term=nl_term)
    reno_msgs['en'][key] = reno_en(key, en_title)
    reno_msgs['ro'][key] = reno_ro(key, ro_title)
    reno_msgs['de'][key] = reno_de(key, de_title)
    reno_msgs['pl'][key] = reno_pl(key, pl_title)
    reno_msgs['ru'][key] = reno_ru(key, ru_title)

for loc in ['nl','en','ro','de','pl','ru']:
    write(f"{BASE}/{loc}/renovation.json", reno_msgs[loc])

print("\n--- renovation.json done ---\n")

# ─── PAGES.JSON ───────────────────────────────────────────────────────────────

pages = {
    "nl": {
        "About": {
            "title": "Over AZGS — Uw Betrouwbare Partner in Amsterdam",
            "description": "Meer dan 10 jaar ervaring in installaties en renovaties in Amsterdam. Gecertificeerd, verzekerd en 100% klanttevredenheid.",
            "hero": {"badge": "Over Ons", "title": "Over AZGS", "subtitle": "Meer dan 10 jaar uw betrouwbare partner voor installaties en renovaties in Amsterdam en omstreken."},
            "story": {"title": "Ons Verhaal", "text": "AZGS is opgericht met één doel: betrouwbare, vakkundige service leveren aan particulieren en bedrijven in de Amsterdamse regio. Ons team bestaat uit gecertificeerde monteurs en renovatiespecialisten die trots zijn op hun werk."},
            "values": {"title": "Onze Waarden", "item1": "Vakmanschap", "item2": "Betrouwbaarheid", "item3": "Transparantie", "item4": "Klantgerichtheid"},
            "cta": {"title": "Klaar om samen te werken?", "btn": "Neem Contact Op"}
        },
        "Contact": {
            "title": "Contact AZGS — Bel of Mail Ons",
            "description": "Neem contact op met AZGS voor een vrijblijvende offerte of spoedgeval. 24/7 bereikbaar.",
            "hero": {"badge": "Contact", "title": "Neem Contact Op", "subtitle": "Voor offertes, vragen of spoedgevallen. Wij reageren binnen 1 uur."},
            "phone": {"title": "Telefoon", "value": "+31 20 000 0000", "note": "Ma-Za 08:00–20:00 · Spoed 24/7"},
            "email": {"title": "E-mail", "value": "info@azgs.nl", "note": "Reactie binnen 2 uur op werkdagen"},
            "address": {"title": "Werkgebied", "value": "Amsterdam & Omstreken", "note": "Noord-Holland"}
        },
        "Emergency": {
            "title": "Spoed Loodgieter & Elektricien Amsterdam | 24/7 AZGS",
            "description": "Spoedgeval met uw loodgieter, elektricien of verwarming? AZGS is 24/7 bereikbaar in Amsterdam. Binnen 1 uur ter plaatse.",
            "hero": {"badge": "Spoed 24/7", "title": "Spoedservice Amsterdam", "subtitle": "Lekkage, elektrisch probleem of verwarmingsstoring? Wij zijn 24/7 bereikbaar en binnen 1 uur ter plaatse.", "ctaPrimary": "Bel Nu — Spoed", "ctaSecondary": "Meer Informatie"},
            "urgentTitle": "Bel Direct:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Spoeddiensten", "item1": "Lekkage & Waterschade", "item2": "Elektrisch Storing", "item3": "CV-ketel Storing", "item4": "Verstopping Riool", "item5": "Airconditioning Storing"},
            "promise": {"title": "Onze Beloftes", "item1": "Binnen 1-2 uur ter plaatse in Amsterdam", "item2": "24/7 bereikbaar, ook in het weekend", "item3": "Transparante spoedtarieven — geen verborgen kosten", "item4": "Gecertificeerde monteurs"},
            "faq": {"title": "Veelgestelde Vragen Spoed", "q1": "Hoe snel is AZGS ter plaatse bij een noodgeval?", "a1": "Bij noodgevallen streven wij ernaar binnen 1 uur ter plaatse te zijn in Amsterdam.", "q2": "Werkt AZGS ook 's nachts?", "a2": "Ja, onze spoedlijn is 24/7 bereikbaar, inclusief nacht, weekend en feestdagen.", "q3": "Wat kost een spoedoproep?", "a3": "Wij werken met transparante spoedtarieven. U ontvangt altijd een prijsindicatie telefonisch.", "q4": "Voor welke spoedgevallen kan ik AZGS bellen?", "a4": "Lekkage, elektrisch storing, CV-ketel defect, verstopping, airconditioning storing en meer.", "q5": "Werkt AZGS ook in mijn regio?", "a5": "Wij werken in Amsterdam en omstreken, inclusief Amstelveen, Diemen, Zaandam en Haarlem."},
            "cta": {"title": "Heeft u een spoedsituatie?", "text": "Bel ons direct. Onze spoedlijn is dag en nacht bereikbaar.", "btn": "Bel Spoedlijn Nu"}
        }
    },
    "en": {
        "About": {
            "title": "About AZGS — Your Trusted Partner in Amsterdam",
            "description": "Over 10 years of experience in installations and renovations in Amsterdam.",
            "hero": {"badge": "About Us", "title": "About AZGS", "subtitle": "Your trusted partner for installations and renovations in Amsterdam for over 10 years."},
            "story": {"title": "Our Story", "text": "AZGS was founded with one goal: providing reliable, expert service to residents and businesses in the Amsterdam region."},
            "values": {"title": "Our Values", "item1": "Craftsmanship", "item2": "Reliability", "item3": "Transparency", "item4": "Customer Focus"},
            "cta": {"title": "Ready to work together?", "btn": "Contact Us"}
        },
        "Contact": {
            "title": "Contact AZGS — Call or Email Us",
            "description": "Contact AZGS for a free quote or emergency. Available 24/7.",
            "hero": {"badge": "Contact", "title": "Get in Touch", "subtitle": "For quotes, questions or emergencies. We respond within 1 hour."},
            "phone": {"title": "Phone", "value": "+31 20 000 0000", "note": "Mon-Sat 08:00–20:00 · Emergency 24/7"},
            "email": {"title": "Email", "value": "info@azgs.nl", "note": "Response within 2 hours on business days"},
            "address": {"title": "Service Area", "value": "Amsterdam & Surroundings", "note": "North Holland"}
        },
        "Emergency": {
            "title": "Emergency Plumber & Electrician Amsterdam | 24/7 AZGS",
            "description": "Emergency plumber, electrician or heating in Amsterdam? AZGS is available 24/7. On-site within 1 hour.",
            "hero": {"badge": "Emergency 24/7", "title": "Emergency Service Amsterdam", "subtitle": "Leak, electrical problem or heating failure? We are available 24/7 and on-site within 1 hour.", "ctaPrimary": "Call Now — Emergency", "ctaSecondary": "More Information"},
            "urgentTitle": "Call Directly:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Emergency Services", "item1": "Leak & Water Damage", "item2": "Electrical Failure", "item3": "Boiler Breakdown", "item4": "Drain Blockage", "item5": "AC Failure"},
            "promise": {"title": "Our Promises", "item1": "On-site within 1-2 hours in Amsterdam", "item2": "24/7 available including weekends", "item3": "Transparent emergency rates", "item4": "Certified technicians"},
            "faq": {"title": "Emergency FAQ", "q1": "How quickly can AZGS arrive in an emergency?", "a1": "We aim to be on-site within 1 hour in Amsterdam.", "q2": "Does AZGS work at night?", "a2": "Yes, our emergency line is available 24/7 including nights and weekends.", "q3": "What does an emergency call cost?", "a3": "We work with transparent emergency rates. You always receive a price indication by phone.", "q4": "For which emergencies can I call AZGS?", "a4": "Leaks, electrical failures, boiler breakdowns, blockages and more.", "q5": "Does AZGS work in my area?", "a5": "We work in Amsterdam and surroundings including Amstelveen, Diemen and Haarlem."},
            "cta": {"title": "Emergency situation?", "text": "Call us directly. Our emergency line is available day and night.", "btn": "Call Emergency Line Now"}
        }
    },
    "ro": {
        "About": {
            "title": "Despre AZGS — Partenerul Dumneavoastră în Amsterdam",
            "description": "Peste 10 ani experiență în instalații și renovări în Amsterdam.",
            "hero": {"badge": "Despre Noi", "title": "Despre AZGS", "subtitle": "Partenerul dumneavoastră de încredere pentru instalații și renovări în Amsterdam."},
            "story": {"title": "Povestea noastră", "text": "AZGS a fost fondată cu un singur scop: a oferi servicii de calitate locuitorilor și firmelor din Amsterdam."},
            "values": {"title": "Valorile noastre", "item1": "Meșteșug", "item2": "Fiabilitate", "item3": "Transparență", "item4": "Orientare spre client"},
            "cta": {"title": "Gata să colaborăm?", "btn": "Contactați-ne"}
        },
        "Contact": {
            "title": "Contact AZGS — Sunați sau Trimiteți Email",
            "description": "Contactați AZGS pentru un deviz gratuit sau urgențe. Disponibil 24/7.",
            "hero": {"badge": "Contact", "title": "Luați Legătura", "subtitle": "Pentru devize, întrebări sau urgențe. Răspundem în 1 oră."},
            "phone": {"title": "Telefon", "value": "+31 20 000 0000", "note": "Lun-Sâm 08:00–20:00 · Urgențe 24/7"},
            "email": {"title": "Email", "value": "info@azgs.nl", "note": "Răspuns în 2 ore în zilele lucrătoare"},
            "address": {"title": "Zonă de servicii", "value": "Amsterdam și Împrejurimi", "note": "Noord-Holland"}
        },
        "Emergency": {
            "title": "Urgențe Instalații Amsterdam | 24/7 AZGS",
            "description": "Urgențe sanitare, electrice sau de încălzire în Amsterdam? AZGS disponibil 24/7. Intervenție în 1 oră.",
            "hero": {"badge": "Urgențe 24/7", "title": "Serviciu de Urgență Amsterdam", "subtitle": "Scurgeri, probleme electrice sau defecțiuni termice? Suntem disponibili 24/7.", "ctaPrimary": "Sună Acum — Urgență", "ctaSecondary": "Mai Multe Informații"},
            "urgentTitle": "Sună Direct:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Servicii de Urgență", "item1": "Scurgeri & Inundații", "item2": "Defecțiuni Electrice", "item3": "Centrală Termică", "item4": "Canalizare Blocată", "item5": "Defecțiuni AC"},
            "promise": {"title": "Promisiunile Noastre", "item1": "La fața locului în 1-2 ore în Amsterdam", "item2": "Disponibil 24/7 inclusiv weekenduri", "item3": "Tarife de urgență transparente", "item4": "Tehnicieni certificați"},
            "faq": {"title": "Întrebări Frecvente Urgențe", "q1": "Cât de repede ajunge AZGS la o urgență?", "a1": "Urmărim să ajungem în 1 oră în Amsterdam.", "q2": "Lucrează AZGS noaptea?", "a2": "Da, linia de urgențe este disponibilă 24/7.", "q3": "Cât costă un apel de urgență?", "a3": "Lucrăm cu tarife transparente. Primiți o indicație telefonică.", "q4": "Pentru ce urgențe pot suna?", "a4": "Scurgeri, defecțiuni electrice, centrale termice, canalizare și altele.", "q5": "Lucrează AZGS în zona mea?", "a5": "Lucrăm în Amsterdam și împrejurimi."},
            "cta": {"title": "Situație de urgență?", "text": "Sunați-ne direct. Linia de urgențe este disponibilă zi și noapte.", "btn": "Sună Linia de Urgențe"}
        }
    },
    "de": {
        "About": {
            "title": "Über AZGS — Ihr zuverlässiger Partner in Amsterdam",
            "description": "Über 10 Jahre Erfahrung in Installationen und Renovierungen in Amsterdam.",
            "hero": {"badge": "Über Uns", "title": "Über AZGS", "subtitle": "Ihr zuverlässiger Partner für Installationen und Renovierungen in Amsterdam."},
            "story": {"title": "Unsere Geschichte", "text": "AZGS wurde mit einem Ziel gegründet: zuverlässige, fachkundige Dienstleistungen für Bewohner und Unternehmen in Amsterdam."},
            "values": {"title": "Unsere Werte", "item1": "Handwerkskunst", "item2": "Zuverlässigkeit", "item3": "Transparenz", "item4": "Kundenorientierung"},
            "cta": {"title": "Bereit zur Zusammenarbeit?", "btn": "Kontakt aufnehmen"}
        },
        "Contact": {
            "title": "Kontakt AZGS — Anrufen oder E-Mail",
            "description": "Kontaktieren Sie AZGS für ein kostenloses Angebot oder Notfall. 24/7 erreichbar.",
            "hero": {"badge": "Kontakt", "title": "Kontakt aufnehmen", "subtitle": "Für Angebote, Fragen oder Notfälle. Wir antworten innerhalb 1 Stunde."},
            "phone": {"title": "Telefon", "value": "+31 20 000 0000", "note": "Mo-Sa 08:00–20:00 · Notdienst 24/7"},
            "email": {"title": "E-Mail", "value": "info@azgs.nl", "note": "Antwort innerhalb 2 Stunden an Werktagen"},
            "address": {"title": "Servicegebiet", "value": "Amsterdam & Umgebung", "note": "Noord-Holland"}
        },
        "Emergency": {
            "title": "Notdienst Sanitär & Elektro Amsterdam | 24/7 AZGS",
            "description": "Notfall mit Sanitär, Elektro oder Heizung in Amsterdam? AZGS ist 24/7 erreichbar.",
            "hero": {"badge": "Notdienst 24/7", "title": "Notdienst Amsterdam", "subtitle": "Wasserschaden, Stromausfall oder Heizungsausfall? Wir sind 24/7 erreichbar.", "ctaPrimary": "Jetzt Anrufen — Notfall", "ctaSecondary": "Mehr Informationen"},
            "urgentTitle": "Direkt Anrufen:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Notdienstleistungen", "item1": "Wasserschaden & Rohrbruch", "item2": "Stromausfall", "item3": "Heizungsausfall", "item4": "Rohrverstopfung", "item5": "Klimaanlage Störung"},
            "promise": {"title": "Unsere Versprechen", "item1": "Innerhalb 1-2 Stunden vor Ort in Amsterdam", "item2": "24/7 erreichbar auch am Wochenende", "item3": "Transparente Notdiensttarife", "item4": "Zertifizierte Techniker"},
            "faq": {"title": "Notdienst FAQ", "q1": "Wie schnell ist AZGS bei einem Notfall?", "a1": "Bei Notfällen sind wir in der Regel innerhalb 1 Stunde in Amsterdam.", "q2": "Arbeitet AZGS nachts?", "a2": "Ja, unser Notdienst ist 24/7 erreichbar.", "q3": "Was kostet ein Notfalleinsatz?", "a3": "Wir arbeiten mit transparenten Tarifen. Sie erhalten immer eine telefonische Preisangabe.", "q4": "Für welche Notfälle kann ich AZGS anrufen?", "a4": "Wasserschäden, Stromausfälle, Heizungsausfälle, Verstopfungen und mehr.", "q5": "Arbeitet AZGS in meiner Region?", "a5": "Wir arbeiten in Amsterdam und Umgebung."},
            "cta": {"title": "Notfallsituation?", "text": "Rufen Sie uns direkt an.", "btn": "Notfallnummer Anrufen"}
        }
    },
    "pl": {
        "About": {
            "title": "O AZGS — Twój Zaufany Partner w Amsterdamie",
            "description": "Ponad 10 lat doświadczenia w instalacjach i renowacjach w Amsterdamie.",
            "hero": {"badge": "O Nas", "title": "O AZGS", "subtitle": "Twój zaufany partner w zakresie instalacji i renowacji w Amsterdamie."},
            "story": {"title": "Nasza historia", "text": "AZGS zostało założone z jednym celem: świadczenie niezawodnych, fachowych usług dla mieszkańców Amsterdamu."},
            "values": {"title": "Nasze wartości", "item1": "Rzemiosło", "item2": "Niezawodność", "item3": "Przejrzystość", "item4": "Orientacja na klienta"},
            "cta": {"title": "Gotowy do współpracy?", "btn": "Skontaktuj się"}
        },
        "Contact": {
            "title": "Kontakt AZGS — Zadzwoń lub Napisz",
            "description": "Skontaktuj się z AZGS po bezpłatną wycenę lub w nagłym przypadku. Dostępni 24/7.",
            "hero": {"badge": "Kontakt", "title": "Skontaktuj się z Nami", "subtitle": "W sprawach wycen, pytań lub awarii. Odpowiadamy w ciągu 1 godziny."},
            "phone": {"title": "Telefon", "value": "+31 20 000 0000", "note": "Pon-Sob 08:00–20:00 · Pogotowie 24/7"},
            "email": {"title": "E-mail", "value": "info@azgs.nl", "note": "Odpowiedź w 2 godziny w dni robocze"},
            "address": {"title": "Obszar obsługi", "value": "Amsterdam i Okolice", "note": "Noord-Holland"}
        },
        "Emergency": {
            "title": "Pogotowie Hydrauliczne i Elektryczne Amsterdam | 24/7 AZGS",
            "description": "Awaria hydrauliczna, elektryczna lub grzewcza w Amsterdamie? AZGS dostępny 24/7.",
            "hero": {"badge": "Pogotowie 24/7", "title": "Pogotowie Amsterdam", "subtitle": "Wyciek, awaria elektryczna lub ogrzewania? Jesteśmy dostępni 24/7.", "ctaPrimary": "Zadzwoń Teraz — Awaria", "ctaSecondary": "Więcej Informacji"},
            "urgentTitle": "Zadzwoń Bezpośrednio:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Usługi Awaryjne", "item1": "Wyciek & Zalanie", "item2": "Awaria Elektryczna", "item3": "Awaria Kotła", "item4": "Zatkana Kanalizacja", "item5": "Awaria Klimatyzacji"},
            "promise": {"title": "Nasze Obietnice", "item1": "Na miejscu w 1-2 godz. w Amsterdamie", "item2": "Dostępni 24/7 w tym weekendy", "item3": "Przejrzyste taryfy awaryjne", "item4": "Certyfikowani technicy"},
            "faq": {"title": "FAQ Pogotowie", "q1": "Jak szybko przyjedzie AZGS?", "a1": "W nagłych przypadkach staramy się dotrzeć w ciągu 1 godziny.", "q2": "Czy AZGS pracuje w nocy?", "a2": "Tak, linia awaryjna jest czynna 24/7.", "q3": "Ile kosztuje wyjazd awaryjny?", "a3": "Pracujemy z przejrzystymi taryfami. Zawsze podajemy cenę przez telefon.", "q4": "W jakich awariach można dzwonić?", "a4": "Wycieki, awarie elektryczne, kotły, zatkana kanalizacja i inne.", "q5": "Czy AZGS działa w moim rejonie?", "a5": "Działamy w Amsterdamie i okolicach."},
            "cta": {"title": "Sytuacja awaryjna?", "text": "Zadzwoń bezpośrednio.", "btn": "Zadzwoń Na Pogotowie"}
        }
    },
    "ru": {
        "About": {
            "title": "О компании AZGS — Ваш надёжный партнёр в Амстердаме",
            "description": "Более 10 лет опыта в монтажных работах и ремонте в Амстердаме.",
            "hero": {"badge": "О нас", "title": "О компании AZGS", "subtitle": "Ваш надёжный партнёр по монтажным работам и ремонту в Амстердаме."},
            "story": {"title": "Наша история", "text": "AZGS основана с одной целью: предоставлять надёжные профессиональные услуги жителям и предприятиям Амстердама."},
            "values": {"title": "Наши ценности", "item1": "Мастерство", "item2": "Надёжность", "item3": "Прозрачность", "item4": "Клиентоориентированность"},
            "cta": {"title": "Готовы сотрудничать?", "btn": "Свяжитесь с нами"}
        },
        "Contact": {
            "title": "Контакты AZGS — Позвоните или напишите",
            "description": "Свяжитесь с AZGS для бесплатной сметы или аварийного вызова. Доступны 24/7.",
            "hero": {"badge": "Контакт", "title": "Свяжитесь с нами", "subtitle": "По вопросам смет, консультаций или аварийного выезда. Отвечаем в течение 1 часа."},
            "phone": {"title": "Телефон", "value": "+31 20 000 0000", "note": "Пн-Сб 08:00–20:00 · Аварийный 24/7"},
            "email": {"title": "Email", "value": "info@azgs.nl", "note": "Ответ в течение 2 часов в рабочие дни"},
            "address": {"title": "Зона обслуживания", "value": "Амстердам и окрестности", "note": "Noord-Holland"}
        },
        "Emergency": {
            "title": "Аварийный сантехник и электрик Амстердам | 24/7 AZGS",
            "description": "Аварийный вызов сантехника, электрика или отопления в Амстердаме? AZGS доступен 24/7.",
            "hero": {"badge": "Срочный вызов 24/7", "title": "Аварийная служба Амстердам", "subtitle": "Утечка, проблемы с электрикой или отоплением? Мы доступны 24/7, выезд в 1 час.", "ctaPrimary": "Позвонить — Аварийно", "ctaSecondary": "Подробнее"},
            "urgentTitle": "Звоните напрямую:",
            "phone": "+31 20 000 0000",
            "services": {"title": "Аварийные услуги", "item1": "Утечка и затопление", "item2": "Электрическая авария", "item3": "Котёл не работает", "item4": "Засор канализации", "item5": "Поломка кондиционера"},
            "promise": {"title": "Наши обещания", "item1": "На месте в 1-2 часа по Амстердаму", "item2": "Доступны 24/7 включая выходные", "item3": "Прозрачные аварийные тарифы", "item4": "Сертифицированные мастера"},
            "faq": {"title": "Часто задаваемые вопросы", "q1": "Как быстро приедет AZGS?", "a1": "При аварии обычно приезжаем в течение 1 часа.", "q2": "Работает ли AZGS ночью?", "a2": "Да, аварийная линия работает 24/7.", "q3": "Сколько стоит аварийный вызов?", "a3": "Работаем по прозрачным тарифам. Цену сообщают по телефону.", "q4": "При каких авариях звонить?", "a4": "Утечки, электроаварии, котлы, засоры и другое.", "q5": "Работает ли AZGS в нашем районе?", "a5": "Работаем по Амстердаму и окрестностям."},
            "cta": {"title": "Аварийная ситуация?", "text": "Звоните напрямую. Линия работает круглосуточно.", "btn": "Позвонить в аварийную службу"}
        }
    }
}

for loc, data in pages.items():
    write(f"{BASE}/{loc}/pages.json", data)

print("\n--- pages.json done ---\n")
print("✅ All message files generated.")
