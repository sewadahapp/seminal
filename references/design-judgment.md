# Design Judgment

How to make the calls in workflow step 5. Use the Convention Ledger, balance the tensions, and spend
novelty where it pays off.

## 1. The Convention Ledger

Make one row per significant convention on the surface. Five to fifteen rows is typical. Skip
trivia.

| Convention | Verdict | Reason | Notes |
|---|---|---|---|
| Search bar as primary entry | Keep | Users arrive from Tokopedia/Shopee; search is how they shop | Autocomplete with categories |
| Filter sidebar | Refine | Users expect it; usual weakness is dead-end zero results | Live result counts per option |
| Cart | Replace → booking basket | Rentals need dates per item; a quantity cart doesn't fit | Passed Innovation Test: Q3 fails |
| Wishlist | Drop | Not in v1 scope; no account system yet | — |

Verdict meanings:
- **Keep:** use the convention as users know it. Most rows end up here, and that is a success, not
  a lack of ambition.
- **Refine:** same mental model, better execution. This is where most valuable "innovation" really
  happens.
- **Replace:** a different interaction model. It requires the Innovation Test (SKILL.md) and a
  written problem statement.
- **Drop:** the convention is irrelevant to this product.

## 2. Separate the three layers explicitly

For each design idea, ask which layer it belongs to:

- "Product cards with a hand-drawn price tag style" → **Identity.** Fine, as long as price stays
  legible and scannable.
- "Products shown as a swipe deck instead of a grid" → **Innovation (Replace).** It must pass the test.
  For comparison shopping it fails: users need to see several options at once.
- "Filters show live counts" → **Convention, Refine.**
- "Checkout with a distinctive illustrated success screen" → **Identity** on a low-frequency moment.
  Good place for it.

When an idea mixes layers ("a bold new card layout"), split it: is the *layout* changing what users
can do (innovation), or how it looks (identity)?

## 3. Tensions to balance

These are not dials with presets. For each one, read the signals and decide for the specific surface.

| Tension | Lean towards the first when… | Lean towards the second when… |
|---|---|---|
| Familiarity ↔ originality | Frequent use, high stakes, broad or non-expert audience, established category | Rare use, persuasion, a new category, the brand is the differentiator |
| Efficiency ↔ exploration | Users know what they want; repeated tasks | Users are browsing, discovering, or learning |
| Density ↔ spaciousness | Experts, comparison, monitoring, large datasets | First-time users, storytelling, single decisions |
| Predictability ↔ flexibility | Shared workflows, compliance, money | Personal tools, power users who customise |
| Functional clarity ↔ visual expression | Operating and transacting surfaces | Brand, campaign, onboarding moments, empty states |
| Standard ↔ bespoke components | A design system exists; the task is common | No component fits the medium (canvas, timeline, novel data) |
| Brand expression ↔ neutrality | Few brand touchpoints, consumer surfaces | User content or data should be the hero (editors, dashboards, galleries) |

Different surfaces of the same product can sit at different points. Say why for each.

## 4. The novelty budget

Treat novelty as a budget that each surface spends. Users pay for every unfamiliar thing with
attention.

- **Spend it where the product is different from others.** A rental marketplace spends it on
  availability and dates, not on reinventing the product card.
- **Spend it on rare, high-emotion moments** (first run, success, milestone), not on actions that
  repeat dozens of times a day.
- **Don't spend it on infrastructure** such as navigation, forms, tables, auth, settings, or undo.
  Unfamiliar infrastructure taxes every other task.
- **Visual novelty is cheaper than interaction novelty.** A striking type system costs users
  nothing. A new scroll model costs them every time they scroll.

## 5. When to push back on the conventional

Reject the overly conventional solution when:
- The convention **actively mismatches** the workflow (a cart for a time-slot booking, a modal form
  for a 40-field record, a pie chart for change over time).
- The category convention is a **known dark pattern** (pre-checked add-ons, confirm-shaming,
  hidden fees). Don't preserve those.
- The surface's job is **persuasion or differentiation**, and the default output would pass the swap
  test (interchangeable with any competitor).
- The product is **genuinely new**, and borrowing a nearby category's model would mislead users about
  what it does.
- The medium needs **direct manipulation** that forms and tables cannot provide.

## 6. When to push back on novelty

Reject the unnecessary innovation when:
- It replaces a pattern users perform **habitually** (navigation, search, list → detail, back).
- Its benefit is **aesthetic only**, but its cost is behavioural (hidden controls, gesture-only
  actions, custom scrollbars, scroll-jacking).
- It **breaks the platform** (links that aren't links, broken back button, unselectable text,
  no keyboard path).
- It **looks impressive in a screenshot** but slows the 50th use.
- A **refinement** of the convention gets most of the benefit.

## 7. Explaining decisions

When a decision is non-obvious, or contradicts what the user might expect, write one sentence
naming the layer, the verdict and the reason. For example:

> "Kept a standard filter sidebar (convention). Users of this category expect it, and the
> distinctive part of the brand comes through the type and editorial category pages instead
> (identity)."

Don't write essays. Decisions that are obvious need no explanation.

## 8. Precedence when sources conflict

1. The user's explicit brief and constraints, including the visual references they give. Those
   govern composition and feel. Behaviour they imply still goes through the ledger: raise a
   conflict with a Keep verdict once.
2. Accessibility and legal requirements.
3. The existing product's working conventions (for changes to an existing product).
4. Category and platform conventions (Keep verdicts).
5. Identity and innovation choices.
6. Specialist-skill presets and stylistic defaults.

If the brief demands something that hurts users, such as removing a review step from money
transfers, do it if the user insists. Say the risk in one sentence and offer the safer alternative.
