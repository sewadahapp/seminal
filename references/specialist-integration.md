# Specialist Skill Integration (Optional)

Seminal is the decision and methodology layer. Specialist skills are execution layers. Use them
only if they are installed, and only after Seminal's steps 1–5 have produced a posture per surface
and a Convention Ledger. Seminal never depends on them.

## Detecting what's available

Check the agent's skill listing or skill directories (e.g. `.claude/skills/`, `.agents/skills/`,
`~/.claude/skills/`, plugin directories). Don't install anything without the user's consent.

## Routing table

| Need | Specialist (if present) | How Seminal uses it | Filter to apply |
|---|---|---|---|
| Visual direction and execution on surfaces that step forward (landing, campaign, brand) | **Taste**, **Frontend Design** | Hand over the identity levers and the ledger. Let it execute composition, type, imagery and moments | Keep conventional nav, CTA and pricing findability. Taste's marketing-site house rules (mandatory moments, hover lift on cards, one section per screen) **do not** transfer to app or dashboard surfaces |
| Critique, audits, polish, hardening | **Impeccable** (`critique`, `audit`, `polish`, `harden`, `clarify`, `adapt`) | Run after implementation as an extra review pass. Map its findings to Seminal's layers | Findings that would reduce familiarity on a receding surface need a ledger check before applying |
| Pattern and style lookup, stack-specific guidance, chart types | **UI UX Pro Max** (`search.py --domain`, `--stack`) | Query for specific components or stack implementation details | Treat style and palette presets as suggestions. Reject presets that clash with posture (e.g. glassmorphism or heavy effects on dense operational data) |
| Spotting generic output | **Anti-Slop Atlas** tells, Impeccable detector | Use as a *questions list* during validation | A tell is a problem only when unchosen. Don't add decoration to an operational tool to avoid "plain" |
| Motion and micro-interaction craft | **Emil Kowalski's design-engineering skills** (e.g. animation review/remove skills), Impeccable `animate` | Apply after deciding the motion budget by frequency | No animation on keyboard or very frequent actions, regardless of what the specialist suggests for flair |
| Charts and dashboards | Any installed data-visualisation skill | Chart form, colour scales, KPI tiles | Chart choice follows the analytical question in the ledger |
| Accessibility debugging | Browser a11y tooling or skills | Validation step | — |

## Handoff format

When delegating to a specialist (another skill in the same session, or a sub-agent), pass:

```
Surface: <name> — posture: <recede|balanced|step forward> — why: <signals>
Keep (do not change): <list of ledger Keep items>
Identity levers: <2–4 levers with concrete direction>
Innovation bets: <list, or "none">
Constraints: <stack, component library, tokens, brand assets>
Ask: <what the specialist should do>
```

## Conflict resolution

1. Follow the precedence order in [design-judgment.md §8](design-judgment.md). Specialist rules come last.
2. If a specialist rule conflicts with a Keep verdict (e.g. "never use the system font", "every
   section needs a moment"), follow the ledger on receding surfaces. On surfaces that step forward,
   let the specialist lead unless it touches a usability convention.
3. If two specialists disagree on style, pick the one whose stated target matches the surface type
   (Taste: marketing sites; Impeccable Operate mode: product UI).

## Avoid duplication

Don't re-implement a specialist's deep content (detector rules, style databases, motion recipes)
inside Seminal's output. Seminal's value is deciding *which* specialist capability applies, *where*,
and *how much*.
