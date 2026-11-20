---
name: seminal
description: Context-aware interface design methodology. Decides what in a UI should stay familiar, what should be refined, what should carry brand identity, and what genuinely deserves a new interaction — before and while building. Use when designing, redesigning, building, or reviewing any user interface (landing pages, marketplaces, e-commerce, SaaS, dashboards, admin panels, analytics, developer tools, creative apps, mobile or desktop apps), when choosing between conventional and bespoke patterns, when a design feels generic or, conversely, needlessly strange, or when coordinating other design skills.
license: MIT
metadata:
  version: "1.1.0"
  philosophy: "Design with judgment, not just taste."
---

# Seminal

**Borrow familiarity, preserve usability, express identity, innovate with intention.**

Seminal is a decision layer. It does not prescribe a look. It makes you work out what users already
expect, which of those expectations to keep, where the product's identity should show, and which
problems — if any — deserve a new solution. Then it makes you build that and check it honestly.

## The core model: three layers, decided separately

Every interface decision belongs to one of three layers. Agents make bad design when they mix them up.

| Layer | Question | Default stance |
|---|---|---|
| **Convention** | How do users expect this kind of product to *work*? | Keep it, unless it fails this workflow |
| **Identity** | What makes this product *recognisably itself*? | Express it deliberately; never borrow another product's |
| **Innovation** | What new behaviour makes the experience *meaningfully better*? | Earn it with a named problem it solves |

Consequences:

- Familiar UX does not mean familiar visuals. A marketplace keeps search → results → filters →
  product page → cart → checkout, and still looks like no other marketplace.
- Visual originality does not license interaction originality, and the reverse holds too.
- "Generic" is a failure of the Identity layer. "Confusing" is usually a failure of the Convention
  layer. "Gimmicky" is a failure of the Innovation layer. Diagnose before fixing.

There are two failure modes, and Seminal guards against both:

1. **Conformity slop:** default kit components, no point of view, could be any product.
2. **Novelty slop:** reinvented affordances, decorative motion and clever navigation that make users relearn
   things they already knew.

## Workflow

Scale the depth to the task. For a one-component tweak, steps 1–5 can take a few sentences. For a
new product or surface, write them down as a Design Decision Record (template:
[assets/design-decision-record.md](assets/design-decision-record.md)). Aim for about one screen
per surface.

**What to load, by task** (load only what the task needs):

| Task | Load |
|---|---|
| Small change in an existing UI | existing-projects, plus ux-patterns or visual-direction for the part you touch |
| Plan or direction only (no code yet) | product-conventions (the relevant section), interface-classification, design-judgment |
| New surface or product, built end to end | All step references, as each step comes up |
| Review or critique of an existing UI | validation, design-judgment, product-conventions (the relevant section) |
| A ledger call feels close | examples |

### 1. Understand the product and its users
Establish: what the product is for, who uses it, how often, at what expertise level, and what is at
stake when they get it wrong. If the brief is silent on this, infer it from the codebase, data
model, copy and routes, state your assumptions explicitly, and ask only when a wrong guess would change
the design's direction.

### 2. Inspect the existing project (skip only for an empty folder)
Read before deciding: component library, tokens, theme, layout shell, routing, existing pages,
copy voice, responsive approach. Working decisions are preserved by default. If the user only
describes the stack and you can't see the code, plan against what they described, list what you
would check, and confirm before building.
→ [references/existing-projects.md](references/existing-projects.md)

### 3. Map expectations: the reference set
Name the 2–5 products users most likely arrive from (e.g. an Indonesian marketplace: Tokopedia,
Shopee; an issue tracker: Jira, Linear, GitHub Issues). From them, extract the **mental model**,
not the visuals. Then list the conventions for this category. For internal tools, the reference set is
often a spreadsheet, a legacy system or paper. Find out what users would lose by leaving it (bulk
paste, free-form sorting, keyboard speed) and keep those.
→ [references/product-conventions.md](references/product-conventions.md)

### 4. Classify each surface
One product has many surfaces (marketing site, onboarding, workspace, analytics, settings, admin).
Classify each surface on its own by reading five signals: **frequency of use, stakes, user expertise,
intent** (transact / operate / explore / learn / create / be persuaded), and **information density**.
Together they give the surface's *posture*: how much the interface should step back from the task
or step forward to express itself.
→ [references/interface-classification.md](references/interface-classification.md)

### 5. Decide strategy: the Convention Ledger
For each significant convention on the surface, record a verdict:

- **Keep:** users expect it and it fits. (Most entries.)
- **Refine:** keep the model, fix a known weakness (better filter feedback, clearer empty state).
- **Replace:** only after passing the Innovation Test below. Write down the problem it solves.
- **Drop:** the convention doesn't apply to this workflow at all.

Then name the **identity levers** for the surface. These are where the brand shows: type, colour, composition,
imagery, voice, component shape, signature interactions. Then name the **innovation bets** (zero is a
valid number).
→ [references/design-judgment.md](references/design-judgment.md)

### 6. Establish UX and interaction patterns
Information architecture, navigation, the core task flows, component behaviour, forms and
validation, feedback, every state (empty, loading, partial, error, success, offline, no permission),
recovery and undo, keyboard and screen-reader access, and responsive behaviour. Decide these *before*
styling.
→ [references/ux-patterns.md](references/ux-patterns.md)

### 7. Establish or reuse the visual system
Reuse the project's system if one exists. Otherwise, derive tokens from the identity levers and the
surface posture: density, type scale, colour roles, surface treatment, motion budget.
→ [references/visual-direction.md](references/visual-direction.md)

### 8. Implement
Work in the project's own framework, components and conventions. Use real or realistic content
(real product names, realistic numbers, long and short strings, empty datasets), not lorem ipsum
in a perfect 3-row table.

### 9. Inspect and validate
Look at the rendered result. If browser tooling exists, screenshot the key states at mobile and
desktop widths, and exercise the core flow with keyboard and pointer. Then run the validation questions.
→ [references/validation.md](references/validation.md)

### 10. Refine based on actual problems
Fix what inspection found, in order of user impact. Don't do polish passes that only move pixels
around. Then report what was verified, what was only reviewed in code, and what was not checked.

## The Innovation Test

Before replacing or inventing a pattern, answer these questions honestly:

1. Is there an established convention for this interaction?
2. Will users understand and expect it?
3. Does the convention actually fit *this* workflow, data and user?
4. What specific, nameable problem does the change solve?
5. What does it cost in learning, discoverability, accessibility, platform consistency, and effort?
6. Could refining the existing pattern get most of the benefit?
7. Is the novelty useful to users, or only visually interesting?

**Decision rule:** proceed only when **both** hold:
- **A real gap:** the convention doesn't fit (3 = no), *or* the change solves a nameable problem
  users actually have (4), and
- **No cheaper path:** refining the convention would not get most of the benefit (6 = no), and the
  costs in (5) are proportionate to that benefit.

If the honest answer to (7) is "only visually interesting", it is an identity decision, not an
innovation. Move it to the identity layer and keep the behaviour conventional. A bespoke interaction must also hold up on its 50th use, not just its first. It must be
discoverable without a tutorial, or teachable in one moment. It must be accessible by keyboard and
screen reader, and it must not break platform expectations (back button, links, selection, copy,
scroll).

## The Identity Tests

- **Swap test:** put a competitor's logo on the screen. If nothing feels wrong, the identity layer
  is empty.
- **Clone test:** if a screenshot could be mistaken for the reference product, you borrowed its
  skin instead of its model. Change the identity layer, not the conventions.
- **Default test:** list the choices you made because they were defaults (framework theme, stock
  font, kit radius, stock gradient). Keep a default only when it was chosen on purpose. On an
  operational tool, many defaults are *correctly* chosen.

## Posture rules of thumb (signals, not presets)

- High frequency + expert users + high density → the interface recedes. Familiar patterns,
  keyboard paths, compact density, restrained colour, near-zero decorative motion. Identity lives in
  precision: type, spacing rhythm, data formatting, microcopy, one accent.
- Transactional consumer flows → conventions carry trust. Identity lives in brand surfaces such as
  merchandising, imagery, voice and promo moments. Checkout and payment stay boring.
- Persuasion surfaces (landing, campaign) → the widest licence for visual experimentation. Still
  keep conventional navigation, clear CTAs, readable text and fast loading.
- Creative and exploratory tools → a larger innovation budget when the task really has no good
  precedent (spatial canvases, timelines, novel manipulation). Keep the frame — file, edit, undo,
  export, settings — conventional.
- Data/analytics → chart choice follows the question being asked. Hierarchy follows the decision the
  user makes. Decoration competes with data.

Different surfaces of one product can take different postures. Keep them coherent through shared
tokens, voice and component behaviour, not by making every page look the same.

## Working with specialist skills (optional)

Seminal decides; specialists execute. If skills such as Impeccable, Taste, UI UX Pro Max,
Anti-Slop references, Frontend Design, or motion/design-engineering skills are installed, route
work to them after steps 1–5. Filter their output through the Convention Ledger. A specialist
preset never overrides a Keep verdict on a high-frequency surface.
→ [references/specialist-integration.md](references/specialist-integration.md)

Seminal works fully without any of them.

## Honesty rules

- Never claim you visually validated something you did not render and look at. Say "verified in
  browser", "reviewed in code only", or "not checked", whichever is true.
- State your assumptions about users and their reference products. Don't present guesses as research.
- When the user asks for something that fails the Innovation Test (or for a convention that
  mismatches the workflow), raise it **once, in the first reply**: one or two sentences on the
  trade-off, and the alternative you recommend. Then ask which way to go, or, if the task is
  meant to run without interruption, build what they asked for and offer the alternative as a
  follow-up. Don't silently substitute your preference, and don't re-argue after they decide.
  Make the alternative concrete enough to choose: a sketch of the flow, a phased plan. Don't wave
  at it as "optional later". A recommendation the user can't evaluate isn't one.
- Cover the whole brief. Before finishing, check that every object and task the request names
  (e.g. "moves *and* formations", "logs *and* env vars") has a place in the design.

## More

- Good and bad decisions, worked through: [references/examples.md](references/examples.md)
  (useful whenever a ledger call feels close).
- Skill maintainers: the `evals/` directory holds regression scenarios. Agents doing design work
  should not read it.
