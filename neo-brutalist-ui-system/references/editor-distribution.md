# Editor Distribution Guide

Use this guide when the user asks to install this skill globally or across AI coding editors.

## 1. Keep a Portable Skill Package

Required:
- `SKILL.md`

Recommended:
- `agents/openai.yaml`
- `references/*`
- `scripts/*`

Rule:
- Avoid editor-specific assumptions in core instructions. Keep `SKILL.md` generic and stack-aware.

## 2. Codex / skills CLI Distribution

1. Push `neo-brutalist-ui-system/` to a public GitHub repository.
2. Install via:
   - `npx skills add <github_repo_or_skill_url>`
3. Trigger with:
   - `$neo-brutalist-ui-system`

## 3. Claude / OpenCode Distribution Pattern

- If the editor supports skill folders/prompts from git or local path, import this folder directly.
- If it does not support native skill loading, use `SKILL.md` as the canonical system prompt and keep `references/*` nearby for progressive loading.
- Preserve the same skill name (`neo-brutalist-ui-system`) across tools for prompt consistency.

## 4. Publish to skills.sh

1. Ensure `SKILL.md` has clear trigger contexts.
2. Ensure `agents/openai.yaml` has:
   - `display_name`
   - `short_description`
   - `default_prompt` using `$neo-brutalist-ui-system`
3. Verify install from a clean environment with `npx skills add ...`.
4. Share install command publicly.

## 5. Versioning Advice

- Use semantic tags (`v1.0.0`, `v1.1.0`) in Git for stable installs.
- Keep breaking changes documented in commit messages.
- Keep references and scripts backward-compatible where possible.
