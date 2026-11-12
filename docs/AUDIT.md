# Rising Sun Newspapers — site audit summary

**Audited:** 12 November 2026 · risingsunnewspapers.co.za · Lighthouse 13.6.0 · mobile emulation
**Source:** client-supplied Lighthouse report (`agentic-browsing` category included).

## Scores

| Category | Score | Notes |
| --- | --- | --- |
| Performance | **72** | LCP 3.5 s · TBT 610 ms · TTI 15.7 s · Speed Index 4.2 s |
| Accessibility | **86** | Contrast, alt text, link names, heading order |
| Best Practices | **92** | Console errors, low-resolution icon |
| SEO | **77** | No meta description, invalid robots.txt |
| Agentic Browsing | **49** | AI-agent readiness — the newest and most urgent category |

## Findings (evidence-backed)

### 1. Discoverability — critical
- `meta-description`: FAIL — homepage has no meta description.
- `robots-txt`: FAIL — 2 syntax errors; crawler directives may be ignored.
- `llms-txt`: not found — no machine-readable site summary for AI assistants.
- `image-alt`: FAIL — top-navigation icon image has no alt attribute.
- `link-name`: FAIL — image links to network titles (Highway Mail, Kempton Express,
  Pretoria Rekord, Caxton Network News, The Citizen) have no accessible names.
- `image-size-responsive`: FAIL — favicon.ico used as a navigation icon (low resolution).

### 2. Agentic browsing — critical (score 49/100)
- `agent-accessibility-tree`: **0** — the accessibility tree is not well-formed, so AI
  agents and screen readers cannot reliably navigate the page.
- `heading-order`: FAIL — the "TOP STORIES" block skips heading levels.
- `color-contrast`: FAIL — "Read More", "All" and network-title links below WCAG AA.
- `webmcp-*`: not applicable — no WebMCP tools registered.
- `ard-schema`: not found — no agent-readiness manifest.
- `cumulative-layout-shift`: 0.059 (passing, but driven by an unsized header logo).

### 3. Performance — high
- Time to Interactive **15.7 s** (score 6/100) on emulated mobile.
- Total Blocking Time 610 ms; LCP 3.5 s; FCP 2.0 s; Speed Index 4.2 s.
- DOM: **2,617 elements at 22 levels deep** (Jannah/WordPress theme bloat).
- Longest critical network chain **2,478 ms** (render-blocking CSS + font chain).
- Forced reflows from theme JavaScript; browser console errors unresolved.
- Unsized header logo image is a named CLS culprit.
- jQuery 3.7.1 plus multiple theme CSS/JS bundles ship on every page load.
- Unused preconnects to ad-tech origins (tags.crwdcntrl.net, bcp.crwdcntrl.net, c.ltmsphrcl.net).

### 4. Trust, security & hygiene — medium
- `clickjacking-mitigation`: informative with **High severity** — no `X-Frame-Options`
  header and no CSP `frame-ancestors` directive found.
- Third-party sprawl: Clicky analytics, Lotame (crwdcntrl), onthe.io, consent tooling.
- `errors-in-console`: FAIL.

## Context worth knowing

- The site already carries a `google-preferred-source` plugin ("Add as a preferred
  source on Google") and an AI Policy page stating Caxton Local Media does not use AI
  to generate news and will not replace journalists with AI — a strong foundation the
  AI-discoverability work should build on, not contradict.
- Platform: WordPress with the Jannah theme (TieLabs), media served from
  images.caxton.co.za, GetClicky analytics, jQuery 3.7.1.

## Recommended targets (new templates)

Performance 95+ · Accessibility 98+ · SEO 100 · Agentic Browsing 90+ · LCP < 2.5 s on
mid-range mobile · zero console errors · valid robots.txt · llms.txt + full structured
data · monthly scorecard reporting.

## Server-header snippet for the clickjacking fix (hosting level)

```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Content-Security-Policy "frame-ancestors 'self' https://*.caxton.co.za" always;
```

(Apache equivalent: `Header always set X-Frame-Options "SAMEORIGIN"` etc.)
