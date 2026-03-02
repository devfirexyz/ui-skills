---
name: neo-brutalist-ui-system
description: Build reusable neo-brutalist design systems and landing pages with shadcn-style component APIs, strong typography, and adaptive two-color tokens. Use when users ask for bold UI systems, landing pages, section recipes, Tailwind/CVA architecture, or cross-project visual consistency.
---

# Neo-Brutalist UI Design System Skill

Implement a reusable design system for agent-built products with two modes:
- `product-ui`: app surfaces and dashboards
- `marketing-page`: hero-led landing pages

Generate accessible tokens, apply section/component recipes, and ship portable outputs across frameworks and editors.

## Quick Start

1. Collect `base` and `accent` colors (`#rrggbb`).
2. Run `scripts/generate_blocky_palette.py --base <hex> --accent <hex>`.
3. Choose style mode:
   - `product-ui` for dashboards/apps
   - `marketing-page` for hero-led marketing pages
4. Apply generated tokens in the project theme file (`globals.css`, `app.css`, `theme.css`, etc.).
5. Build components using `references/component-recipes.md`.
6. Build full landing sections with `references/marketing-section-recipes.md` and `assets/templates/marketing_landing_template.jsx`.
7. If requested, capture project-specific screenshots and add to `assets/screenshots/`.

## Workflow

### 1. Confirm the UI direction
- Ask for stack + scope first (`React/Tailwind`, `plain CSS`, `Vue`, `Svelte`, `RN-web`, full page vs components).
- Choose mode:
  - `product-ui`: restrained layout rhythm, clear utility-first surfaces.
  - `marketing-page`: louder headline scale, sticker blocks, high-contrast CTAs.
- Keep controls deliberate and high-contrast.
- Prefer 2px borders and hard offset shadows over soft blur shadows.
- Preserve fast interactions and avoid blocking states.

### 2. Generate adaptive colors from two shades
- Treat `base` as the structural color (background/surfaces).
- Treat `accent` as action emphasis (buttons, focus, highlights).
- Run the palette generator script and paste emitted `:root` and dark-theme tokens into the target stylesheet.
- If contrast feels weak in context, rerun with adjusted colors instead of hand-editing many tokens.

### 3. Assemble blocky components
- Start from recipes in `references/component-recipes.md`.
- Follow shadcn-style structure: primitive wrapper + `cva` variants + `cn` utility.
- Prefer variants over one-off classes, regardless of framework.
- Keep hover/active motion direct (`translate` + shadow reduction), not subtle opacity fades.

### 4. Compose layout sections
- For app UI, keep hierarchy typographic with clean card/group rhythm.
- For marketing pages, compose from:
  - fixed bordered nav
  - oversized headline hero
  - rotated sticker blocks
  - feature grid with `divide-x` / `divide-y`
  - process cards with dark headers
  - hard-border CTA strip
- Use `references/marketing-section-recipes.md` for exact section patterns.

### 5. Enforce guardrails
- Performance: avoid heavy visual effects and unnecessary client-side waterfalls.
- Convenience: keep navigation direct and obvious.
- Security: do not expose privileged actions without auth checks.
- Responsiveness: verify mobile layouts (single-column fallbacks for multi-column sections).

## Shadcn Principles

- Keep components local to the project; treat them as owned source, not black-box dependencies.
- Build from accessible primitives and preserve keyboard/focus behavior.
- Use `class-variance-authority` for variant APIs (`variant`, `size`, state).
- Use a shared `cn()` helper (`clsx` + `tailwind-merge`) for class composition.
- Centralize theme values in CSS variables; consume variables inside component classes.
- If shadcn is unavailable, mirror the same API ideas with local primitives and variant maps.

## Resources

- `scripts/generate_blocky_palette.py`: Generate light/dark design tokens from two colors.
- `references/component-recipes.md`: Generic component and layout recipes with shadcn-style patterns.
- `references/marketing-section-recipes.md`: Generic landing-page section recipes.
- `assets/templates/marketing_landing_template.jsx`: Reusable landing-page scaffold.
- `references/publishing-skills-sh.md`: Publish checklist and listing expectations.
- `references/editor-distribution.md`: Make this skill portable across Codex, Claude, OpenCode, and skills.sh.
- `assets/screenshots/*.png`: Optional project-specific screenshots for the listing.

## Example Prompts

- "Use `$neo-brutalist-ui-system` in `marketing-page` mode to build a bold landing page with typographic hierarchy, hard borders, and blocky CTAs."
- "Use `$neo-brutalist-ui-system` in `product-ui` mode to design a dashboard with base `#f2f1eb` and accent `#2f5f3a`."
- "Create reusable card, button, and input variants with shadcn-style APIs and mobile-safe section layouts."
- "Package this skill for cross-editor install and publish on skills.sh."

## Output Standard

- Return:
  - A generated token block.
  - Updated component classes/variants for the user's stack.
  - Section plan (hero, features, process, CTA) when building marketing pages.
  - A short rationale about contrast, hierarchy, and usability.
  - Any screenshot paths used for sharing or listing (if provided).

## Portability Standard

- Keep all workflow instructions inside `SKILL.md` + `references/*` so the skill is self-contained.
- Keep code templates in `assets/templates/*` for reuse instead of rewriting from scratch.
- Keep editor-specific metadata minimal in `agents/`; avoid platform lock-in.
- When asked about distribution, follow `references/editor-distribution.md`.
