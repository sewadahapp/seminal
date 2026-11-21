# Layout and Composition

Workflow steps 3, 6 and 7. Page structure is where owners most often have a picture in mind, and
where a wrong guess costs a full rebuild. This file gives trade-offs, not a look. Pick from them
with the owner's references (SKILL.md step 3) and show options when more than one fits (step 8).

## 1. The page content column

Most app pages are one column of content inside a shell (sidebar, top bar). Decide the column once
for the whole product, not per page.

- **One shared max-width, or a small set.** For example, a reading/form width (≈640–720px), a
  standard width (≈960–1200px) and full width for data-heavy views. Every page uses one of them,
  by name (a layout component or token), not a one-off `max-width`.
- **Centred vs left-aligned.** Pick one rule and apply it to every page that uses a max-width.
  - *Centred* reads as balanced and calm. Content narrower than the viewport sits in the middle,
    so wide screens don't leave a large empty right side. Common in content lists, settings and
    artifact or file galleries (e.g. Claude's artifact list, Vercel's project pages).
  - *Left-aligned* keeps a fixed starting edge next to the sidebar. It works when pages are
    full-width or nearly so (data tables, consoles). With narrow pages on wide screens, it looks
    lopsided.
  - Mixing them (centred settings, left-aligned lists, a one-off width elsewhere) is what makes
    moving between sections feel jumpy.
- **Same edges across sections.** Page title, toolbar, content and footer share the column's left
  and right edges. Check this by measuring, not by eye (see §6).
- **Scrollbar gutter.** Reserve it (`scrollbar-gutter: stable` or equivalent) so the centred
  column doesn't shift sideways when one page scrolls and the next doesn't.
- **Narrow screens:** the column becomes full width with a consistent side padding (≈16px on
  phones). Don't keep desktop margins.

## 2. Collection views: table, list, card list, grid

The common mistake is treating "dense app" as "use a table". Choose by what users do with each
record.

| Form | Best when | Costs | Familiar from |
|---|---|---|---|
| **Table** | Users compare attributes across many records, sort by columns, select in bulk | Visually heavy; poor on mobile; feels like admin | Spreadsheets, Drive list view, admin panels |
| **Plain list** (rows, dividers) | Sequential reading or quick open; 1–2 attributes per row | Little room for status or metadata | Inbox, activity, settings lists |
| **Card list** (one card per row) | Users scan a few key facts per record and pick one; records have a title plus 2–5 facts | Fewer records per screen than a table | Flight/train search results, job boards, GitHub repo lists |
| **Grid of cards** | Records are visual (thumbnails, covers) or the set is small and browsed | Hard to compare; ragged with uneven content | Galleries, Notion gallery, Dribbble, product grids |

Notes:
- A card list is a valid **receding** form. It can be quiet, compact and keyboard-navigable.
- Offering a list/grid toggle is fine when both are real needs. Make one the default.
- Whatever the form, keep the behaviour conventions: sort, filter, search, empty and loading
  states, keyboard navigation, URL state (see ux-patterns.md).

## 3. App shell patterns

Familiar structures for signed-in apps. These are conventions (Keep by default); identity goes
into their details.

- **Sidebar:** product mark at the top, primary navigation, optional secondary group (projects,
  recent items), and a **footer**.
- **Sidebar footer:** the most common form is the **account block**: avatar, name and workspace,
  opening a menu with profile, settings, theme, help and sign out. Optionally, a small **promo or
  status card** above it (upgrade, new feature, usage meter, "built with …"). A single line of
  footer text is rare in apps and often reads as unfinished.
- **Page header:** title (matching the nav label), short description if useful, primary action on
  the right, then a toolbar row (search, filters, view toggle) sharing the content column's edges.
- **Mobile:** the sidebar becomes a drawer with an accessible name and a visible trigger. The account
  block moves into the drawer or a top-bar avatar.

## 4. Alignment and rhythm

- Align to a few vertical lines: the column edges, and inside cards one content edge. Measure
  shared edges in the browser. Off-by-a-few-pixels alignment is often what owners mean by "looks off".
- Use a spacing scale (e.g. 4/8-based) and give related items less space than unrelated ones.
- In a list or card list, keep columns of facts aligned across rows (dates, statuses, counts) so
  the eye can scan down them.

## 5. Showing options before building

When two or more of the above are valid, sketch them for the owner (SKILL.md step 8). Keep it
fast: a line each, or a small ASCII sketch, plus a recommendation.

```
A. Table (like Drive list view): dense, sortable, compares columns
   ┌────────────────────┬──────────┬──────────┐
   │ Name               │ Status   │ Edited   │
   ├────────────────────┼──────────┼──────────┤
   │ Q3 launch plan     │ Active   │ 2h ago   │
   └────────────────────┴──────────┴──────────┘

B. Card per row (like flight results): scannable, calmer, fewer per screen
   ┌───────────────────────────────────────────┐
   │ Q3 launch plan                   ● Active │
   │ 12 parts · edited 2h ago                  │
   └───────────────────────────────────────────┘

Recommend B: people scan titles and status here and rarely sort by column.
```

Name each option after a pattern the owner probably knows. "Like flight results" is easier to
judge than "card-based list layout".

## 6. Checking layout in the browser

These sit alongside the inspection set in validation.md:
- Measure the content column's left and right edges (`getBoundingClientRect`) on every top-level
  section at ≈1280 and ≥1440 widths. They should match, or differ only by a named width.
- Check that header, toolbar and content share edges, and that sticky elements still stick inside
  the new layout.
- Navigate between sections and watch for horizontal shifts (column width, scrollbar).
