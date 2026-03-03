# UI Skills Repo

This repo is organized to keep:
- your own skills (first-party)
- mirrored external skills you use (third-party, with attribution)

## Folder Layout

- `neo-brutalist-ui-system/`
  - Your authored skill.
- `inference-agent-ui/`
  - Your authored skill.
- `dexiejs/`
  - Your authored skill.
- `third_party_skills/`
  - Mirrored snapshots of skills from `~/.agents/skills`.
- `scripts/sync-third-party-skills.sh`
  - Sync tool for third-party mirror + provenance files.
- `SKILLS.md`
  - Ownership map.

---

## 1) Use Your First-Party Skill

Your skill lives here:

`neo-brutalist-ui-system/`
`inference-agent-ui/`
`dexiejs/`

Trigger:

```text
$neo-brutalist-ui-system
$inference-agent-ui
$dexiejs
```

Install from GitHub:

```bash
npx skills add https://github.com/devfirexyz/ui-skills --skill neo-brutalist-ui-system
npx skills add https://github.com/devfirexyz/ui-skills --skill inference-agent-ui
npx skills add https://github.com/devfirexyz/ui-skills --skill dexiejs
```

Pinned install:

```bash
npx skills add https://github.com/devfirexyz/ui-skills/tree/v1.0.3/neo-brutalist-ui-system
```

---

## 2) Mirror Third-Party Skills (Attribution-Safe)

The mirror is manifest-driven:

`third_party_skills/MANIFEST.tsv`

Run sync:

```bash
bash scripts/sync-third-party-skills.sh
```

What sync does:
- copies each listed skill from `~/.agents/skills/<name>` into `third_party_skills/<name>/`
- keeps available license files
- writes/updates `PROVENANCE.md` per skill

---

## 3) Auto-Discover New Installed Skills

If new skills are added in `~/.agents/skills`, use auto-discovery:

```bash
AUTO_DISCOVER=1 FIRST_PARTY_SKILLS="neo-brutalist-ui-system,inference-agent-ui,dexiejs" bash scripts/sync-third-party-skills.sh
```

This will:
- append missing installed skills to `third_party_skills/MANIFEST.tsv`
- skip your first-party skills from `FIRST_PARTY_SKILLS`
- sync everything after manifest update

If you have multiple first-party skills:

```bash
AUTO_DISCOVER=1 FIRST_PARTY_SKILLS="neo-brutalist-ui-system,inference-agent-ui,dexiejs,my-other-skill" bash scripts/sync-third-party-skills.sh
```

---

## 4) Update Attribution Metadata

After auto-discovery, open:

`third_party_skills/MANIFEST.tsv`

Fill real values where possible:
- `upstream` (repo/package URL)
- `license`
- `owner`
- `notes`

Then run sync again:

```bash
bash scripts/sync-third-party-skills.sh
```

---

## 5) Add a New First-Party Skill

1. Create new folder:
   - `<skill-name>/SKILL.md`
2. Add trigger-friendly frontmatter:
   - `name`
   - `description`
3. Add scripts only if needed (`scripts/`).
4. Add skill name to first-party list you use in sync command:
   - `FIRST_PARTY_SKILLS="neo-brutalist-ui-system,inference-agent-ui,dexiejs,<new-skill>"`

---

## 6) Publish to skills.sh

1. Push `master` + tags:

```bash
git push origin master
git push origin --tags
```

2. Install test:

```bash
npx skills add https://github.com/devfirexyz/ui-skills --skill neo-brutalist-ui-system
```

3. Use listing URL:

`https://skills.sh/devfirexyz/ui-skills/neo-brutalist-ui-system`

Note:
- skills.sh page content may lag behind latest commit due to crawler/cache.
- install command can still fetch latest correctly.

---

## 7) Daily Commands

Sync third-party mirror:

```bash
bash scripts/sync-third-party-skills.sh
```

Auto-discover + sync:

```bash
AUTO_DISCOVER=1 FIRST_PARTY_SKILLS="neo-brutalist-ui-system,inference-agent-ui,dexiejs" bash scripts/sync-third-party-skills.sh
```

Check repo changes:

```bash
git status --short
```
