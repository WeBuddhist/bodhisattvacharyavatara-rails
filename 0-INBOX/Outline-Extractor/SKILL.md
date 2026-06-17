---
name: Outline-Extractor
description: Extract the embedded structural outline (ས་བཅད།) from any Tibetan commentary file and emit it as a flat, tab-indented bullet list with hierarchical ^TOC- block IDs — reproducing the exact format of the kunpal ས་བཅད་རྐྱང་པ། outline. Use whenever asked to pull the ས་བཅད / topical outline / table of contents out of a Tibetan commentary.
---

# Outline-Extractor

A Tibetan commentary (འགྲེལ་པ་ / ཚིག་འགྲེལ་) carries its own **structural outline** — the ས་བཅད། (sa bcad) — woven directly into the prose. The author announces how many parts a topic has, names each part, then elaborates each in turn, often repeating the announcement locally before each elaboration begins. This skill reads that prose, recovers the full nested topic tree, and writes it out as a **flat tab-indented bullet list** with hierarchical block IDs (`^TOC-N`, `^TOC-N-N`, …), one entry per ས་བཅད node.

The output reproduces the format demonstrated by the Khenpo Kunpal outline file `bo-མཁན་པོ་ཀུན་དཔལ། སྤྱོད་འཇུག་ས་བཅད། ས་བཅད་རྐྱང་པ།.md`. The method is source-agnostic: it works on any Tibetan commentary whose ས་བཅད is expressed in the standard enumerate-then-elaborate style.

---

## Inputs

| Input | Description | Example |
|---|---|---|
| `commentary-file` | Path to the Tibetan commentary to outline | `1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md` |
| `commentary-id` | Short slug for the output folder/filename | `bo-kunpal` |
| `title-bo` | Tibetan title of the work being outlined | `སྤྱོད་འཇུག་ས་བཅད།` |
| `outline-title` *(optional)* | Heading text for the title line | defaults to `དཀར་ཆག་ས་བཅད།` |

If `commentary-id` or `title-bo` is missing, derive a candidate (strip the `bo-` prefix from the filename for the id; read the commentary frontmatter `title:` for the title) and confirm with the user before proceeding. If the `commentary-file` does not exist, stop and report.

---

## Output

One file, created or overwritten:

```
3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ས་བཅད་རྐྱང་པ།.md
```

`ས་བཅད་རྐྱང་པ།` means "outline, plain/flat" — a single linear list whose nesting is carried by indentation and by the dotted block IDs. The output folder is created if it does not exist.

> The vault also recognises a nested heading-based variant (`ལྟེ་བའི་དཀར་ཆག།`). This skill produces the **flat** file only, which is the demonstrated deliverable. If the nested variant is also wanted, generate it afterward by mapping each depth to a heading level (depth 1→`##`, 2→`###`, … 5→`######`, 6+→indented `- **bold**`), preserving every block ID.

---

## Output file format

```markdown
- # དཀར་ཆག་ས་བཅད།

- བཤད་བྱའི་ཡན་ལག་བཤད་པ། ^TOC-1

	- སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། ^TOC-1-1

		- སློབ་དཔོན་སངས་རྒྱས་ཀྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། ^TOC-1-1-1

	- སློབ་མས་ཇི་ལྟར་ཉན་པའི་ཚུལ། ^TOC-1-2

- བཤད་བྱ་དངོས་བཤད་པ་ལ། ^TOC-2

	- བསྟན་བཅོས་ཀྱི་མཚན། ^TOC-2-1
```

Format rules, exactly as in the demonstrated file:

1. **Title line first:** `- # <outline-title>` (default `- # དཀར་ཆག་ས་བཅད།`). No block ID on this line.
2. **Every node is a Markdown list item** `- <text> ^TOC-…`.
3. **Indentation = depth, one tab per level.** A depth-1 node has zero leading tabs; depth-2 has one tab; depth-N has N−1 tabs. Use literal tab characters, not spaces.
4. **One blank line between every entry** (including between siblings, and between the title line and the first entry). The file is double-spaced throughout.
5. **Verbatim Tibetan text.** Copy each ས་བཅད phrase exactly as written in the commentary, including its trailing punctuation (`།`, `་`, etc.). Do not translate, paraphrase, normalise spelling, or strip the shad.
6. **Hierarchical block ID on every node:** `^TOC-` followed by the node's full position path joined by hyphens. The first child of `^TOC-1` is `^TOC-1-1`; its first child is `^TOC-1-1-1`; the second top-level node is `^TOC-2`; and so on. Numbers are natural (no zero-padding), sequential within each parent, never skipped or reused.

---

## How to read the ས་བཅད out of the prose

The outline is not a separate list in the file — it is embedded in sentences. Identify nodes by these recurring markers:

- **Enumeration announcements** — a phrase stating that a topic divides into N parts, typically `…ལ་གཉིས།`, `…ལ་གསུམ་སྟེ།`, `…ལ་བཞི།`, `…ལ་ལྔ་སྟེ།`, `…གཉིས་ལས།`, `…རྣམ་པ་གསུམ་…`. The number word (གཉིས་=2, གསུམ་=3, བཞི་=4, ལྔ་=5, དྲུག་=6, …) tells you **how many children** the current node has. The following clauses name them.
- **The named children**, listed in sequence, each usually a noun phrase ending in a shad (`།`) — e.g. `སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། … སློབ་མས་ཇི་ལྟར་ཉན་ཚུལ། … དཔོན་སློབ་གཉིས་ཀས་འཆད་ཉན་ཇི་ལྟར་བགྱི་བའི་ཚུལ་ལོ།`.
- **Ordinal re-announcements** before each elaboration — `དང་པོ་` (1st), `གཉིས་པ་` (2nd), `གསུམ་པ་` (3rd), `བཞི་པ་`, `ལྔ་པ་`, … These restate a child by name and then frequently announce its own sub-division (`དང་པོ་ X ལ་གསུམ་སྟེ།`). Use them to (a) confirm the child's exact wording and (b) descend a level.

Worked example (from the Kunpal commentary opening, blocks `^0-8`–`^0-11`):

> `…འཆད་པར་བྱེད་པ་ལ། བཤད་བྱའི་ཡན་ལག་བཤད་པ་དང་། བཤད་བྱ་དངོས་བཤད་པ་གཉིས་ལས།`
> → the work has **2** top-level parts: `བཤད་བྱའི་ཡན་ལག་བཤད་པ།` (`^TOC-1`) and `བཤད་བྱ་དངོས་བཤད་པ།` (`^TOC-2`).
>
> `དང་པོ་བཤད་བྱའི་ཡན་ལག་བཤད་པ་ལ་གསུམ་སྟེ། སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། སློབ་མས་ཇི་ལྟར་ཉན་ཚུལ། དཔོན་སློབ་གཉིས་ཀས་འཆད་ཉན་ཇི་ལྟར་བགྱི་བའི་ཚུལ་ལོ།`
> → part 1 has **3** children: `^TOC-1-1`, `^TOC-1-2`, `^TOC-1-3`.
>
> `དང་པོ་སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ་ལ་གསུམ་སྟེ། སློབ་དཔོན་སངས་རྒྱས་…`
> → `^TOC-1-1` itself has 3 children: `^TOC-1-1-1`, `^TOC-1-1-2`, `^TOC-1-1-3`. Descend.

Cross-checking tip: the count word in an announcement must equal the number of children you record under that node. If they disagree, you have either merged two nodes or split one — re-read the passage. When the announcement uses the verbatim child wording, prefer it over a looser later restatement.

---

## Procedure

### Step 1 — Confirm inputs
Verify `commentary-file` exists. Resolve `commentary-id` and `title-bo` (asking/confirming if derived). If output already exists, warn it will be overwritten.

### Step 2 — Read the whole commentary
Read the file end to end. The ས་བཅད is usually densest in the opening (the author lays out the whole skeleton) and is then re-announced locally before each section. Build the tree primarily from the announcements, using the local re-announcements to verify wording and depth.

### Step 3 — Build the outline tree
Maintain a tree where each node has: `text` (verbatim Tibetan), `depth` (≥1), and `id` (`^TOC-…`). When an announcement says a node has N parts, create N children at depth+1 with sequential IDs. Recurse for every child that is itself subdivided. Process in document order so IDs come out sequential.

### Step 4 — Write the flat file
Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` if needed. Write the title line `- # <outline-title>`, a blank line, then each node in depth-first order as:

```
<(depth−1) tabs>- <verbatim text> ^TOC-<dash-joined-path>
```

with exactly one blank line after every line.

### Step 5 — Verify (see checklist below).

---

## Rules

1. **`1-SOURCES/` is read-only.** Extract only; never edit, correct, or re-punctuate the commentary.
2. **Verbatim Tibetan.** No translation, paraphrase, spelling normalisation, or shad removal in node text.
3. **One node per ས་བཅད entry.** Do not invent structure the text does not announce, and do not drop announced nodes.
4. **IDs mirror the hierarchy exactly** — the dotted path of `^TOC-…` equals the node's position; sequential within each parent; no skips, no reuse.
5. **This output is an Adaptation, not a source.** It lives under `3-TRANSFORMATIONS/Adaptations/` and must never be transcluded or cited by `2-RAILS/` files; rails cite the original `1-SOURCES/` commentary blocks instead.
6. **`status` stays `draft`** if frontmatter is added; only a human specialist marks it complete.

---

## Completion check

- [ ] `commentary-file` confirmed to exist in `1-SOURCES/`
- [ ] Output folder `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` exists
- [ ] Title line is `- # <outline-title>` with no block ID
- [ ] Every node is a tab-indented `- ` list item (depth−1 tabs) ending in `^TOC-…`
- [ ] Exactly one blank line between every entry
- [ ] Every announced count matches the number of children recorded under that node
- [ ] Block-ID paths are sequential within each parent, with no skips or reuse
- [ ] No node text was translated, paraphrased, or re-punctuated
- [ ] Nothing in `1-SOURCES/` was modified
