---
name: tag-inline-toc
description: >
  Identify inline structural announcement phrases (sa bcad) in a formatted
  Tibetan commentary file, wrap the announced terms in Obsidian wikilinks,
  and insert standalone markdown heading lines with block IDs per CLAUDE.md §5b.
  Run after format-commentary, before structural-outline-ingest.

  Trigger this skill when the user says things like:
  "tag the inline TOC", "add wikilinks to the outline phrases",
  "mark up the sa bcad", "tag the structural announcements",
  "add table of content tags", or "add headings to this commentary".
---

# tag-inline-toc

Tibetan commentaries use **inline structural announcements** (*sa bcad*): sentences where the author enumerates the sub-topics that will follow before treating each one in turn. This skill makes those announcements machine-readable by doing **two things**:

1. **Inline TOC** — wrapping each announced term and each section-body restatement in `[[#^N-N-0|term]]` Obsidian wikilinks.
2. **Heading TOC** — inserting a standalone markdown heading line (`##` / `###` / `####`) with a block ID immediately before each section-body paragraph.

This implements the convention in CLAUDE.md §5b. The output is saved to `0-INBOX/temp/` and is **not** yet a `1-SOURCES/` file; human review is required before ingest.

---

## Inputs

| Field | Description |
|---|---|
| Input file | Path to a formatted Tibetan commentary file — typically `0-INBOX/segmentation/<filename>.md` |
| Block ID map | The operator supplies, or Claude derives from the sa bcad structure, a mapping of section → block ID (`^N-N-0`) |

The input file must already have:
- YAML frontmatter (at minimum `title:`, `author:`, `file_type:`, `language_tag:`)
- No wikilink tags on announcement phrases yet
- No standalone heading lines yet

---

## Output

A single file at:

```
0-INBOX/temp/tagged-<original-filename>
```

The output adds two types of markup to the original prose:

1. **Wikilinks** — wrap existing terms in `[[#^block-id|term]]`; no prose text is deleted or reordered.
2. **Heading lines** — new `##` / `###` / `####` lines inserted on a blank line immediately before each section-body paragraph. These are net-new lines not present in the source.

---

## Output file format

### Heading line format

Insert one heading line per section, on its own line, immediately before the paragraph that opens that section's body. Use a blank line before and after the heading.

| Depth | Heading level | Format |
|---|---|---|
| 1 (top-level) | `##` | `## <title> ^N-0` |
| 2 | `###` | `### <title> ^N-N-0` |
| 3 | `####` | `#### <title> ^N-N-N-0` |

The `<title>` is the short section name (the announced term or section title, not the full ordinal phrase).

Example:
```
## མཚན་གྱི་དོན། ^1-0

## སྤྱིའི་ཕྱག། ^2-0

### རྩོམ་པ་ལ་འཇུག་ཚུལ། ^3-1-0

#### མཆོད་པར་བརྗོད་པ། ^3-1-1-0
```

### Wikilink format — announcement sentence

In the enumeration sentence, each announced term becomes a link pointing **forward** to the block ID of the section it announces:

```
[[#^1-1-0|མདོར་བསྟན་པ་]]
```

Example:

Before:
```
ལེའུ་དང་པོ་ལ་མདོར་བསྟན་པ་དང་རྒྱས་པར་བཤད་པ་གཉིས་ཡོད་པ་ལས།
```

After:
```
ལེའུ་དང་པོ་ལ་[[#^1-1-0|མདོར་བསྟན་པ་]]དང་[[#^1-2-0|རྒྱས་པར་བཤད་པ་]]གཉིས་ཡོད་པ་ལས།
```

### Wikilink format — section body restatement (inline heading tag)

At the opening of each section, the ordinal-plus-title phrase is wrapped in a self-referential link. This stays **inline in the prose** alongside the heading line above it.

Before:
```
གཉིས་པ་བཤད་པ་ནི་སྤངས་རྟོགས་མཐར་ཕྱིན་པའི་...
གསུམ་པ་འདོགས་ཚུལ་ནི་དཔེ་དང་གཞུང་ཚད་དང་...
```

After (heading line inserted above, wikilink added inline):
```
### བཤད་པ། ^1-2-0

[[#^1-2-0|གཉིས་པ་བཤད་པ་]]ནི་སྤངས་རྟོགས་མཐར་ཕྱིན་པའི་...

#### འདོགས་ཚུལ། ^1-3-0

[[#^1-3-0|གསུམ་པ་འདོགས་ཚུལ་]]ནི་དཔེ་དང་གཞུང་ཚད་དང་...
```

---

## Rules

1. **Insert heading lines before each section body.** Each section gets exactly one `##` / `###` / `####` heading line placed on a blank line immediately before its opening paragraph. Depth-1 → `##`, depth-2 → `###`, depth-3 → `####`.
2. **Do not insert, delete, or alter any existing prose text.** The only permitted changes are: (a) inserting new heading lines, and (b) wrapping an existing term in `[[#^id|term]]`. No words, characters, punctuation, or whitespace in the existing prose may be added, removed, or reordered.
3. **Heading title is the short section name.** Use the announced/section term, not the full ordinal phrase. E.g. `བཤད་པ།` not `གཉིས་པ་བཤད་པ།`.
4. **Block ID on the heading line.** Append the block ID directly after the heading title, separated by a space: `### བཤད་པ། ^1-2-0`.
5. **Wrap only the minimal display text in wikilinks.** Structural term only — not surrounding particles, conjunctions, or count words.
6. **Block ID scheme.** Section block IDs follow the `^N-N-0` pattern (depth-1 → `^1-0`; depth-2 → `^1-1-0`; depth-3 → `^1-1-1-0`). Maximum four segments (`^N-N-N-0`).
7. **Announced terms must link to real block IDs.** Every `[[#^id|term]]` must correspond to a block ID on a heading line in the same file.
8. **Self-referential links are intentional.** The inline wikilink at the start of a section body (`[[#^1-2-0|གཉིས་པ་བཤད་པ་]]`) points to the heading line directly above it.
9. **Output file goes to `0-INBOX/temp/`**, never to `1-SOURCES/` or `2-RAILS/`.

---

## Procedure

### Step 1 — Read the file

Read the full input file. Extract and hold:
- The YAML frontmatter block.
- The full body text.

---

### Step 2 — Identify announcement sentences

Scan the body for **structural announcement phrases**. These are sentences (or short clauses) that enumerate upcoming sub-topics. Two distinct surface forms appear:

#### Form A — Full-sentence style (longer)

- Enumerate two or more upcoming sub-topics joined by `དང་`.
- End (or nearly end) with a count word: `གཉིས།`, `གཉིས་ལས།`, `གཉིས་སྟེ།`, `གསུམ།`, `གསུམ་ལས།`, `གསུམ་སྟེ།`, `བཞི།`, `བཞི་ལས།`, `ལྔ།`, `དྲུག།` (and so on).
- Often begin with the parent section title or ordinal: `X ལ་ Y དང་ Z གཉིས།`.

Example:
```
ལེའུ་དང་པོ་ལ་མདོར་བསྟན་པ་དང་རྒྱས་པར་བཤད་པ་གཉིས་ཡོད་པ་ལས།
```

#### Form B — Short commentary style (compact)

In commentaries, outlines frequently appear as a compact line containing the **count immediately after** `་ལ་` or `་ལ་ཡང་`, followed by the topic names separated by `དང༌།` on the same line, with the last topic ending in `འོ། །`.

Pattern:
```
[parent section]་ལ་[count]། [topic 1]དང༌། [topic 2]དང༌། [topic N]འོ། །
[parent section]་ལ་ཡང་[count]། [topic 1]དང༌། [topic 2]འོ། །
```

Example:
```
གཉིས་པ་ལ་བཞི། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ་དང༌། བྱང་ཆུབ་ཀྱི་སེམས་ངོས་བཟུང་བ་དང༌། དེ་ལ་ཕན་ཡོན་དེ་དག་འབྱུང་བའི་རྒྱུ་མཚན་དང༌། བྱང་ཆུབ་ཀྱི་སེམས་སྒོམ་པའི་གང་ཟག་ལ་བསྟོད་པའོ། །
```

Here `གཉིས་པ་ལ་བཞི།` declares four sub-topics; the four terms follow inline, each ended by `དང༌།` except the last which ends `འོ། །`. Extract each `དང༌།`-separated segment as an announced term (strip trailing `འོ། །` from the last).

Count words that trigger Form B detection (appearing directly after `་ལ་` or `་ལ་ཡང་`):

`གཉིས།` `གསུམ།` `བཞི།` `ལྔ།` `དྲུག།` `བདུན།` `བརྒྱད།` `དགུ།` `བཅུ།`

---

#### Identifying section-body restatements

Also identify **section-body restatements**: the paragraph that opens a section. After a count is declared, each sub-section may be addressed in **one of three forms**:

| Form | Pattern | Example |
|---|---|---|
| Ordinal only | `[ordinal]་ནི།` or `[ordinal]་ནི` | `གཉིས་པ་ནི།` |
| Name only | `[topic name]་ནི།` or `[topic name]་ནི` | `དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི` |
| Ordinal + name | `[ordinal]་[topic name]་ནི།` | `གཉིས་པ་དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི` |

When scanning for section-body openings, match any of the three forms. Use the declared topic list from the nearest ancestor announcement to resolve which sub-section is being opened when the form is "ordinal only" or "name only".

Common section-start ordinals:

| Tibetan | Meaning |
|---|---|
| དང་པོ། / དང་པོ་ནི། | First |
| གཉིས་པ། / གཉིས་པ་ནི། | Second |
| གསུམ་པ། / གསུམ་པ་ནི། | Third |
| བཞི་པ། / བཞི་པ་ནི། | Fourth |
| ལྔ་པ། | Fifth |
| དྲུག་པ། | Sixth |
| བདུན་པ། | Seventh |
| བརྒྱད་པ། | Eighth |
| དགུ་པ། | Ninth |
| བཅུ་པ། | Tenth |

---

### Step 3 — Build the section hierarchy and assign block IDs

Working through the document from top to bottom, reconstruct nesting from the announcements:

1. Top-level announcement → **depth-1** sections, block IDs `^1-0`, `^2-0`, `^3-0`, …
2. Announcement inside a depth-1 section → **depth-2**, block IDs `^1-1-0`, `^1-2-0`, …
3. Announcement inside a depth-2 section → **depth-3**, block IDs `^1-1-1-0`, …
4. Do not go deeper than depth-3.

Record for each section: its block ID, short title, announced title, and the paragraph where its body opens.

---

### Step 4 — Extract announced terms

For an announcement such as:

```
ལེའུ་དང་པོ་ལ་མདོར་བསྟན་པ་དང་རྒྱས་པར་བཤད་པ་གཉིས་ཡོད་པ་ལས།
```

The announced terms are the elements between `ལ་` and the count word, joined by `དང་`:
1. `མདོར་བསྟན་པ` → block ID `^1-1-0`, short title `མདོར་བསྟན་པ།`
2. `རྒྱས་པར་བཤད་པ` → block ID `^1-2-0`, short title `རྒྱས་པར་བཤད་པ།`

If the announcement is ambiguous, leave a `<!-- TODO: unclear -->` comment and continue.

---

### Step 5 — Tag announcement sentences

In each announcement sentence, wrap each announced term in `[[#^block-id|term]]`.

- Wrap only the minimal structural term; leave particles and count words outside.
- Do not create overlapping links.

Example:
```
# Before
ལེའུ་དང་པོ་ལ་མདོར་བསྟན་པ་དང་རྒྱས་པར་བཤད་པ་གཉིས་ཡོད་པ་ལས།

# After
ལེའུ་དང་པོ་ལ་[[#^1-1-0|མདོར་བསྟན་པ་]]དང་[[#^1-2-0|རྒྱས་པར་བཤད་པ་]]གཉིས་ཡོད་པ་ལས།
```

---

### Step 6 — Insert heading lines and tag section-body restatements

For each section opening, do both actions together:

**6a — Insert heading line** immediately before the section-body paragraph:

```
### བཤད་པ། ^1-2-0
```

Ensure there is a blank line before the heading (after the previous paragraph) and a blank line after the heading (before the section-body paragraph).

**6b — Wrap the inline restatement** in a self-referential wikilink on the same paragraph:

```
[[#^1-2-0|གཉིས་པ་བཤད་པ་]]ནི་སྤངས་རྟོགས་མཐར་ཕྱིན་པའི་...
```

Combined result for a section opening:

```
(blank line)
### བཤད་པ། ^1-2-0

[[#^1-2-0|གཉིས་པ་བཤད་པ་]]ནི་སྤངས་རྟོགས་མཐར་ཕྱིན་པའི་བྱང་ཆུབ་ཐོབ་པའི་...
```

---

### Step 7 — Write output file

Compose the final document:
- YAML frontmatter (unchanged)
- Full body text with heading lines inserted and wikilinks applied

Write to:
```
0-INBOX/temp/tagged-<original-filename>
```

If a file with that name already exists, append `-v2` (then `-v3`, etc.) rather than overwriting.

---

### Step 8 — Verify and present

Read the output file. Confirm:
- YAML frontmatter intact
- Heading lines present (`##` / `###` / `####` with block IDs)
- At least one `[[#^...|...]]` wikilink present in an announcement sentence
- At least one `[[#^...|ordinal+title]]` wikilink present at a section opening
- Existing prose text unchanged (no deletions or reordering)

Report to the user:
- Number of heading lines inserted
- Number of announcement sentences tagged
- Number of section-body restatements tagged (inline heading tags)
- Any positions where parsing was ambiguous (left as `<!-- TODO -->`)
- The output file path

---

## Completion check

- [ ] Input file read
- [ ] All structural announcement sentences identified
- [ ] Section hierarchy and block ID map built (`^N-0`, `^N-N-0`, `^N-N-N-0`)
- [ ] Every announced term in every announcement sentence wrapped in `[[#^id|term]]`
- [ ] Heading line (`##` / `###` / `####` with block ID) inserted before each section body
- [ ] Every section-body restatement wrapped in `[[#^id|ordinal+title]]` (inline heading tag)
- [ ] Existing prose text unchanged (no insertions into prose, no deletions)
- [ ] Output written to `0-INBOX/temp/tagged-<filename>`
- [ ] Verification pass confirms headings and wikilinks both present
