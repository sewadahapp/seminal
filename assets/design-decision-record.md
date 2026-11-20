# Design Decision Record — <product / surface>

> Fill this in before building a new product or surface. Keep it short: bullets, not essays.
> Save it next to the code (e.g. `docs/design/<surface>.md` or in `DESIGN.md`) if the project
> keeps design docs.

## 1. Product and users
- **Purpose:** <what the product/surface is for, one sentence>
- **Users:** <who, expertise, context of use>
- **Frequency / stakes:** <how often, what goes wrong if they err>
- **Assumptions:** <anything inferred rather than given>

## 2. Existing project (or "greenfield")
- **Stack / components / tokens:** <…>
- **Patterns to preserve:** <…>

## 3. Reference set and mental model
- **Users arrive from:** <2–5 products>
- **Mental model:** <the flow/structure they expect>

## 4. Surfaces and posture
| Surface | Job | Signals (freq · stakes · expertise · intent · density) | Posture |
|---|---|---|---|
| | | | recede / balanced / step forward |

## 5. Convention Ledger
| Convention | Verdict (Keep/Refine/Replace/Drop) | Reason |
|---|---|---|
| | | |

## 6. Identity levers (2–4)
- <lever>: <concrete direction, e.g. "Type — a condensed grotesk for prices and headings, Inter-like body; tabular numerals">

## 7. Innovation bets (zero is fine)
| Bet | Problem it solves | Innovation Test notes | Fallback if it fails |
|---|---|---|---|

## 8. Key UX states and flows
- **Top 3 flows (steps):** <…>
- **States designed:** empty (first use / no results) · loading · error · partial/stale · success · no permission · <domain-specific, e.g. payment pending>

## 9. Identity check
- **Swap / clone / default tests:** <one line each; bar scaled to posture>

## 10. Validation plan
- **Widths / states / flows to inspect:** <…>
- **Tooling available:** <browser automation / screenshots / code only>
- **Innovation bets to test with users:** <first-use test, A/B, metric, fallback>

## 11. Open questions for the user
- <only questions whose answer would change the direction>

> Length: aim for about one screen per surface. For multi-surface products, keep the shared parts
> (users, reference set, identity levers) once and add a short posture + ledger per surface.
