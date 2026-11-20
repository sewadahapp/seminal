# Working in Existing Projects

Workflow step 2. Read the project before deciding anything. Preserve what works. Change things
only for a reason you can name.

## Inspection checklist

Do this quickly; most of it takes a few file reads and a search.

1. **Stack and framework:** `package.json`, `pubspec.yaml`, `*.xcodeproj`, `Gemfile`,
   `composer.json`, etc. Note the framework version and rendering model (SPA, SSR, static, native).
2. **Component library:** shadcn/ui, MUI, Chakra, Ant Design, Radix, Mantine, Vuetify, Headless UI,
   in-house `components/ui`. Find the primitives (Button, Input, Table, Dialog) and how variants
   are expressed.
3. **Tokens and theme:** Tailwind config / CSS variables / theme files / design-token JSON. Note colour
   roles, type scale, spacing scale, radius, shadows, dark mode strategy.
4. **Design docs:** `DESIGN.md`, `PRODUCT.md`, Storybook, `docs/`, brand guidelines, Figma links in
   README.
5. **Layout shell:** app frame, navigation, page header pattern, content width, breakpoints.
6. **Interaction conventions in use:** how existing pages handle tables, filters, forms, toasts,
   modals vs drawers, empty and loading states, errors, confirmations.
7. **Copy voice:** sentence case vs title case, terminology (e.g. "workspace" vs "project"), tone.
8. **Responsive and a11y practice:** what is already done (focus styles, aria usage, mobile layouts).
9. **Visual truth:** if the app can run, look at it. If it can't, look at screenshots, stories, or
   visual-regression goldens. Code alone can mislead about what users see.

Write a 3–6 line summary of what you found before designing.

## Respect the system without following it blindly

- **Reuse primitives.** Don't create a new Button because the existing one lacks a variant: add the
  variant in the system's own style.
- **Behaviour must be consistent everywhere.** The same action works the same way on every page
  (same confirm pattern, same toast, same shortcut).
- **Appearance can vary by surface.** Consistency doesn't mean every page looks identical. A reports
  page can be denser than a settings page, and an onboarding screen can be more expressive, all
  with the same tokens.
- **Fix the system, not the instance.** If a token is wrong (contrast failure, clashing state
  colours), propose fixing the token, not overriding it locally on one page.
- **Leave inconsistencies outside your scope alone** unless asked. Mention them instead of
  silently "cleaning up" other pages.

## When to change established decisions

Change an existing pattern only when one of these is true:
- It fails users measurably: accessibility failures, error-prone flows, unreadable density.
- It contradicts the product category's conventions in a way that confuses users, and there is no
  product reason for it.
- The user asked for a redesign. Even then, carry over product truth (content, features,
  terminology users learned, data model) and treat the old look only as evidence.

When you change something, state what changed, why, and what else may need to follow for consistency.

## Greenfield (no existing project)

- Choose a mainstream, well-supported stack unless the user specified one. Prefer a solid
  accessible primitives library over hand-rolled widgets for dialogs, menus, comboboxes and date
  pickers.
- Set tokens (colour roles, type, spacing, radius, motion) **before** adding components. Untouched
  kit defaults are the most common source of an empty identity layer.
- Write a short `DESIGN.md` (or add to an existing one) recording the posture per surface, the
  identity levers and the key ledger decisions, so later work stays coherent.
