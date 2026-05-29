---
name: create-skill
description: Scaffold a new skill completely and correctly — creates the SKILL.md with the required structure, registers it in SKILLS-CATALOG.md, creates the slash command file, and optionally adds it to the CLAUDE.md quick-reference table. Use this skill every time a new skill is created to guarantee all four registration locations are populated in one pass.
---

# create-skill

This is the canonical way to add a new skill to the vault. It replaces the four-step manual checklist in `4-SYSTEM/Guidelines/skills-system.md` with a single guided procedure that cannot omit a registration step.

Never create a skill folder manually and register it piecemeal. Use this skill. The `vault-audit` skill checks that every skill folder is registered in all required locations — if you use this skill, those checks will always pass.

---

## Inputs

Gather the following before starting. If any item is unknown, ask the human contributor before proceeding — do not guess or leave fields blank.

| Field | Description | Example |
|---|---|---|
| `skill-name` | Lowercase, hyphenated, unique | `translate-section` |
| `purpose` | One sentence, terse — used in frontmatter, catalog, and command file | `Translate a small batch of TOC nodes into the target language.` |
| `catalog-section` | Which section of SKILLS-CATALOG.md it belongs to | `Translation skills` |
| `inputs-description` | What the skill needs to run | Files, IDs, prior outputs |
| `outputs-description` | What it produces and where | File path(s) |
| `commonly-used` | Whether it belongs in the CLAUDE.md §12 quick-reference table | yes / no |
| `claude-md-task-description` | If commonly-used: the left-column task phrase for the §12 table | `Translate a TOC node batch` |

---

## Output

Four files written or modified:

| Location | Action |
|---|---|
| `4-SYSTEM/Skills/<skill-name>/SKILL.md` | Created |
| `4-SYSTEM/Skills/SKILLS-CATALOG.md` | Entry appended to the correct section |
| `.claude/commands/<skill-name>.md` | Created |
| `4-SYSTEM/CLAUDE.md` | Row added to §12 table (only if `commonly-used: yes`) |

---

## Rules

1. **Never overwrite an existing skill folder.** If `4-SYSTEM/Skills/<skill-name>/` already exists, stop and report the conflict to the human contributor. Do not proceed.
2. **The skill-name must be unique.** Check both the Skills folder and SKILLS-CATALOG.md for collisions before writing anything.
3. **All four locations must be written in a single execution.** Do not write the SKILL.md and stop. Do not skip the command file because it "seems obvious." Complete all four steps every time.
4. **The SKILL.md must include all required sections** (see Procedure — Step 2). A SKILL.md missing required sections is not a valid skill.
5. **Append to the correct catalog section.** If the target section does not exist in SKILLS-CATALOG.md, create it. Do not append to the wrong section or add a top-level entry outside any section.
6. **Mark new catalog entries `[exists]`.** Never mark a newly created skill `[planned]` — that marker is for skills that have been decided on but not yet written.
7. **Do not modify any file in `1-SOURCES/`.** This skill writes only to the four locations listed above.

---

## Procedure

### Step 1 — Pre-flight checks

1. Confirm `4-SYSTEM/Skills/<skill-name>/` does not already exist.
2. Confirm `<skill-name>` does not appear as a `### \`<skill-name>\`` heading in `SKILLS-CATALOG.md`.
3. Confirm `.claude/commands/<skill-name>.md` does not already exist.
4. If any collision is found, stop. Report the exact collision to the human contributor and ask how to proceed.

### Step 2 — Create the SKILL.md

Create the directory `4-SYSTEM/Skills/<skill-name>/` and write `SKILL.md` using the template below. Fill every placeholder. Do not leave template placeholder text in the output.

```markdown
---
name: <skill-name>
description: <purpose — one sentence, terse>
---

# <skill-name>

<Two to four sentences explaining what this skill produces, why it exists, and what failure mode it prevents or consistency it enforces. Be specific about what "correct output" looks like.>

---

## Inputs

<List every input required before the skill can start. For each input, name it, describe what it is, and give the expected file path or format. If an input is missing, the skill should stop and ask — never proceed on assumptions.>

## Output

<State the exact file path(s) this skill writes to. Include the full path from the vault root. If the path is dynamic (e.g. includes a verse ID), show the pattern.>

---

## Output file format

<Provide a complete template of the output file — YAML frontmatter, headings, section structure. Use fenced code blocks. This is the canonical shape every output of this skill must match.>

---

## Rules

<Numbered list of invariants. Each rule is a constraint that must hold throughout execution — something that must never happen, or something that must always be true of the output. Be specific enough that a violation is unambiguous.>

---

## Procedure

<Numbered execution steps in exact order. Each step is a concrete action. Where a step has sub-steps, use lettered sub-items. Reference exact file paths. Do not use vague verbs like "handle" or "process" — say exactly what to do.>

---

## Completion check

- [ ] <Specific verifiable condition>
- [ ] <Specific verifiable condition>
- [ ] <Add as many checks as needed — one per material requirement of the skill>
```

The following sections are **required** in every SKILL.md. A skill missing any of these is incomplete:
- YAML frontmatter with `name:` and `description:`
- Purpose paragraph (the body text immediately after the H1)
- Inputs
- Output
- Output file format
- Rules
- Procedure
- Completion check

### Step 3 — Add the catalog entry

Open `4-SYSTEM/Skills/SKILLS-CATALOG.md`. Locate the section matching `catalog-section`. Append the following entry at the end of that section, after the last existing skill entry and before the next `---` divider:

```markdown
### `<skill-name>` **[exists]**
**Purpose:** <purpose sentence>
**Inputs:** <inputs-description, condensed to one sentence>
**Outputs:** <outputs-description, condensed to one sentence>
→ [`<skill-name>/SKILL.md`](<skill-name>/SKILL.md)
```

If the target section does not exist in SKILLS-CATALOG.md, create it at the end of the file:

```markdown
---

## <catalog-section>

<One sentence describing what skills in this section do and when they are used.>

### `<skill-name>` **[exists]**
**Purpose:** <purpose sentence>
**Inputs:** <inputs-description, condensed to one sentence>
**Outputs:** <outputs-description, condensed to one sentence>
→ [`<skill-name>/SKILL.md`](<skill-name>/SKILL.md)
```

### Step 4 — Create the slash command file

Write `.claude/commands/<skill-name>.md` with exactly this content (no extra lines):

```markdown
Read `4-SYSTEM/Skills/<skill-name>/SKILL.md` in full, then execute it on the file(s) or input the user specifies.

Skill purpose: <purpose sentence>
```

### Step 5 — Update CLAUDE.md §12 (conditional)

If `commonly-used` is **yes**:

Open `4-SYSTEM/CLAUDE.md` and find the quick-reference table in §12. Append a new row at the end of the table:

```markdown
| <claude-md-task-description> | `<skill-name>` |
```

If `commonly-used` is **no**, skip this step.

### Step 6 — Self-verification

After all writes are complete, verify each of the four registration locations:

1. `4-SYSTEM/Skills/<skill-name>/SKILL.md` — exists and contains all eight required sections.
2. `4-SYSTEM/Skills/SKILLS-CATALOG.md` — contains `### \`<skill-name>\`` with `[exists]` marker.
3. `.claude/commands/<skill-name>.md` — exists and references the correct SKILL.md path.
4. `4-SYSTEM/CLAUDE.md` §12 — contains a row for `<skill-name>` (only if `commonly-used: yes`).

If any verification fails, fix the gap before reporting completion.

---

## Completion check

- [ ] No pre-existing collision found for `<skill-name>`
- [ ] `4-SYSTEM/Skills/<skill-name>/SKILL.md` created with all eight required sections populated (no placeholder text remaining)
- [ ] Catalog entry added to the correct section with `[exists]` marker
- [ ] `.claude/commands/<skill-name>.md` created with the correct two-line content
- [ ] CLAUDE.md §12 updated if `commonly-used: yes`; untouched if `commonly-used: no`
- [ ] All four locations verified after writing
