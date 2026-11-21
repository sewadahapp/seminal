# Validation

Workflow steps 9–10. Look at what you built, judge it against its purpose, fix real problems, and
report honestly. For layout-specific measurements, see [layout.md §6](layout.md).

## 1. Inspect (use what the environment offers)

In order of preference:
1. **Browser automation** (Chrome DevTools MCP, Playwright, Puppeteer, a browser extension, an
   agent's built-in browser). Render the page, screenshot the key states, interact with the flow.
2. **Headless screenshot script** (e.g. `npx playwright screenshot`) when there's no interactive browser.
3. **Build + tests + type check**, and existing visual-regression tests.
4. **Code review only.** Declare this explicitly as the evidence level.

Minimum inspection set for a UI change:
- Widths: ~375 (mobile), ~768, ~1280, plus ≥1440 for layouts with max widths.
- States: default with realistic data, empty, loading, error, and the longest realistic content.
- Interaction: complete the primary flow with the pointer, then with the keyboard only (tab order, visible
  focus, Esc closes overlays).
- Themes: light and dark if both exist. Reduced motion if motion was added.
- Console: no errors or warnings introduced.

Batch it: take one round of screenshots, fix everything they show, then take the next round. Don't
re-screenshot after each tiny edit.

## 2. Judge against purpose

Answer each question in a word or a sentence. "No" or "unsure" means a refinement task.

**Users and conventions**
- Would a user from the reference set know how to do the top three tasks without help?
- Did every Keep verdict end up implemented as users would recognise it?
- Is every bespoke interaction justified in the ledger, discoverable, and keyboard accessible?

**Identity**
- Swap test: does a competitor's logo look wrong on it? (Surfaces that step forward must pass. For
  receding surfaces, the bar is "precise and coherent", not "striking".)
- Clone test: is it clearly *not* a reskin of the reference product?
- Are the visual choices decisions or defaults? Name any defaults that stayed and why.

**Hierarchy and density**
- Is the focal point the user's most important decision or action?
- Is the density right for the posture? (Operators: enough rows to work. Readers: enough air to read.)

**Workflow efficiency**
- How many steps or clicks does the most frequent task take? Can any be removed?
- Are high-frequency actions free of animation and confirmation friction?

**Quality floor**
- Contrast, focus visibility, labels, semantic structure, target sizes, reduced motion.
- Responsive behaviour is structural and the primary action stays reachable on mobile.
- All states designed, with realistic content.
- Uses the existing components, tokens and architecture; no parallel mini design system.

**Generic-pattern check**
- Any unchosen defaults from visual-direction.md §6 present? Remove them, or record why they were chosen.

## 3. Refine

- Rank issues by user impact: broken task > misleading convention > accessibility failure >
  hierarchy/density problem > identity weakness > polish.
- Fix causes rather than symptoms. Fix a token, not 12 overrides; fix the flow, not the copy on a
  confusing button.
- Don't do polish loops that only move pixels around once the real issues are fixed.

## 4. Responding to vague feedback

"Looks off", "hard to read", "doesn't feel right" and "not what I pictured" are real signals, but
they don't say what to fix. Guessing and rebuilding costs a full loop. Instead:

1. **Measure the rendered UI.** Screenshot it and measure the area in question: edges, widths,
   spacing, alignment of repeated elements, contrast, type size. Without a browser, measure from
   the code and say that's what you did. Many "looks off" reports are a
   few pixels of misalignment or an inconsistent edge.
2. **List 2–3 concrete hypotheses**, each tied to something visible. For example: "the footer text
   doesn't share the nav's left edge", "the footer is a single text line where dashboards usually
   have an account block", "the column is left-aligned, so wide screens look lopsided".
3. **Sort them into defect or taste.** A defect (misalignment, low contrast, broken state) can be
   fixed right away; say what you fixed. A taste question (structure, layout form, feel) needs the
   owner: ask which product or screen they have in mind, or show 2–3 options (SKILL.md step 8).
4. **Say which one you'll act on and why**, in a sentence, before changing code.

Don't treat a taste signal as a bug, and don't polish the wrong thing in the meantime. Once the
owner names a reference, it becomes the target (SKILL.md step 3).

## 5. Validating innovation bets with people

Inspection proves a bespoke interaction *works*. It doesn't prove users *prefer* it. For each
innovation bet in the ledger, propose (don't fake) a check proportionate to its risk:
- A first-use test: can 5 representative users complete the core task without help? Note where
  they hesitate.
- A timed comparison against the conventional pattern for a frequent task.
- Staged rollout or A/B test with a success metric and a rollback path (keep the conventional
  fallback built).
- Monitoring after launch: usage of the bespoke path vs the fallback, error and abandonment rates.

## 6. Report

End with a short report:

```
Verified in browser: <what, at which widths/states>
Reviewed in code only: <what>
Not checked: <what, and why — e.g. no browser tooling, no backend data>
Ledger highlights: <the 2–4 decisions that shaped the result>
Known limitations / next steps: <…>
```

Never say "looks great", "fully responsive" or "accessible" without the evidence level next to it.
