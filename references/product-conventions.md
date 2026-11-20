# Product Conventions

What users already expect from common product categories. Use this file in workflow step 3.

**How to read each entry**
- **Mental model:** the structure users carry in their heads from other products.
- **Preserve:** conventions where breaking them costs trust or task success. They default to *Keep*.
- **Room to refine:** known weak spots in the category where better execution pays off.
- **Identity lives in:** where this category can be distinctive without hurting usability.
- **Innovation is plausible when:** the conditions under which a new pattern is worth its cost.
- **Common mistakes:** what agents get wrong in this category.

These are starting points, not templates. Always check each convention against the actual
workflow (Innovation Test, question 3). Regional reference sets matter: Indonesian shoppers arrive
from Tokopedia and Shopee, US shoppers from Amazon, Chinese shoppers from Taobao. Their expectations
differ in details such as voucher mechanics, chat-with-seller, COD and live shopping.

---

## Marketplace (multi-seller)

**Mental model:** search or browse → results grid → filter/sort → product page → seller trust → cart → checkout → order tracking → review.

**Preserve**
- A prominent search field with autocomplete (queries, categories, recent searches). It is the main entry point.
- Category navigation reachable from everywhere (mega menu on desktop, category screen or tab on mobile).
- A results grid of product cards: image, title (2 lines max), price, discount, rating with count, location or shipping hint, seller badge.
- Filters for price range, rating, location/shipping, condition and category-specific attributes. Applied filters show as removable chips with a result count. Sort by relevance, newest, price and best-selling.
- A product page with a gallery, price block, variant selectors, quantity, primary "Buy now" / "Add to cart", seller card (rating, response time, location), shipping estimate, specifications, reviews with photos, and Q&A or chat.
- A cart grouped by seller. Checkout with address, shipping option per seller, voucher, payment method and order summary. Then order status timeline and transaction history.
- Trust signals: verified seller, ratings with counts, return policy, buyer protection.

**Room to refine:** filter feedback (live counts, no zero-result dead ends), comparing similar listings, honest total cost earlier (shipping + fees), seller trust condensed into one scannable card, review summarisation, empty search states that suggest corrections.

**Identity lives in:** typography and price styling, brand colour used on actions and promos (not everywhere), card composition and image treatment, category illustrations, campaign and promo surfaces, voice in microcopy, delight on post-purchase moments (order confirmed, delivered), mascot or illustration system.

**Innovation is plausible when:** the inventory is unusual. Examples: rentals (date-range availability in place of a cart), used goods (condition grading), services (booking slots), local pickup (map-first discovery), or a niche where attributes matter more than images (e.g. specs-first comparison for components).

**Curated vs. mass marketplaces:** search must always be visible in the header. How prominent the home page makes it depends on intent. A mass marketplace (users know what they want) leads with search and categories. A curated or gift-led marketplace (crafts, design, vintage) can lead with editorial browsing, such as collections, makers and occasions, while keeping search in the header and the results/product/checkout model unchanged.

**Regional detail (Indonesia example):** voucher entry and stacking rules shown before payment; e-wallet, QRIS, bank virtual account (with expiry countdown and a "payment pending" state) and COD; chat with seller from product and order pages; order status in local logistics terms; Bahasa Indonesia-first copy with Rupiah formatting (`Rp 125.000`).

**Common mistakes:** a hero-heavy home page that pushes search out of the header; a bespoke "discovery experience" that hides search; card designs that drop price or rating for aesthetics; copying Shopee's orange, flash-sale chrome and density outright; checkout steps reordered or merged in unfamiliar ways.

## E-commerce (single brand)

**Mental model:** browse collections → product page → cart → checkout → order confirmation and history.

**Preserve:** cart icon with count top-right; product page with gallery, price, variants, add-to-cart above the fold on mobile; size guide; shipping/returns info near the CTA; guest checkout; order confirmation and email; account → orders.

**Room to refine:** variant selection that updates imagery; stock and delivery date clarity; fewer checkout fields; accurate payment-method logos.

**Identity lives in:** a lot of places. Editorial composition, photography direction, type, product storytelling sections and brand voice. A single-brand store has much more visual freedom than a marketplace because it carries one brand, not many sellers.

**Innovation is plausible when:** the product needs configuration (3D configurators, made-to-order builders) or in-context try-on.

**Common mistakes:** making the store so editorial that the price and add-to-cart are hard to find; carousels as the main navigation.

## Email client

**Mental model:** folders/labels → message list → reading pane or thread → reply/forward → compose.

**Preserve:** a list showing sender, subject, snippet, time and unread weight; threads; compose button always available; archive/delete/mark-unread/move with keyboard shortcuts (users bring Gmail shortcuts: `j/k`, `e`, `r`, `c`); search with operators; undo send / undo archive; drafts autosave.

**Room to refine:** triage speed, bulk selection, attachment previews, smarter search filters.

**Identity lives in:** type, density options, sender avatars, empty inbox moment, voice.

**Innovation is plausible when:** the workflow is a different job (e.g. split inboxes for high-volume support, screener for unknown senders). These need a clear explanation on first use.

**Common mistakes:** animating archive/next-message (it happens hundreds of times a day); hiding the folder list behind a hamburger menu on desktop.

## Project / task management

**Mental model:** workspace → projects → tasks (title, status, assignee, due date, priority) → views (list, board, timeline/calendar) → task detail.

**Preserve:** status columns on boards with drag-and-drop between them; list view with sortable columns; task detail as a side panel or page with comments and activity; assignee avatars; due dates with overdue state; filters and saved views; `C` to create a task and `Cmd/Ctrl+K` command palette (Linear/Jira users expect them); bulk edit.

**Room to refine:** creating tasks with few fields, keyboard flow, clear notifications, cross-project overview, dependencies.

**Identity lives in:** type, colour of statuses and labels, density modes, empty states, motion on state changes (kept short), voice.

**Innovation is plausible when:** the domain changes the unit of work (e.g. a construction punch list tied to floor plans, or editorial workflows tied to publish dates).

**Common mistakes:** a playful board that cannot display 200 tasks; status shown only by colour.

## Banking / fintech

**Mental model:** accounts → balance → transactions → transfer/pay → statements → cards → settings/security.

**Preserve:** balance prominence (with a hide toggle); transaction list grouped by date with merchant, category and amount (signed, coloured *and* signed text); transfer flow with recipient → amount → review → authenticate → receipt; explicit review step before money moves; receipts and references; statement download; card freeze; strong confirmation and security patterns.

**Room to refine:** merchant name cleanup, search and filtering of transactions, clear fees and exchange rates before confirming, plain-language errors.

**Identity lives in:** type, the card artwork, colour, insight moments (spending summaries), voice (calm and precise). Avoid playful movement on money actions.

**Innovation is plausible when:** it removes risk or confusion (e.g. a preview of the balance after the transfer, scheduled payments shown on a timeline).

**Common mistakes:** a one-tap money transfer without a review step; red/green as the only sign of debit vs credit; celebratory animations on payments.

## Analytics / BI

**Mental model:** pick a scope (date range, segment, filters) → headline metrics → trend charts → breakdowns → drill-down → export/share.

**Preserve:** global date-range picker with comparison period; filters persist in the URL; KPI tiles with value, delta and period; time-series line charts; tables with sorting next to charts; drill-down by clicking a chart element; export CSV; tooltips with exact values.

**Room to refine:** chart choice fitted to the question being asked; clear explanations of metric definitions; anomaly annotations; empty and sparse data states; loading performance on large ranges.

**Identity lives in:** the palette of the data (accessible, consistent category colours), type and numerals (tabular figures), annotation style, the voice of insight text.

**Innovation is plausible when:** the analysis really is new (e.g. funnels with editable steps, cohort exploration). Also when natural-language querying cuts real effort, as long as results stay inspectable.

**Common mistakes:** pie charts with eight slices; 3D or gradient charts; KPI cards with sparkline, icon and gradient but no comparison period; dark "mission control" styling for an occasional business review.

## Developer tools

**Mental model:** project → files/resources → editor/config → run/deploy → logs/output → settings/secrets.

**Preserve:** monospace for code, logs, IDs and hashes; copy buttons on tokens/commands; logs with timestamps, level, filter and follow/tail; diff views with red/green *and* +/− markers; keyboard shortcuts and a command palette; a dark theme *available* (following the OS setting; it doesn't need to be the default); links that can be deep-linked and shared; CLI parity for UI actions; environment and branch always visible.

**Room to refine:** error messages that name the cause and the fix; long-running operations with progress and cancel; resource tables that work at high density.

**Identity lives in:** type pairing (sans + mono), restrained accent, syntax theme, docs voice, illustration on marketing and empty states.

**Innovation is plausible when:** it visualises a system that text describes badly (dependency graphs, traces, request waterfalls).

**Common mistakes:** large rounded marketing cards inside the console; proportional fonts for IDs; hiding raw output behind summaries.

## Admin panel / back office / CRUD

**Mental model:** sidebar of resources → list (table) → filter/search → detail → edit form → save; settings; users and roles.

**Preserve:** persistent left navigation; data tables with sorting, filtering, pagination or virtual scroll, column choice, row selection and bulk actions; detail pages or drawers; forms with labelled fields and inline validation; confirmations for destructive actions and undo where possible; role-aware hiding or disabling with an explanation; audit history.

**Room to refine:** saved filters, keyboard navigation in tables, inline edit for common fields, error messages, consistency across modules.

**Identity lives in:** quiet precision. Type, spacing rhythm, a single accent, crisp state colours, good microcopy.

**Innovation is plausible when:** a specific high-volume task is slow (e.g. a review queue with keyboard triage).

**Common mistakes:** marketing-style hero headers on every admin page; cards where a table is needed; low-contrast grey text; modals for every edit.

## Inventory / operations

All admin conventions apply, plus: SKU, quantity, location, status columns; stock thresholds (low/out) shown with icon + text + colour; bulk adjust/transfer/export; barcode or scan input; movement/audit log per item; import from CSV with a preview and error report; numbers right-aligned in tabular figures; sticky headers and first column.

**Common mistakes:** low-density cards showing 8 items per screen; decorative charts above the table that push the work below the fold.

## Grocery / quick commerce

**Mental model:** address/delivery slot → categories and search → add to basket with quantity steppers on cards → basket → slot and substitutions → pay → live order tracking → reorder.

**Preserve:** quantity steppers directly on product cards; unit price (per kg/litre) next to price; "buy again" / past orders; substitution preferences per item; delivery slot or ETA visible before checkout; a persistent basket total and minimum-order indicator.

**Innovation is plausible when:** it speeds up repeat shopping (recipe → basket, "my usual" lists, natural-language add). The visible basket stays the source of truth.

## AI / conversational features inside a product

**Mental model:** users treat chat as an *assistant*, not as the product's structure. They expect to see, edit and undo what it did.

**Preserve:** results land in the product's normal UI (cart, table, document), not only in the chat transcript; actions are previewed before anything irreversible; sources and reasoning can be inspected where trust matters; a way to stop or regenerate; a non-chat path for every task.

**Common mistakes:** chat as the only way to do a task that's habitual or comparative (shopping, triage); hiding state inside the conversation.

## Billing / subscription management

**Mental model:** current plan → usage against limits → change plan (comparison) → payment method → invoices/receipts → cancel.

**Preserve:** current plan and renewal date at the top; usage meters with limits and reset date; plan comparison with the current plan marked and prorated price shown before confirming; invoice list with download; payment method update; tax/VAT details; a findable cancellation path (no confirm-shaming).

**Identity lives in:** the plan comparison composition, usage visualisation, voice. Money flows stay calm.

## Geo / fleet / live operations console

**Mental model:** live map + list of assets → status and alerts → select asset → detail (position, telemetry, history) → act (contact, dispatch, acknowledge) → replay a trip or incident.

**Preserve:** map and list kept in sync (selecting in one highlights the other); alert queue sorted by severity with acknowledge/assign; a data freshness indicator ("updated 12s ago", stale assets marked); clustering at low zoom; time scrubber for replay; filters by status/region/group.

**Room to refine:** alarm fatigue (grouping, snoozing, severity thresholds), clarity when connections drop, shift handover summaries.

**Common mistakes:** a decorative "command centre" aesthetic; status by colour alone on the map; alerts that can't be acknowledged in bulk.

## Event planning / seating / spatial layout tools

**Mental model:** floor plan with tables/zones → guest or attendee list → drag people to seats → constraints (capacity, groups together, conflicts apart) → print/export.

**Preserve:** a spatial canvas with drag-and-drop; a searchable side list of unassigned people; capacity indicators per table; a printable/exportable plan; undo.

## Messaging / chat

**Mental model:** conversation list → thread → composer at the bottom; unread counts; presence; attachments; reactions; search.

**Preserve:** newest message at the bottom, composer pinned, Enter to send (with Shift+Enter for a new line on desktop), delivery/read states, timestamps grouped, scroll position preserved, jump to latest.

**Innovation is plausible when:** the conversation has structure (threads tied to tasks, AI assistants with tool output).

## Social / content feed

**Mental model:** infinite or paginated feed → item (author, media, text, actions) → detail/comments → profile → create post.

**Preserve:** action row conventions (like, comment, share, save); tap targets; pull to refresh on mobile; profile structure.

**Identity lives in:** content presentation, type, brand interactions (a signature like animation is fine: occasional, meaningful, short).

## Booking / travel / reservations

**Mental model:** where + when + who → results with price and availability → detail → select option → guest details → pay → confirmation with reference.

**Preserve:** date range picker with clear check-in/out; price per night vs total clarity; map + list for location-based search; cancellation policy near the CTA; confirmation number.

**Common mistakes:** hidden fees revealed at payment; date pickers that don't show availability or price.

## CRM / sales tools

**Mental model:** contacts/companies/deals → pipeline board → record detail with activity timeline → tasks/reminders → reports.

**Preserve:** pipeline stages with values; activity timeline; quick log (call, email, note); search across records; import/export.

## Documentation / knowledge base

**Mental model:** left nav tree → article → in-page table of contents → search → next/previous.

**Preserve:** search (`/` or `Cmd+K`), heading anchors, code blocks with copy, version selector, readable measure (60–80ch), "edit this page" / feedback.

**Identity lives in:** type, code theme, diagrams, voice.

## Media / streaming

**Mental model:** rows of categories → title detail → play → continue watching → my list.

**Preserve:** player controls (space, arrows, captions, fullscreen), continue-watching row, resume position.

## Creative tools (design, audio, video, 3D, writing)

**Mental model (the frame):** files/projects → canvas/document → tools → layers/properties panel → undo/redo history → export → share.

**Preserve:** undo/redo everywhere (`Cmd/Ctrl+Z`), standard shortcuts for copy/paste/duplicate/delete, zoom and pan conventions (`Cmd +/-`, space-drag), save/autosave indication, export dialogs, selection behaviour.

**Room for invention:** the **core manipulation** of the medium is where creative tools earn bespoke interaction: direct manipulation on canvas, timeline scrubbing, node graphs, gesture-based tools, non-destructive history branching. The frame stays conventional so the invention has somewhere stable to sit.

**Common mistakes:** forcing a form-and-table admin pattern on a medium that needs direct manipulation; reinventing undo; new tools with no visible affordance or shortcut hint.

## Marketing site / landing page

**Mental model:** top nav (logo left, links, primary CTA right) → hero states what it is → proof → how it works / features → pricing → FAQ → final CTA → footer.

**Preserve:** a clear statement of what the product is in the first viewport; a primary CTA that is visible and repeated; navigation that works; pricing findable; legal and contact in the footer; fast load; readable body text.

**Identity lives in:** almost everything else. Composition, typography as image, art direction, motion moments, narrative order, copy voice. This is where the largest visual risks are justified.

**Innovation is plausible when:** it demonstrates the product (interactive demo, live playground) instead of decorating.

**Common mistakes:** the generic sequence (centred hero → three feature cards → testimonials → CTA) used without considering the story; abstract visuals in place of the real product; scroll-jacking that breaks reading and back navigation.

---

## Platform conventions (cross-cutting)

- **iOS:** tab bar at the bottom (≤5), navigation stack with back swipe, sheets, SF symbols style, large titles where content-led, system share sheet, Dynamic Type.
- **Android:** Material navigation patterns, system back, top app bar, FAB only for a single primary action, edge-to-edge.
- **Desktop apps:** menu bar/shortcuts per OS (`Cmd` vs `Ctrl`), resizable panes, context menus, drag and drop, multi-window.
- **Web:** links are links (open in new tab works), back button restores state, URLs reflect filters/views, text is selectable, forms submit with Enter, browser zoom works.

## Cross-cutting flows users expect everywhere

- **Auth:** email/password with show-password toggle, password manager compatible fields (`autocomplete`), SSO buttons, "forgot password", passkeys where supported. Never block paste.
- **Onboarding:** short, skippable, progressive. Get the user to the first real value quickly.
- **Settings:** grouped sections with left nav or list; explicit save or clear autosave; danger zone at the bottom with confirmation.
- **Search:** visible field or `/` / `Cmd+K`; recent searches; typo tolerance; empty results with suggestions.
- **Notifications:** bell with count, list with read/unread, mark all read, link to source, preferences.
- **Destructive actions:** confirmation proportional to damage; undo preferred over confirmation for reversible actions.
