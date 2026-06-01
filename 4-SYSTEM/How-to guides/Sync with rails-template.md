# How to sync with rails-template

This guide covers two operations:
- **Pulling updates from the template into a vault** (e.g. a new skill or CLAUDE.md improvement)
- **Backporting improvements from a vault into the template** (e.g. a generic skill that other vaults should have)

---

## What to always exclude

The following folders are vault-specific and must **never** be touched when syncing in either direction:

| Path | Reason |
|------|--------|
| `gemini-scribe/` | Vault-specific plugin state (prompts, scheduled-tasks JSON, agent sessions) |
| `4-SYSTEM/gemini-scribe/` | Vault-specific AGENTS.md and plugin sessions |
| `4-SYSTEM/Guidelines/vault-annex.md` | Vault-specific addressing scheme, commentary IDs, language tracks |
| `4-SYSTEM/Skills/<vault-specific-skills>/` | Skills that only make sense for this text (e.g. `atthakatha-summaries`, `daily-tipitaka-day`, `practice-summaries`) |
| `.claude/commands/<vault-specific-commands>.md` | Command files for vault-specific skills |
| `1-SOURCES/` | All source material is vault-specific |
| `2-RAILS/` | All rails are vault-specific |
| `3-TRANSFORMATIONS/` | All outputs are vault-specific |
| `0-INBOX/` | All inbox content is vault-specific |

---

## What is safe to sync

Files that carry generic methodology and should stay in sync across all vaults:

| Path | Notes |
|------|-------|
| `4-SYSTEM/CLAUDE.md` | Apply additions; preserve vault-specific §12 table rows and annex link |
| `4-SYSTEM/Skills/SKILLS-CATALOG.md` | Apply generic sections; preserve vault-specific skill entries |
| `4-SYSTEM/Guidelines/0-VAULT-Structure.md` | Generic architecture doc |
| `4-SYSTEM/Guidelines/why-rails.md` | Generic methodology doc |
| `4-SYSTEM/Guidelines/skills-system.md` | Generic skills discovery doc |
| `4-SYSTEM/Skills/<generic-skill>/` | Any skill that works in any vault (add-toc, epub-to-markdown, verse-context, create-skill, vault-audit, etc.) |
| `.claude/commands/<generic-command>.md` | Command files for generic skills |
| `.obsidian/plugins/` | Plugin updates (main.js, manifest.json, styles.css) — not data.json |
| `4-SYSTEM/How-to guides/` | Generic how-to docs |
| `README.md` | Apply structural improvements; preserve vault-specific text |

---

## When pulling from rails-template into a vault

1. Open both repos side by side.
2. For each file in the "safe to sync" list above, diff template vs vault.
3. Apply additions and structural improvements to the vault copy.
4. When updating `CLAUDE.md` or `SKILLS-CATALOG.md`: merge carefully — the vault version has vault-specific content (annex links, skill rows) that must be preserved.
5. After adding any new generic skill from the template, check that its `.claude/commands/` file is also present in the vault.
6. **Do not touch anything in the "always exclude" list.**

## When backporting from a vault into rails-template

1. Identify the change to backport: a new generic skill, a CLAUDE.md improvement, a new script, etc.
2. Check whether the change is truly generic (works in any vault) or vault-specific. If vault-specific, do not backport.
3. For generic skills: copy the skill folder, update SKILLS-CATALOG.md (generic sections only), add the `.claude/commands/` file.
4. For CLAUDE.md improvements: apply them in template-neutral language (remove vault-specific text like commentary IDs, specific skill names that only exist in the source vault).
5. **Do not touch anything in the "always exclude" list.**
