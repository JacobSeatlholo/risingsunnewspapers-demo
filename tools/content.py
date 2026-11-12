#!/usr/bin/env python3
"""Content data for the Rising Sun Newspapers demo build.

Sources:
- Headlines, editions and organisation facts: risingsunnewspapers.co.za (fetched 12 Nov 2026)
- Audit findings: Lighthouse 13.6.0 report supplied by the client (12 Nov 2026, mobile)
All copy is demo/illustrative except where a fact is quoted from the sources above.
"""

SITE_URL = "https://risingsunnewspapers.co.za"
BRAND = "Rising Sun Newspapers"
TAGLINE = "Breaking local news in KZN"
FOUNDED = 1986

NAV = [
    ("News", "index.html#latest", None),
    ("Sport", "index.html#desks", None),
    ("Business", "index.html#desks", None),
    ("Lifestyle", "index.html#desks", None),
    ("e-Papers", "index.html#editions", None),
    ("About", "about.html", "about"),
    ("Advertise", "advertise.html", "advertise"),
]
NAV_CTA = ("Audit & Roadmap", "audit.html", "audit")

HEADLINES = [
    {
        "kicker": "News",
        "title": "Jobless youth question eThekwini's unemployment decrease",
        "author": "Sibahle Anthony Siqathule",
        "author_role": "Rising Sun reporter",
        "date": "12 November 2026",
        "date_iso": "2026-11-12",
        "slug": "article-jobless-youth.html",
        "img": "hero-durban",
        "alt": "Golden sunrise over the Durban city skyline and Indian Ocean (illustrative demo image)",
        "flag": "Latest",
    },
    {
        "kicker": "Community",
        "title": "A seat at the Christmas table: TAFTA launches annual campaign with support from special guest, Mariam Bassa",
        "author": "Rising Sun Newsroom",
        "author_role": "Community desk",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "slug": "article-christmas-table.html",
        "img": "lifestyle",
        "alt": "Volunteers serving meals at long communal tables during a charity event (illustrative demo image)",
        "flag": None,
    },
    {
        "kicker": "Education",
        "title": "Orient Islamic School innovators put water conservation in the spotlight at robotics competition",
        "author": "Rising Sun Newsroom",
        "author_role": "Schools desk",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "slug": "article-christmas-table.html",
        "img": "education",
        "alt": "High school learners building a robotics project in a classroom (illustrative demo image)",
        "flag": None,
    },
]

MORE_ROWS = [
    {
        "kicker": "Crime & Courts",
        "title": "Father sentenced to life imprisonment for raping his teenage daughter",
        "date": "11 November 2026",
        "slug": "article-jobless-youth.html",
    },
    {
        "kicker": "Crime & Courts",
        "title": "Man killed, another injured in Montford shooting",
        "date": "11 November 2026",
        "slug": "article-jobless-youth.html",
    },
]

TICKER = [
    "Jobless youth question eThekwini's unemployment decrease",
    "TAFTA launches annual Christmas table campaign",
    "Orient Islamic School innovators shine at robotics competition",
    "New e-Papers: Chatsworth, Overport, Merebank and more",
]

DESKS = [
    ("News & Crime", "Court sentences, municipal matters and the stories that shape daily life across south Durban and beyond."),
    ("Schools & Education", "Matric results, school sport, robotics competitions and the classrooms raising the next generation."),
    ("Sport", "Local leagues, school derbies and clubhouse heroes - the matches our communities actually talk about."),
    ("Business", "Small business wins, market trends, tenders and the traders who keep local economies moving."),
    ("Lifestyle & Get It", "Food, homes, health and the people doing extraordinary things in ordinary neighbourhoods."),
    ("Motoring & Promotions", "New launches, road safety and the specials worth driving across town for."),
]

STATS = [
    ("40", "Years serving KZN", "Family-founded in 1986"),
    ("7", "Community editions", "Print titles plus weekly e-papers"),
    ("100%", "Free to read", "Accessible community journalism"),
    ("100%", "Human journalism", "No AI-generated news, by policy"),
]

EDITIONS = [
    ("Rising Sun Chatsworth", "Latest e-paper: 10 November 2026"),
    ("Rising Sun Overport", "Latest e-paper: 12 November 2026"),
    ("Rising Sun Merebank", "Latest e-paper: 10 November 2026"),
    ("Mid South Coast Rising Sun", "Latest e-paper: 10 November 2026"),
    ("North Coast Rising Sun", "Latest e-paper: 11 November 2026"),
    ("Rising Sun Lenasia", "Latest e-paper: 10 November 2026"),
    ("Rising Sun Weekly", "Weekly edition"),
    ("Rising Sun Shoppers Guide", "Seasonal specials guide"),
]

SISTERS = ["Highway Mail", "Kempton Express", "Pretoria Rekord", "Caxton Network News", "The Citizen"]

# ---------------------------------------------------------------- audit data
AUDIT_META = "Lighthouse 13.6.0 · Mobile emulation · risingsunnewspapers.co.za · Audited 12 November 2026"

SCORES = [
    ("Performance", 72, "mid", 72, "LCP 3.5s · TBT 610ms · TTI 15.7s"),
    ("Accessibility", 86, "mid", 86, "Contrast, alt text, link names"),
    ("Best Practices", 92, "mid", 92, "Console errors, icon sizing"),
    ("SEO", 77, "mid", 77, "Meta description, robots.txt"),
    ("Agentic Browsing", 49, "bad", 49, "AI-agent readiness score"),
]

FINDINGS = [
    {
        "title": "Discoverability — search engines and AI assistants cannot read you properly",
        "sev": ("critical", "Critical"),
        "items": [
            ("Homepage has no meta description",
             "The Lighthouse SEO audit fails outright. Google and AI assistants fall back to arbitrary snippets, so your own description of the paper never appears.",
             "meta-description: fail"),
            ("robots.txt is invalid — 2 syntax errors",
             "A malformed robots.txt means crawler directives may simply be ignored. You may be accidentally blocking (or failing to guide) both search and AI crawlers.",
             "robots-txt: 2 errors"),
            ("No llms.txt — no machine-readable site summary",
             "The Lighthouse agentic-browsing category reports llms.txt absent. AI assistants that look for a curated map of the site find nothing.",
             "llms-txt: not found"),
            ("Images without alt attributes",
             "The top-navigation icon image ships with no alt text — a free accessibility and SEO win currently missed.",
             "image-alt: fail"),
            ("Links without discernible names",
             "Image links to Highway Mail, Kempton Express, Pretoria Rekord, Caxton Network News and The Citizen have no accessible names — invisible to screen readers and to agents.",
             "link-name: fail"),
            ("Low-resolution favicon used as a navigation icon",
             "The site serves a .ico file where a modern icon belongs — blurry rendering and an image-resolution audit failure.",
             "image-size-responsive: fail"),
        ],
    },
    {
        "title": "Agentic browsing — the newest score: 49/100",
        "sev": ("critical", "Critical"),
        "items": [
            ("Accessibility tree is not well-formed",
             "AI agents and screen readers both navigate via the accessibility tree. This audit scores 0 — the page is effectively unreadable to automated assistants.",
             "agent-accessibility-tree: 0"),
            ("Heading order breaks the document outline",
             "The 'TOP STORIES' block skips heading levels, so the page structure agents rely on to summarise content collapses.",
             "heading-order: fail"),
            ("Colour contrast below WCAG AA",
             "'Read More', 'All' and the network-title links fail contrast checks — text both humans and machines struggle to read reliably.",
             "color-contrast: fail"),
            ("No WebMCP tools or agent manifests registered",
             "The emerging WebMCP audits report nothing registered — the site offers no structured way for agents to interact with it (search, subscribe, verify).",
             "webmcp-*: not applicable"),
            ("No agent readiness (ARD) manifest",
             "No manifest declaring the site's agent-facing capabilities exists.",
             "ard-schema: not found"),
        ],
    },
    {
        "title": "Performance — readers wait, agents time out",
        "sev": ("high", "High"),
        "items": [
            ("Time to Interactive: 15.7 seconds on mobile",
             "Lighthouse scores this 6/100. Readers on mid-range phones wait 15 seconds before the page truly responds; agents consider the page unresponsive.",
             "TTI 15,722ms · score 6"),
            ("Total Blocking Time 610ms · LCP 3.5s · Speed Index 4.2s",
             "Heavy theme JavaScript (jQuery plus Jannah bundles) blocks the main thread; the largest element paints late.",
             "TBT 606ms · LCP 3,453ms"),
            ("DOM of 2,617 elements at 22 levels deep",
             "Theme bloat inflates style and layout cost. A lean news article needs roughly a quarter of that.",
             "dom-size: 2,617 nodes"),
            ("Critical network chain of 2.48 seconds",
             "Render-blocking CSS files and a font dependency chain delay first paint — with unused preconnects to ad-tech origins wasting connection time.",
             "longest chain 2,478ms"),
            ("Forced reflows and console errors from theme scripts",
             "Layout-thrashing JavaScript and unresolved browser errors drag interactivity down further.",
             "forced-reflow: fail · console errors"),
            ("Unsized logo image shifts the layout",
             "The header logo loads without reserved space and pushes content down as it paints — a core CLS culprit named in the report.",
             "cls-culprits: unsized img"),
        ],
    },
    {
        "title": "Trust, security & hygiene",
        "sev": ("medium", "Medium"),
        "items": [
            ("No frame-control policy — clickjacking exposure rated High",
             "Lighthouse finds neither X-Frame-Options nor a CSP frame-ancestors directive. Any site could embed yours and trick readers.",
             "clickjacking: High severity"),
            ("Third-party sprawl",
             "Clicky analytics, Lotame (crwdcntrl) data brokers, onthe.io and consent tooling all add weight — with unused preconnects to ad-tech origins signalling past integrations still haunting the head.",
             "5+ third-party origins"),
            ("Console errors unresolved",
             "Browser errors logged on load indicate failing requests and scripts — a best-practices audit failure.",
             "errors-in-console: fail"),
        ],
    },
]

FIXMAP = [
    ("No meta description", "Unique, descriptive 150–160 character meta description on every page template", "generated head — view source"),
    ("Invalid robots.txt", "Valid robots.txt with an explicit, named welcome for AI crawlers", "robots.txt"),
    ("No llms.txt", "Curated llms.txt plus llms-full.txt summarising the brand, pages and policies", "llms.txt · llms-full.txt"),
    ("Broken heading order", "One h1 per page, strict h2→h3 hierarchy in every template", "every page"),
    ("Contrast failures", "AA-verified palette — ratios checked at build time", "assets/css/style.css"),
    ("Missing alt & link names", "Descriptive alt text and aria-labels on every image and icon link", "index.html footer & cards"),
    ("Low-resolution icon", "Crisp vector SVG favicon and manifest icons", "favicon.svg · manifest.webmanifest"),
    ("TTI 15.7s · TBT 610ms", "Zero-framework static HTML, ~5KB of dependency-free JavaScript, no jQuery", "assets/js/main.js"),
    ("2.48s font chain", "Two font families, preconnected, with font-display: swap", "assets/css/style.css"),
    ("DOM of 2,617 nodes", "Lean semantic markup — a fraction of the node count per page", "index.html"),
    ("Unsized images (CLS)", "Explicit width/height and aspect-ratio on every image", "all templates"),
    ("No clickjacking headers", "X-Frame-Options / CSP frame-ancestors snippet documented for hosting", "docs/AUDIT.md"),
    ("Console errors", "Clean browser console across the demo", "browser devtools"),
    ("No structured data", "NewsArticle, NewsMediaOrganization, FAQPage and BreadcrumbList JSON-LD", "view source on any page"),
]

PHASES = [
    ("Search & AI quick wins", "Weeks 1–2", [
        "Meta descriptions on every template",
        "Fix robots.txt; publish valid AI-crawler policy",
        "Ship llms.txt and llms-full.txt",
        "Alt text, link names, heading order, crisp favicon",
        "Add clickjacking headers at the web server",
    ]),
    ("Performance & platform cleanup", "Weeks 3–6", [
        "Image pipeline: sizing, lazy-loading, modern formats",
        "Font strategy: preload, swap, fewer weights",
        "Defer or drop non-essential theme scripts",
        "Audit third-party tags; retire unused trackers",
        "Slim the DOM; clear console errors",
    ]),
    ("AI-native layer", "Weeks 7–10", [
        "NewsArticle schema at scale across the CMS",
        "Sitemap hygiene and agent-accessibility QA in the publish workflow",
        "WebMCP / agent-manifest readiness",
        "AI-referral analytics and preferred-source completion",
    ]),
    ("Governance", "Ongoing", [
        "Monthly Lighthouse scorecard against agreed targets",
        "Screen-reader accessibility passes each quarter",
        "Schema validation in the editorial CI",
        "Alignment with the existing human-journalism AI Policy",
    ]),
]

FAQ = [
    ("Will AI replace our journalists?",
     "No — and your own AI Policy says so: Caxton Local Media does not use AI to generate news, and AI will never replace journalists or editors. Our work makes that human journalism legible to machines: agents quote your reporting accurately, attribute it properly and send readers (and new audiences) back to you."),
    ("What is 'agentic browsing'?",
     "Assistants and AI browsers (ChatGPT, Claude, Perplexity, Gemini and others) now fetch, summarise and act on web pages on a reader's behalf. Lighthouse 13 introduced an agentic-browsing category that scores how well a page serves those agents — this site currently scores 49/100. The demo shows exactly what that number wants."),
    ("Why does robots.txt matter so much?",
     "When robots.txt is malformed, crawlers may ignore your instructions entirely — you lose control over what is and is not fetched. A valid file also lets you explicitly welcome AI assistants instead of leaving the decision to chance."),
    ("What is llms.txt?",
     "An emerging convention: a short, structured file at the root of the site that tells large language models what the site is, what matters most and where to look. It is the fastest, cheapest AI-discoverability win available — the demo ships one."),
    ("Is this a full redesign of our website?",
     "No. It is a demonstration of direction. Phases 1 and 2 of the roadmap deliberately work with your existing WordPress platform; a move to a faster stack is an option, not a requirement."),
    ("How will we know it worked?",
     "A monthly scorecard: Lighthouse categories, Core Web Vitals from real users, search impressions from Google Search Console, and referral traffic from AI assistants. Targets we propose: Performance 95+, Accessibility 98+, SEO 100, Agentic Browsing 90+ on the new templates."),
]

TARGETS = "Proposed targets on the new templates: Performance 95+ · Accessibility 98+ · SEO 100 · Agentic Browsing 90+ · LCP under 2.5s on mid-range mobile."

ARTICLES = {
    "article-jobless-youth": {
        "kicker": "News",
        "title": "Jobless youth question eThekwini's unemployment decrease",
        "standfirst": "Young residents say the lived reality on the ground tells a different story than the latest positive numbers.",
        "author": "Rising Sun Newsroom",
        "initials": "RS",
        "date": "12 November 2026",
        "date_iso": "2026-11-12",
        "reading": "4 min read",
        "img": "hero-durban",
        "alt": "Golden sunrise over the Durban city skyline and Indian Ocean (illustrative demo image)",
        "caption": "Illustrative demo image — final template carries the newsroom's own photography and captions.",
        "body_demo_note": "This sample article demonstrates the new article template. The headline reflects genuine recent coverage on risingsunnewspapers.co.za, where the story was reported by Rising Sun journalist Sibahle Anthony Siqathule. The body text below is illustrative placeholder copy written for this demo.",
        "sections": [
            ("h2", "When the numbers and the street disagree"),
            ("p_first", "A positive headline about falling unemployment should have been good news for eThekwini's young people. Instead, it has become the latest flashpoint between official statistics and the day-to-day reality of job-seeking in communities like Chatsworth, Merebank and Montford."),
            ("p", "On the ground, the questions come quickly: which jobs were counted, where are they, and who got them? For households where one income supports several people, the gap between a percentage point and a payslip is the whole story."),
            ("p", "Youth unemployment has been one of the defining challenges facing South Africa's metros for more than a decade. When a municipality reports improvement, residents naturally want to see the evidence in their own neighbourhoods - in vacancy lists, in learnership intakes, in the queue outside the local employment office."),
            ("h2", "What young residents say they want"),
            ("p", "In conversations reflected in Rising Sun's coverage, the same themes keep returning:"),
            ("ul", [
                "Visibility - knowing which opportunities actually exist, and where to apply",
                "Transport - getting to an interview should not cost a day's wage",
                "Skills - short courses and learnerships that end in real contracts",
                "Local first - municipal jobs and procurement that look to nearby communities",
            ]),
            ("p", "Each of these sits within the reach of local government, business and community organisations working together - which is precisely why readers keep holding the numbers to account."),
            ("h2", "Why local journalism matters here"),
            ("p", "National headlines move on within a news cycle. A community newspaper stays: it attends the community meetings, asks the ward councillors, and returns to the same young people a month later to ask what changed. That continuity is what turns a statistic back into a story."),
            ("p", "Read the original reporting and ongoing coverage on the live site."),
        ],
        "related": ["article-christmas-table", "TAFTA campaign", "More community coverage"],
        "ld_type": "NewsArticle",
    },
    "article-christmas-table": {
        "kicker": "Community",
        "title": "A seat at the Christmas table: TAFTA launches annual campaign with support from special guest, Mariam Bassa",
        "standfirst": "The season of giving returns as the long-standing Durban organisation caring for older persons invites the community to pull up a chair.",
        "author": "Rising Sun Newsroom",
        "initials": "RS",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "reading": "3 min read",
        "img": "lifestyle",
        "alt": "Volunteers serving meals at long communal tables during a charity event (illustrative demo image)",
        "caption": "Illustrative demo image — final template carries the newsroom's own photography and captions.",
        "body_demo_note": "This sample article demonstrates the new article template. The headline reflects genuine recent coverage on risingsunnewspapers.co.za. The body text below is illustrative placeholder copy written for this demo.",
        "sections": [
            ("h2", "A table that holds a whole community"),
            ("p_first", "For many older residents, the festive season can be the loneliest time of the year - and the easiest time for the rest of us to change that. TAFTA, the Durban organisation with a long history of caring for older persons, has launched its annual Christmas table campaign for 2026, with support from special guest Mariam Bassa."),
            ("p", "The idea behind the campaign is as warm as it is practical: no resident of a TAFTA home should spend Christmas Day without a full table, familiar faces and the feeling of a community that remembers them."),
            ("blockquote", "A seat at the table is a small thing to give, and an enormous thing to receive."),
            ("h2", "How the community can help"),
            ("p", "Campaigns like this one succeed because local people treat them as their own. Typical ways to take part include:"),
            ("ul", [
                "Donating festive groceries or sponsoring a table for a home",
                "Volunteering time on the day - serving, singing, simply sitting with residents",
                "Spreading the word through family WhatsApp groups and community pages",
            ]),
            ("p", "Readers who want the full details of this year's campaign - including how to donate - will find the complete story and contact information in the live coverage on the Rising Sun website."),
            ("h2", "The paper behind the campaign"),
            ("p", "Stories like this one are why community newspapers exist. Nobody else is going to spend the second week of November in a retirement home dining hall, taking down names and asking what Christmas means to the people seated there. The Rising Sun does - and has, for forty years."),
        ],
        "related": ["article-jobless-youth", "eThekwini youth story", "More local news"],
        "ld_type": "NewsArticle",
    },
}
