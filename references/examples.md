# Good and Bad Design Decisions

Worked examples of the judgment Seminal asks for. Each one names the layer, the verdict, and the
reason.

---

## 1. Rental marketplace: cart vs booking basket
**Bad:** Keep the e-commerce cart with a quantity stepper because "marketplaces have carts".
**Good:** Replace the quantity cart with a basket where each item carries its own rental dates and
availability check. Keep the cart icon, count badge and location. **Why:** the convention mismatches
the workflow (Innovation Test Q3 fails). The icon and placement stay familiar, so users still find
it.

## 2. Marketplace: swipe deck discovery
**Bad:** Replace the results grid with a Tinder-style swipe deck "to make browsing fun".
**Good:** Keep the grid. Spend identity on card art direction, price typography and category pages.
**Why:** shoppers compare options side by side. A deck shows one item at a time and hides the
alternatives. The novelty is visual-only in benefit and behavioural in cost.

## 3. Marketplace identity without imitation
**Bad:** Orange header, dense flash-sale banners and a coin-voucher system copied from Shopee.
**Good:** Same structure (search-first header, category rail, product grid, voucher field at
checkout), with the brand's own deep green, a characterful grotesk for prices, illustrated category
icons drawn in-house, and calm promo slots. **Why:** borrow the model, not the skin. Clone test.

## 4. Inventory dashboard: cards vs table
**Bad:** Products displayed as large image cards with shadows, 8 per screen, plus three decorative
KPI charts above.
**Good:** A dense sortable table (SKU, name, location, on hand, reserved, available, reorder point,
status), sticky header, bulk-action bar on selection, saved filters, low-stock shown with icon + text
+ colour. The KPI strip is reduced to the two numbers operators act on (low stock count, pending
transfers), both linking to filtered views. **Why:** high frequency, expert users, comparison across
records. The posture is recede.

## 5. Inventory dashboard: over-correcting into "anti-generic"
**Bad:** Avoiding the "generic" look by using a display serif for table headers, a cream background,
and animated row entrances.
**Good:** System or neutral sans, tabular numerals, one accent for selection and primary actions.
Identity comes from microcopy and crisp state colours. **Why:** anti-generic rules apply to
surfaces that step forward. Here, familiarity *is* the quality bar.

## 6. Analytics: chart choice
**Bad:** A donut chart of revenue by month; a 3D bar chart; eight-colour pie for channel share.
**Good:** Revenue over time → line with comparison period. Channel share → sorted horizontal
bars with values. Conversion funnel → funnel or stepped bars with drop-off %. **Why:** chart
form follows the question (trend, ranking, flow).

## 7. Analytics: dark "mission control" for a monthly review
**Bad:** Neon-on-black dashboard with glowing gradients for a finance team reviewing monthly results.
**Good:** Light theme with dark mode available, a calm palette, annotated anomalies, export to
CSV/PDF. **Why:** signals say occasional, decision-oriented, shared in meetings. "Futuristic" serves
nobody here.

## 7b. Counter-example: dark is right for a 24/7 operations room
**Bad:** Applying #7 mechanically and shipping a bright white theme for a dispatch console shown on
wall displays in a dim control room overnight.
**Good:** A dark default chosen for the *environment* (dim room, long shifts, wall screens). Calm
neutrals, colour reserved for alert severity, and a light theme available. **Why:** theme follows
the usage context, not the industry stereotype, in both directions.

## 8. Landing page: too conventional
**Bad:** A gradient blob hero with "Supercharge your workflow", three icon feature cards,
testimonial carousel, CTA band. It passes the swap test for any SaaS.
**Good:** Open with the product doing its job (an interactive diff for a code-review tool),
type-led composition specific to the domain, one orchestrated reveal, then proof and pricing. Keep
standard nav and CTA placement. **Why:** a persuasion surface; the identity layer was empty.

## 9. Landing page: scroll-jacking
**Bad:** A pinned, scroll-jacked storytelling sequence that takes 12 wheel turns to reach pricing.
**Good:** Native scroll, with one scroll-linked moment that doesn't trap the user. Pricing is
reachable from the nav. **Why:** visual freedom doesn't extend to breaking navigation.

## 10. Developer tool: logs
**Bad:** Logs rendered in proportional font inside rounded cards with relative timestamps only.
**Good:** Monospace virtualised log stream, absolute timestamps (relative on hover), level filter,
search with highlight, follow/tail toggle, copy-line and permalink, wrap toggle. **Why:** these are
developer conventions, and logs are scanned under pressure.

## 11. Developer tool: config editor
**Bad:** Forcing a 60-key YAML config into a giant form wizard.
**Good:** Both: a structured form for the common 10 keys with validation, and a code editor with
schema validation and diff-before-apply for the rest. **Why:** experts expect file-level control;
newcomers benefit from guided fields. Refine, don't replace.

## 12. Creative app: too conventional
**Bad:** A music-arrangement tool built as a CRUD table of clips with start/end time inputs.
**Good:** A timeline canvas with direct manipulation (drag, trim handles, snap, zoom), scrubbing,
keyboard nudge, and a conventional frame (file menu, undo/redo, export dialog, inspector panel).
**Why:** the medium needs direct manipulation, and forms can't express it (Q3 fails for the
"standard admin" convention).

## 13. Creative app: reinventing undo
**Bad:** A custom "time river" gesture replaces `Cmd+Z` for history.
**Good:** Standard undo/redo shortcuts, plus a visible history panel with branch points as a
refinement. **Why:** undo is infrastructure, and users perform it by reflex.

## 14. Banking: celebratory transfer
**Bad:** Confetti and a bouncy card flip after every transfer, with the review step removed "for speed".
**Good:** Keep the review step, show the resulting balance and fees before confirming, quiet success
with a receipt and reference number. Save the delight for occasional milestones (savings goal
reached). **Why:** high stakes, trust-first posture.

## 15. Email: animating triage
**Bad:** A 400ms slide-out animation on archive and an animated transition to the next message.
**Good:** Instant archive with undo toast; `e`, `j/k` shortcuts; no motion. **Why:** it happens
hundreds of times a day, so motion makes it feel slow.

## 16. Existing project: the new page looks off
**Bad:** Building a new settings page with a fresh set of hand-rolled inputs and a different radius
because "the existing style is bland".
**Good:** Use the project's form primitives and tokens. If they have a real problem (contrast),
propose a token fix for the whole system. **Why:** consistency of behaviour and vocabulary across
the product.

## 17. User asks for novelty that hurts
**Request:** "Make the admin table horizontally scrolling cards so it feels modern."
**Good response:** Explain in one or two sentences that operators comparing many records lose
column alignment and scanning speed with cards. Offer a modernised table instead (better density
controls, refined typography, row hover actions). If the user still wants cards, build them well.
**Why:** the user's brief wins after the trade-off is stated.
