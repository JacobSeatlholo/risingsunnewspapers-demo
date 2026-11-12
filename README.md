# Rising Sun Newspapers — demo site + AI discoverability showcase

A zero-dependency, static demo rebuild of **risingsunnewspapers.co.za**, generated for
**git@github.com:JacobSeatlholo/risingsunnewspapers-demo.git**.

It demonstrates two things at once:

1. **What the site could feel like** — a fast, accessible, modern front page, article
   template, about story and advertising offer, built around forty years of community
   journalism (founded 1986 by Vijay Maharaj, a product of Caxton Local Media).
2. **How the audit findings get fixed** — the current site scored Performance 72,
   Accessibility 86, Best Practices 92, SEO 77 and **Agentic Browsing 49** in the
   Lighthouse report dated 12 November 2026. Every failing audit is mapped to a fix
   that is *already shipped in this repository* — see `audit.html` and `docs/FIX-MAP.md`.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Demo homepage: hero, latest news, desks, stats, AI band, editions, newsletter |
| `article-jobless-youth.html` | Sample hard-news article template (headline from genuine coverage) |
| `article-christmas-table.html` | Sample community article template (headline from genuine coverage) |
| `about.html` | The 40-year story, values, team roles |
| `audit.html` | The full Lighthouse findings + fix map + AI discoverability layer + roadmap + FAQ |
| `advertise.html` | Advertising products and contact |
| `404.html` | Branded not-found page |

## AI discoverability artefacts (the point of the exercise)

| File | What it does |
| --- | --- |
| `robots.txt` | Valid syntax (the live site's file fails this audit) + explicit `Allow` for GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot/Claude-User/Claude-SearchBot, PerplexityBot/Perplexity-User, Google-Extended, Applebot(-Extended), meta-externalagent, DuckAssistBot + `Sitemap:` line |
| `llms.txt` | Curated site summary for large language models (brand, editions, desks, policies, citation guidance) |
| `llms-full.txt` | Extended version with per-page descriptions |
| `sitemap.xml` | Clean XML sitemap |
| JSON-LD on every page | `NewsMediaOrganization`, `WebSite` (+SearchAction), `NewsArticle`, `BreadcrumbList`, `FAQPage` |
| Semantic templates | One `h1` per page, ordered headings, alt text everywhere, named links, WCAG AA palette (ratios verified at build time by `tools/build.py`) |
| Performance posture | No framework, no jQuery, ~5 KB of dependency-free JS, explicit image dimensions, `font-display: swap`, two font families |

## Quick start

No build step. Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Regenerating pages

All HTML is generated from `tools/content.py` (data) + `tools/build.py` (templates):

```bash
python3 tools/build.py
```

Edit the data file (headlines, editions, findings, FAQ) and re-run — pages, robots.txt,
llms.txt, llms-full.txt and sitemap.xml regenerate together. The script also prints the
WCAG contrast verification for the palette.

## Deploying

### GitHub Pages (recommended for the demo)

1. Push this repository to `JacobSeatlholo/risingsunnewspapers-demo`.
2. Repository **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
3. Branch: `main`, folder: `/ (root)` → Save.
4. The site goes live at `https://jacobseatlholo.github.io/risingsunnewspapers-demo/`.
   All asset paths are relative, so it works from any base path.

Then run PageSpeed Insights / Lighthouse on the live URL — the demo is built to the
targets printed on `audit.html` (Performance 95+, Accessibility 98+, SEO 100,
Agentic Browsing 90+).

### Notes on the content

- Headlines and editions mirror genuine content on risingsunnewspapers.co.za
  (fetched 12 November 2026).
- Article bodies are illustrative demo copy and are labelled as such on the page.
- All imagery is AI-generated placeholder artwork; the production build would carry the
  newsroom's own photography.

## Repository layout

```
.
├── index.html                # generated
├── article-*.html            # generated
├── about.html                # generated
├── audit.html                # generated — the pitch page
├── advertise.html            # generated
├── 404.html                  # generated
├── robots.txt                # generated
├── llms.txt / llms-full.txt  # generated
├── sitemap.xml               # generated
├── manifest.webmanifest
├── favicon.svg
├── assets/css/style.css      # design system (hand-written)
├── assets/js/main.js         # progressive enhancement (hand-written)
├── assets/img/*.jpg          # optimised placeholder imagery
├── tools/content.py          # all content data
├── tools/build.py            # generator
└── docs/
    ├── AUDIT.md              # written audit (mirror of audit.html)
    └── FIX-MAP.md            # issue → fix → where to see it
```
