# Seminal Evaluation Rubric (v3)

v3 adds the steering rubric for scenarios K–O (owner references, options, vague feedback).

v2 changes after the first evaluation run: added *Brief coverage*; made layer separation and
validation substantive rather than about section headings; trap scenarios now use a dedicated
judgment rubric.

## Design scenarios (A–F, I, J)

Score each criterion 0–2. 0 = absent or wrong, 1 = partial, 2 = clear and correct. Max 18.
**Score the substance, not the headings:** a labelled section with generic content scores 1 at
most. An unlabelled but correct decision can score 2.

| # | Criterion | What 2 looks like |
|---|---|---|
| 1 | **Context understanding** | Users, frequency, stakes, expertise identified; assumptions flagged |
| 2 | **Reference set and mental model** | Realistic reference products (or an incumbent tool like spreadsheets); the model extracted, not visuals |
| 3 | **Surface classification** | Density, motion, colour and type decisions visibly follow from frequency/stakes/intent, not from industry stereotype |
| 4 | **Convention judgment** | Keeps what users rely on; refines weak spots; replacements justified; nothing replaced on whim |
| 5 | **Layer separation** | At least one decision shows identity expressed *without* changing behaviour, or innovation justified independently of looks |
| 6 | **Identity** | Levers specific to the subject; not a reskin of the reference product; bar scaled to posture |
| 7 | **Innovation judgment** | Innovates where the workflow demands; declines novelty that fails the test; trade-offs explained briefly |
| 8 | **Implementation & validation readiness** | Concrete states and patterns; respects the existing system; validation steps specific to *this* design (not a boilerplate line) |
| 9 | **Brief coverage** | Every object and task named in the prompt has a place in the design |

**Pass:** ≥14/18, and no 0 on criteria 4, 7 or 9.

## Trap scenarios (G, H)

Max 8. Pass ≥6 with no 0.

| # | Criterion | What 2 looks like |
|---|---|---|
| T1 | **Diagnosis** | Correctly identifies why the requested approach is a poor fit for this workflow |
| T2 | **Advocacy** | Recommends a concrete better design (a flow, a phased plan), not a vague "maybe later" |
| T3 | **User authority** | Raises it once, asks or proceeds as appropriate, and shows how the requested version would be built well |
| T4 | **Brief coverage** | The requested version and the alternative both cover the brief's objects and tasks |

## Steering scenarios (K–O)

Score each applicable criterion 0–2 (three per scenario, so max 6). Pass at ≥5/6 (75% of the
applicable maximum), with no 0.

| Scenario | Applicable | Note |
|---|---|---|
| K | S1, S2, S4 | |
| L | S2, S3, S4 | Asking for a reference counts under S2 |
| M | S1, S2, S4 | S4 must include measurement across sections; promising it without saying what is measured scores 1 |
| N | S2, S3, S4 | |
| O | S1, S2, S4 | |

| # | Criterion | What 2 looks like |
|---|---|---|
| S1 | **Owner input** | Asks for or uses the owner's visual references at the right moment; if no one can be asked, states the reference it assumed |
| S2 | **Options before build** | Shows 2–3 concrete options named after familiar patterns, with a reasoned recommendation, before writing code, when more than one fits |
| S3 | **Defect vs taste** | Measures before fixing; separates measurable defects from taste questions and handles each appropriately |
| S4 | **Conventions and honesty** | Keeps behaviour conventions whatever the look; layout verified by measurement; evidence level stated |

## Automatic fail conditions (all scenarios)
- Claims visual validation without having rendered anything.
- Copies a reference product's visual identity (palette, signature chrome) on a "not a clone" brief.
- Replaces habitual infrastructure (navigation, search, cart, undo, back) without a stated problem.
- Applies expressive marketing treatments (decorative motion, display type in data, effects) to a
  high-frequency operational surface.

## Known rubric limits
- Plan-level runs can't test project inspection (scenario I) or real rendering. Use build-level
  runs in a real repo for those.
- Graders should run blind (strip condition labels from files) and should not reward length.
