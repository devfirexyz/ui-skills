# Third-Party Skills Mirror

This directory mirrors external skills used in this repository.

Purpose:
- keep a reproducible snapshot of skills used during development
- preserve attribution and licensing metadata
- avoid mixing third-party work with first-party skills

What this is:
- a vendor-style mirror from `~/.agents/skills` based on `MANIFEST.tsv`

What this is not:
- a claim of authorship over mirrored skill content

## Policy

- First-party skills (authored in this repo) stay outside this folder.
- Third-party skills are mirrored here with `PROVENANCE.md`.
- Keep upstream license files intact if present.
- Do not remove attribution from `SKILL.md` metadata when available.

## Sync

Run:

```bash
bash scripts/sync-third-party-skills.sh
```

This will:
- read `third_party_skills/MANIFEST.tsv`
- copy each skill from `$HOME/<source_rel_path>` into `third_party_skills/<skill-name>/`
- create/update `PROVENANCE.md` with upstream, owner, and license notes

Auto-discover new skills from `~/.agents/skills` (excluding first-party):

```bash
AUTO_DISCOVER=1 FIRST_PARTY_SKILLS="neo-brutalist-ui-system" bash scripts/sync-third-party-skills.sh
```

This appends missing skills to `MANIFEST.tsv` with placeholder provenance fields.

## Manifest Format

`MANIFEST.tsv` columns:

1. `skill_name`
2. `source_rel_path` (relative to `$HOME`)
3. `upstream`
4. `license`
5. `owner`
6. `notes`
