# Skills — how to discover, run, and create them

This document explains the skills system for any AI agent working in this vault: what skills are, how agents find them, how to execute one, how to add a new one, and how to keep the three discovery mechanisms in sync.

---

## What a skill is

A skill is a reusable, step-by-step procedure for one well-defined vault operation. It replaces ad-hoc improvisation with a fixed, reviewed workflow that has been calibrated to produce consistent output — correct frontmatter, correct citation format, correct file locations — every time.

Skills live at:

```
4-SYSTEM/Skills/<skill-name>/SKILL.md
```

Every skill that exists is listed in the catalog:

```
4-SYSTEM/Skills/SKILLS-CATALOG.md
```

---

## The rule: check before starting

**Before beginning any task in this vault, read `4-SYSTEM/Skills/SKILLS-CATALOG.md` and check whether a skill covers the task.** This rule appears in both `4-SYSTEM/CLAUDE.md` and `4-SYSTEM/gemini-scribe/AGENTS.md`. It is not advisory. A task completed without its skill must be redone.

If a matching skill exists:

1. Open and read its `SKILL.md` in full.
2. Follow the execution steps exactly — do not invent shortcuts or skip sections.
3. Use the completion checklist at the end (if present) before considering the task done.

---

## How agents discover skills

There are three mechanisms, one per agent type:

### Claude Code — `CLAUDE.md` import chain

The vault root contains a `CLAUDE.md` with a single line:

```
@4-SYSTEM/CLAUDE.md
```

Claude Code auto-loads `CLAUDE.md` from the git root at the start of every session. That import pulls in the full operational instructions, including the skills-first rule in §1 and the skills reference table in §12. No path needs to be specified — the rule is active by default.

### Claude Code — slash commands

`.claude/commands/` contains one `.md` file per skill. Each file tells Claude to load and execute a specific skill. In any Claude Code session, typing `/verse-context`, `/epub-to-markdown`, `/glossary-combine`, and so on will immediately load the correct `SKILL.md` and begin execution.

Current commands mirror every skill in `SKILLS-CATALOG.md`. When you add a new skill, add a matching command file (see below).

### Gemini Scribe — `AGENTS.md`

`4-SYSTEM/gemini-scribe/AGENTS.md` is the system prompt loaded by the Gemini Scribe plugin. It opens with the same skills-first gate as `CLAUDE.md`: read the catalog, open the matching `SKILL.md`, follow it exactly. Gemini has file-read tools and can retrieve any `SKILL.md` from the vault during a session.

---

## What a SKILL.md contains

Every `SKILL.md` must include:

| Section | Required | Notes |
|---|---|---|
| YAML frontmatter | yes | `name:` and `description:` at minimum |
| Purpose paragraph | yes | One short paragraph stating what the skill does and why it exists |
| Inputs | yes | List every input the skill needs before it can start |
| Output | yes | Exact file path(s) the skill produces |
| Output file format | yes | The exact Markdown/YAML structure of the output — include a full template |
| Rules | yes | Numbered list of invariants that must hold; what must never happen |
| Procedure | yes | Numbered execution steps in exact order |
| Completion checklist | recommended | Checkbox list the agent ticks before declaring the task done |

`verse-context/SKILL.md` is a clean reference for a prose-workflow skill. `epub-to-markdown/SKILL.md` is a reference for a technical multi-step skill that invokes Python scripts.

---

## How to add a new skill

Follow these steps in order. Do not add a skill to only one of these locations — all four must stay in sync.

### 1. Create the skill folder and SKILL.md

```
4-SYSTEM/Skills/<skill-name>/SKILL.md
```

Name the skill in lowercase, hyphenated form. Write the `SKILL.md` following the section structure above. Include a YAML frontmatter block:

```yaml
---
name: <skill-name>
description: <one sentence, terse — this appears in the catalog and the slash command description>
---
```

If the skill invokes Python scripts or other supporting files, add them to the same folder.

### 2. Add an entry to SKILLS-CATALOG.md

`4-SYSTEM/Skills/SKILLS-CATALOG.md` lists every skill grouped by workflow phase. Add the new skill to the correct group. Each entry follows this template:

```markdown
### `<skill-name>` **[exists]**
**Purpose:** <what the skill does>
**Inputs:** <what it needs>
**Outputs:** <what it produces>
**Rules:** <any critical constraint not obvious from purpose>
→ [`<skill-name>/SKILL.md`](<skill-name>/SKILL.md)
```

### 3. Add a slash command for Claude Code

Create a file at:

```
.claude/commands/<skill-name>.md
```

Contents:

```markdown
Read `4-SYSTEM/Skills/<skill-name>/SKILL.md` in full, then execute it on the file(s) or input the user specifies.

Skill purpose: <copy the one-sentence description from the SKILL.md frontmatter>
```

This makes the skill available as `/<skill-name>` in any Claude Code session.

### 4. Update CLAUDE.md §12 if the skill is commonly used

`4-SYSTEM/CLAUDE.md` §12 contains a quick-reference table of key skills. Add a row if the skill is likely to be needed frequently:

```markdown
| <Task description> | `<skill-name>` |
```

---

## Running a skill step-by-step

1. **Read the catalog** — `4-SYSTEM/Skills/SKILLS-CATALOG.md`. Find the skill.
2. **Read the SKILL.md** — open the linked `SKILL.md` and read it in full before touching any file.
3. **Confirm inputs** — verify every input the skill requires is available. If an input is missing, stop and ask the human contributor.
4. **Execute the procedure** — follow the numbered steps in the Procedure section. Do not reorder or skip steps.
5. **Apply the rules** — the Rules section lists invariants that must hold throughout. Check them as you go.
6. **Tick the completion checklist** — if the skill has a completion checklist, verify every item before writing the output.
7. **Write the output** — to the path specified in the Output section. If the file already exists, update in place rather than overwriting unless the skill says otherwise.

---

## Maintenance — keeping the three mechanisms in sync

The three discovery mechanisms (CLAUDE.md import, slash commands, AGENTS.md) all point to the same source of truth: `SKILLS-CATALOG.md`. When the catalog changes, the other two must change too:

| Change | What to update |
|---|---|
| New skill added | SKILLS-CATALOG.md entry + `.claude/commands/<skill-name>.md` + CLAUDE.md §12 table (if commonly used) |
| Skill renamed | Rename the folder, update SKILLS-CATALOG.md, rename the command file, update CLAUDE.md §12 |
| Skill removed | Mark as `[removed]` in SKILLS-CATALOG.md, delete or update the command file |
| Skill description changed | Update SKILLS-CATALOG.md entry + command file `Skill purpose:` line |

The `4-SYSTEM/` folder is read-only for agents — these updates are made by the human contributor. If an agent identifies a gap (no skill for a common task) it should flag it but not write to `4-SYSTEM/`.
