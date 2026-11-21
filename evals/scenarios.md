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

---

## Steering scenarios (owner taste and feedback)

These come from dogfooding on a real redesign, where the agent verified its work well but built the
wrong direction three times because it never asked for the owner's references. They use the
steering rubric in [rubric.md](rubric.md). L and M assume an earlier turn. For plan-level runs,
send the *plan-level context* below with the prompt, as evals.json does. Build-level runs in a real
repo test measurement properly.

## K. Collection view: don't default to a table
**Prompt (repo: a Nuxt app built on a component library the owner also maintains):** "Redesign the
projects page of our app. Each project has a name, a status, a part count and a last-edited time.
The current table is hard to read. This app is also the showcase for our UI library."

**Plan-level context:** the page is a table with columns Name, Status, Parts, Last edited. A
typical user has 10–60 projects and opens this page several times a day to open one.

**Expected outcome:** inspects the current page, then shows 2–3 options before building, each named
after a familiar pattern: a cleaner table (Drive list view), a card per row (flight/train results,
GitHub repo list) and possibly a grid. Recommends one with a reason tied to what users do (they
scan names and status and open one; they rarely sort by column, so a card per row fits). Notes the
showcase context and asks whether the owner has a reference screen in mind. Keeps search, sort,
empty/loading states and keyboard navigation whichever form is chosen.

**Reasoning:** "frequent use → recede" doesn't imply a table. Unlike scenario B (operators comparing
stock across columns), these records are scanned, not compared. The owner's taste is a primary
input on a showcase product.

**Pass:** options shown before code; card list among them; recommendation reasoned from user tasks;
asks for or uses an owner reference; conventions kept.
**Fail signals:** restyles the table without offering alternatives; justifies a table only by
"recede"; builds one option and waits for correction.

## L. Vague "looks off" feedback
**Prompt (after the agent has built a sidebar):** "The sidebar footer that says 'Powered by Selaras'
looks off. Fix it."

**Plan-level context:** the sidebar the agent built (no account menu exists yet; account settings
live under a "Settings" nav item). Footer text starts 12px from the edge, nav labels 16px:

```vue
<aside class="flex h-full w-60 flex-col border-r">
  <div class="px-4 py-3"><AppLogo /></div>
  <nav class="flex-1 space-y-0.5 px-2">
    <NavItem v-for="item in items" :key="item.to" v-bind="item" class="px-2 py-1.5" />
  </nav>
  <footer class="border-t px-3 py-2 text-xs text-muted">Powered by Selaras</footer>
</aside>
```

**Expected outcome:** measures the footer in the rendered UI before changing anything. Lists 2–3
hypotheses, for example (a) its text doesn't share the nav items' left edge, (b) a single line of
text is unusual for an app sidebar footer, where users expect an account block (avatar, name,
menu) and sometimes a small promo card. Fixes any measurable defect and says so. For the structural
question, sketches 2–3 footer options or asks which dashboard the owner has in mind.

**Reasoning:** "looks off" is a taste signal, not just a defect report. Fixing alignment alone and
declaring it done fixed the wrong thing in the original session.

**Pass:** measures first; separates defect from taste; offers concrete footer options or asks for a
reference before rebuilding; reports evidence level.
**Fail signals:** nudges alignment and says "fixed"; rebuilds the footer into something new without
asking; claims it looks right without rendering it.

## M. Owner supplies a reference mid-task
**Prompt (turn 2, after the agent proposed left-aligned pages of different widths):** "[screenshot of
Claude's artifact list] I want our pages to feel like this."

**Plan-level context:** the earlier proposal was Workspace full width with 24px padding, Agents
`max-w-3xl` and Settings `max-w-2xl`, all left-aligned "for a consistent left edge". Describe the
screenshot in text: one centred column about 760px wide with equal side margins; title, then a
search field and "New" button on one row sharing the column edges; rows of title + grey subtitle
(type · edited time) separated by thin dividers; generous spacing; no table header.

**Expected outcome:** reads the screenshot for composition: one centred column, its approximate
width, the header/toolbar/content sharing edges, spacing and density. States what changes from its
earlier plan. Applies the rule to every section through a shared layout primitive, not just the page
in view. Keeps the product's own type, colour and voice (doesn't copy the reference's brand) and
keeps behaviour conventions. Verifies by measuring column edges across sections.

**Reasoning:** an owner-supplied screenshot is the target composition (SKILL.md step 3). It
outranks the agent's own convention guess for layout and feel.

**Pass:** adopts the reference's composition; applies it product-wide; keeps own identity; says what
changed; verifies by measurement.
**Fail signals:** argues for its earlier layout; applies the change to one page only; copies the
reference's visual brand.

## N. Consistent margins across sections
**Prompt (repo with Workspace, Agents and Settings pages):** "Workspace, Agents and Settings all have
different margins and widths. Make them consistent."

**Plan-level context:** `layouts/default.vue` is a sidebar plus `<main class="flex-1 overflow-y-auto">`.
Workspace root `<div class="p-6">` (full width, `sticky top-0` toolbar, grid of project cards);
Agents `<div class="mx-auto max-w-4xl px-8 py-6">`; Settings `<div class="max-w-2xl p-4">`.

**Expected outcome:** measures each section's content column (left/right edges, max-width) at ≈1280
and ≥1440. Proposes one rule: a small set of named widths and one alignment, centred or left, shown
as options if both fit, with a recommendation. Implements it once in a shared layout component or
token. Reserves the scrollbar gutter. Checks that page header, toolbar and sticky elements still
line up. Re-measures every section and reports the numbers.

**Reasoning:** consistency is a system decision (fix the system, not the instance), and only
measurement proves it.

**Pass:** measurements before and after; a shared primitive; one alignment rule; sticky/toolbar checked;
honest evidence level.
**Fail signals:** per-page padding tweaks; "looks consistent now" without numbers; mixed alignment left
in place.

## O. No one to ask
**Prompt:** "Redesign the home screen of our open-source note-taking app. Work autonomously; I'm
away until tomorrow, so don't wait for me."

**Plan-level context:** React, Tailwind, shadcn/ui. The home screen shows a "Recent notes" list, a
"New note" button and a tag cloud.

**Expected outcome:** doesn't stop to ask. Notes that on an open-source app the UI is also the
project's showcase. Picks a direction, writes down the reference and posture it assumed and the
options it considered, builds the recommended one, validates it, and lists the alternatives as
concrete follow-ups in the report.

**Reasoning:** the steering guidance must not block autonomous runs. The fallback is to state the
assumption and offer the alternatives.

**Pass:** builds without blocking; states the assumed reference/posture; lists alternatives
concretely; honest validation report.
**Fail signals:** ends the turn with questions and nothing built; or builds silently with no stated
assumptions or alternatives.
