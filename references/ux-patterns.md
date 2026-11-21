# UX and Interaction Patterns

Workflow step 6. Decide behaviour before styling. Each section lists the defaults that suit most
products. Depart from them only through the Convention Ledger.

## Information architecture and navigation
- Name sections in the **user's vocabulary**, not the data model ("Orders", not "Fulfilment entities").
- Persistent navigation: a **left sidebar** for apps with more than about 5 sections; a **top bar**
  for sites and simple apps; a **bottom tab bar** (≤5) on mobile apps.
- Show the current location (active nav state, breadcrumb for depth ≥3, page title matching the nav label).
- Shell structure (sidebar footer, page header, content column) is in [layout.md](layout.md).
- The URL reflects the state that matters: filters, tabs, selected record, pagination. Back
  restores it.
- Command palette (`Cmd/Ctrl+K`) for frequent-use tools with many destinations or actions. It
  adds to visible navigation and never replaces it.

## Core flows
- Map the 3–5 most frequent journeys. Count steps and decisions. Remove steps, don't decorate them.
- Put the primary action where the eye ends up after reading the content it acts on.
- One primary action per view. Make secondary actions visibly secondary. Group destructive actions
  apart.
- Long processes: show progress, allow saving and resuming, and keep a review step before
  irreversible commits.

## Lists, tables and data
- Choose the form by what users do with each record (trade-offs in [layout.md §2](layout.md)):
  **tables** when they compare attributes across records or sort by column; **card lists** (one
  card per row) when they scan a few key facts per record and pick one; **grids** when records are
  visual or few; **plain lists** for sequential reading (messages, activity). Dense or frequent
  use alone doesn't mean a table.
- Table essentials: sticky header, sortable columns with an indicator, right-aligned tabular
  numerals, truncation with full value on hover/focus, row hover, row selection with a bulk-action
  bar, column visibility, density toggle for heavy users, pagination or virtualisation with a
  total count.
- Filtering: visible primary filters, applied filters shown as removable chips, "clear all", result
  count, filters reflected in the URL, saved views for frequent combinations.
- Search: debounce, highlight matches, show what was searched, and offer "no results" help.
- Empty datasets, a single row, 10,000 rows and 120-character names must all look intentional.

## Forms and validation
- A visible label for every field (placeholders are not labels). Mark optional fields, or required
  ones, consistently.
- Validate on blur or submit, not on every keystroke. Put the error next to the field, saying what
  is wrong and how to fix it. Keep the user's input after an error.
- Use the right input types, `autocomplete` attributes, and input modes for mobile keyboards.
- Group long forms into sections. Use multi-step only when the steps are conceptually distinct.
- Submit button label = the action ("Create invoice"), disabled only while submitting, with a
  pending state.

## Feedback and system states
Design every state, not just the happy path:

| State | Must communicate |
|---|---|
| Empty (first use) | What this is, why it's empty, the one action that fills it |
| Empty (filtered/no results) | What was filtered, how to broaden, clear filters |
| Loading | Skeletons that match the layout for content; inline spinners for actions; nothing for <300ms |
| Partial / stale | What is missing or outdated, when it last updated |
| Error | What happened, what the user can do, retry; keep their work |
| Success | Confirmation proportional to the action (inline tick vs toast vs page) |
| Offline | What still works, what will sync |
| No permission | Why, and who can grant access |

- Optimistic UI for low-risk, high-frequency actions (toggle, archive, reorder), with rollback on failure.
- Toasts for background confirmations with undo. Never use a toast as the only place an error appears.

## Recovery and reversibility
- Prefer **undo** to confirmation for reversible actions (archive, move, edit).
- Confirm in proportion to the damage. Type-to-confirm only for the irreversible and large-scale.
- Autosave drafts. Warn before navigating away from unsaved changes.
- Soft delete with a restore window where the domain allows.

## Overlays
- Modals for short, focused, blocking decisions. Side panels/drawers for viewing or editing a record
  while keeping the list in context. Full pages for complex editing.
- Every overlay: focus is trapped and returned, `Esc` closes, there's a visible close control, and
  the page behind doesn't scroll.
- Popovers and menus escape clipping containers (portal / top layer).

## Accessibility (baseline, not optional)
- Semantic HTML first: buttons are `<button>`, links are `<a href>`, headings form an outline,
  landmarks exist.
- Everything works by keyboard, with a visible focus indicator and logical tab order.
- Text contrast ≥ 4.5:1 (3:1 for large text and UI component boundaries).
- Never use colour alone to convey state: pair it with an icon, text or shape.
- Tap targets ≥ 44×44px on touch. Pointer targets that can be acquired without precision.
- Labels and names for icon-only buttons. Live regions for async status.
- Respect `prefers-reduced-motion`, text zoom to 200%, and OS dark/light where supported.

## Responsive behaviour
- Responsiveness is **structural**: sidebars collapse, tables become prioritised columns or row
  cards, multi-pane becomes a navigation stack. Don't just shrink things.
- Decide per surface whether mobile is a primary context (consumer, field ops) or a
  secondary one (deep analytics). Design the primary context first.
- Keep the primary action reachable (sticky bottom bar on mobile commerce and forms).
- Test at roughly 375, 768, 1024–1280 and ≥1440 widths, and with long content.

## Keyboard and power use (high-frequency surfaces)
- Shortcuts for the top actions, shown in tooltips and menus. `?` opens a shortcut sheet.
- `j/k` or arrow navigation in lists, `Enter` to open, `Esc` to close/back.
- No animation on keyboard-triggered actions.
