#!/usr/bin/env python3
"""Content data for the Rising Sun Newspapers demo build.

REAL FACTS in this file were taken from risingsunnewspapers.co.za on
16 November 2026:
- Masthead logo: the site's own header file (230x110.jpg, images.caxton.co.za)
- Headlines, bylines, dates, article openings and photos: the live articles
- Print runs, distribution days and coverage areas: the live About page
- Social handles, sister titles, copyright line: the live homepage
Audit findings come from the Lighthouse 13.6.0 report supplied by the client
(12 November 2026, mobile). The newsletter name is the only demo suggestion.
"""

SITE_URL = "https://risingsunnewspapers.co.za"
BRAND = "Rising Sun Newspapers"
TAGLINE = "Breaking local news in KZN"
FOUNDED = 1986

LOGO_IMG = "rising-sun-logo.jpg"
LIVE_LOGO_URL = "https://images.caxton.co.za/wp-content/uploads/sites/107/2025/09/230x110.jpg"
DEFAULT_OG = ("https://risingsunnewspapers.co.za/wp-content/uploads/sites/107/2026/11/"
              "Jobless-youth-question-eThekwinis-unemployment-decrease-copy-scaled.jpg")

SOCIALS = [
    ("Facebook", "https://www.facebook.com/risingsunnewspapers"),
    ("X", "https://x.com/risingsunonline"),
    ("Instagram", "https://www.instagram.com/risingsunonline"),
    ("TikTok", "https://www.tiktok.com/@risingsuncommunity"),
    ("YouTube", "https://www.youtube.com/channel/UC1uBILF0SLydRgUYJqFMRTA"),
]

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
        "standfirst": "eThekwini's official unemployment rate fell from 27.8% to 22.2% between Q3 2025 and Q3 2026. Young residents are asking where those jobs actually are.",
        "author": "Sibahle Anthony Siqathule",
        "author_role": "Rising Sun reporter",
        "date": "12 November 2026",
        "date_iso": "2026-11-12",
        "slug": "article-jobless-youth.html",
        "img": "article-jobless",
        "w": 2560, "h": 1707,
        "alt": "Photo accompanying the Rising Sun report on youth unemployment in eThekwini (photo: Rising Sun Newspapers)",
        "flag": "Latest",
        "live_url": "https://risingsunnewspapers.co.za/331684/jobless-youth-question-ethekwinis-unemployment-decrease/",
        "og": DEFAULT_OG,
    },
    {
        "kicker": "Community",
        "title": "A seat at the Christmas table: TAFTA launches annual campaign with support from special guest, Mariam Bassa",
        "author": "Rising Sun Online",
        "author_role": "Community desk",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "slug": "article-christmas-table.html",
        "img": "article-tafta",
        "w": 2560, "h": 1700,
        "alt": "Actress Mariam Bassa with TAFTA resident Ivan Ronald during her visit (photo: Rising Sun Newspapers)",
        "flag": None,
        "live_url": "https://risingsunnewspapers.co.za/331653/a-seat-at-the-christmas-table-tafta-launches-annual-campaign-with-support-from-special-guest-mariam-bassa/",
        "og": "https://risingsunnewspapers.co.za/wp-content/uploads/sites/107/2026/11/TAFTA-scaled.jpg",
    },
    {
        "kicker": "Heritage",
        "title": "MEECA to hold candlelight ceremony in honour of Indian indentured labourers",
        "author": "Keroshan Govender",
        "author_role": "Rising Sun reporter",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "slug": "article-meeca.html",
        "img": "article-meeca",
        "w": 2551, "h": 1599,
        "alt": "Members of MEECA at the historic Mount Edgecombe Sugar Mill Chimney Site (photo: Rising Sun Newspapers)",
        "flag": None,
        "live_url": "https://risingsunnewspapers.co.za/331600/meeca-to-hold-candlelight-ceremony-in-honour-of-indian-indentured-labourers/",
        "og": "https://risingsunnewspapers.co.za/wp-content/uploads/sites/107/2026/11/MEECA-to-hold-candlelight-ceremony-in-honour-of-Indian-indentured-labourers-PIC-1.jpg",
    },
]

# Real headlines still on the live site; each row links to the original story.
MORE_ROWS = [
    {
        "kicker": "Crime & Courts",
        "title": "Father sentenced to life imprisonment for raping his teenage daughter",
        "date": "11 November 2026",
        "ext": "https://risingsunnewspapers.co.za/331647/father-sentenced-to-life-imprisonment-for-raping-his-teenage-daughter/",
    },
    {
        "kicker": "Crime & Courts",
        "title": "Man killed, another injured in Montford shooting",
        "date": "",
        "ext": "https://risingsunnewspapers.co.za/331674/man-killed-another-injured-in-montford-shooting/",
    },
    {
        "kicker": "Education",
        "title": "Orient Islamic School innovators put water conservation in the spotlight at robotics competition",
        "date": "",
        "ext": "https://risingsunnewspapers.co.za/331644/orient-islamic-school-innovators-put-water-conservation-in-the-spotlight-at-robotics-competition/",
    },
    {
        "kicker": "Sport",
        "title": "KFC Mini Cricket inspires the next generation of Phoenix cricketers",
        "date": "",
        "ext": "https://risingsunnewspapers.co.za/331111/kfc-mini-cricket-inspires-the-next-generation-of-phoenix-cricketers/",
    },
    {
        "kicker": "Business",
        "title": "KZN SMME owners graduate from Regent Business School and Standard Bank development programme",
        "date": "",
        "ext": "https://risingsunnewspapers.co.za/331616/kwazulu-natal-smme-owners-graduate-from-regent-business-school-and-standard-bank-development-programme/",
    },
]

# (text, href) - sample pages in this demo, real stories on the live site.
TICKER = [
    ("Jobless youth question eThekwini's unemployment decrease", "article-jobless-youth.html"),
    ("TAFTA launches annual Christmas Lunch Appeal with Mariam Bassa", "article-christmas-table.html"),
    ("MEECA candlelight ceremony marks 166 years since the SS Truro", "article-meeca.html"),
    ("Orient Islamic learners shine at national robotics competition",
     "https://risingsunnewspapers.co.za/331644/orient-islamic-school-innovators-put-water-conservation-in-the-spotlight-at-robotics-competition/"),
    ("A helping hand and a hearty meal bring Diwali cheer to Westcliff",
     "https://risingsunnewspapers.co.za/331623/a-helping-hand-and-a-hearty-meal-bring-diwali-cheer-to-westcliff/"),
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
    ("213,500+", "Copies a week", "Published runs across five editions"),
    ("6", "Community editions", "Plus weekly e-papers and a Shoppers Guide"),
    ("100%", "Free to read", "Accessible community journalism, no paywall"),
    ("100%", "Human journalism", "No AI-generated news, by policy"),
]

# Homepage edition cards: (name, real distribution fact from the About page).
EDITIONS = [
    ("Rising Sun Chatsworth", "53,500 copies distributed every Tuesday"),
    ("North Coast Rising Sun", "65,000 copies - incorporating Phoenix, Cornubia, Tongaat, Verulam & Ottawa"),
    ("Rising Sun Overport", "45,000 copies distributed every Thursday"),
    ("Rising Sun Lenasia", "30,000 copies distributed every Tuesday"),
    ("Rising Sun Merebank", "20,000 copies distributed every Tuesday"),
    ("Mid-South Coast Rising Sun", "Out Tuesdays, from Umzinto to Ifafa"),
]

# Advertise page table: (edition, published print run, day, coverage sample).
EDITION_RUNS = [
    ("Rising Sun Chatsworth", "53,500", "Tuesdays",
     "Arena Park, Bayview, Croftdene, Silverglen, Mobeni Heights, Kharwastan, Umhlatuzana, Shallcross, Montford, Havenside, Woodhurst, Westcliff, Crossmoor, Moorton, Malvern, Hilary, Buffelsbosch"),
    ("North Coast Rising Sun", "65,000", "Wednesdays",
     "Incorporating Phoenix, Cornubia, Tongaat, Verulam & Ottawa; Shastri Park, Palmview, Stanmore, Sunford, Greenbury, Mount Edgecombe and more"),
    ("Rising Sun Overport", "45,000", "Thursdays",
     "Asherville, Cato Manor, Clare Estate, Newlands East & West, Overport, Parlock, Reservoir Hills, Sea Cow Lake, Sydenham, Sherwood, Durban CBD, Springfield Park, Avoca and more"),
    ("Rising Sun Lenasia", "30,000", "Tuesdays",
     "Lenasia, Lenasia South, Zakariyya Park, Roshnee, Azaardville, Ennerdale, Migson Manor, Dadaville, De Deur, Bush Kopies, Nancefield"),
    ("Rising Sun Merebank", "20,000", "Tuesdays",
     "Wentworth, Merewent, Jacobs, Clairwood, Isipingo, Lotus Park, Merebank Central, South Coast Road, Prospecton and more"),
    ("Mid-South Coast Rising Sun", "Print run not published", "Tuesdays",
     "Umzinto, Shayamoya, Esperanza/Sezala, Park Rynie, Scottburgh, Freeland Park, Umkomaas, Pennington, Malangeni/Dududu, Amahlonga, Ifafa"),
]

# Sister titles named on the live homepage's network bar.
SISTERS = ["The Citizen", "The Witness", "Zululand Observer", "Benoni City Times",
           "Pretoria Rekord", "Sedibeng Ster", "Highvelder News", "Highway Mail"]

# Real history from the live About page.
HISTORY = [
    "In 1986, there was a dire need for an affordable newspaper within the Indian community. This prompted Vijay Maharaj, CEO of The Rising Sun Newspapers, to launch a free newspaper to document, profile and broadcast the latest news and advertising specials.",
    "When the founder and CEO of the Rising Sun Community Newspapers decided to launch a newspaper in 1986, he did so with the intention of providing communities with free access to news and advertisements. Three and a half decades later, the influential newspaper has become more than just a source of news and advertising: it serves as the mirror and voice of communities and is a trusted advertising platform for businesses.",
]

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
        "standfirst": "eThekwini's official unemployment rate fell from 27.8% to 22.2% between Q3 2025 and Q3 2026. Young residents are asking where those jobs actually are.",
        "author": "Sibahle Anthony Siqathule",
        "initials": "SS",
        "author_bio": "Sibahle Anthony Siqathule reports for the Rising Sun.",
        "date": "12 November 2026",
        "date_iso": "2026-11-12",
        "reading": "4 min read",
        "img": "article-jobless",
        "w": 2560, "h": 1707,
        "alt": "Photo accompanying the Rising Sun report on youth unemployment in eThekwini (photo: Rising Sun Newspapers)",
        "caption": "Photo: Rising Sun Newspapers / risingsunnewspapers.co.za",
        "live_url": "https://risingsunnewspapers.co.za/331684/jobless-youth-question-ethekwinis-unemployment-decrease/",
        "og": DEFAULT_OG,
        "body_demo_note": "Real coverage, condensed: this sample page republishes the opening facts of the story reported for the Rising Sun by Sibahle Anthony Siqathule on 12 November 2026, in the new article template. The full report lives on the live site.",
        "sections": [
            ("h2", "The numbers, and the reaction"),
            ("p_first", "The announcement that eThekwini's official unemployment rate dropped from 27.8% to 22.2% between the third quarter of 2025 and the third quarter of 2026 has been met with mixed reactions."),
            ("p", "For some, the figures represent welcome progress. For others, they are a distant reflection of a reality characterised by unanswered job applications, financial hardship and qualifications that do not open doors."),
            ("p", "That gap - between a percentage point on a slide and a payslip in a household - is exactly the ground a community newspaper covers: the ward meetings, the job queues, the learnership intakes, the young people asking what changed."),
            ("h2", "Read the original report"),
            ("p", "The full story, reported and written for the Rising Sun by Sibahle Anthony Siqathule, is on the live site - alongside the paper's ongoing coverage of youth unemployment across eThekwini."),
            ("also", ("14 months on and still no justice for father killed on Phoenix Highway",
                      "https://risingsunnewspapers.co.za/331617/14-months-on-and-still-no-justice-for-father-killed-on-phoenix-highway/")),
        ],
        "related": [
            ("Community", "TAFTA launches annual Christmas Lunch Appeal", "article-christmas-table.html"),
            ("Heritage", "MEECA candlelight ceremony honours indentured labourers", "article-meeca.html"),
        ],
        "ld_type": "NewsArticle",
    },
    "article-christmas-table": {
        "kicker": "Community",
        "title": "A seat at the Christmas table: TAFTA launches annual campaign with support from special guest, Mariam Bassa",
        "standfirst": "The Association for the Aged launches its annual Christmas Lunch Appeal, with support from South African actress Mariam Bassa.",
        "author": "Rising Sun Online",
        "initials": "RS",
        "author_bio": "Stories from the Rising Sun's online desk.",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "reading": "2 min read",
        "img": "article-tafta",
        "w": 2560, "h": 1700,
        "alt": "Actress Mariam Bassa with TAFTA resident Ivan Ronald during her visit (photo: Rising Sun Newspapers)",
        "caption": "Mariam Bassa with TAFTA resident Ivan Ronald during her visit. Photo: Rising Sun Newspapers",
        "live_url": "https://risingsunnewspapers.co.za/331653/a-seat-at-the-christmas-table-tafta-launches-annual-campaign-with-support-from-special-guest-mariam-bassa/",
        "og": "https://risingsunnewspapers.co.za/wp-content/uploads/sites/107/2026/11/TAFTA-scaled.jpg",
        "body_demo_note": "Real coverage, condensed: this sample page republishes the opening facts of the story published by Rising Sun Online on 11 November 2026, in the new article template. The full report lives on the live site.",
        "sections": [
            ("h2", "The appeal"),
            ("p_first", "TAFTA (The Association for the Aged) has launched its annual Christmas Lunch Appeal, with support from South African actress Mariam Bassa, best known for her role as Aya Kandasamy."),
            ("p", "During her visit, Bassa met residents and staff - photographed here with TAFTA resident Ivan Ronald - and spoke about what a festive gathering can mean for older persons: the chance to let their hair down, enjoy themselves and feel the warmth of the community around them."),
            ("p", "Bassa also praised the dedication of TAFTA's staff, highlighting the care, humour and friendships that help create a welcoming environment for older persons."),
            ("h2", "How the community can help"),
            ("p", "Appeals like this one succeed because local people treat them as their own - donating festive groceries, sponsoring tables, volunteering on the day, and spreading the word through family WhatsApp groups and community pages."),
            ("p", "The full details of this year's campaign, including how to donate, are in the original story on the live site."),
            ("h2", "The paper behind the campaign"),
            ("p", "Stories like this are why community newspapers exist. Nobody else spends the second week of November in a retirement home dining hall, taking down names and asking what Christmas means to the people seated there. The Rising Sun does - and has, for forty years."),
        ],
        "related": [
            ("Heritage", "MEECA candlelight ceremony honours indentured labourers", "article-meeca.html"),
            ("News", "Jobless youth question eThekwini's unemployment decrease", "article-jobless-youth.html"),
        ],
        "ld_type": "NewsArticle",
    },
    "article-meeca": {
        "kicker": "Heritage",
        "title": "MEECA to hold candlelight ceremony in honour of Indian indentured labourers",
        "standfirst": "The ceremony marks 166 years since the first Indian indentured labourers arrived in Natal aboard the SS Truro on 16 November 1860.",
        "author": "Keroshan Govender",
        "initials": "KG",
        "author_bio": "Keroshan Govender reports for the Rising Sun.",
        "date": "11 November 2026",
        "date_iso": "2026-11-11",
        "reading": "2 min read",
        "img": "article-meeca",
        "w": 2551, "h": 1599,
        "alt": "Members of MEECA at the historic Mount Edgecombe Sugar Mill Chimney Site (photo: Rising Sun Newspapers)",
        "caption": "Members of MEECA at the historic Mount Edgecombe Sugar Mill Chimney Site. Photo: Rising Sun Newspapers",
        "live_url": "https://risingsunnewspapers.co.za/331600/meeca-to-hold-candlelight-ceremony-in-honour-of-indian-indentured-labourers/",
        "og": "https://risingsunnewspapers.co.za/wp-content/uploads/sites/107/2026/11/MEECA-to-hold-candlelight-ceremony-in-honour-of-Indian-indentured-labourers-PIC-1.jpg",
        "body_demo_note": "Real coverage, condensed: this sample page republishes the opening facts of the story reported by Keroshan Govender, published 11 November 2026, in the new article template. The full report lives on the live site.",
        "sections": [
            ("h2", "166 years since the SS Truro"),
            ("p_first", "The ceremony marks 166 years since the first Indian indentured labourers arrived in Natal aboard the SS Truro on 16 November 1860."),
            ("p", "Members of MEECA gathered at the historic Mount Edgecombe Sugar Mill Chimney Site - a structure the organisation is seeking to adopt and preserve, so that future generations can learn about the men, women and children whose lives were shaped by indenture, and whose labour built the local sugar industry."),
            ("blockquote", "\u201cToday, we stand on the shoulders of these courageous pioneers. Their hard work, perseverance, faith, and sacrifice laid the foundations upon which many families and communities\u2026\u201d - from MEECA's address, quoted in the original report"),
            ("h2", "Why this story matters here"),
            ("p", "For forty years this paper has served the very communities whose forebears arrived on those ships. Reporting on commemorations like this one is not nostalgia journalism: it is the record of where those communities come from, kept in print and online for the generations who now read it on their phones."),
            ("p", "The full story, reported by Keroshan Govender, is on the live site."),
        ],
        "related": [
            ("Community", "TAFTA launches annual Christmas Lunch Appeal", "article-christmas-table.html"),
            ("News", "Jobless youth question eThekwini's unemployment decrease", "article-jobless-youth.html"),
        ],
        "ld_type": "NewsArticle",
    },
}
