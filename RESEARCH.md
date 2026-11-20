# Research Notes: The Design-Skill Ecosystem

Research done for Seminal on 2026-11-20, by reading each project's actual instruction files (not
just READMEs). This file is for maintainers. Agents using the skill don't need it.

## What was inspected

| Project | Files read |
|---|---|
| Impeccable (pbakaus/impeccable) | `skill/SKILL.src.md`, `skill/reference/operate.md`, reference index |
| Taste (leonxlnx/taste-skill) | `skills/taste-skill/SKILL.md` (v2.5.1), reference index |
| UI UX Pro Max (nextlevelbuilder/ui-ux-pro-max-skill) | `.claude/skills/ui-ux-pro-max/SKILL.md`, `src/ui-ux-pro-max/data/ui-reasoning.csv` |
| Anti-Slop Atlas (phcodesage/anti-slop-atlas) | `README.md` ("The slop tells" and skill index) |
| Anthropic Frontend Design (anthropics/skills) | `skills/frontend-design/SKILL.md` |
| Emil Kowalski (emilkowal.ski, emilkowalski/skills) | "Great animations", "You don't need animations", `emil-design-eng` SKILL.md |
| Agent Skills spec (agentskills.io/specification) | Full specification |

## Findings

### Impeccable: critique vocabulary and surface modes
- **Strengths:** the most mature of the group. It has a command vocabulary (critique, audit,
  polish, harden, distill, bolder/quieter), *surface modes* (Persuade / Operate / Read /
  Experience) chosen per surface rather than per product, explicit "refinement preserves, redesign
  replaces" semantics, rendered-output verification, and an Operate reference that values "earned
  familiarity" and bans reinvented affordances.
- **Targets:** the full range, including native iOS/Android.
- **Limits for our goal:** familiarity is treated as a property of the Operate mode, not as a
  first-class analysis of *what users already expect from this category*. There's no category
  convention inventory, no reference-set step ("users arrive from Tokopedia"), and no explicit
  innovation test. It depends heavily on its own CLI/binary and project files (PRODUCT.md,
  DESIGN.md). Its overall voice ("out-of-distribution craft", "award-winning design director") pulls
  towards expression.

### Taste: high-end marketing-site execution
- **Strengths:** very concrete execution for company websites. Real photography, real product UI in
  the hero, copy discipline, an automated browser "finish gate" that checks the build.
- **Targets:** marketing/company websites by business kind (software, product, service, place).
- **Limits:** its house rules are hard requirements, for example: hover micro-animations on every
  linked card, "every page carries one dealt moment", "one section per screen", shader effects for
  tech. These are good for a landing page and wrong for an inventory table. It has no model of
  operational apps, dashboards, or task frequency. It explicitly says "never a generic dashboard"
  but never says how to design a real one. It requires Node 22 and a Chromium browser.

### UI UX Pro Max: a searchable pattern database
- **Strengths:** a large searchable dataset (styles, palettes, font pairings, 130 UX guidelines,
  chart types, 22 stacks), priority-ordered rule categories (accessibility first), stack detection,
  and "treat search results as recommendations".
- **Limits:** the reasoning is **preset-by-category**. In `ui-reasoning.csv`, "SaaS (General)" maps to
  "Glassmorphism + Flat Design" and its `if_data_heavy` rule also points to glassmorphism. Those are
  exactly the decorations that hurt dense operational UIs. It recommends a style for a category but
  doesn't analyse the user's existing mental model or the workflow. It's useful as a lookup tool,
  not as the source of judgment.

### Anti-Slop Atlas: the generic-output critique
- **Strengths:** a crisp list of AI-default "tells" (purple gradients, Inter everywhere, centred
  hero → 3 cards, untouched shadcn, glassmorphism, emoji icons, fade-up everywhere, buzzword copy)
  and a good map of tools (skills, DESIGN.md, MCP "eyes").
- **Limits:** the tells don't depend on context. "Inter or the system sans for everything" and
  "untouched component library" are often *correct* for an admin tool. Applied to operational UI,
  anti-slop pressure produces **novelty slop**: decorative type, effects and custom controls on
  tools that should disappear into the task.

### Anthropic Frontend Design: distinctive visual identity
- **Strengths:** grounds visual choices in the subject's world; plan → review against generic
  defaults → build → self-critique; "spend your boldness in one place"; strong writing guidance; a
  calibrated list of current AI-default looks, with the caveat "all traits are legitimate for some
  briefs".
- **Limits:** written from the stance of a design studio that wants every client to look unique. It
  is biased towards visual distinctiveness and the hero. It says little about operational density,
  product-category conventions or interaction patterns.

### Emil Kowalski: motion based on how often an action happens
- **Strengths:** the clearest principle in the ecosystem for *when not to* design something: animate
  based on frequency of use (no animation for keyboard-triggered or 100+/day actions), purpose
  before polish, short ease-out durations under ~300ms for UI, interruptible transitions,
  origin-aware popovers, reduced motion meaning "gentler", not "none".
- **Relevance:** this frequency logic generalises beyond motion. Seminal applies the same thinking to
  novelty, density and decoration.

## The gap Seminal fills

1. **Existing skills guard against one failure mode, not two.** They all fight *generic* output.
   None of them systematically fights *gratuitous novelty*: reinvented affordances, broken
   mental models.
2. **No skill keeps an inventory of user expectations by category.** Familiarity is treated as a
   mood ("operate mode is calmer"), not as a concrete list of conventions to keep, refine, replace or
   drop.
3. **No skill separates the three layers** (convention, identity, innovation) explicitly, so "make it
   distinctive" leaks into interaction design and "keep it familiar" leaks into visual blandness.
4. **No explicit innovation test** says when a bespoke interaction has earned its place.
5. **Presets replace judgment** in database-driven skills, and house rules for one surface type
   (marketing) are applied to others.

## Design decisions taken from the research

- Use **surface-level classification** (an idea Impeccable validates), but derive posture from five
  observable signals instead of four named modes, so hybrid surfaces are handled naturally.
- Generalise Emil's **frequency principle** into a "novelty budget".
- Treat Anti-Slop tells as **questions, not bans** ("decision or default?") and scope them by posture.
- Make specialist skills **optional executors** behind a routing table with explicit filters for
  each one's known blind spots.
- Keep the skill **dependency-free**: plain Markdown, one optional zero-dependency validator script,
  no CLI binary or hooks, so it works in any agent that supports the Agent Skills format.
