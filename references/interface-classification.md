# Interface Classification

Workflow step 4. Classify **surfaces**, not products. A SaaS product can contain a landing page,
a sign-up flow, onboarding, a daily workspace, an analytics area, settings, and an admin
console. Each surface gets its own posture, inside one coherent identity.

## Step A: list the surfaces

Write each distinct surface with its primary job in one line:

```
Marketing site    — persuade a team lead to start a trial
Onboarding        — get a new user to their first imported dataset
Workspace         — daily triage of incoming orders (operators, 6h/day)
Reports           — weekly review by managers
Settings / admin  — occasional configuration by an owner
```

## Step B: read five signals per surface

| Signal | Ask | Low end | High end |
|---|---|---|---|
| **Frequency** | How often does a user come back to this surface or action? | Once / rarely | Many times per hour |
| **Stakes** | What happens if they get it wrong? | Nothing / easily undone | Money, data loss, safety, legal |
| **Expertise** | How fluent is the user in the domain and tool? | First-timer | Daily expert |
| **Intent** | What is the user trying to do? | Be persuaded · learn · explore | Transact · operate · create |
| **Density** | How much information must be visible at once to decide? | One message | Hundreds of records |

## Step C: write the posture

From the signals, write one or two sentences saying how far the interface should **recede**
(get out of the way of the task) or **step forward** (express, guide, persuade). For example:

> Workspace: high frequency, high expertise, high density, operate intent → recede. Compact
> table-first layout, keyboard paths, restrained colour reserved for state, no decorative motion.
> Identity through type, numerals and microcopy only.

> Marketing site: rare, low stakes, persuade intent → step forward. Expressive type and
> composition, show the real product UI, one strong motion moment, conventional nav and CTA.

### The three posture words
- **Recede:** the task and data are the hero. The interface is quiet, dense where needed, and
  familiar. Identity shows only in precise details.
- **Balanced:** content leads, and brand chrome frames it with visible personality. Typical for
  consumer browse surfaces (marketplace home, media rows, onboarding). Merchandising and editorial
  areas can be expressive. The controls (search, filters, cart, player) stay conventional and calm.
- **Step forward:** the design is part of the message. Expressive type, composition, imagery and
  motion, around conventional navigation and calls to action.

These are positions on a spectrum, not modes. Write the sentence that explains *why*; the word
alone isn't enough.

## Common surface types (shorthand, not templates)

| Surface type | Typical signals | Typical posture | Novelty budget |
|---|---|---|---|
| Landing / marketing | rare, low stakes, persuade | Step forward | High (visual), low (navigation) |
| Editorial / docs | occasional, learn | Recede into readability, identity in type | Low–medium |
| Consumer browse (marketplace, media) | frequent, low–medium stakes, explore | Balanced: content-forward with brand chrome | Medium (merchandising), low (flows) |
| Transaction (checkout, transfer, booking) | occasional, high stakes, transact | Recede, trust-first | Very low |
| Onboarding / first run | once, medium stakes, learn | Step forward gently, short | Medium |
| Operational workspace (admin, inventory, CRM, support) | very frequent, expert, dense, operate | Recede strongly | Low; refine, don't replace |
| Analytics / monitoring | frequent, decision-making, dense | Recede; data is the hero | Low (chrome), medium (visualisation, if justified) |
| Developer tool | frequent, expert, dense | Recede; follow developer conventions | Low, except system visualisation |
| Creative tool (canvas, timeline) | frequent, expert, create | Frame recedes; core manipulation may be bespoke | High for core interaction only |
| Settings / account | rare, medium stakes | Recede, predictable | Very low |
| Empty / success / milestone states | rare, emotional | Step forward | Medium–high |

## Hybrid and multi-surface products

- **Coherence comes from the system, not sameness.** Share tokens (colour roles, type families,
  radius logic, spacing scale), voice, iconography, and component behaviour. Vary density,
  type scale, and expressiveness by surface.
- **Transitions between surfaces matter.** Marketing → sign-up → onboarding → workspace should feel
  like one product getting more focused, not like four different vendors.
- **The marketing site may show the product.** Show the real workspace UI, not an imaginary,
  more decorative version of it.
- **Two audiences, one dataset** (e.g. analysts exploring daily, executives reviewing weekly): treat
  them as two surfaces over the same data. Give the explorers flexible filters, drill-down and
  saved views. Give the reviewers a curated, annotated, stable view (a saved report, a digest)
  that uses the same metric definitions and links into exploration.
- **Mixed-intent screens:** a home dashboard that is both overview (scan) and launch pad (act).
  Order by the user's most frequent next action, not by what looks balanced.

## Classification mistakes to avoid

- Classifying by **industry** ("fintech → dark mode, gradients") instead of by surface and signals.
- Treating the **whole product** as one posture (an expressive landing-page style leaking into the admin).
- Assuming **B2B = boring** or **consumer = playful**. Read frequency, stakes and intent instead.
- Ignoring **who** uses a surface: an internal ops tool used 8 hours a day by trained staff differs
  from the same data shown to customers once a month.
