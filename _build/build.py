"""Builds every page of the Blaum Dienstleistungen site.

Run from the repository root:  python _build/build.py
Edit page texts in the data below (or _build/home-main.html for the homepage),
then run the script again. Shared styles: assets/style.css, script: assets/site.js.
"""
import os
import re
from html import escape as e

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
SPRITE = open(os.path.join(HERE, "sprite.html"), encoding="utf-8").read()
HOME_MAIN = open(os.path.join(HERE, "home-main.html"), encoding="utf-8").read()

VER = "3"  # bump after changing style.css or site.js so browsers reload them
PHONE, PHONE_HREF = "0173 2831352", "tel:+491732831352"
MAIL = "info@blaum-dienstleistungen.de"
ADDR = "Myliusstraße 11, 50823 Köln"

# Order and names as in the live site's "Leistungen" menu
SERVICES = [
    ("praxisreinigung", "Praxisreinigung", "i-praxis", "praxis"),
    ("airbnb-service", "AirBnB Service", "i-airbnb", "airbnb"),
    ("baureinigung", "Baureinigung", "i-bau", "bau"),
    ("treppenhausreinigung", "Treppenhausreinigung", "i-treppe", "treppe"),
    ("hausmeisterservice", "Hausmeisterservice", "i-haus", "haus"),
    ("unterhaltsreinigung", "Unterhaltsreinigung", "i-unterhalt", "unterhalt"),
    ("glasreinigung", "Glasreinigung", "i-glas", "glas"),
    ("grundreinigung", "Grundreinigung", "i-grund", "grund"),
]


def ico(i, cls="ico", style=""):
    st = f' style="{style}"' if style else ""
    return f'<svg class="{cls}"{st}><use href="#{i}"/></svg>'


ARROW = f'<span class="dot">{ico("i-arrow", style="width:14px;height:14px")}</span>'


def head(title, desc):
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="assets/logo-mark.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={VER}">
</head>
<body>

{SPRITE}
"""


def header(active):
    def cur(key):
        return ' aria-current="page"' if key == active else ""
    in_svc = active == "leistungen" or any(s[0] == active for s in SERVICES)
    sub = "".join(
        f'<a href="{slug}.html"{cur(slug)}><span class="tic">{ico(icon)}</span>{e(name)}</a>'
        for slug, name, icon, _ in SERVICES)
    return f"""<header id="top">
  <div class="wrap nav">
    <a href="index.html" class="logo" aria-label="Blaum Dienstleistungen, Startseite">
      <img class="mark" src="assets/logo-mark.png" alt="" width="44" height="43">
      <span>Blaum<small>Dienstleistungen</small></span>
    </a>
    <nav class="menu" aria-label="Hauptnavigation">
      <a href="index.html"{cur("start")}>Start</a>
      <div class="has-sub">
        <a href="leistungen.html"{' class="active"' if in_svc else ""}{cur("leistungen")}>Leistungen {ico("i-chev", "ico chev")}</a>
        <div class="sub"><div class="sub-in">{sub}<a class="sub-all" href="leistungen.html">Alle Leistungen {ico("i-arrow")}</a></div></div>
      </div>
      <a href="ueber-uns.html"{cur("ueber-uns")}>Über uns</a>
      <a href="kontakt.html"{cur("kontakt")}>Kontakt</a>
      <a class="mlegal" href="datenschutz.html"{cur("datenschutz")}>Datenschutz</a>
      <a class="mlegal" href="impressum.html"{cur("impressum")}>Impressum</a>
    </nav>
    <div class="nav-cta">
      <a class="phone-link" href="{PHONE_HREF}">{ico("i-phone")}{PHONE}</a>
      <a class="btn btn-primary" href="kontakt.html">Angebot anfragen {ARROW}</a>
      <button class="burger" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
</header>
"""


def footer():
    svc = "".join(f'<li><a href="{slug}.html">{e(name)}</a></li>' for slug, name, _, _ in SERVICES)
    return f"""
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a href="index.html" class="foot-logo" aria-label="Blaum Dienstleistungen, Startseite"><img src="assets/logo-full.png" alt="Blaum Dienstleistungen. Wir halten Ihre Umgebung sauber" width="150" height="194" loading="lazy"></a>
        <p>Blaum Dienstleistungen. Gebäudereinigung in Köln &amp; Umgebung.</p>
      </div>
      <div>
        <h4>Leistungen</h4>
        <ul>{svc}</ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li>Myliusstraße 11<br>50823 Köln</li>
          <li><a href="{PHONE_HREF}">{PHONE}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© <span id="yr"></span> Blaum Dienstleistungen</span>
      <nav><a href="index.html">Startseite</a><a href="leistungen.html">Leistungen</a><a href="kontakt.html">Kontakt</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></nav>
    </div>
    <div class="bigword" aria-hidden="true">Blitzblank.</div>
  </div>
</footer>

<div class="mbar" id="mbar">
  <a href="{PHONE_HREF}">{ico("i-phone")}Anrufen</a>
  <a href="kontakt.html">Angebot anfragen</a>
</div>

<script src="assets/site.js?v={VER}"></script>
</body>
</html>
"""


LINK = re.compile(r'(href|src|poster)="(?!https?:|mailto:|tel:|#|data:)([^"]*)"')


def clean_urls(html, prefix):
    """Turn 'x.html' links into clean folder URLs ('x/') relative to the page."""
    def fix(m):
        attr, url = m.groups()
        if url.startswith("assets/"):
            url = prefix + url
        elif url.startswith("index.html"):
            url = (prefix or "./") + url[len("index.html"):]
        else:
            m2 = re.match(r"([a-z0-9-]+)\.html(.*)$", url)
            if m2:
                url = f"{prefix}{m2.group(1)}/{m2.group(2)}"
        return f'{attr}="{url}"'
    return LINK.sub(fix, html)


def write(slug, html):
    """index -> /index.html, everything else -> /<slug>/index.html (served as /<slug>/)."""
    prefix = "" if slug == "index" else "../"
    folder = ROOT if slug == "index" else os.path.join(ROOT, slug)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_urls(html, prefix))
    print("wrote", "/" if slug == "index" else f"/{slug}/")


def page(fname, title, desc, active, main):
    html = head(title, desc) + header(active) + "\n<main>\n" + main + "\n</main>\n" + footer()
    write(fname[:-len(".html")], html)


def crumbs(*items):
    out = ['<a href="index.html">Start</a>']
    for i, (label, href) in enumerate(items):
        out.append('<span class="sep">/</span>')
        if href:
            out.append(f'<a href="{href}">{e(label)}</a>')
        else:
            out.append(f'<span aria-current="page">{e(label)}</span>')
    return f'<nav class="crumbs" aria-label="Brotkrumen">{"".join(out)}</nav>'


RINGS = '<svg class="rings" viewBox="0 0 200 200" fill="none" stroke="#3FE0B5" aria-hidden="true"><circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="55"/><circle cx="100" cy="100" r="80"/><circle cx="100" cy="100" r="99"/></svg>'


def cta_band(title, paras, pick=None, eyebrow="Kontakt"):
    q = f"?leistung={pick}" if pick else ""
    ps = "".join(f"<p>{e(p)}</p>" for p in paras)
    return f"""<section class="tight">
  <div class="wrap">
    <div class="cta-band">
      <div style="position:relative;z-index:1">
        <span class="eyebrow">{e(eyebrow)}</span>
        <h2>{e(title)}</h2>
        {ps}
      </div>
      <div class="acts">
        <a class="btn btn-primary" href="kontakt.html{q}">Zum Kontaktformular {ARROW}</a>
        <a class="btn btn-ghost" href="mailto:{MAIL}">{ico("i-mail")} E-Mail senden</a>
        <a class="btn btn-ghost" href="{PHONE_HREF}">{ico("i-phone")} Anrufen: {PHONE}</a>
      </div>
      {RINGS}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- service pages
# Texts taken from the live pages (emoji bullets turned into design elements).
DETAIL = {
    "praxisreinigung": dict(
        img="praxis", badge="Hygienisch sauber",
        lead="Hygiene ist Vertrauen. Wir sorgen für beides.",
        intro=["In Arztpraxen, Zahnarztpraxen und Therapieeinrichtungen spielt Hygiene eine entscheidende Rolle. Patienten und Besucher sollen sich wohlfühlen und zugleich auf höchste Sauberkeit und Infektionsschutz vertrauen können.",
               "Mit Blaum Dienstleistungen haben Sie einen erfahrenen Partner an Ihrer Seite, der die besonderen Anforderungen der Praxisreinigung kennt und erfüllt.",
               "Wir reinigen Ihre Praxisräume gründlich, hygienisch und diskret, angepasst an Ihre Öffnungszeiten und an die individuellen Hygienevorgaben."],
        sections=[
            ("features", "Unsere Leistungen im Überblick", [
                ("Böden & Oberflächen gründlich reinigen", "Hartböden, Teppiche, Möbeloberflächen, Fensterbänke"),
                ("Desinfektion von Behandlungs- und Untersuchungsräumen", "Tische, Liegen, medizinische Geräte, gemäß Hygienevorgaben"),
                ("Empfangsbereiche & Wartezimmer reinigen und desinfizieren", "Tresen, Stühle, Wartezonen, Zeitschriftenablagen"),
                ("Sanitärbereiche hygienisch reinigen", "Toiletten, Waschbecken, Armaturen, Spiegel"),
                ("Hygieneschwerpunkte: Türen, Griffe, Lichtschalter", "Regelmäßige Desinfektion stark berührter Flächen"),
                ("Fenster & Glasflächen reinigen (optional)", "Innen und außen"),
                ("Abfallbehälter leeren & hygienische Entsorgung", "")]),
            ("benefits", "Warum Blaum Dienstleistungen?", [
                "Fachgerechte Hygienereinigung nach aktuellen Standards", "Diskretes, freundliches Personal",
                "Reinigung nach Ihrem Zeitplan, auch außerhalb der Sprechzeiten",
                "Flexible Leistungen: von täglicher Unterhaltsreinigung bis zu individuellen Hygienediensten",
                "Verwendung von umweltfreundlichen und zugelassenen Reinigungs- und Desinfektionsmitteln"]),
            ("audience", "Für wen bieten wir Praxisreinigung an?", [
                "Allgemeinmedizinische Praxen", "Zahnarztpraxen", "Facharztpraxen",
                "Physiotherapie- und Ergotherapiepraxen", "Heilpraktiker", "Kosmetik- und Fußpflegepraxen"]),
        ],
        cta=("Sprechen Sie uns an!", ["Gern erstellen wir Ihnen ein individuelles Angebot für die Reinigung Ihrer Praxisräume.",
                                      "Nehmen Sie Kontakt mit uns auf. Wir freuen uns auf Ihre Anfrage!"])),
    "airbnb-service": dict(
        img="airbnb", badge="Bereit für Gäste",
        lead="Saubere Apartments, zufriedene Gäste",
        intro=["Als Gastgeber wissen Sie: Der erste Eindruck zählt!",
               "Ein frisch gereinigtes und ordentlich vorbereitetes Apartment trägt entscheidend dazu bei, dass Ihre Gäste sich willkommen fühlen und positive Bewertungen hinterlassen.",
               "Mit Blaum Dienstleistungen haben Sie einen zuverlässigen Partner für die professionelle Reinigung und Übergabe Ihrer Ferienwohnung oder AirBnB-Unterkunft, flexibel, gründlich und termintreu."],
        sections=[
            ("features", "Unser Service für Ihre Ferienwohnung", [
                ("Komplette Reinigung von Bad & Küche", ""), ("Reinigung aller Böden, Möbel und Oberflächen", ""),
                ("Frische Bettwäsche und Handtücher bereitstellen (optional)", ""),
                ("Müllentsorgung und Nachfüllen von Verbrauchsartikeln", ""),
                ("Kontrolle auf Schäden oder vergessene Gegenstände", ""),
                ("Flexible Einsätze, auch kurzfristig bei schnellen Gästewechseln", "")]),
            ("benefits", "Warum Blaum Dienstleistungen für Ihren AirBnB-Service?", [
                "Zuverlässigkeit und Pünktlichkeit", "Flexibler Service, angepasst an Ihre Buchungen",
                "Sorgfältige und hygienische Reinigung", "Persönlicher Kontakt und individuelle Absprachen",
                "Faire Preise und transparente Leistungen"]),
            ("audience", "Für wen bieten wir unseren AirBnB-Service an?", [
                "Private Gastgeber in Köln", "Professionelle Vermieter & Agenturen",
                "Betreiber von Ferienwohnungen und möblierten Apartments"]),
        ],
        cta=("Kontaktieren Sie uns!", ["Gern übernehmen wir die Reinigung und Übergabe Ihrer Ferienwohnung, damit Ihre Gäste begeistert sind und gerne wiederkommen.",
                                       "Fordern Sie jetzt Ihr individuelles Angebot an. Wir freuen uns auf Ihre Anfrage!"])),
    "baureinigung": dict(
        img="bau", badge="Bezugsfertig",
        lead="Saubere Übergabe nach Bau oder Renovierung",
        intro=["Ob Neubau, Umbau oder Sanierung: Nach Abschluss der Bauarbeiten ist meist eine gründliche Reinigung nötig, damit die Immobilie in bestem Zustand übergeben werden kann.",
               "Mit Blaum Dienstleistungen erhalten Sie eine professionelle Baureinigung in Köln und Umgebung: Wir sorgen dafür, dass Staub, Bauschmutz und Rückstände zuverlässig entfernt werden, für eine bezugsfertige und saubere Immobilie.",
               "Wir arbeiten flexibel, termintreu und stimmen unsere Leistungen individuell auf Ihre Baustelle ab. Ob Wohnhäuser, Gewerbeobjekte oder öffentliche Gebäude: Wir sind für Sie da!"],
        sections=[
            ("features", "Unsere Leistungen im Bereich Baureinigung", [
                ("Entfernung von Bauschmutz, Staub und Bauresten", ""),
                ("Fachgerechte Entsorgung von Verpackungsmaterialien und Baustellenabfällen", ""),
                ("Reinigung von Fenstern, Rahmen und Glasflächen", "Auch Baureste wie Mörtel, Farbe etc."),
                ("Reinigung von Türen, Türrahmen, Sockelleisten und Beschlägen", ""),
                ("Gründliche Reinigung aller Böden", "Hartböden, Fliesen, Teppich, Laminat"),
                ("Feinreinigung aller Oberflächen", "Steckdosen, Lichtschalter, Heizkörper"),
                ("Sanitärreinigung", "Bäder, Toiletten und Küchenbereiche bezugsfertig reinigen")]),
            ("benefits", "Warum Blaum Dienstleistungen für Ihre Baureinigung?", [
                "Gründliche Reinigung bis ins Detail", "Erfahrung mit Baustellen und speziellen Anforderungen",
                "Flexible und termingerechte Einsätze", "Individuelle Planung je nach Objekt und Zeitplan",
                "Einsatz umweltfreundlicher Reinigungsmittel und moderner Technik"]),
            ("audience", "Für wen bieten wir Baureinigung an?", [
                "Baufirmen & Bauträger", "Architekten & Planungsbüros", "Wohnungsbaugesellschaften & Hausverwaltungen",
                "Privatkunden nach Neubau oder Renovierung", "Gewerbliche Kunden (Büros, Ladenlokale, Praxisräume etc.)"]),
        ],
        cta=("Sprechen Sie uns an!", ["Ob Neubau, Umbau oder Sanierung: Wir übernehmen die professionelle Baureinigung in Köln und Umgebung.",
                                      "Gern erstellen wir Ihnen ein individuelles und unverbindliches Angebot. Kontaktieren Sie uns jetzt!"])),
    "treppenhausreinigung": dict(
        img="treppe", badge="Erster Eindruck",
        lead="Saubere und gepflegte Gemeinschaftsbereiche",
        intro=["Das Treppenhaus ist die Visitenkarte eines Gebäudes. Es vermittelt Mietern, Bewohnern und Besuchern den ersten Eindruck. Ein sauberes und ordentlich gepflegtes Treppenhaus trägt wesentlich zum Erscheinungsbild und zur Werterhaltung Ihrer Immobilie bei.",
               "Mit Blaum Dienstleistungen bieten wir Ihnen eine professionelle und zuverlässige Treppenhausreinigung in Köln und Umgebung. Ob Wohnhaus, Bürogebäude oder Gewerbeimmobilie: Wir sorgen für gepflegte Gemeinschaftsbereiche, die sich sehen lassen können."],
        sections=[
            ("features", "Unsere Leistungen im Bereich Treppenhausreinigung", [
                ("Gründliche Reinigung von Treppen, Stufen und Podesten", ""),
                ("Reinigung von Eingangsbereichen, Türen und Türrahmen", ""),
                ("Reinigung von Handläufen und Geländern", ""),
                ("Feuchtreinigung von Sockelleisten und Fußleisten", ""),
                ("Fegen und Wischen von Kellergängen und Fluren", ""),
                ("Reinigung von Aufzugskabinen und Aufzugstüren", "Falls vorhanden"),
                ("Leeren von Papierkörben und Abfallbehältern", ""),
                ("Glas- und Fensterreinigung in den Treppenhäusern", "Optional")]),
            ("benefits", "Warum Blaum Dienstleistungen für Ihre Treppenhausreinigung?", [
                "Gründliche und regelmäßige Reinigung", "Flexible Einsatzzeiten nach Ihrem Bedarf",
                "Freundliches und zuverlässiges Reinigungsteam",
                "Individuelle Angebote für Hausverwaltungen & Eigentümergemeinschaften", "Faire und transparente Preise"]),
            ("audience", "Für wen bieten wir Treppenhausreinigung an?", [
                "Hausverwaltungen", "Eigentümergemeinschaften (WEG)", "Wohnungsbaugesellschaften",
                "Private Vermieter", "Gewerbeobjekte & Bürogebäude"]),
        ],
        cta=("Sprechen Sie uns an!", ["Gern übernehmen wir die regelmäßige Reinigung Ihrer Treppenhäuser, damit Ihre Immobilie stets gepflegt wirkt und Mieter sowie Besucher einen positiven Eindruck erhalten.",
                                      "Fordern Sie jetzt Ihr individuelles und unverbindliches Angebot an. Wir freuen uns auf Ihre Anfrage!"])),
    "hausmeisterservice": dict(
        img="haus", badge="Alles im Blick",
        lead="Zuverlässige Betreuung für Ihre Immobilie.",
        intro=["Ein gepflegtes Gebäude und ein reibungsloser Ablauf im Alltag: Das ist, was Eigentümer, Mieter und Verwalter erwarten. Unser Hausmeisterservice kümmert sich zuverlässig um alle anfallenden Aufgaben rund um Ihre Immobilie, kompetent, freundlich und einsatzbereit.",
               "Ob regelmäßige Kontrollgänge, kleinere Reparaturen oder die Koordination von Handwerkern: Wir sind Ihr Ansprechpartner für Werterhalt und Ordnung."],
        sections=[
            ("features", "Unsere Leistungen im Überblick", [
                ("Kleinreparaturen", "Schnelle Hilfe bei alltäglichen Mängeln: defekte Leuchtmittel, tropfende Wasserhähne, lose Türgriffe u. v. m."),
                ("Zustandskontrollen", "Regelmäßige Begehung von Technikräumen, Treppenhäusern, Tiefgaragen oder Außenanlagen, mit Dokumentation auf Wunsch."),
                ("Müllbereitstellung & Sauberkeit", "Bereitstellen der Mülltonnen, Reinigung von Müllplätzen und Kontrolle der Mülltrennung."),
                ("Pflege von Außenanlagen", "Kehren, Unkrautentfernung, Laubbeseitigung, Winterdienst (nach Vereinbarung)."),
                ("Koordination externer Dienstleister", "Anwesenheit bei Reparaturen, Kontakt mit Handwerkern, Meldung von Störungen."),
                ("Schließdienste", "Schlüsselverwaltung, Öffnungs- und Schließdienste nach Bedarf.")]),
            ("benefits", "Ihre Vorteile", [
                "Feste Ansprechpartner & regelmäßige Betreuung", "Zuverlässige Ausführung aller Aufgaben",
                "Individuell an Ihre Immobilie angepasst", "Mehr Ordnung, Sicherheit und Werterhalt",
                "Persönlicher Service mit Blick fürs Detail"]),
            ("audience", "Einsatzbereiche", [
                "Mehrfamilienhäuser & Wohnanlagen", "Schulen & Kindergärten",
                "Gewerbeimmobilien & Ladenlokale", "Privatobjekte & kleine Wohnhäuser"]),
        ],
        cta=("Sprechen Sie uns an!", ["Mit unserem Hausmeisterservice haben Sie weniger Sorgen, und Ihre Mieter, Kunden oder Bewohner ein gepflegtes, funktionierendes Umfeld."])),
    "unterhaltsreinigung": dict(
        img="unterhalt", badge="Im festen Rhythmus",
        lead="Regelmäßige Sauberkeit für ein gepflegtes Umfeld",
        intro=["Eine saubere Umgebung trägt maßgeblich zum Wohlbefinden bei, ob im Büro, in der Praxis oder im Wohnhaus. Unsere Unterhaltsreinigung sorgt für dauerhafte Sauberkeit in Ihren Räumlichkeiten, ganz nach Ihren Wünschen und im individuell abgestimmten Rhythmus.",
               "Mit einem zuverlässigen Team, modernen Reinigungsmitteln und einem geschulten Blick für Details übernehmen wir die regelmäßige Reinigung Ihrer Immobilie, damit Sie sich auf das Wesentliche konzentrieren können."],
        sections=[
            ("features", "Unsere Leistungen im Rahmen der Unterhaltsreinigung", [
                ("Oberflächenreinigung", "Tische, Arbeitsflächen, Fensterbänke, Türklinken & Co: gründlich abgewischt und desinfiziert."),
                ("Mobiliarpflege", "Schonende Reinigung von Bürostühlen, Schränken, Empfangsbereichen u.v.m."),
                ("Bodenpflege", "Staubsaugen, Kehren oder Wischen, je nach Bodenart individuell angepasst."),
                ("Sanitärreinigung", "Hygienische Reinigung von Toiletten, Waschbecken, Duschen & Gemeinschaftsbereichen."),
                ("Abfallentsorgung", "Leeren von Mülleimern, fachgerechtes Trennen & Austausch von Müllbeuteln."),
                ("Küchen- & Teeküchenpflege", "Arbeitsplatten, Spülbecken, Kaffeemaschinen und Küchenutensilien reinigen & pflegen."),
                ("Reinigungsplan nach Maß", "Täglich, wöchentlich oder in individuellem Turnus. Wir richten uns ganz nach Ihnen.")]),
            ("audience", "Geeignet für", [
                "Büros & Agenturen", "Praxen & Kanzleien", "Wohnanlagen & Hausverwaltungen",
                "Schulen & Kitas", "Läden & Gastronomie", "Privatkunden mit regelmäßiger Reinigung"]),
            ("benefits", "Ihre Vorteile mit Blaum Dienstleistungen", [
                "Regelmäßige & verlässliche Reinigung", "Freundliches, geschultes Personal",
                "Diskrete & sorgfältige Arbeitsweise", "Maßgeschneiderte Reinigungspläne",
                "Flexible Zeiten, auch früh morgens oder spät abends", "Fester Ansprechpartner für Ihre Anliegen"]),
        ],
        cta=("Sprechen Sie uns an!", ["Ob einmal pro Woche oder täglich: Wir richten uns ganz nach Ihrem Bedarf. Gerne erstellen wir ein individuelles Angebot für Ihre Unterhaltsreinigung in Köln und Umgebung."])),
    "glasreinigung": dict(
        img="glas", badge="Streifenfrei",
        lead="Für streifenfreien Durchblick und glänzende Fenster.",
        intro=["Klare Sicht und gepflegte Glasflächen sind die Visitenkarte eines Gebäudes, egal ob im privaten oder gewerblichen Bereich. Mit unserer professionellen Glasreinigung sorgen wir dafür, dass Ihre Fenster, Glasfronten und Rahmen dauerhaft sauber und gepflegt bleiben.",
               "Ob kleine Fenster in Wohnungen, große Glasfassaden in Büros oder Schaufenster von Ladengeschäften: Wir reinigen schnell, gründlich und zuverlässig."],
        sections=[
            ("features", "Unser Service", [
                ("Reinigung von Fenstern & Rahmen", ""), ("Glasfassaden", ""), ("Glastrennwände & Glastüren", ""),
                ("Schaufenster & Wintergärten", ""), ("Spiegel & andere Glasflächen", ""),
                ("Entfernung von hartnäckigen Verschmutzungen, Staub und Fingerabdrücken", ""),
                ("Reinigung innen & außen", "Je nach Wunsch")]),
            ("benefits", "Ihre Vorteile", [
                "Streifenfreie, saubere Glasflächen", "Mehr Helligkeit und ein gepflegtes Erscheinungsbild",
                "Werterhalt von Fenstern und Fassaden", "Individuell auf Ihre Bedürfnisse abgestimmt",
                "Auch regelmäßige Reinigungsintervalle möglich (z. B. monatlich, vierteljährlich oder nach Absprache)"]),
            ("audience", "Für wen wir arbeiten", [
                "Firmen & Gewerbe", "Privatwohnungen & Einfamilienhäuser", "Ladengeschäfte & Gastronomie",
                "Arztpraxen & Kanzleien", "Hotels & Ferienwohnungen"]),
        ],
        cta=("Kontaktieren Sie uns!", ["Wir erstellen Ihnen gerne ein individuelles Angebot für Ihre Glasreinigung in Köln und Umgebung, einmalig oder als regelmäßiger Service.",
                                       "Jetzt anfragen. Wir freuen uns auf Sie!"])),
    "grundreinigung": dict(
        img="grund", badge="Bis ins Detail",
        lead="Perfekte Sauberkeit für Ihre Räume",
        intro=["Im Laufe der Zeit sammeln sich Schmutz, Staub und Ablagerungen, die bei der normalen Unterhaltsreinigung oft nicht vollständig entfernt werden. Hier kommt die Grundreinigung ins Spiel: eine besonders gründliche, tiefgehende Reinigung Ihrer Räume.",
               "Mit Blaum Dienstleistungen bieten wir Ihnen eine professionelle Grundreinigung in Köln und Umgebung, für Wohnräume, Büros, Praxen, Gewerbeflächen und mehr. Wir sorgen dafür, dass Ihre Räume wieder in neuem Glanz erstrahlen."],
        sections=[
            ("features", "Unsere Leistungen im Bereich Grundreinigung", [
                ("Gründliche Reinigung aller Bodenbeläge", "Teppich, Fliesen, Laminat, PVC, Parkett, inkl. Spezialbehandlung"),
                ("Reinigung von Türen, Türrahmen und Sockelleisten", ""),
                ("Intensive Fenster- und Glasreinigung", "Innen und außen"),
                ("Gründliche Reinigung von Möbeln, Schränken und Oberflächen", ""),
                ("Entfernung von haftenden Verschmutzungen und Ablagerungen", ""),
                ("Komplettreinigung von Sanitärbereichen", "Bad, WC, Küche"),
                ("Reinigung von Heizkörpern, Lichtschaltern und Steckdosen", ""),
                ("Fegen und Reinigen von schwer zugänglichen Bereichen", "")]),
            ("when", "Wann ist eine Grundreinigung sinnvoll?", [
                "Nach Renovierung oder Umbau", "Bei Einzug oder Auszug (Endreinigung)",
                "In regelmäßigen Abständen als Ergänzung zur Unterhaltsreinigung",
                "Bei besonders starken Verschmutzungen", "Zur Werterhaltung von Immobilien"]),
            ("benefits", "Warum Blaum Dienstleistungen für Ihre Grundreinigung?", [
                "Sorgfältige, intensive Reinigung bis in die kleinsten Ecken",
                "Individuelle Planung je nach Objekt und Verschmutzungsgrad",
                "Fachkundige Reinigungskräfte mit Erfahrung",
                "Einsatz hochwertiger und umweltfreundlicher Reinigungsmittel",
                "Flexible Termine, auch kurzfristig möglich"]),
            ("audience", "Für wen bieten wir Grundreinigung an?", [
                "Privatkunden (Wohnungen & Häuser)", "Hausverwaltungen & Vermieter", "Gewerbliche Kunden & Büros",
                "Praxen & Therapieräume", "Einzelhandel & Gastronomie"]),
        ],
        cta=("Sprechen Sie uns an!", ["Gern erstellen wir Ihnen ein individuelles und unverbindliches Angebot für Ihre Grundreinigung in Köln und Umgebung.",
                                      "Kontaktieren Sie uns jetzt. Wir freuen uns auf Ihre Anfrage!"])),
}

# Short texts from the live "Leistungen" overview page
OVERVIEW = {
    "airbnb-service": ("AirBnB-Reinigung & Übergabe", "Komplette Reinigung und vorbereitende Übergabe Ihrer Ferienwohnungen und AirBnB-Apartments, für zufriedene Gäste und stressfreie Wechsel."),
    "unterhaltsreinigung": ("Unterhaltsreinigung", "Regelmäßige Reinigung von Büros, Praxen und gewerblichen Räumen, zuverlässig und flexibel."),
    "praxisreinigung": ("Praxisreinigung", "Hygienische und gründliche Reinigung für Arztpraxen, Therapiezentren und Gesundheitsdienstleister, für ein sicheres und sauberes Umfeld."),
    "grundreinigung": ("Grundreinigung", "Gründliche Intensivreinigung von Böden, Oberflächen und schwer zugänglichen Bereichen, ideal als Ergänzung zur regelmäßigen Reinigung."),
    "glasreinigung": ("Glasreinigung", "Streifenfreie Reinigung von Fenstern, Glasfassaden und Schaufenstern, für klaren Durchblick und gepflegte Optik."),
    "treppenhausreinigung": ("Treppenhausreinigung", "Saubere Treppenhäuser und Gemeinschaftsbereiche, für ein gepflegtes Wohnumfeld in Mehrfamilienhäusern und Gewerbeobjekten."),
    "baureinigung": ("Baureinigung", "Reinigung nach Neu- oder Umbau, Renovierungen oder Sanierungen. Wir entfernen Bauschmutz und sorgen für bezugsfertige Räume."),
    "hausmeisterservice": ("Hausmeisterservice", "Zuverlässige Betreuung rund ums Gebäude, von kleinen Reparaturen bis zur Objektkontrolle. Unser Hausmeisterservice sorgt für Ordnung, Sicherheit und den Werterhalt Ihrer Immobilie. Ideal für Wohnanlagen, Gewerbeobjekte und private Immobilien."),
}
OVERVIEW_ORDER = ["airbnb-service", "unterhaltsreinigung", "praxisreinigung", "grundreinigung",
                  "glasreinigung", "treppenhausreinigung", "baureinigung", "hausmeisterservice"]


def svc_by_slug(slug):
    return next(s for s in SERVICES if s[0] == slug)


def render_section(kind, title, items, idx, icon):
    if kind == "features":
        if sum(1 for _, d in items if d) * 2 < len(items):
            lis = "".join(
                f'<li><span class="ck">{ico("i-check")}</span><span>{e(t)}{f"<small>{e(d)}</small>" if d else ""}</span></li>'
                for t, d in items)
            body = f'<div class="feat-panel"><ul class="checks">{lis}</ul></div>'
        else:
            cards = "".join(
                f'<div class="feat"><div class="cic">{ico(icon)}</div><h3>{e(t)}</h3>{f"<p>{e(d)}</p>" if d else ""}</div>'
                for t, d in items)
            body = f'<div class="feats">{cards}</div>'
        return f"""<section id="leistungen-im-detail" class="tight">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Leistungsumfang</span><h2 style="max-width:18ch">{e(title)}</h2></div></div>
    {body}
  </div>
</section>
"""
    if kind == "benefits":
        lis = "".join(f'<li><span class="ck">{ico("i-check")}</span>{e(t)}</li>' for t in items)
        return f"""<section class="process" style="margin-top:80px">
  <div class="wrap" style="position:relative">
    <div class="sec-head"><div><span class="eyebrow">Warum Blaum</span><h2 style="max-width:20ch">{e(title)}</h2></div></div>
    <ul class="ticks">{lis}</ul>
  </div>
</section>
"""
    if kind == "when":
        lis = "".join(f'<li><span class="ck">{ico("i-check")}</span>{e(t)}</li>' for t in items)
        return f"""<section class="tight">
  <div class="wrap who">
    <div><span class="eyebrow">Der richtige Zeitpunkt</span><h2>{e(title)}</h2></div>
    <div class="feat-panel"><ul class="checks" style="grid-template-columns:1fr">{lis}</ul></div>
  </div>
</section>
"""
    if kind == "audience":
        sp = "".join(f'<span><i>{ico("i-check")}</i>{e(t)}</span>' for t in items)
        return f"""<section>
  <div class="wrap who">
    <div><span class="eyebrow">Zielgruppen</span><h2>{e(title)}</h2></div>
    <div class="who-list" style="padding-top:8px">{sp}</div>
  </div>
</section>
"""
    raise ValueError(kind)


def more_services(exclude):
    links = "".join(
        f'<a href="{slug}.html"><img src="assets/svc-{img}.webp" alt="" loading="lazy">{e(name)}{ico("i-arrow")}</a>'
        for slug, name, _, img in SERVICES if slug != exclude)
    return f"""<section class="tight" style="padding-bottom:40px">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:28px"><div><span class="eyebrow">Weitere Leistungen</span><h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem);max-width:none">Alles aus einer Hand.</h2></div></div>
    <div class="more">{links}</div>
  </div>
</section>
"""


def media(img, name):
    """Looping clip if assets/vid-<img>.mp4 exists, otherwise the still photo."""
    if os.path.exists(os.path.join(ROOT, "assets", f"vid-{img}.mp4")):
        return (f'<video autoplay muted loop playsinline preload="metadata" poster="assets/svc-{img}.webp" '
                f'aria-label="{e(name)}"><source src="assets/vid-{img}.mp4" type="video/mp4"></video>')
    return f'<img src="assets/svc-{img}.webp" alt="{e(name)}" fetchpriority="high">'


def build_service(slug):
    _, name, icon, _ = svc_by_slug(slug)
    d = DETAIL[slug]
    title_name = OVERVIEW[slug][0] if slug == "airbnb-service" else name
    intro = "".join(f"<p>{e(p)}</p>" for p in d["intro"])
    hero = f"""<section class="phero">
  <div class="wrap phero-grid">
    <div>
      {crumbs(("Leistungen", "leistungen.html"), (name, None))}
      <span class="eyebrow">Leistungen · Köln &amp; Umgebung</span>
      <h1><span class="shine">{e(title_name)}</span></h1>
      <p class="lead">{e(d["lead"])}</p>
      <div class="intro">{intro}</div>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="kontakt.html?leistung={slug}">Angebot anfragen {ARROW}</a>
        <a class="btn btn-ghost" href="{PHONE_HREF}">{ico("i-phone")} {PHONE}</a>
      </div>
    </div>
    <div class="visual">
      <div class="frame">{media(d["img"], name)}<span class="badge">{ico(icon)}{e(d["badge"])}</span></div>
      <div class="floating f1"><span class="ic">{ico("i-pin")}</span><span><b>Köln &amp; Umgebung</b>Regional verwurzelt</span></div>
      <div class="floating f2"><span class="ic">{ico("i-euro")}</span><span><b>Faire Preise</b>individuelles Angebot</span></div>
    </div>
  </div>
</section>
"""
    secs = "".join(render_section(k, t, it, i, icon) for i, (k, t, it) in enumerate(d["sections"]))
    main = hero + secs + cta_band(d["cta"][0], d["cta"][1], slug) + more_services(slug)
    page(f"{slug}.html", f"{title_name} in Köln | Blaum Dienstleistungen",
         f"{title_name} in Köln & Umgebung von Blaum Dienstleistungen: {d['lead']}", slug, main)


def build_overview():
    cards = []
    for i, slug in enumerate(OVERVIEW_ORDER):
        _, name, icon, img = svc_by_slug(slug)
        t, desc = OVERVIEW[slug]
        cards.append(f"""<a class="scard" href="{slug}.html">
      <figure><img src="assets/svc-{img}.webp" alt="{e(name)}" loading="lazy"><figcaption>{ico(icon)}</figcaption></figure>
      <div class="body"><span class="num">{i+1:02d} / 08</span><h2>{e(t)}</h2><p>{e(desc)}</p><span class="go">Mehr erfahren <span class="dot">{ico("i-arrow")}</span></span></div>
    </a>""")
    main = f"""<section class="phero" style="padding-bottom:40px">
  <div class="wrap phero-grid">
    <div>
      {crumbs(("Leistungen", None))}
      <span class="eyebrow">Unsere Leistungen</span>
      <h1 style="font-size:clamp(2.4rem,4.4vw,3.9rem)">Professionelle Reinigung und Service für <span class="shine">Köln</span> und Umgebung</h1>
      <div class="intro">
        <p>Wir von Blaum Dienstleistungen bieten Ihnen ein umfangreiches Leistungsspektrum im Bereich Reinigung und Objektpflege, zuverlässig, flexibel und ganz auf Ihre Bedürfnisse abgestimmt.</p>
        <p>Ob für Privatkunden, Gewerbe oder Ferienwohnungen: Wir sorgen für Sauberkeit und ein gepflegtes Umfeld, auf das Sie sich verlassen können.</p>
      </div>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="kontakt.html">Kostenloses Angebot {ARROW}</a>
        <a class="btn btn-ghost" href="#uebersicht">Zur Übersicht</a>
      </div>
    </div>
    <div class="visual">
      <div class="frame wide"><img src="assets/svc-unterhalt.webp" alt="Reinigung eines Büros" fetchpriority="high"><span class="badge">{ico("i-grid")}8 Leistungen</span></div>
      <div class="floating f1"><span class="ic">{ico("i-building")}</span><span><b>Firmenkunden</b>Büros, Praxen, Gewerbe</span></div>
      <div class="floating f2"><span class="ic">{ico("i-home")}</span><span><b>Privatkunden</b>Wohnungen &amp; Apartments</span></div>
    </div>
  </div>
</section>

<section id="uebersicht" class="tight">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Übersicht</span><h2 style="max-width:24ch">Hier finden Sie einen Überblick über unsere Leistungen.</h2></div></div>
    <div class="svc-cards">
    {"".join(cards)}
    </div>
  </div>
</section>
""" + cta_band("Haben wir Ihr Interesse geweckt?", ["Melden Sie sich gern für eine Beratung bei uns. Wir beantworten Ihre Fragen und gehen individuell auf Ihr Anliegen ein."])
    page("leistungen.html", "Leistungen | Blaum Dienstleistungen Köln",
         "Alle Leistungen von Blaum Dienstleistungen in Köln: Praxisreinigung, AirBnB-Service, Baureinigung, Treppenhausreinigung, Hausmeisterservice, Unterhaltsreinigung, Glasreinigung und Grundreinigung.",
         "leistungen", main)


def build_about():
    spectrum = [("unterhaltsreinigung", "Unterhaltsreinigung für Privat- und Geschäftsräume"),
                ("glasreinigung", "Glas- und Fensterreinigung"), ("praxisreinigung", "Praxis- und Büroreinigung"),
                ("treppenhausreinigung", "Treppenhausreinigung"), ("baureinigung", "Baureinigung und Grundreinigung"),
                ("airbnb-service", "AirBnB-Service & Apartmentreinigung")]
    sp = "".join(f'<a href="{s}.html"><span class="tic">{ico(svc_by_slug(s)[2])}</span>{e(t)}</a>' for s, t in spectrum)
    main = f"""<section class="phero">
  <div class="wrap about-grid">
    <div class="portrait">
      <img class="pimg" src="assets/about.webp" alt="Aufgeräumter Reinigungswagen mit Mikrofasertüchern in einem hellen Flur" fetchpriority="high">
      <div class="cap"><div><b>Pascal Blaum</b><span>Gründer, Blaum Dienstleistungen</span></div><img src="assets/logo-mark-sm.png" alt="" width="36" height="35" style="width:36px;height:auto"></div>
    </div>
    <div class="about-text">
      {crumbs(("Über uns", None))}
      <span class="eyebrow">Über uns</span>
      <h1 style="font-size:clamp(2.2rem,4.4vw,3.6rem);margin:18px 0 8px">Persönlicher Service für Firmen und Privatkunden in Köln</h1>
      <blockquote>Persönlich, flexibel und professionell.</blockquote>
      <p>Mein Name ist Pascal Blaum, Gründer von Blaum Dienstleistungen. Mit meinem Team stehe ich für einen Reinigungsservice, auf den Sie sich verlassen können: persönlich, flexibel und professionell.</p>
      <p>Ob Privatwohnung, Ferienapartment, Praxis oder Büro: Wir sorgen dafür, dass Ihre Räume stets gepflegt und einladend sind. Dabei ist uns der direkte Kontakt zu unseren Kunden besonders wichtig. Wir hören zu, gehen auf individuelle Wünsche ein und bieten maßgeschneiderte Lösungen.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Unser Leistungsspektrum</span><h2>Alles rund um Reinigung und Objektpflege.</h2></div><a class="btn btn-ghost" href="leistungen.html">Alle Leistungen</a></div>
    <div class="spectrum">{sp}</div>
    <div class="aud" style="margin-top:40px">
      <div class="card"><div class="cic">{ico("i-building")}</div><div><h3>Für Firmenkunden</h3><p>Für Firmenkunden bieten wir zuverlässige und flexible Reinigungslösungen, die sich optimal in Ihre Betriebsabläufe integrieren.</p></div></div>
      <div class="card"><div class="cic">{ico("i-home")}</div><div><h3>Für Privatkunden</h3><p>Privatkunden schätzen unseren freundlichen Service, die Gründlichkeit und die persönliche Betreuung.</p></div></div>
    </div>
  </div>
</section>

<section class="process" style="margin-top:40px">
  <div class="wrap" style="position:relative">
    <div class="sec-head" style="margin-bottom:0"><div><span class="eyebrow">Unser Versprechen</span><h2 style="max-width:22ch">Ihre Zufriedenheit steht für uns an erster Stelle.</h2></div>
    <p class="lead">Ganz gleich ob einmalige Reinigung oder dauerhafte Zusammenarbeit. Ich freue mich auf Ihre Anfrage und darauf, Sie persönlich kennenzulernen!</p></div>
  </div>
</section>
""" + cta_band("Haben wir Ihr Interesse geweckt?", ["Melden Sie sich gern für eine Beratung bei uns."])
    page("ueber-uns.html", "Über uns | Blaum Dienstleistungen Köln",
         "Blaum Dienstleistungen: persönlicher Service für Firmen und Privatkunden in Köln. Gründer Pascal Blaum und sein Team.",
         "ueber-uns", main)


def build_contact():
    main = f"""<section class="phero contact-page" style="padding-bottom:60px">
  <div class="wrap">
    {crumbs(("Kontakt", None))}
    <div class="contact">
      <div class="contact-info">
        <div>
          <span class="eyebrow">Kontakt</span>
          <h1 style="font-size:clamp(2.2rem,4.2vw,3.2rem);margin:16px 0 14px">Nehmen Sie Kontakt mit uns auf</h1>
          <p class="lead">Gerne beantworten wir Ihre Fragen und gehen individuell auf Ihre Anliegen ein. Wir freuen uns, Ihnen helfen zu dürfen.</p>
        </div>
        <div style="display:grid;gap:10px;position:relative;z-index:1">
          <a class="cline" href="{PHONE_HREF}"><span class="ci">{ico("i-phone")}</span><span><small>Telefon</small><b>{PHONE}</b></span></a>
          <a class="cline" href="mailto:{MAIL}"><span class="ci">{ico("i-mail")}</span><span><small>E-Mail</small><b>{MAIL}</b></span></a>
          <a class="cline" href="https://www.google.com/maps/search/?api=1&query=Myliusstra%C3%9Fe+11%2C+50823+K%C3%B6ln" target="_blank" rel="noopener"><span class="ci">{ico("i-pin")}</span><span><small>Adresse</small><b>{ADDR}</b></span></a>
        </div>
        <div class="hours"><span>Köln &amp; Umgebung</span><span>Auch kurzfristig</span><span>Unverbindlich &amp; kostenlos</span></div>
        <svg class="skyline" viewBox="0 0 400 80" preserveAspectRatio="none" aria-hidden="true"><path fill="#3FE0B5" d="M0 80V60h40V40h22V28h30v32h20V36h26v24h18V44h14v16h16V40l5-22 4-18 4 18 5 22v-4h10v4l5-22 4-18 4 18 5 22v40h30V50h30V40h28v20h24V46h28v14h40v20z"/></svg>
      </div>

      <form id="form" novalidate>
        <h2 style="font-size:1.8rem;margin-bottom:6px;letter-spacing:-.01em">Wir freuen uns auf Ihre Anfrage!</h2>
        <p class="sub">Unverbindlich und kostenlos. Wir melden uns schnellstmöglich bei Ihnen.</p>
        <div class="row">
          <div class="field"><label for="name">Name <em>*</em></label><input id="name" name="name" required autocomplete="name" placeholder="Max Mustermann"></div>
          <div class="field"><label for="firma">Firma</label><input id="firma" name="firma" autocomplete="organization" placeholder="optional"></div>
        </div>
        <div class="row">
          <div class="field"><label for="email">E-Mail <em>*</em></label><input id="email" name="email" type="email" required autocomplete="email" placeholder="name@beispiel.de"></div>
          <div class="field"><label for="tel">Telefon</label><input id="tel" name="tel" type="tel" autocomplete="tel" placeholder="optional"></div>
        </div>
        <div class="field">
          <label id="svcLbl">Welche Leistung interessiert Sie?</label>
          <div class="chips" role="group" aria-labelledby="svcLbl" id="chips"></div>
        </div>
        <div class="field"><label for="msg">Nachricht <em>*</em></label><textarea id="msg" name="msg" required placeholder="Objekt, Größe, gewünschter Rhythmus …"></textarea></div>
        <div class="form-foot">
          <small>Mit dem Absenden stimmen Sie der Verarbeitung Ihrer Angaben gemäß unserer <a href="datenschutz.html" style="text-decoration:underline">Datenschutzerklärung</a> zu.</small>
          <button class="btn btn-primary" type="submit">Absenden {ARROW}</button>
        </div>
        <div class="sent" id="sent" role="status">{ico("i-check")}<span></span></div>
      </form>
    </div>
  </div>
</section>
"""
    page("kontakt.html", "Kontakt | Blaum Dienstleistungen Köln",
         "Kontakt zu Blaum Dienstleistungen: Myliusstraße 11, 50823 Köln, Telefon 0173 2831352, info@blaum-dienstleistungen.de.",
         "kontakt", main)


def legal(fname, active, h1, eyebrow, body, toc=None):
    toc_html = ""
    if toc:
        toc_html = '<nav class="toc" aria-label="Inhalt">' + "".join(f'<a href="#{a}">{e(t)}</a>' for a, t in toc) + "</nav>"
    main = f"""<section class="phero" style="padding-bottom:20px">
  <div class="wrap">
    {crumbs((h1, None))}
    <span class="eyebrow">{e(eyebrow)}</span>
    <h1 style="margin-bottom:0">{e(h1)}</h1>
  </div>
</section>
<section class="tight">
  <div class="wrap{' legal-grid' if toc else ''}">
    {toc_html}
    <article class="prose">{body}</article>
  </div>
</section>
"""
    page(fname, f"{h1} | Blaum Dienstleistungen", f"{h1} von Blaum Dienstleistungen, Gebäudereinigung in Köln.", active, main)


def build_impressum():
    body = f"""
<div class="addr">
  <div><small>Anbieter</small><p>Pascal Blaum<br>Blaum Dienstleistungen<br>Myliusstr. 11<br>50823 Köln<br>Deutschland</p></div>
  <div><small>Kontakt</small><p>Telefon: <a href="{PHONE_HREF}">{PHONE}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p></div>
</div>
<h2>Verbraucherstreitbeilegung / Universalschlichtungsstelle</h2>
<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2>
<p>Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäß § 7 Abs. 1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>
<h2>Haftung für Links</h2>
<p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2>
<p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.</p>
"""
    legal("impressum.html", "impressum", "Impressum", "Rechtliches", body)


def ul(items):
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def build_datenschutz():
    toc = [("verantwortlicher", "1. Verantwortlicher"), ("erhebung", "2. Erhebung und Speicherung"),
           ("weitergabe", "3. Weitergabe von Daten"), ("cookies", "4. Cookies"), ("rechte", "5. Ihre Rechte"),
           ("widerspruch", "6. Widerspruchsrecht"), ("sicherheit", "7. Datensicherheit"), ("aktualitaet", "8. Aktualität")]
    body = f"""
<p>Wir freuen uns über Ihr Interesse an unserer Website und an unserem Unternehmen. Der Schutz Ihrer persönlichen Daten ist uns sehr wichtig. Nachfolgend informieren wir Sie darüber, wie wir Ihre personenbezogenen Daten verarbeiten und welche Rechte Ihnen zustehen.</p>
<h2 id="verantwortlicher" style="margin-top:28px">1. Verantwortlicher</h2>
<div class="addr"><div><small>Verantwortlicher</small><p>Blaum Dienstleistungen<br>Inhaber: Pascal Blaum<br>Myliusstr. 11<br>50823 Köln</p></div>
<div><small>Kontakt</small><p>Telefon: <a href="{PHONE_HREF}">{PHONE}</a><br>E-Mail: <a href="mailto:blaumdienstleistungen@web.de">blaumdienstleistungen@web.de</a></p></div></div>
<h2 id="erhebung">2. Erhebung und Speicherung personenbezogener Daten sowie Art und Zweck von deren Verwendung</h2>
<h3>a) Beim Besuch der Website</h3>
<p>Beim Aufrufen unserer Website werden durch den auf Ihrem Endgerät zum Einsatz kommenden Browser automatisch Informationen an den Server unserer Website gesendet. Diese Informationen werden temporär in einem sogenannten Logfile gespeichert. Folgende Informationen werden dabei ohne Ihr Zutun erfasst und bis zur automatisierten Löschung gespeichert:</p>
{ul(["IP-Adresse des anfragenden Rechners", "Datum und Uhrzeit des Zugriffs", "Name und URL der abgerufenen Datei", "Website, von der aus der Zugriff erfolgt (Referrer-URL)", "verwendeter Browser und ggf. das Betriebssystem Ihres Rechners sowie der Name Ihres Access-Providers"])}
<p>Die genannten Daten werden durch uns zu folgenden Zwecken verarbeitet:</p>
{ul(["Gewährleistung eines reibungslosen Verbindungsaufbaus der Website", "Gewährleistung einer komfortablen Nutzung unserer Website", "Auswertung der Systemsicherheit und -stabilität", "zu weiteren administrativen Zwecken"])}
<p>Die Rechtsgrundlage für die Datenverarbeitung ist Art. 6 Abs. 1 S. 1 lit. f DSGVO. Unser berechtigtes Interesse folgt aus oben aufgelisteten Zwecken.</p>
<h3>b) Bei Nutzung unseres Kontaktformulars oder per E-Mail</h3>
<p>Wenn Sie uns über das Kontaktformular auf der Website oder per E-Mail kontaktieren, werden folgende personenbezogene Daten erhoben:</p>
{ul(["Name", "E-Mail-Adresse", "Telefonnummer (sofern angegeben)", "Ihre Nachricht / Anfrage"])}
<p>Die Datenverarbeitung erfolgt zum Zweck der Bearbeitung Ihrer Anfrage und zur Kontaktaufnahme. Rechtsgrundlage hierfür ist Art. 6 Abs. 1 S. 1 lit. b DSGVO.</p>
<h2 id="weitergabe">3. Weitergabe von Daten</h2>
<p>Eine Übermittlung Ihrer persönlichen Daten an Dritte zu anderen als den im Folgenden aufgeführten Zwecken findet nicht statt. Wir geben Ihre persönlichen Daten nur an Dritte weiter, wenn:</p>
{ul(["Sie Ihre ausdrückliche Einwilligung dazu erteilt haben (Art. 6 Abs. 1 S. 1 lit. a DSGVO),", "die Weitergabe zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist (Art. 6 Abs. 1 S. 1 lit. f DSGVO),", "eine gesetzliche Verpflichtung besteht (Art. 6 Abs. 1 S. 1 lit. c DSGVO),", "oder dies gesetzlich zulässig und für die Abwicklung von Vertragsverhältnissen mit Ihnen erforderlich ist (Art. 6 Abs. 1 S. 1 lit. b DSGVO)."])}
<h2 id="cookies">4. Cookies</h2>
<p>Unsere Website verwendet Cookies. Hierbei handelt es sich um kleine Dateien, die Ihr Browser automatisch erstellt und die auf Ihrem Endgerät gespeichert werden. Cookies richten auf Ihrem Endgerät keinen Schaden an und enthalten keine Viren.</p>
<p>Die in Cookies gespeicherten Informationen dienen dazu, die Nutzung unseres Angebots für Sie angenehmer zu gestalten (z. B. zur Sitzungssteuerung oder für die Sprachauswahl). Die Rechtsgrundlage für die Verarbeitung personenbezogener Daten unter Verwendung von Cookies ist Art. 6 Abs. 1 lit. f DSGVO.</p>
<p>Sie können Ihre Cookie-Einstellungen im Browser jederzeit selbst anpassen und die Nutzung von Cookies einschränken oder verhindern.</p>
<h2 id="rechte">5. Ihre Rechte als betroffene Person</h2>
<p>Sie haben das Recht:</p>
{ul(["gemäß Art. 15 DSGVO Auskunft über Ihre bei uns gespeicherten personenbezogenen Daten zu verlangen,", "gemäß Art. 16 DSGVO die Berichtigung unrichtiger oder Vervollständigung Ihrer bei uns gespeicherten personenbezogenen Daten zu verlangen,", "gemäß Art. 17 DSGVO die Löschung Ihrer bei uns gespeicherten personenbezogenen Daten zu verlangen,", "gemäß Art. 18 DSGVO die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen,", "gemäß Art. 20 DSGVO Ihre personenbezogenen Daten in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten oder die Übermittlung an einen anderen Verantwortlichen zu verlangen,", "gemäß Art. 77 DSGVO sich bei einer Aufsichtsbehörde zu beschweren."])}
<h2 id="widerspruch">6. Widerspruchsrecht</h2>
<p>Sofern Ihre personenbezogenen Daten auf Grundlage von berechtigten Interessen gemäß Art. 6 Abs. 1 lit. f DSGVO verarbeitet werden, haben Sie das Recht, gemäß Art. 21 DSGVO Widerspruch gegen die Verarbeitung einzulegen.</p>
<h2 id="sicherheit">7. Datensicherheit</h2>
<p>Wir verwenden innerhalb des Website-Besuchs das verbreitete SSL-Verfahren (Secure Socket Layer) in Verbindung mit der jeweils höchsten Verschlüsselungsstufe, die von Ihrem Browser unterstützt wird. Außerdem setzen wir geeignete technische und organisatorische Sicherheitsmaßnahmen ein, um Ihre Daten gegen zufällige oder vorsätzliche Manipulationen, teilweisen oder vollständigen Verlust, Zerstörung oder gegen den unbefugten Zugriff Dritter zu schützen.</p>
<h2 id="aktualitaet">8. Aktualität und Änderung dieser Datenschutzerklärung</h2>
<p>Diese Datenschutzerklärung ist aktuell gültig und hat den Stand Juni 2025. Durch die Weiterentwicklung unserer Website und Angebote oder aufgrund geänderter gesetzlicher beziehungsweise behördlicher Vorgaben kann es notwendig werden, diese Datenschutzerklärung zu ändern.</p>
<p>Die jeweils aktuelle Datenschutzerklärung finden Sie jederzeit auf unserer Website.</p>
"""
    legal("datenschutz.html", "datenschutz", "Datenschutzerklärung", "Rechtliches", body, toc)


def build_home():
    h = head("Blaum Dienstleistungen | Gebäudereinigung Köln",
             "Gebäudereinigung in Köln & Umgebung: Unterhaltsreinigung, Praxisreinigung, Glasreinigung, Treppenhausreinigung, Baureinigung, Grundreinigung, AirBnB-Service und Hausmeisterservice.")
    h = h.replace('<link rel="icon"', '<link rel="preload" as="image" href="assets/hero-poster.webp" fetchpriority="high">\n<link rel="icon"')
    html = h + header("start") + "\n<main>\n" + HOME_MAIN + "\n</main>\n" + footer()
    write("index", html)


if __name__ == "__main__":
    build_home()
    build_overview()
    for slug, *_ in SERVICES:
        build_service(slug)
    build_about()
    build_contact()
    build_impressum()
    build_datenschutz()
