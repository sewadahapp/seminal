# Visual Direction

Workflow step 7. Express identity through the visual layer, scaled to the surface posture. Reuse
the existing system first.

## 1. Identity levers

Distinctiveness comes from a few deliberate choices that hang together, not from adding effects.
Choose **2–4 levers** to carry the identity and keep the rest quiet.

| Lever | Expressive surfaces | Receding surfaces |
|---|---|---|
| Typography | Display face with character, large scale contrast, type as image | One well-tuned family (or sans + mono), tight scale (≈1.125–1.2), tabular numerals |
| Colour | Committed brand colour, bold grounds, art-directed palettes | Neutral surfaces, one accent reserved for action/selection, semantic state colours |
| Composition | Asymmetry, editorial grids, scale shifts, narrative pacing | Predictable grid, alignment, consistent panel structure |
| Imagery | Art-directed photography, illustration system, the real product | Data and user content are the imagery; illustration only in empty/onboarding states |
| Component shape | Distinct radius logic, signature buttons/cards | Consistent, crisp, minimal ornament; hierarchy via weight and spacing |
| Voice | Point-of-view copy, headlines that say something specific | Precise, short, consistent verbs; the voice is clarity |
| Motion | One orchestrated moment, scroll-linked storytelling (sparingly) | State-change feedback only, 100–250ms |
| Signature interaction | Product demo, interactive hero | Small details: a satisfying completion tick, a well-crafted command palette |

Derive the levers from the **subject matter and audience** (materials, vocabulary, culture,
heritage of the domain), not from whatever is currently trendy.

## 2. Density and spacing
- Set density by the posture. Operational tools: 4px base grid, 28–36px rows, 13–14px UI text.
  Consumer and reading surfaces: 8px base, 16–18px body, generous line height.
- Spacing expresses grouping. Related items sit closer than unrelated ones. Avoid giving every
  block the same padding.
- Whitespace is not automatically "premium". On a monitoring screen, it is lost information.

## 3. Hierarchy
- One focal point per view, matching the user's most important decision or action.
- Build hierarchy with **size, weight, position and contrast** before colour, borders or shadows.
- Use structural devices (borders, numbering, labels, dividers) only when they encode information.
  Numbered steps only for real sequences.

## 4. Colour roles
Define roles, not just a palette: background, surface, surface-raised, border, text-primary,
text-secondary, accent/action, focus, selected, success, warning, danger, info, plus data-viz
categorical and sequential scales. Check contrast for each pairing used. Dark mode is designed
(adjusted elevation, desaturated accents), not inverted.

## 5. Motion budget (frequency-scaled)
| How often the action happens | Motion |
|---|---|
| Many times per hour, or keyboard-initiated | None |
| Tens of times per day (hover, list nav, tab switch) | None or a minimal 100–150ms colour/opacity change |
| Occasional (menus, drawers, modals, toasts) | Short (150–250ms), ease-out, origin-aware (popovers grow from their trigger) |
| Rare / emotional (onboarding, success, marketing reveal) | May be expressive; one orchestrated moment beats many scattered ones |

Animate transform and opacity. Use transitions (interruptible) for interactive UI. Provide a
reduced-motion alternative: keep opacity and colour, remove movement. Motion must show *what
changed* or *where something went*. Otherwise, cut it.

## 6. Generic patterns, judged in context

Common AI-generated defaults are only a problem when nobody **chose** them. Ask "is this a
decision or a default?" for each of these:

- Indigo/purple-to-blue gradient as the brand; glow blobs; glassmorphism everywhere.
- The same rounded card with the same soft shadow for every type of content.
- Centred hero → three feature cards → testimonials → CTA, regardless of story.
- Eyebrow labels in tracked caps above every heading; emoji as icons; `→` appended to every link.
- Fade-up-on-scroll on every section; hover lift on every card.
- KPI tiles with an icon, a big number and a fake sparkline, without a comparison period.
- Abstract 3D, orbs or a fake dashboard image in place of the real product.
- Copy like "Unlock the power of…", "Seamless", "Revolutionise your workflow".

**Context matters:** a system sans, neutral greys and standard table styling are often *correct* for an
operational tool, where they serve recognisability and density. The same choices on a brand's
landing page are usually an empty identity layer. Don't apply anti-generic rules to receding
surfaces in a way that adds decoration users have to work around.

## 7. Borrow the model, not the skin
When the reference product is well known (Amazon, Tokopedia, Shopee, Linear, Stripe, Notion), take:
- **Yes:** information structure, flow order, control types, label conventions users know, state
  semantics.
- **No:** their exact palette, logo-adjacent marks, signature illustrations, proprietary type,
  distinctive layout signatures, or copy. A screenshot must not be mistaken for theirs (Clone test).
