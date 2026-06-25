# add-block-id-root-text

A skill for adding Obsidian block IDs to root-text Markdown files. It targets Sanskrit root texts (and their translations) that follow the vault's chapter-verse structure — not commentaries.

---

## What it does

Takes a raw or partially-indexed `.md` file and assigns every content block a unique, citable ID of the form `^chapter-verse` (e.g. `^6-134`). After the skill runs, every verse, colophon, heading, and back-matter block has an ID, enabling Obsidian transclusions, cross-references, and the study-plan pipeline to work correctly.

Specifically it:
- Adds heading IDs (`^0`, `^1-0`, `^I-0`, etc.)
- Assigns verse IDs per chapter (`^1-1` … `^1-36`, `^2-1` … etc.)
- Tags chapter colophons (`^1-a`, `^2-a`, …)
- Tags book back-matter blocks (`^a`, `^b`, …)
- Strips ordinal prefixes left over from OCR or copy-paste (`1. verse text` → `verse text ^1-1`)
- Normalises spacing: one blank line between stanzas, one space before `^`
- Removes null bytes and collapses multiple blank lines

---

## Block ID Convention

IDs follow a **three-zone scheme** based on content role, not heading position.

### Zones

| Zone | Marker | Examples |
|---|---|---|
| Pre-title (before `#` heading) | `T` | `^T-1`, `^T-2` |
| Front matter | Roman numeral | `^I-1`, `^II-3` |
| Chapter verses | Arabic numbers | `^1-1`, `^8-185` |
| Back matter / colophons | Lowercase letter | `^a`, `^b`, `^1-a` |

### Heading IDs

| Heading | ID |
|---|---|
| `#` book title (root book) | `^0` |
| `#` collection title (book is at `##`) | no ID |
| `## N. Chapter` | `^N-0` |
| `## 0. Introduction` (front matter) | `^I-0` |
| `## Colophon` (back matter section) | `^a-0`, `^b-0` |

### Content IDs

| Content | ID format |
|---|---|
| Front matter block | `^I-1`, `^I-2`… |
| Chapter intro (before first verse) | `^N-I`, `^N-II`… |
| Chapter verse | `^N-V` (V = source verse number) |
| Chapter colophon | `^N-a` |
| Book back matter | `^a`, `^b`… |

### Key rules

**Verse numbers come from the source, not a counter.** For Sanskrit, read the `॥N॥` markers. `^8-24` means verse 24 of chapter 8 in the source text — not the 24th block you counted.

**Zone by content, not position.** A colophon gets `^N-a` even if it sits inside a chapter's `##` section with no separator heading. Read the text to confirm the role.

**Interpolated verses** (same number appears twice in the source): first occurrence keeps `^C-V`, duplicate gets `^C-Vx1`, second duplicate `^C-Vx2`. Never use a bare `^C-Vx`.

**Multi-line stanzas**: ID goes on the last line only.

**Back matter under a heading**: if `## Colophon ^a-0` exists, content beneath it gets `^a-1`, `^a-2`… (same pattern as front matter). Without a heading, use bare `^a`, `^b`….

---

## Workflow

The skill combines a Python helper script (`apply.py`) for mechanical changes with LLM judgment for ambiguous cases.

### Step 0 — OCR cleanup (if needed)

Before indexing, remove OCR artifacts:
- Standalone line-number-only blocks (`1`, `2`, `3` as their own paragraphs) — delete entirely
- Page headers/footers embedded in the body
- Hyphenation artifacts

Do **not** strip ordinal prefixes (`1. verse text`) at this stage — the script uses them to set verse numbers.

### Step 1 — Audit

```bash
python "<skill-dir>/apply.py" audit "<file.md>"
```

Prints:
- Heading structure with any missing IDs flagged
- Every block without an ID, labelled `[auto]` (script can handle it) or `[needs LLM judgment]`
- Verse counts per chapter vs. expected Sanskrit counts
- Other issues (null bytes, double-spacing, multiple blanks)

### Step 2 — LLM reviews flagged blocks

For each `[needs LLM judgment]` block, determine its zone by reading the content:
- Is it front matter, a chapter intro, a colophon, or an interpolated verse?
- Is it a multi-line stanza?

### Step 3 — Apply mechanical changes

```bash
python "<skill-dir>/apply.py" apply "<file.md>"
```

Handles everything it can automatically, then prints a fresh audit showing what remains.

### Step 4 — LLM applies the rest

For anything still untagged — ambiguous blocks, interpolated verses, multi-line stanzas — add IDs directly with the Edit tool.

---

## How to use it

Tell Claude:

> Apply `4-SYSTEM/Skills/add-block-id-root-text/SKILL.md` on `<path-to-file.md>`

Claude will run the audit, review flagged blocks, run apply, then handle any remainder manually.

**This skill is for root texts only.** For commentaries, use `format-commentary`. For translations that follow the same chapter-verse structure, the same skill applies — the verse IDs must still match the source verse numbers.
