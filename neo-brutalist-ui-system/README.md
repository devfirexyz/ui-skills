# Neo Brutalist UI System

Production-ready design-system skill for applying a bold neo-brutalist visual language across existing or new frontend projects.

Works for:
- landing pages
- marketing pages
- portfolios
- dashboards
- app surfaces

It is design-system-first, not template-first:
- preserves existing information architecture by default
- standardizes primitives and tokens before layout-level rewrites
- only rebuilds page structure when explicitly requested

---

## Copy-Paste Description For skills.sh

Use this block as your listing description:

```md
Apply a reusable neo-brutalist design system to any frontend project using strong typography, tokenized theming, and variant-driven component primitives.

This skill works across landing pages, marketing sites, portfolios, dashboards, and app surfaces. It starts with design-DNA extraction from your existing codebase (fonts, tokens, primitives, layout rhythm), then performs a layout-preserving refactor by default.

What it does well:
- Standardizes component primitives (button, card, input, dialog, dropdown, tabs, tooltip, progress, badge, etc.)
- Enforces cohesive token architecture (background/surface/foreground/border/accent/shadow)
- Applies high-contrast, hard-edged interaction language (2px borders, offset shadows, direct hover/active states)
- Improves hierarchy and scanability without breaking existing product intent
- Supports both light/dark token systems when available

Includes a palette generator script to derive adaptive token sets from two colors.
```

---

## Short One-Liner (Optional)

```md
Design-system-first neo-brutalist UI skill for tokenized, layout-preserving frontend refactors across any page type.
```

---

## Install

Branch install:

```bash
npx skills add https://github.com/devfirexyz/ui-skills/tree/master/neo-brutalist-ui-system
```

Pinned install:

```bash
npx skills add https://github.com/devfirexyz/ui-skills/tree/v1.0.0/neo-brutalist-ui-system
```

---

## Trigger

Use in prompts with:

```text
$neo-brutalist-ui-system
```

---

## Example Prompts

- Use `$neo-brutalist-ui-system` in `layout-preserving` mode; keep my current section order and restyle the full UI system.
- Use `$neo-brutalist-ui-system` in `component-only` mode and standardize button/card/input/dialog/dropdown/tabs with shared tokens.
- Use `$neo-brutalist-ui-system` for my dashboard and improve scanability, hierarchy, and interaction clarity without changing product intent.

---

## Script Usage

Generate adaptive tokens from two colors:

```bash
python3 scripts/generate_blocky_palette.py --base "#f2f1eb" --accent "#2f5f3a" --format both
```

This prints:
- CSS variable blocks (`:root` and dark theme block)
- JSON token output

---

## What Makes This Skill Different

- Extracts project design DNA before edits (fonts, tokens, primitives, layout rhythm)
- Preserves architecture by default (no forced “marketing template” rewrites)
- Focuses on reusable primitives + token coherence
- Encodes a production-oriented visual language, not one-off styling hacks
