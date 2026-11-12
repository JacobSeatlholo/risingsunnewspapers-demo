# Fix map — audit issue → demo implementation

Every failing audit from the 12 November 2026 Lighthouse report, and where the fix
lives in this repository.

| # | Issue on the live site | Fix shipped in this demo | Where to verify |
| --- | --- | --- | --- |
| 1 | No meta description (`meta-description: FAIL`) | Unique 150–160 char description generated per page | View source on any page, `<meta name="description">` |
| 2 | robots.txt invalid — 2 errors (`robots-txt: FAIL`) | Valid robots.txt with explicit AI-crawler `Allow` blocks + Sitemap line | `robots.txt` (parse it with any validator) |
| 3 | No llms.txt (`llms-txt: not found`) | `llms.txt` + `llms-full.txt` summarising brand, editions, desks, policies, citation guidance | `llms.txt`, `llms-full.txt` |
| 4 | Accessibility tree not well-formed (`agent-accessibility-tree: 0`) | Semantic landmarks, one `h1` per page, ordered headings, named controls | `audit.html` + any a11y tree inspector |
| 5 | Heading order broken ("TOP STORIES" skips levels) | Strict h1→h2→h3 hierarchy in every template | View source headings outline |
| 6 | Colour contrast failures (`color-contrast: FAIL`) | AA-verified palette; ratios checked by the build script and printed at generation time | `python3 tools/build.py` output; `assets/css/style.css` |
| 7 | Images without alt (`image-alt: FAIL`) | Descriptive alt on every `<img>`, decorative art marked | Any page source |
| 8 | Links without discernible names (`link-name: FAIL`) | Text links with clear labels for network titles | `index.html` footer (Caxton network row) |
| 9 | Low-resolution favicon as nav icon (`image-size-responsive: FAIL`) | Crisp vector `favicon.svg` + manifest icons | `favicon.svg`, `manifest.webmanifest` |
| 10 | TTI 15.7 s, TBT 610 ms (score 6/100) | Zero-framework static HTML; ~5 KB dependency-free JS; no jQuery | `assets/js/main.js`; run Lighthouse on the deployed URL |
| 11 | DOM of 2,617 nodes at depth 22 | Lean semantic markup (roughly a quarter of the node count) | View source on `index.html` |
| 12 | Critical network chain 2,478 ms | Two font families, preconnected, `font-display: swap`; single CSS file; one deferred JS file | `assets/css/style.css`, `<head>` |
| 13 | Forced reflows + console errors | Clean console across the demo; single small script with no layout reads | Browser devtools on any page |
| 14 | Unsized logo image (CLS culprit) | Explicit `width`/`height` and aspect-ratio on every image | Any page source; `.lead-media img` CSS |
| 15 | No clickjacking headers (High severity) | X-Frame-Options / CSP snippet documented for hosting | `docs/AUDIT.md` (server snippet) |
| 16 | No structured data on pages | `NewsMediaOrganization` + `WebSite`+SearchAction (home), `NewsArticle` (articles), `BreadcrumbList` (interior), `FAQPage` (audit) | View source; validate at validator.schema.org |
| 17 | Third-party sprawl (Clicky, Lotame, onthe.io) | Zero third-party requests in this demo | Network tab of devtools |
| 18 | No agent manifests (WebMCP / ARD) | Documented as roadmap phase 3 (`audit.html`) | `audit.html` roadmap |

## What this deliberately does NOT do

- It does not fake scores. The demo is built *to* the targets; measure it on real
  hosting with PageSpeed Insights before quoting numbers to the client.
- It does not replace the newsroom's WordPress workflow. Phases 1–2 of the roadmap
  (`audit.html`) are designed to work inside the existing platform.
