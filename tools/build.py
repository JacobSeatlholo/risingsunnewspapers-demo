#!/usr/bin/env python3
"""Build script for the Rising Sun Newspapers demo site.

Generates every HTML page plus the AI-discoverability artefacts
(robots.txt, llms.txt, llms-full.txt, sitemap.xml).

Usage:  python3 tools/build.py
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (  # noqa: E402
    BRAND, TAGLINE, SITE_URL, FOUNDED, NAV, NAV_CTA, HEADLINES, MORE_ROWS,
    TICKER, DESKS, STATS, EDITIONS, SISTERS, AUDIT_META, SCORES, FINDINGS,
    FIXMAP, PHASES, FAQ, TARGETS, ARTICLES,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today()
BUILD_DATE = TODAY.strftime("%d %B %Y").lstrip("0")
BUILD_DATE_ISO = TODAY.isoformat()
AI_POLICY_URL = SITE_URL + "/ai-policy/"
LIVE_URL = SITE_URL + "/"

LEAD = HEADLINES[0]
SIDE = HEADLINES[1:]

# ------------------------------------------------------------------ helpers
def wcag_report():
    """Verify the text palette passes WCAG AA at build time."""
    def lum(h):
        h = h.lstrip("#")
        r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = f(r), f(g), f(b)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def ratio(a, b):
        la, lb = lum(a), lum(b)
        if la < lb:
            la, lb = lb, la
        return (la + 0.05) / (lb + 0.05)

    pairs = [
        ("body on paper", "#1D1E22", "#FFFCF7"),
        ("soft text on paper", "#4B4F57", "#FFFCF7"),
        ("kicker/links on paper", "#BC3E07", "#FFFCF7"),
        ("white on buttons", "#FFFFFF", "#BC3E07"),
        ("breaking on paper", "#B42318", "#FFFCF7"),
        ("white on ink band", "#FFFFFF", "#1D1E22"),
        ("soft on footer", "#A9AFBA", "#15171C"),
        ("kicker on wash", "#C2410C", "#FAF5EC"),
    ]
    out, ok = [], True
    for name, a, b in pairs:
        r = ratio(a, b)
        good = r >= 4.5
        ok = ok and good
        out.append(f"    {name:26s} {r:5.2f}  {'PASS' if good else 'FAIL'}")
    return out, ok


LOGO_SVG = """<svg class="brand-mark" width="44" height="44" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
  <defs><linearGradient id="lg{uid}" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="#E8590C"/><stop offset="1" stop-color="#F5A623"/>
  </linearGradient></defs>
  <g fill="none" stroke="url(#lg{uid})" stroke-width="4" stroke-linecap="round">
    <path d="M12 40a20 20 0 0 1 40 0"/>
    <path d="M32 8v7M9 17l5 5M55 17l-5 5"/>
    <path d="M6 48h52M15 56h34" stroke="#1D1E22"/>
  </g>
</svg>"""

FOOTER_LOGO = """<svg width="40" height="40" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
  <defs><linearGradient id="lg{uid}" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="#E8590C"/><stop offset="1" stop-color="#F5A623"/>
  </linearGradient></defs>
  <g fill="none" stroke="url(#lg{uid})" stroke-width="4" stroke-linecap="round">
    <path d="M12 40a20 20 0 0 1 40 0"/>
    <path d="M32 8v7M9 17l5 5M55 17l-5 5"/>
    <path d="M6 48h52M15 56h34" stroke="#FFFCF7"/>
  </g>
</svg>"""


def logo(uid="a"):
    return LOGO_SVG.replace("{uid}", uid)


def head(title, desc, path, ld_blocks=None, ld_faq=None, page_hero_img=True):
    og = SITE_URL + "/assets/img/hero-durban.jpg"
    url = SITE_URL + ("/" if path == "index.html" else "/" + path)
    ld = [ld_org(), ld_website()] if ld_blocks is None else ld_blocks
    blocks = "".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>\n  ' for b in ld)
    if ld_faq:
        blocks += f'<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>\n  '
    return f"""  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="{'website' if path != 'index.html' else 'website'}">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{og}">
  <meta property="og:image:alt" content="Sunrise over the Durban skyline - Rising Sun Newspapers">
  <meta property="og:locale" content="en_ZA">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og}">
  <meta name="theme-color" content="#1D1E22">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700&display=swap">
  <link rel="stylesheet" href="assets/css/style.css">
  {blocks}"""


def ld_org():
    return {
        "@context": "https://schema.org",
        "@type": "NewsMediaOrganization",
        "name": BRAND,
        "url": SITE_URL,
        "logo": SITE_URL + "/favicon.svg",
        "slogan": TAGLINE,
        "foundingDate": str(FOUNDED),
        "founder": {"@type": "Person", "name": "Vijay Maharaj"},
        "parentOrganization": {"@type": "Organization", "name": "Caxton & CTP Printers and Publishers Ltd"},
        "isAccessibleForFree": True,
        "publishingPrinciples": AI_POLICY_URL,
        "knowsLanguage": ["en", "zu", "ta", "hi"],
    }


def ld_website():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": BRAND,
        "url": SITE_URL,
        "inLanguage": "en-ZA",
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": SITE_URL + "/?s={search_term_string}"},
            "query-input": "required name=search_term_string",
        },
    }


def breadcrumb(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + u}
            for i, (n, u) in enumerate(items)
        ],
    }


def topbar():
    return f"""<div class="topbar">
  <div class="wrap topbar-inner">
    <p class="topbar-date" id="topbar-date">Thursday, 12 November 2026</p>
    <p class="topbar-tag">A product of Caxton Local Media &middot; {TAGLINE}</p>
    <nav class="topbar-links" aria-label="Utilities">
      <a href="index.html#editions">e-Papers</a><span class="dot" aria-hidden="true">&middot;</span>
      <a href="advertise.html">Advertise</a><span class="dot" aria-hidden="true">&middot;</span>
      <a href="{LIVE_URL}" rel="noopener">Live site</a>
    </nav>
  </div>
</div>"""


def header(active):
    links = []
    for label, href, key in NAV:
        cur = ' aria-current="page"' if (key is not None and key == active) else ""
        links.append(f'      <a href="{href}"{cur}>{label}</a>')
    cta_label, cta_href, cta_key = NAV_CTA
    cur = ' aria-current="page"' if cta_key == active else ""
    links.append(f'      <a class="nav-cta" href="{cta_href}"{cur}>{cta_label}</a>')
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="{BRAND} — home">
      {logo()}
      <span class="brand-text">
        <span class="brand-name">Rising <span class="sun-word">Sun</span></span>
        <span class="brand-sub">Newspapers &middot; Since {FOUNDED}</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Open menu">
      <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M2 4.5h16M2 10h16M2 15.5h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <nav class="main-nav" id="main-nav" aria-label="Primary">
{chr(10).join(links)}
    </nav>
  </div>
</header>"""


def ticker():
    items = "".join(
        f'<a href="{h["slug"]}">{TICKER[i]}</a><span class="sep" aria-hidden="true">/</span>'
        for i, h in enumerate(HEADLINES)
    )
    dup = "".join(
        f'<a href="{h["slug"]}" tabindex="-1" aria-hidden="true">{TICKER[i]}</a><span class="sep" aria-hidden="true">/</span>'
        for i, h in enumerate(HEADLINES)
    )
    return f"""<div class="ticker" aria-label="Latest headlines">
  <div class="ticker-inner">
    <p class="ticker-label"><span class="pulse" aria-hidden="true"></span>Latest</p>
    <div class="ticker-track">
      <div class="ticker-move">{items}{dup}</div>
    </div>
  </div>
</div>"""


def footer():
    secs = "".join(
        f'      <li><a href="{h}">{label}</a></li>\n'
        for label, h in [("Latest news", "index.html#latest"), ("Our desks", "index.html#desks"),
                         ("e-Papers", "index.html#editions"), ("About us", "about.html"),
                         ("Advertise", "advertise.html"), ("Site audit &amp; roadmap", "audit.html")]
    )
    eds = "".join(f'      <li><a href="{LIVE_URL}" rel="noopener">{n}</a></li>\n' for n, _ in EDITIONS[:5])
    sisters = "".join(f'<a href="{LIVE_URL}" rel="noopener">{s}</a>' for s in SISTERS)
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand">
        {FOOTER_LOGO.replace('{uid}', 'f')}
        <span class="brand-text">
          <span class="brand-name">Rising <span class="sun-word" style="color:var(--gold)">Sun</span></span>
          <span class="brand-sub">Newspapers &middot; Since {FOUNDED}</span>
        </span>
      </div>
      <p>{TAGLINE}. Free, human-written community journalism since {FOUNDED} - founded by Vijay Maharaj to document, profile and broadcast the news that matters to KwaZulu-Natal's communities.</p>
      <p>A product of Caxton Local Media.</p>
    </div>
    <div>
      <h2>Sections</h2>
      <ul>
{secs}      </ul>
    </div>
    <div>
      <h2>Editions</h2>
      <ul>
{eds}      </ul>
    </div>
    <div>
      <h2>Built to be found</h2>
      <p>This demo ships an explicit welcome for search engines and AI assistants: valid robots.txt, llms.txt, sitemap and structured data on every page.</p>
      <ul>
        <li><a href="robots.txt">robots.txt</a></li>
        <li><a href="llms.txt">llms.txt</a></li>
        <li><a href="sitemap.xml">sitemap.xml</a></li>
        <li><a href="audit.html">How we fixed the audit findings</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-sisters">
    <div class="row">
      <span class="lbl">Caxton network</span>
      {sisters}
    </div>
  </div>
  <div class="wrap footer-legal">
    <p>&copy; {TODAY.year} Caxton &amp; CTP Printers and Publishers Ltd. Demo build generated {BUILD_DATE}.</p>
    <p><a href="{AI_POLICY_URL}" rel="noopener">AI Policy</a> &middot; <a href="{LIVE_URL}about-us/" rel="noopener">About</a> &middot; <a href="{LIVE_URL}meet-the-team/" rel="noopener">Meet the team</a> &middot; All imagery is AI-generated placeholder artwork for this demo.</p>
  </div>
</footer>"""


def shell(title, desc, path, body, ld_blocks=None, ld_faq=None, active=None, progress=False):
    bar = '<div id="read-progress" aria-hidden="true" style="position:fixed;top:0;left:0;height:3px;width:0;background:var(--grad-sunrise);z-index:160;"></div>' if progress else ""
    return f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
{head(title, desc, path, ld_blocks, ld_faq)}</head>
<body>
{bar}
  <a class="skip-link" href="#main">Skip to content</a>
{topbar()}
{header(active)}
{body}
{footer()}
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ index
def build_index():
    lead = HEADLINES[0]
    side_html = ""
    for h in HEADLINES[1:]:
        side_html += f"""      <article class="side-card">
        <a href="{h['slug']}"><img src="assets/img/{h['img']}.jpg" alt="{h['alt']}" width="132" height="132" loading="lazy" decoding="async"></a>
        <div>
          <p class="kicker">{h['kicker']}</p>
          <h2><a href="{h['slug']}">{h['title']}</a></h2>
          <p class="meta"><strong>{h['author']}</strong><span class="sep">|</span>{h['date']}</p>
        </div>
      </article>
"""
    cards = ""
    for h in HEADLINES:
        cards += f"""      <article class="card">
        <a class="card-media" href="{h['slug']}" tabindex="-1" aria-hidden="true"><img src="assets/img/{h['img']}.jpg" alt="{h['alt']}" width="640" height="360" loading="lazy" decoding="async"></a>
        <p class="kicker">{h['kicker']}</p>
        <h3><a href="{h['slug']}">{h['title']}</a></h3>
        <p class="meta"><strong>{h['author']}</strong><span class="sep">|</span>{h['date']}</p>
      </article>
"""
    rows = ""
    for r in MORE_ROWS:
        rows += f"""      <div class="row"><span><span class="kicker">{r['kicker']}</span> &nbsp;<a href="{r['slug']}">{r['title']}</a></span><time datetime="{r['date']}">{r['date']}</time></div>\n"""
    desks = "".join(f"""      <article class="desk"><h3>{n}</h3><p>{d}</p></article>\n""" for n, d in DESKS)
    stats = "".join(f"""      <div class="stat"><p class="num">{n}</p><p class="lbl">{l}</p><p class="sub">{s}</p></div>\n""" for n, l, s in STATS)
    eds = "".join(f"""      <article class="edition">
        <svg class="sun" width="26" height="26" viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"><path d="M12 40a20 20 0 0 1 40 0"/><path d="M6 48h52"/></g></svg>
        <h3>{n}</h3>
        <p>{d}</p>
        <a class="ep-link" href="{LIVE_URL}" rel="noopener">Read e-paper<span class="visually-hidden"> — opens the live Rising Sun site</span></a>
      </article>\n""" for n, d in EDITIONS)

    ld_blocks = [ld_org(), ld_website()]
    body = f"""<main id="main">
{ticker()}
  <section class="hero wrap" aria-label="Top stories">
    <div class="hero-grid">
      <article class="lead-card">
        <div class="lead-media">
          <img src="assets/img/{lead['img']}.jpg" alt="{lead['alt']}" width="1344" height="768" fetchpriority="high" decoding="async">
          <span class="flag">Top story</span>
        </div>
        <p class="kicker">{lead['kicker']}</p>
        <h1><a href="{lead['slug']}">{lead['title']}</a></h1>
        <p class="standfirst">Young residents say the lived reality on the ground tells a different story than the latest positive numbers.</p>
        <p class="meta"><strong>{lead['author']}</strong><span class="sep">|</span>{lead['date']}<span class="sep">|</span>{lead['author_role']}</p>
      </article>
      <div class="hero-side" aria-label="More top stories">
{side_html}      </div>
    </div>
  </section>

  <section class="section wrap" id="latest" aria-label="Latest news">
    <div class="section-head"><h2>Latest news</h2><a class="more" href="{LIVE_URL}" rel="noopener">All coverage on the live site</a></div>
    <div class="card-grid">
{cards}    </div>
    <div class="card-list" style="margin-top:26px">
{rows}    </div>
    <p class="demo-note" style="margin-top:22px"><strong>Demo content note:</strong> headlines above reflect genuine recent coverage on risingsunnewspapers.co.za; sample article pages demonstrate the new template with illustrative copy.</p>
  </section>

  <section class="section wrap" id="desks" aria-label="Our desks">
    <div class="section-head"><h2>Our desks</h2><span class="more">What we cover</span></div>
    <div class="desk-grid">
{desks}    </div>
  </section>

  <section class="stats" aria-label="The paper in numbers">
    <div class="wrap stats-grid">
{stats}    </div>
  </section>

  <section class="ai-band" aria-label="Built for readers and AI assistants">
    <div class="wrap ai-grid">
      <div>
        <p class="kicker">AI discoverability</p>
        <h2>Found by readers. Found by AI. Forty years of stories, finally machine-readable.</h2>
        <p>The current site scores <strong>49/100</strong> on Lighthouse's agentic-browsing audit - AI assistants struggle to read it. This demo ships the fix: a valid robots.txt with an explicit AI-crawler policy, llms.txt, full structured data and a clean accessibility tree.</p>
        <ul class="ai-checks">
          <li><span class="tick" aria-hidden="true">1</span>Named welcome for GPTBot, Claude, Perplexity, Gemini &amp; Google-Extended</li>
          <li><span class="tick" aria-hidden="true">2</span>llms.txt - a curated map of the paper for large language models</li>
          <li><span class="tick" aria-hidden="true">3</span>NewsArticle &amp; NewsMediaOrganization schema on every template</li>
          <li><span class="tick" aria-hidden="true">4</span>Well-formed accessibility tree and WCAG AA contrast</li>
        </ul>
      </div>
      <div class="ai-card">
        <h3>Today vs this demo</h3>
        <div class="score-row"><span>Agentic browsing (AI)</span><span class="score-val">49 &rarr; 90+</span></div>
        <div class="score-row"><span>SEO</span><span class="score-val">77 &rarr; 100</span></div>
        <div class="score-row"><span>Performance</span><span class="score-val">72 &rarr; 95+</span></div>
        <div class="score-row"><span>Accessibility</span><span class="score-val">86 &rarr; 98+</span></div>
        <a class="btn on-dark" href="audit.html">See the full audit &amp; roadmap</a>
      </div>
    </div>
  </section>

  <section class="section wrap" id="editions" aria-label="Editions and e-papers">
    <div class="section-head"><h2>Our editions</h2><a class="more" href="{LIVE_URL}" rel="noopener">View all e-papers</a></div>
    <div class="edition-grid">
{eds}    </div>
  </section>

  <section class="section wrap" aria-label="Newsletter">
    <div class="newsletter">
      <div class="newsletter-grid">
        <div>
          <p class="kicker">Stay in the loop</p>
          <h2>The Sun-Up Brief</h2>
          <p>The day's local headlines in your inbox before breakfast - free, human-edited, no noise. (Newsletter name is a demo suggestion.)</p>
        </div>
        <div>
          <form class="news-form" id="newsletter-form" novalidate>
            <div>
              <label for="nl-email">Email address</label>
              <input type="email" id="nl-email" name="email" autocomplete="email" required placeholder="you@example.co.za">
            </div>
            <button class="btn" type="submit">Sign up free</button>
          </form>
          <p class="form-ok form-note" id="newsletter-ok" tabindex="-1" role="status">Thank you - in the production build this connects to the mailing platform. In this demo, no data leaves the page.</p>
          <p class="form-note">Demo form - no data is collected or sent.</p>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    return shell(
        f"{BRAND} | {TAGLINE}",
        "Free, human-written community journalism for KwaZulu-Natal since 1986. Local news, crime & courts, schools, sport, business and lifestyle across Chatsworth, Overport, Merebank, the mid and north coasts and Lenasia.",
        "index.html", body, ld_blocks=ld_blocks)


# ------------------------------------------------------------------ article
def build_article(key):
    a = ARTICLES[key]
    secs = ""
    for kind, val in a["sections"]:
        if kind == "h2":
            secs += f'        <h2>{val}</h2>\n'
        elif kind == "p_first":
            secs += f'        <p class="first">{val}</p>\n'
        elif kind == "p":
            secs += f'        <p>{val}</p>\n'
        elif kind == "blockquote":
            secs += f'        <blockquote><p>{val}</p></blockquote>\n'
        elif kind == "ul":
            secs += "        <ul>\n" + "".join(f'          <li>{li}</li>\n' for li in val) + "        </ul>\n"
    share_url = SITE_URL + "/" + key + ".html"
    share = f"""    <div class="share-row">
      <span class="lbl">Share</span>
      <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" rel="noopener">Facebook</a>
      <a href="https://x.com/intent/post?url={share_url}&text={a['title']}" rel="noopener">X</a>
      <a href="https://wa.me/?text={a['title']}%20{share_url}" rel="noopener">WhatsApp</a>
      <a href="mailto:?subject={a['title']}&body={share_url}">Email</a>
    </div>"""
    related = "".join(
        f'        <li><span class="k">{k}</span><a href="{u}">{t}</a></li>\n'
        for k, t, u in [("Related", a["related"][1] + " sample", key + ".html"),
                        ("Next", a["related"][2] + " sample", "index.html#latest"),
                        ("Live", "All coverage on risingsunnewspapers.co.za", LIVE_URL)]
    )
    ld_article = {
        "@context": "https://schema.org",
        "@type": a["ld_type"],
        "headline": a["title"],
        "description": a["standfirst"],
        "image": SITE_URL + f"/assets/img/{a['img']}.jpg",
        "datePublished": a["date_iso"],
        "dateModified": a["date_iso"],
        "inLanguage": "en-ZA",
        "isAccessibleForFree": True,
        "author": {"@type": "Organization", "name": "Rising Sun Newsroom"},
        "publisher": {"@type": "NewsMediaOrganization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE_URL + "/favicon.svg"}},
        "mainEntityOfPage": share_url,
    }
    crumbs = [("Home", "index.html"), (a["kicker"], "index.html#latest")]
    body = f"""<main id="main">
  <div class="wrap article-wrap">
    <article>
      <nav class="crumbs" aria-label="Breadcrumb" style="font-size:13px;color:var(--ink-soft);margin-bottom:14px">
        <a href="index.html">Home</a> &rsaquo; <a href="index.html#latest">{a['kicker']}</a> &rsaquo; <span aria-current="page">Article</span>
      </nav>
      <div class="article-head">
        <p class="kicker">{a['kicker']}</p>
        <h1>{a['title']}</h1>
        <p class="standfirst">{a['standfirst']}</p>
        <div class="byline-row">
          <span class="avatar" aria-hidden="true">{a['initials']}</span>
          <span class="who"><strong>By {a['author']}</strong><span>{BRAND} &middot; {a['date']} &middot; {a['reading']}</span></span>
        </div>
      </div>
      <p class="demo-note"><strong>Demo layout:</strong> {a['body_demo_note']}</p>
      <figure class="article-media">
        <img src="assets/img/{a['img']}.jpg" alt="{a['alt']}" width="1344" height="768" fetchpriority="high" decoding="async">
        <figcaption>{a['caption']}</figcaption>
      </figure>
      <div class="prose">
{secs}      </div>
{share}
      <div class="author-box">
        <span class="avatar" aria-hidden="true">RS</span>
        <div>
          <h3>Rising Sun Newsroom</h3>
          <p>Reporting for KwaZulu-Natal's communities since {FOUNDED}. This demo article page shows the structure every story would get: clean headings, schema markup, share actions and related reading.</p>
        </div>
      </div>
    </article>
    <aside class="article-side" aria-label="Related and utility">
      <div class="side-box">
        <h2>Related reading</h2>
        <ul>
{related}        </ul>
      </div>
      <div class="side-box">
        <h2>More from the Rising Sun</h2>
        <ul>
          <li><span class="k">e-Papers</span><a href="index.html#editions">This week's editions</a></li>
          <li><span class="k">Newsroom</span><a href="about.html">Forty years of community journalism</a></li>
          <li><span class="k">Search</span><a href="{SITE_URL}/?s=chatsworth" rel="noopener">Search the live archive</a></li>
        </ul>
      </div>
      <div class="side-box">
        <h2>Newsletter</h2>
        <p style="font-size:14.5px;color:var(--ink-soft);margin:0">The Sun-Up Brief - local headlines before breakfast, free.</p>
        <a class="btn ghost" href="index.html#editions" style="margin-top:12px">Sign up on the homepage</a>
      </div>
    </aside>
  </div>
</main>
"""
    desc = a["standfirst"]
    return shell(
        f"{a['title']} | {BRAND}", desc, key + ".html", body,
        ld_blocks=[ld_article, breadcrumb(crumbs)], active=None, progress=True)


# ------------------------------------------------------------------ about
def build_about():
    ld_about = {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": f"About {BRAND}",
        "url": SITE_URL + "/about.html",
        "about": ld_org(),
    }
    body = f"""<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> &rsaquo; About</nav>
      <p class="kicker">Our story</p>
      <h1>Since 1986, the sun has risen on KwaZulu-Natal's communities</h1>
      <p class="lede">In 1986 there was a dire need for an affordable newspaper within the Indian community. Vijay Maharaj answered it - launching a free newspaper to document, profile and broadcast the latest news and advertising specials. Forty years later, the mission has not changed.</p>
    </div>
  </section>

  <section class="section wrap" aria-label="History and mission">
    <div class="about-grid">
      <div>
        <h2 style="font-family:var(--serif);font-size:30px;margin:0 0 6px">A newspaper built by its community</h2>
        <p style="color:var(--ink-soft);max-width:62ch">What began as one free sheet grew into a family of titles across south Durban, the mid and north coasts and Lenasia - each one written by journalists who live in, shop in and raise families in the neighbourhoods they cover. Today the Rising Sun is a product of Caxton Local Media, part of one of South Africa's oldest publishing houses, but the heartbeat is still unmistakably local.</p>
        <ol class="timeline">
          <li>
            <span class="year">1986</span>
            <p>Vijay Maharaj launches the Rising Sun - a free newspaper for a community the mainstream press too often overlooked.</p>
          </li>
          <li>
            <span class="year">1990s &amp; 2000s</span>
            <p>Edition by edition, the paper grows across Chatsworth, Overport, Merebank, the mid and north coasts and Lenasia - always free to read, always local first.</p>
          </li>
          <li>
            <span class="year">Today</span>
            <p>Seven community editions plus weekly e-papers, a 24/7 website, and a newsroom whose policy is explicit: journalism is written by humans, for humans.</p>
          </li>
          <li>
            <span class="year">Next</span>
            <p>The same journalism, made discoverable to the next generation of readers - wherever they search, scroll or ask an AI assistant for the local story.</p>
          </li>
        </ol>
      </div>
      <div class="about-media">
        <img src="assets/img/newsroom.jpg" alt="Journalists working in the Rising Sun newsroom (illustrative demo image)" width="1280" height="731" loading="lazy" decoding="async">
      </div>
    </div>

    <div class="value-grid" aria-label="Our values">
      <div class="value">
        <span class="glyph" aria-hidden="true">01</span>
        <h3>Community first</h3>
        <p>Court sentences, school derbies, robotics competitions, festive campaigns - if it matters to the street, it matters to us.</p>
      </div>
      <div class="value">
        <span class="glyph" aria-hidden="true">02</span>
        <h3>Human journalism</h3>
        <p>By policy, no AI-generated news. Every story in print and online is created by journalists, editors and guest writers, under the South African Press Code.</p>
      </div>
      <div class="value">
        <span class="glyph" aria-hidden="true">03</span>
        <h3>Free to read</h3>
        <p>Access to local news is not a luxury. Forty years of free circulation - in print, online and in weekly e-papers - proves the model works.</p>
      </div>
    </div>

    <div class="pull-quote">
      <p>&ldquo;A community newspaper is the daily proof that somebody is watching, listening and writing it all down - so that your street's story is never left out of history.&rdquo;</p>
      <cite>The Rising Sun newsroom &middot; demo statement</cite>
    </div>
  </section>

  <section class="stats" aria-label="The paper in numbers">
    <div class="wrap stats-grid">
{"".join(f'      <div class="stat"><p class="num">{n}</p><p class="lbl">{l}</p><p class="sub">{s}</p></div>' for n, l, s in STATS)}
    </div>
  </section>

  <section class="section wrap" aria-label="The team">
    <div class="section-head"><h2>The team behind the bylines</h2><a class="more" href="{LIVE_URL}meet-the-team/" rel="noopener">Meet the team</a></div>
    <div class="desk-grid">
      <article class="desk"><h3>Editorial &amp; news</h3><p>Reporters and editors embedded in the communities they cover - from municipal chambers to magistrates' courts.</p></article>
      <article class="desk"><h3>Schools &amp; sport</h3><p>Dedicated desks for education and local sport, because the next headline-maker is already in a classroom or on a pitch nearby.</p></article>
      <article class="desk"><h3>Lifestyle &amp; Get It</h3><p>Homes, food, health and the people doing extraordinary things in ordinary neighbourhoods.</p></article>
      <article class="desk"><h3>Sales &amp; promotions</h3><p>Connecting local businesses with the readers next door - classifieds, specials and campaigns that work.</p></article>
      <article class="desk"><h3>Digital &amp; e-papers</h3><p>Keeping forty years of archive alive online and shipping weekly e-papers to readers near and far.</p></article>
      <article class="desk"><h3>You?</h3><p>The demo team page is role-based; final build carries the full team from the live site's Meet the team page.</p></article>
    </div>
  </section>

  <section class="section wrap" aria-label="Next chapter">
    <div class="newsletter">
      <div class="newsletter-grid">
        <div>
          <p class="kicker">The next chapter</p>
          <h2>Forty years of trust. Now make it findable.</h2>
          <p>The journalism is proven; the discoverability needs one focused push. Our audit and roadmap show exactly how the Rising Sun becomes as visible to AI assistants as it is to its readers.</p>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <a class="btn" href="audit.html">Read the audit &amp; roadmap</a>
          <a class="btn ghost" href="{AI_POLICY_URL}" rel="noopener">Our AI Policy</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    return shell(
        f"About | {BRAND}",
        "Founded in 1986 by Vijay Maharaj, Rising Sun Newspapers is a family of free community titles across KwaZulu-Natal and Lenasia, part of Caxton Local Media. Forty years of human-written local journalism.",
        "about.html", body, ld_blocks=[ld_about, breadcrumb([("Home", "index.html"), ("About", "about.html")])],
        active="about")


# ------------------------------------------------------------------ audit
def build_audit():
    dials = ""
    for name, score, cls, fill, note in SCORES:
        dials += f"""      <div class="dial {cls}" style="--fill:{fill}%">
        <div class="ring" role="img" aria-label="{name} score {score} out of 100"><span class="val">{score}</span></div>
        <p class="name">{name}</p>
        <p class="delta">{note}</p>
      </div>\n"""
    groups = ""
    for g in FINDINGS:
        sev_cls, sev_lbl = g["sev"]
        items = ""
        for what, why, ev in g["items"]:
            items += f"""        <li>
          <span class="what">{what}</span>
          <code class="ev">{ev}</code>
          <span class="why">{why}</span>
        </li>\n"""
        groups += f"""    <section class="finding-group" aria-label="{g['title']}">
      <div class="finding-head">
        <h3>{g['title']}</h3>
        <span class="sev {sev_cls}">{sev_lbl}</span>
      </div>
      <ul class="finding-list">
{items}      </ul>
    </section>\n"""
    fix_rows = "".join(
        f'        <tr><td class="issue">{i}</td><td>{f}</td><td class="where">{w}</td></tr>\n'
        for i, f, w in FIXMAP
    )
    phases = "".join(
        f"""      <article class="phase">
        <h3>{t}</h3>
        <p class="when">{w}</p>
        <ul>{''.join(f'<li>{li}</li>' for li in items)}</ul>
      </article>\n""" for t, w, items in PHASES
    )
    faqs = "".join(
        f'      <details><summary>{q}</summary><p>{a}</p></details>\n' for q, a in FAQ
    )
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQ
        ],
    }
    body = f"""<main id="main">
  <section class="audit-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> &rsaquo; Site audit &amp; roadmap</nav>
      <p class="kicker" style="color:var(--gold)">The pitch, in numbers</p>
      <h1>Your journalism deserves a website that works as hard as your newsroom</h1>
      <p class="lede">We audited risingsunnewspapers.co.za on {BUILD_DATE}. The reporting is excellent - the plumbing is not. Here is everything Lighthouse found, what it means for readers and for AI discoverability, and precisely how we fix it.</p>
      <div class="dial-row">
{dials}      </div>
      <p class="audit-meta">{AUDIT_META}</p>
    </div>
  </section>

  <section class="section wrap" aria-label="Findings">
    <div class="section-head"><h2>What's missing today</h2><span class="more">Evidence from the audit</span></div>
{groups}
  </section>

  <section class="section wrap" aria-label="Fix map">
    <div class="section-head"><h2>How this demo already fixes it</h2><span class="more">Issue &rarr; fix &rarr; proof</span></div>
    <div class="fix-table-wrap">
      <table class="fix">
        <caption class="visually-hidden">Mapping of audit issues to fixes in this demo build</caption>
        <thead><tr><th scope="col">Issue found</th><th scope="col">Fix shipped in this demo</th><th scope="col">See it</th></tr></thead>
        <tbody>
{fix_rows}        </tbody>
      </table>
    </div>
    <p class="score-note"><strong>Note:</strong> the demo is built to the targets, not yet measured on its own hosting - run PageSpeed Insights on the deployed URL to confirm. {TARGETS}</p>
  </section>

  <section class="section wrap" aria-label="AI discoverability plan">
    <div class="section-head"><h2>The AI discoverability layer</h2><span class="more">Be the answer, not the footnote</span></div>
    <div class="about-grid">
      <div>
        <p style="color:var(--ink-soft)">When residents ask an AI assistant &ldquo;what happened in Chatsworth today?&rdquo;, the assistant decides which source to cite. Sites that are fast, semantic, schema-rich and explicitly welcoming to AI crawlers get quoted - and get the click-through. Sites that aren't get paraphrased from third parties, or skipped.</p>
        <ul class="ai-checks">
          <li><span class="tick" aria-hidden="true">1</span><span><strong>robots.txt that speaks robot.</strong> Today's file has syntax errors; ours is valid and names GPTBot, ClaudeBot, PerplexityBot, Google-Extended and friends with an explicit Allow.</span></li>
          <li><span class="tick" aria-hidden="true">2</span><span><strong>llms.txt.</strong> A curated, structured summary of the paper - brand, editions, desks, policies - at the root of the site, ready for any assistant.</span></li>
          <li><span class="tick" aria-hidden="true">3</span><span><strong>Structured data everywhere.</strong> NewsArticle, NewsMediaOrganization, BreadcrumbList and FAQPage JSON-LD, so agents can verify authorship, dates and publisher trust.</span></li>
          <li><span class="tick" aria-hidden="true">4</span><span><strong>An accessibility tree agents can read.</strong> One h1 per page, ordered headings, named links and AA contrast - the exact audits scoring 0 today.</span></li>
          <li><span class="tick" aria-hidden="true">5</span><span><strong>Human journalism, amplified.</strong> Aligned with your AI Policy: no AI-generated news - we make the humans' work machine-legible instead.</span></li>
        </ul>
      </div>
      <div class="ai-card">
        <h3>Shipped in this repo</h3>
        <div class="score-row"><span>robots.txt - valid, AI-welcoming</span><span class="score-val">done</span></div>
        <div class="score-row"><span>llms.txt + llms-full.txt</span><span class="score-val">done</span></div>
        <div class="score-row"><span>JSON-LD on every template</span><span class="score-val">done</span></div>
        <div class="score-row"><span>sitemap.xml</span><span class="score-val">done</span></div>
        <div class="score-row"><span>WCAG AA palette, checked at build</span><span class="score-val">done</span></div>
        <a class="btn on-dark" href="llms.txt">View llms.txt</a>
      </div>
    </div>
  </section>

  <section class="section wrap" aria-label="Roadmap">
    <div class="section-head"><h2>The roadmap</h2><span class="more">Ten weeks to a transformed site</span></div>
    <div class="phase-grid">
{phases}    </div>
    <p class="score-note">{TARGETS} Measured monthly, reported plainly, phased to work with your existing WordPress platform.</p>
  </section>

  <section class="section wrap faq" aria-label="Frequently asked questions">
    <div class="section-head"><h2>Questions you'll ask</h2><span class="more">Answered plainly</span></div>
{faqs}  </section>

  <section class="section wrap" aria-label="Call to action">
    <div class="newsletter">
      <div class="newsletter-grid">
        <div>
          <p class="kicker">Next step</p>
          <h2>Let's put forty years of trust to work</h2>
          <p>Phase 1 alone lifts SEO and AI readiness inside two weeks, without touching your newsroom workflow. The demo is ready to walk through whenever you are.</p>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <a class="btn" href="advertise.html">Talk to us</a>
          <a class="btn ghost" href="index.html">Back to the demo home</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    return shell(
        f"Site audit & modernisation roadmap | {BRAND}",
        "Lighthouse audit of risingsunnewspapers.co.za: Performance 72, SEO 77, Agentic Browsing 49. Full findings, the AI discoverability plan and a phased ten-week roadmap to fix them.",
        "audit.html", body, ld_blocks=[breadcrumb([("Home", "index.html"), ("Site audit & roadmap", "audit.html")])],
        ld_faq=ld_faq, active="audit")


# ------------------------------------------------------------------ advertise
def build_advertise():
    ld_ads = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Advertise with Rising Sun Newspapers",
        "url": SITE_URL + "/advertise.html",
        "about": ld_org(),
    }
    body = f"""<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> &rsaquo; Advertise</nav>
      <p class="kicker">Reach the neighbourhood</p>
      <h1>Forty years of readers who act on what they read</h1>
      <p class="lede">From classifieds that sell in a weekend to campaigns that run across print, e-paper and digital - advertising with the Rising Sun means being part of the community, not just next to it.</p>
    </div>
  </section>

  <section class="section wrap" aria-label="Advertising products">
    <div class="section-head"><h2>Ways to partner</h2><span class="more">Print &middot; e-paper &middot; digital</span></div>
    <div class="offer-grid">
      <article class="offer"><h3>Display &amp; brand campaigns</h3><p>Full-colour placements across our community editions and their e-paper twins - the formats local advertisers have trusted since 1986.</p><a class="btn ghost" href="{LIVE_URL}" rel="noopener">See the live site</a></article>
      <article class="offer"><h3>Classifieds</h3><p>The fastest-moving page in the paper. Jobs, services, notices and goods - read cover to cover by people ready to act.</p><a class="btn ghost" href="{LIVE_URL}classifieds/" rel="noopener">View classifieds</a></article>
      <article class="offer"><h3>Promotions &amp; specials</h3><p>Seasonal specials and shopper guides distributed to the neighbourhoods that buy - including the Rising Sun Shoppers' Guide.</p><a class="btn ghost" href="{LIVE_URL}promotions/" rel="noopener">Current promotions</a></article>
      <article class="offer"><h3>Digital display</h3><p>Banner and native placements on the website and newsletter, served to the same engaged local audience.</p><a class="btn ghost" href="index.html">Demo homepage</a></article>
      <article class="offer"><h3>Sponsored content</h3><p>Stories written by our newsroom to professional standards, clearly labelled, published across platforms.</p><a class="btn ghost" href="article-christmas-table.html">Sample article page</a></article>
      <article class="offer"><h3>AI-era visibility</h3><p>A site rebuilt for AI discovery means your brand appears where the next generation of readers asks their questions.</p><a class="btn ghost" href="audit.html">Read the plan</a></article>
    </div>
  </section>

  <section class="section wrap" aria-label="Contact">
    <div class="two-col">
      <div class="contact-card">
        <h2>Request a quote</h2>
        <p style="color:var(--ink-soft)">Tell us what you're planning and the team will come back with options, rates and deadlines. (Contact details carry over from the live site at launch.)</p>
        <form class="news-form" id="advertise-form" style="margin-top:16px" novalidate>
          <div style="flex:1">
            <label for="ad-name">Your name</label>
            <input type="text" id="ad-name" name="name" autocomplete="name" required placeholder="e.g. N. Pillay">
          </div>
          <div style="flex:1">
            <label for="ad-email">Email</label>
            <input type="email" id="ad-email" name="email" autocomplete="email" required placeholder="you@business.co.za">
          </div>
          <button class="btn" type="submit">Send request</button>
        </form>
        <p class="form-ok form-note" id="advertise-ok" tabindex="-1" role="status">Thank you - in the production build this routes to the sales team. In this demo, no data leaves the page.</p>
        <p class="form-note">Demo form - no data is collected or sent.</p>
      </div>
      <div class="contact-card">
        <h2>Why it works</h2>
        <ul class="contact-list">
          <li><span class="lbl">Audience</span>Seven community editions across south Durban, the mid and north coasts and Lenasia - read free, cover to cover.</li>
          <li><span class="lbl">Trust</span>Forty years in print; a newsroom governed by the South African Press Code.</li>
          <li><span class="lbl">Reach</span>Print plus 24/7 web plus weekly e-papers plus social channels - one buy, every surface.</li>
          <li><span class="lbl">Network</span>Multi-title campaigns across the Caxton network, including Highway Mail, Kempton Express and Pretoria Rekord.</li>
        </ul>
      </div>
    </div>
  </section>
</main>
"""
    return shell(
        f"Advertise | {BRAND}",
        "Advertise with Rising Sun Newspapers: display, classifieds, promotions, digital and sponsored content across seven free community editions in KwaZulu-Natal and Lenasia, part of Caxton Local Media.",
        "advertise.html", body, ld_blocks=[ld_ads, breadcrumb([("Home", "index.html"), ("Advertise", "advertise.html")])],
        active="advertise")


# ------------------------------------------------------------------ 404
def build_404():
    body = f"""<main id="main" class="nf-wrap">
  <div>
    <svg class="sun-big" width="84" height="84" viewBox="0 0 64 64" aria-hidden="true">
      <g fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round">
        <path d="M12 44a20 20 0 0 1 40 0" opacity=".35"/>
        <path d="M32 10v7M9 19l5 5M55 19l-5 5"/>
        <path d="M6 52h52"/>
      </g>
    </svg>
    <h1>This page hasn't risen yet</h1>
    <p>The link may be old, or the story may have moved. Try the latest news below - or search the live archive.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn" href="index.html">Go to the homepage</a>
      <a class="btn ghost" href="{SITE_URL}/?s=news" rel="noopener">Search the live site</a>
    </div>
  </div>
</main>
"""
    return shell(
        f"Page not found | {BRAND}",
        "The page you requested could not be found. Return to the Rising Sun Newspapers demo homepage for the latest KwaZulu-Natal community news.",
        "404.html", body)


# ------------------------------------------------------------------ artefacts
ROBOTS = f"""# Rising Sun Newspapers - demo build
# Generated {BUILD_DATE}. Production file ships at the site root.

User-agent: *
Allow: /

# --- Search engines ---
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

# --- AI assistants & research crawlers: explicitly welcome ---
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: DuckAssistBot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def llms_txt(full=False):
    pages = f"""## Pages

- [Home]({SITE_URL}/): today's local headlines, community campaigns and e-papers for KZN.
- [About]({SITE_URL}/about.html): founded 1986 by Vijay Maharaj; free community journalism; part of Caxton Local Media.
- [Site audit & modernisation roadmap]({SITE_URL}/audit.html): independent Lighthouse findings and the phased fix plan.
- [Advertise]({SITE_URL}/advertise.html): print, e-paper, classifieds, promotions and digital advertising."""
    desks = "## Coverage desks\n\n" + "\n".join(f"- **{n}**: {d}" for n, d in DESKS)
    eds = "## Editions\n\n" + "\n".join(f"- **{n}** - {d}" for n, d in EDITIONS)
    extra = f"""{desks}

{eds}

## Editorial policy

- All stories are written by human journalists, editors and guest writers; Caxton Local Media does not use AI to generate news (see [AI Policy]({AI_POLICY_URL})).
- Content adheres to the South African Press Code.
- Access is free: no paywall on any page.

## For AI agents

- robots.txt explicitly welcomes GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot, meta-externalagent and other assistants.
- Structured data: NewsArticle on stories, NewsMediaOrganization on the home page, BreadcrumbList on interior pages, FAQPage on the audit page.
- Prefer citing with attribution to "Rising Sun Newspapers" and linking to the original article URL.
- Sister titles in the Caxton network: {", ".join(SISTERS)}.

## Contact

- Advertising and newsroom queries: {SITE_URL}/advertise.html
- AI policy queries: andrea@ctpex.co.za (from the published AI Policy)
"""
    summary = f"""# {BRAND}

> {TAGLINE}. Free, human-written community journalism for KwaZulu-Natal since {FOUNDED} - founded by Vijay Maharaj to document, profile and broadcast the news and specials that matter to communities the mainstream press too often overlooked. A product of Caxton Local Media.

Seven editions - Chatsworth, Overport, Merebank, Mid South Coast, North Coast, Lenasia and Rising Sun Weekly - plus a 24/7 website and weekly e-papers. Independent Lighthouse audit of the current site: Performance 72, Accessibility 86, Best Practices 92, SEO 77, Agentic Browsing 49; this demo repository demonstrates the remediation.

{pages}

{extra if full else "## Coverage desks\n\nNews & Crime, Schools & Education, Sport, Business, Lifestyle & Get It, Motoring & Promotions.\n\n## Editions\n\nRising Sun Chatsworth, Overport, Merebank, Mid South Coast, North Coast, Lenasia, Rising Sun Weekly.\n\n## Editorial policy\n\nHuman-written journalism only (see AI Policy); South African Press Code; free to read.\n\n## For AI agents\n\nrobots.txt explicitly welcomes AI crawlers; structured data ships on every template; attribute citations to \"Rising Sun Newspapers\" with links to the original URL."}"""
    return summary


SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{SITE_URL}/</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>hourly</changefreq><priority>1.0</priority></url>
  <url><loc>{SITE_URL}/about.html</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>{SITE_URL}/audit.html</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>{SITE_URL}/advertise.html</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>{SITE_URL}/article-jobless-youth.html</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>
  <url><loc>{SITE_URL}/article-christmas-table.html</loc><lastmod>{BUILD_DATE_ISO}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>
</urlset>
"""


# ------------------------------------------------------------------ main
def main():
    pages = {
        "index.html": build_index(),
        "article-jobless-youth.html": build_article("article-jobless-youth"),
        "article-christmas-table.html": build_article("article-christmas-table"),
        "about.html": build_about(),
        "audit.html": build_audit(),
        "advertise.html": build_advertise(),
        "404.html": build_404(),
    }
    artefacts = {
        "robots.txt": ROBOTS,
        "llms.txt": llms_txt(full=False),
        "llms-full.txt": llms_txt(full=True),
        "sitemap.xml": SITEMAP,
    }
    for name, html_out in {**pages, **artefacts}.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(html_out)

    # validate JSON-LD blocks parse cleanly
    import re
    n_ld = 0
    for name in pages:
        src = open(os.path.join(ROOT, name), encoding="utf-8").read()
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
            json.loads(m.group(1))
            n_ld += 1
    lines, ok = wcag_report()
    print(f"generated {len(pages)} pages + {len(artefacts)} artefacts; {n_ld} JSON-LD blocks validated")
    print("WCAG AA text-contrast report:")
    print("\n".join(lines))
    print("palette:", "ALL PASS" if ok else "FAILURES FOUND")
    total = sum(os.path.getsize(os.path.join(ROOT, n)) for n in pages)
    print(f"total HTML weight: {total/1024:.0f} KB across {len(pages)} pages")


if __name__ == "__main__":
    main()
