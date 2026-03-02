# Component Recipes

Use these defaults for generic, reusable blocky components with shadcn-style implementation patterns.

Apply the same principles in any stack (React, Vue, Svelte, plain HTML/CSS): tokenized colors, variant maps, strong borders, and direct interaction states.

For full marketing-page composition (hero/features/process/CTA), pair this file with `references/marketing-section-recipes.md`.

## Core Rules

- Use sharp edges (`rounded-none` or no radius utility).
- Use `border-2` with strong contrast.
- Use hard offset shadows (`shadow-[4px_4px_0px_0px_var(--shadow-color)]`).
- On hover/active, move by 1-2px and reduce shadow offset.
- Keep text bold, uppercase, and tight tracked for CTAs.
- Export typed variant APIs with `cva`.
- Keep components composable (`asChild`/slot pattern where needed).

## Shadcn-Style Component Shape

```tsx
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const styles = cva("base classes", {
  variants: {
    variant: { default: "..." },
    size: { default: "..." },
  },
  defaultVariants: { variant: "default", size: "default" },
});

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> &
  VariantProps<typeof styles> & { asChild?: boolean };
```

## Button Recipe

```tsx
const buttonBase =
  "inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm font-bold uppercase tracking-wider transition-all border-2 active:translate-y-[2px] active:translate-x-[2px] disabled:pointer-events-none disabled:opacity-40";

const buttonPrimary =
  "bg-[var(--accent)] text-[var(--foreground-inverse)] border-[var(--border)] shadow-[4px_4px_0px_0px_var(--shadow-color)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[2px_2px_0px_0px_var(--shadow-color)] hover:bg-[var(--accent-hover)]";
```

## Plain CSS Fallback

```css
.btn {
  border: 2px solid var(--border);
  background: var(--accent);
  color: var(--foreground-inverse);
  box-shadow: 4px 4px 0 0 var(--shadow-color);
  transition: transform 120ms ease, box-shadow 120ms ease, background 120ms ease;
}

.btn:hover {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 0 var(--shadow-color);
  background: var(--accent-hover);
}
```

## Card Recipe

```tsx
const cardBase =
  "border-2 border-[var(--border)] bg-[var(--background)] shadow-[8px_8px_0px_0px_var(--shadow-color)]";
const cardHeader = "p-6";
const cardTitle = "text-xl font-black uppercase tracking-tighter";
const cardDescription = "text-sm text-[var(--foreground-muted)]";
```

## Input Recipe

```tsx
const inputBase =
  "h-10 w-full border-2 border-[var(--border)] bg-[var(--background)] px-3 py-2 text-sm font-mono text-[var(--foreground)] placeholder:text-[var(--foreground-muted)] transition-all focus-visible:border-[var(--accent)] focus-visible:shadow-[4px_4px_0px_0px_var(--shadow-accent)] focus-visible:outline-none";
```

## Layout Recipe

- Alternate section tones using `--background` and `--background-alt`.
- Use typographic hierarchy, not decorative boxes, to guide flow.
- Keep hero to action path short (headline -> proof -> CTA).
- Keep nav simple and links obvious.
- Reuse primitives across pages to avoid drift between products.
- Collapse multi-column sections on mobile; preserve borders and tap targets.
