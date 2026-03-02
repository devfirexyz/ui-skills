# Marketing Section Recipes

Use this when the user wants a bold, neo-brutalist marketing page with reusable section structure.

## Core Style Signals

- Typography-first hierarchy: giant `font-black` sans headlines + mono body.
- Square geometry only: no rounded corners on primary surfaces.
- Strong structural rhythm: `border-2` section splits and card edges.
- Hard shadows: `4px`, `6px`, `8px`, `12px` offsets (no blur-heavy shadows).
- Direct motion: hover/active translate + shadow reduction.
- Uppercase action language with tighter tracking for headings and CTAs.

## Section Blueprint

1. Nav
- Fixed top nav with `border-b-2`.
- Wordmark on left, utility links + CTA on right.
- Link hover should use underline or clear background inversion.

2. Hero
- Massive headline scale (`clamp(80px, 18vw, 220px)`).
- One to two rotated sticker blocks for value proposition.
- Price/CTA strip directly under hero statement.

3. Features Grid
- 2 or 4 column grid on desktop, single-column on mobile.
- Use `divide-x-2 divide-y-2` (or per-cell borders) for structure.
- Each cell has index marker (`/01`, `/02`) + bold title + short proof text.
- Full cell color inversion on hover is preferred over subtle opacity.

4. Process / How It Works
- 3 cards with dark header bars and big numeric step labels.
- Card hover: translate a few pixels and reduce shadow.
- Keep copy short and imperative (`Describe`, `Generate`, `Release`).

5. Final CTA
- Full-width bordered strip.
- High-contrast headline and one primary action.
- Optional secondary trust copy line.

## Color Guidance

- Start from two user-provided colors:
  - base: structural surfaces/background
  - accent: actions and emphasis
- Keep neutrals dominant; use accent sparingly for hierarchy.
- Maintain strong border contrast regardless of palette.

## Responsiveness Rules

- Collapse multi-column grids to 1 column below tablet width.
- Keep headline readable with clamp, not media-query hard jumps.
- Maintain tap targets and visible borders on mobile.
- Avoid fixed pixel widths for CTA and card components.

## Output Checklist

- Includes nav, hero, feature grid, process cards, and CTA sections.
- Uses shared tokens (`--background`, `--foreground`, `--border`, `--accent`).
- Uses hard-edged button/card/input patterns.
- Preserves accessibility: semantic headings, visible focus state, contrast-safe text.
