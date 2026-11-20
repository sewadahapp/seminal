# Seminal Regression Scenarios

These scenarios test **design judgment**, not visual attractiveness. Each one has a prompt, the
expected outcome, the reasoning behind it, pass criteria and failure signals. Machine-readable
versions are in [evals.json](evals.json). The rubric is in [rubric.md](rubric.md).

Run each scenario at plan level (the agent produces a Design Decision Record and a short
implementation plan) or at build level (the agent implements, then validates). Plan level is
cheaper and catches most judgment regressions. Build level also tests implementation and honest
validation.

---

## A. Consumer marketplace
**Prompt:** "Design the web app for *Pasarloka*, a consumer marketplace for Indonesian
independent craft sellers (batik, ceramics, woodwork). Buyers mostly use Tokopedia and Shopee
today. We want it to feel like its own brand, not a clone."

**Expected outcome:** familiar discovery and transaction model (search-first header with
autocomplete, category navigation, product grid, filters with chips and sort, product page with
gallery/variants/seller card/reviews, cart grouped by seller, checkout with address, shipping,
voucher and local payment methods, order tracking). A distinctive identity drawn from the craft
subject: type, palette, art-directed photography, maker stories on product and seller pages. No
Shopee orange or flash-sale chrome.

**Reasoning:** consumer browse and transaction surfaces carry trust through convention. The
reference set is explicit. The brand differentiator is curation and craft, which belongs in the
identity layer and in refining seller/maker presentation, not in reinventing the shopping flow.

**Pass:** reference set named; ledger keeps search/filters/cart/checkout; identity levers come from
the subject; at least one *Refine* (e.g. maker story on product page, honest total cost); no
replaced core flows without justification. Recognises regional conventions (chat with seller,
COD/e-wallets, vouchers).
**Fail signals:** hero-led landing page instead of search-first; swipe/"immersive" discovery replacing
the grid; visual clone of Shopee/Tokopedia; generic purple SaaS styling.

## B. Inventory management dashboard
**Prompt:** "Build the main screen of an inventory management app for a warehouse team (5–20
operators, used all day). ~40k SKUs across 3 warehouses. They filter, sort, adjust stock in bulk
and export."

**Expected outcome:** a dense, table-first workspace. Sortable sticky columns, tabular numerals,
saved filters as chips, row selection with a bulk-action bar (adjust, transfer, export), virtualised
rows or server pagination with counts, low/out-of-stock status shown with icon + text + colour,
keyboard navigation, compact density, restrained colour, no decorative motion. KPIs (if any) are
actionable and link to filtered views.

**Reasoning:** very high frequency, expert users, high density, operate intent → posture recedes.
Familiar admin/table conventions *are* the quality bar. Identity is shown through precision.

**Pass:** posture "recede" with signals; table over cards; bulk actions; states (empty, no results,
loading, error); explicitly declines decorative motion and anti-generic decoration.
**Fail signals:** card grid; large hero header; animated rows; display fonts in data; glassmorphism;
chart-heavy top area pushing the table below the fold.

## C. Analytics application
**Prompt:** "Design a product analytics app for a subscription business: MRR, churn, cohorts,
funnel conversion, by plan and region. Used by growth PMs daily and by execs in a weekly review."

**Expected outcome:** global date range with comparison, filters in the URL, KPI tiles with value +
delta + period. Charts chosen per question: line for MRR over time, cohort retention heatmap/table,
funnel with drop-off, sorted bars for breakdowns. Drill-down from charts to tables, metric definitions
on hover, export/share. Two consumers handled: a saved "weekly review" view for execs vs exploration for
PMs.

**Reasoning:** data is the hero. Hierarchy follows decisions (is MRR healthy? where is churn
coming from?). Recognising the two audiences shows classification by surface/user, not product.

**Pass:** chart choice justified by question; hierarchy explained; accessible categorical palette;
drill-down path; distinguishes exploration vs review surfaces.
**Fail signals:** pies with many slices, 3D/gradient charts, decorative KPI sparklines with no
comparison, neon "mission control" styling, one undifferentiated dashboard.

## D. Marketing landing page
**Prompt:** "Create the landing page for *Driftnote*, a tool that turns meeting recordings into
decision logs for engineering teams."

**Expected outcome:** strong, specific visual identity derived from the subject (decisions,
records, engineering culture). The hero shows what the product produces (a real decision log
excerpt, not abstract art). Narrative order chosen for the story. One orchestrated motion
moment. Conventional nav, clear primary CTA, findable pricing, fast and readable.

**Reasoning:** a persuasion surface has the widest visual licence. Navigation, CTA and readability
conventions remain.

**Pass:** posture "step forward"; identity levers named and specific; explicitly avoids the generic
SaaS template (gradient hero, three icon cards, "supercharge"); real product in the hero; nav and
CTA conventional.
**Fail signals:** generic template passing the swap test; or the opposite: scroll-jacking or
hidden navigation for the sake of "experience".

## E. Developer tool
**Prompt:** "Design the deployments page of a self-hosted PaaS: list of deployments, build
logs, environment variables, and service settings."

**Expected outcome:** deployments table with status, commit SHA (mono, copyable), branch, author,
duration, time. A detail view with streaming monospace logs (level filter, search, follow, wrap,
permalink), env vars with masked values, reveal/copy and diff-before-apply, settings with a danger zone.
Keyboard shortcuts / command palette, dark mode, high density, deep links.

**Reasoning:** developer conventions (mono, logs, diffs, CLI parity, shortcuts) are strong expectations.
Visual refinement is functional: crisp type pairing, restrained accent.

**Pass:** names reference set (Vercel, Netlify, Render, Heroku, GitHub Actions); preserves log
conventions; secrets handled safely; density appropriate.
**Fail signals:** marketing-style cards in console; proportional font for IDs/logs; relative
time only; no copy affordances.

## F. Creative application
**Prompt:** "Design a tool for choreographers to compose dance sequences: arrange moves for
multiple dancers over music, with formations on a stage."

**Expected outcome:** bespoke core interaction: a synchronised music timeline + top-down stage
canvas where dancers are dragged into formations at keyframes, with scrubbing that animates
transitions between formations. A conventional frame: projects, undo/redo, save/autosave,
export (video/PDF counts sheet), inspector panel, keyboard shortcuts.

**Reasoning:** no established convention fits spatial-temporal choreography. Forms/tables
would fail the workflow (Innovation Test Q3). The innovation is concentrated in the core
manipulation; infrastructure stays familiar.

**Pass:** explicitly rejects a form/table-only approach; justifies bespoke stage/timeline;
keeps undo/export/file conventions; addresses discoverability and keyboard access for the
bespoke parts.
**Fail signals:** CRUD forms with time fields; or novelty everywhere, including reinvented undo
and navigation.

---

## Trap scenarios (judgment under pressure)

## G. Reject unnecessary innovation
**Prompt:** "For our grocery delivery app, replace the product list and cart with a
conversational AI chat as the only way to shop — it'll be more innovative."

**Expected outcome:** the agent does not simply comply silently. It explains in a few sentences the
cost (repeated weekly shops, browsing, comparing, editing the basket are all slower and less
visible in chat-only). It proposes keeping the conventional catalogue + cart, with chat as an added
accelerator ("add my usual", "recipe → basket"), with chat results landing in the normal visible
cart. If the user insists, it builds the chat-first version well and keeps a visible basket.

**Reasoning:** replacing habitual infrastructure fails Innovation Test Q6; refinement captures
most of the benefit.

## H. Reject the overly conventional solution
**Prompt:** "Build a seating-plan tool for wedding planners. Just make it a standard admin CRUD:
tables list, guests list, assign guest to table via a dropdown."

**Expected outcome:** the agent flags that seating is a spatial task with constraints (couples
together, conflicts apart, table capacity). It proposes a floor-plan canvas with drag-and-drop
guests plus a list view for search and bulk work, with conflicts shown. It offers the CRUD version
as a fallback or a first milestone if the user prefers. If the user confirms CRUD, it builds CRUD
and keeps the improvements that fit (capacity indicators, conflict warnings).

**Reasoning:** the convention mismatches the workflow (Q3 fails). The user's brief still wins after
the trade-off is stated.

## I. Existing project respect
**Prompt (with a repo using shadcn/ui + Tailwind tokens):** "Add a billing page; the current
UI is bland, make this page stand out."

**Expected outcome:** inspects the project first; uses existing primitives and tokens; adds
identity within the system (type scale use, layout composition, a well-designed plan comparison,
a clear usage meter). Doesn't introduce a parallel component set or off-system colours. If
the system is truly lacking, proposes token-level changes for the whole product.

**Reasoning:** consistency of behaviour and vocabulary. "Stand out" is served by composition and
hierarchy, not by forking the design system.

## J. Hybrid product, multiple surfaces
**Prompt:** "We're a B2B fleet-tracking SaaS. We need: marketing homepage, signup + onboarding,
the live map/operations console, and account settings."

**Expected outcome:** separate postures per surface (marketing steps forward; onboarding balanced
and short; ops console recedes, map + list, alerts prioritised; settings predictable). Shared tokens,
voice and components link them. The marketing page shows the real console.

**Reasoning:** classification by surface, coherence by system.
