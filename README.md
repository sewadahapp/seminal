# Seminal

**Design with judgment, not just taste.**

Seminal is a context-aware interface design skill for AI coding agents, following the
[Agent Skills specification](https://agentskills.io/specification). It teaches an agent to decide
what in an interface should stay **familiar**, what should be **refined**, what should express the
product's **identity**, and what genuinely deserves **innovation**, and then to build and validate
the result honestly.

> Borrow familiarity, preserve usability, express identity, innovate with intention.

## Layout

```
seminal/
├── SKILL.md                         # Core model + 10-step workflow (loaded on activation)
├── references/                      # Loaded on demand (progressive disclosure)
│   ├── product-conventions.md       # What users expect, per product category + platforms
│   ├── design-judgment.md           # Convention Ledger, tensions, novelty budget, precedence
│   ├── interface-classification.md  # Surfaces, five signals, posture
│   ├── ux-patterns.md               # IA, flows, tables, forms, states, a11y, responsive
│   ├── visual-direction.md          # Identity levers, density, colour roles, motion budget
│   ├── layout.md                    # Content column, list vs cards vs table, app shell
│   ├── existing-projects.md         # Inspecting and respecting existing design systems
│   ├── validation.md                # Inspection, judgment questions, honest reporting
│   ├── specialist-integration.md    # Optional routing to Impeccable, Taste, UI UX Pro Max, …
│   └── examples.md                  # 17 good/bad decisions with reasoning
├── assets/design-decision-record.md # Template for the planning artefact
├── evals/                           # Regression scenarios, rubric, evals.json
├── scripts/validate_skill.py        # Zero-dependency spec + link check
└── RESEARCH.md                      # Ecosystem research (maintainers only)
```

## Install

Copy or symlink the `seminal/` directory into your agent's skills folder, for example:

- Claude Code: `~/.claude/skills/seminal` or `<project>/.claude/skills/seminal`
- Other Agent-Skills-compatible agents: their skills directory (often `.agents/skills/`)

The skill is plain Markdown with no runtime dependencies. Browser tooling (Chrome DevTools MCP,
Playwright, etc.) is used for validation when available.

## Validate

```bash
python3 scripts/validate_skill.py      # frontmatter, length, links, evals.json
skills-ref validate .                  # official validator, if installed
```

## Evaluate

See [evals/scenarios.md](evals/scenarios.md). Run each prompt with the skill loaded, then score it
using [evals/rubric.md](evals/rubric.md). Compare against a run without the skill to see the
skill's effect.
