# Publishing on skills.sh

## Practical Workflow

1. Push this skill folder to a public GitHub repo.
2. Verify install works locally:
   - `npx skills add <github_repo_or_skill_url>`
3. Share the same install command publicly.

## Important Platform Behavior

- skills.sh list/leaderboard visibility is tied to installs.
- There is no separate manual listing submission step in docs/FAQ.

## What to Include for a Strong Listing

- Clear `agents/openai.yaml` fields:
  - `display_name`
  - `short_description`
  - `default_prompt` with `$neo-brutalist-ui-system`
- Concrete `SKILL.md` description with trigger contexts.
- Explicit mode language (`product-ui`, `marketing-page`) so users know what outputs to expect.
- Optional visuals in `assets/screenshots/` generated from the user's own project.
- Reusable starter in `assets/templates/` for fast first success.

## Suggested Publish Copy

- Name: `Neo Brutalist UI Design System`
- One-liner: `Build reusable neo-brutalist UI systems with adaptive two-color tokens and shadcn-style architecture.`
- Install: `npx skills add <your-github-url>`
