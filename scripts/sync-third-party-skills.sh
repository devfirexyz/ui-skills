#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
registry_dir="${repo_root}/third_party_skills"
manifest="${registry_dir}/MANIFEST.tsv"
agents_root="${HOME}/.agents/skills"
first_party_default="neo-brutalist-ui-system"

if [[ ! -f "${manifest}" ]]; then
  echo "Manifest not found: ${manifest}" >&2
  exit 1
fi

if [[ "${AUTO_DISCOVER:-0}" == "1" ]]; then
  if [[ ! -d "${agents_root}" ]]; then
    echo "Agents skills directory not found: ${agents_root}" >&2
    exit 1
  fi

  first_party_csv="${FIRST_PARTY_SKILLS:-${first_party_default}}"
  IFS=',' read -r -a fp_items <<< "${first_party_csv}"
  listed_tmp="$(mktemp)"
  while IFS=$'\t' read -r skill_name _; do
    [[ -z "${skill_name}" || "${skill_name}" =~ ^# ]] && continue
    echo "${skill_name}" >> "${listed_tmp}"
  done < "${manifest}"

  while IFS= read -r -d '' dir; do
    name="$(basename "${dir}")"
    is_first_party=0
    for fp in "${fp_items[@]}"; do
      fp_trimmed="$(echo "${fp}" | xargs)"
      if [[ "${name}" == "${fp_trimmed}" ]]; then
        is_first_party=1
        break
      fi
    done
    [[ "${is_first_party}" -eq 1 ]] && continue

    if grep -Fqx "${name}" "${listed_tmp}"; then
      continue
    fi

    printf "%s\t.agents/skills/%s\tUNKNOWN\tUNSPECIFIED\tUNKNOWN\tAuto-discovered from ~/.agents/skills.\n" "${name}" "${name}" >> "${manifest}"
    echo "${name}" >> "${listed_tmp}"
    echo "  added to manifest: ${name}"
  done < <(find "${agents_root}" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)
  rm -f "${listed_tmp}"
fi

echo "Syncing third-party skills from manifest..."

synced=0
while IFS=$'\t' read -r skill_name source_rel_path upstream license owner notes; do
  [[ -z "${skill_name}" || "${skill_name}" =~ ^# ]] && continue

  src="${HOME}/${source_rel_path}"
  dest="${registry_dir}/${skill_name}"

  if [[ ! -d "${src}" ]]; then
    echo "Missing source directory: ${src}" >&2
    exit 1
  fi

  rm -rf "${dest}"
  mkdir -p "${dest}"
  cp -R "${src}/." "${dest}/"

  find "${dest}" -name ".DS_Store" -delete

  skill_md_rel=""
  if [[ -f "${dest}/SKILL.md" ]]; then
    skill_md_rel="${dest}/SKILL.md"
  fi

  cat > "${dest}/PROVENANCE.md" <<EOF
# Provenance

- Skill: \`${skill_name}\`
- Synced from: \`${src}\`
- Upstream: ${upstream}
- License: ${license}
- Owner/Author: ${owner}
- Notes: ${notes}
- Synced at (UTC): $(date -u +"%Y-%m-%dT%H:%M:%SZ")

This directory is a mirrored snapshot for dependency tracking.
Authorship remains with the original owner(s).
EOF

  if [[ -n "${skill_md_rel}" ]]; then
    sha="$(shasum -a 256 "${dest}/SKILL.md" | awk '{print $1}')"
    {
      echo
      echo "- SKILL.md SHA256: \`${sha}\`"
    } >> "${dest}/PROVENANCE.md"
  fi

  synced=$((synced + 1))
  echo "  synced: ${skill_name}"
done < "${manifest}"

echo "Done. Synced ${synced} third-party skills."
