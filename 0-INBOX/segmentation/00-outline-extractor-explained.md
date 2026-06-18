# How the Outline-Extractor skill works

A plain-language analysis of `4-SYSTEM/Skills/Outline-Extractor/SKILL.md`.

## What it does, in one sentence

It reads a raw Tibetan commentary and pulls out only its **ས་བཅད་** (topical-outline / *sa bcad*) skeleton — the section-announcement phrases — then writes that skeleton out twice: once as a flat indented list, once as a properly nested table of contents with YAML frontmatter.

## The problem it solves

A Tibetan commentary like `bo-མཁན་པོ་ཀུན་དཔལ།.md` does not carry its outline in a separate header. The structure is **announced inline**, woven into the prose. For example the commentary says:

```
བཤད་བྱའི་ཡན་ལག་བཤད་པ་དང་། བཤད་བྱ་དངོས་བཤད་པ་གཉིས་ལས།   ^0-8/0-9
   དང་པོ་ ... ལ་གསུམ་སྟེ། ...
      དང་པོ་ ... ལ་གསུམ་སྟེ། ...
```

So "the explanation has two parts; the first has three; the first of those has three…" The actual tree of topics is buried in these enumeration sentences. The skill's job is to lift that tree out and make it explicit and navigable.

## How it recognises an outline line (the core heuristic)

It treats a line as a structural heading — not ordinary prose — when it shows one of three signals (Rule 2):

1. **Ordinal announcements** — `དང་པོ་` (first), `གཉིས་པ་` (second), `གསུམ་པ་` (third)…
2. **Enumeration / list phrases** — `ལ་གསུམ་སྟེ།` (has three), `ལ་གཉིས།` (has two), `གཉིས་ལས།` (of the two)…
3. **Inline TOC phrasing** — a sentence that names the sub-topics before elaborating each one in turn.

Everything else (the actual commentary on the verses) is ignored.

## How depth is assigned

The skill keeps a running tree as it reads (Step 3). When a node announces *N* sub-items, those sub-items attach one level deeper. Each node gets:

- its **verbatim Tibetan text** (never translated or corrected — Rule 3),
- a **depth** integer, and
- a **hierarchical block ID** of the form `^TOC-N`, `^TOC-N-N`, `^TOC-N-N-N`… where each segment is the item's sequential position under its parent. The first child of `^TOC-1` is `^TOC-1-1`, the second `^TOC-1-2`, and so on — never skipped, never reused (Rule 4).

These `^TOC-…` IDs are the spine of both output files and the thing that lets other files point back at a precise node.

## The two outputs

**File 1 — flat outline (`ས་བཅད་རྐྱང་པ།`):** every heading as a Markdown list item, one tab of indentation per level of depth, block ID at the end of each line. A faithful dump of the skeleton.

**File 2 — nested TOC (`ལྟེ་བའི་དཀར་ཆག།`):** the same tree rendered for reading, using a depth-to-format mapping:

| Depth (segments after `TOC-`) | Format |
|---|---|
| 1 | `## ` |
| 2 | `### ` |
| 3 | `#### ` |
| 4 | `##### ` |
| 5 | `###### ` |
| 6 | `- **…**` |
| 7 | `  - **…**` (2 spaces deeper) |
| 8+ | `    - **…**` (2 more spaces per level) |

Markdown only goes to H6, so levels 1–5 use headings `##`–`######`, and level 6 and beyond fall back to indented **bold** list items. File 2 also carries YAML frontmatter (`title`, `commentary`, `derived_from`, `file_type: adaptation`, `lang_tag: bo`, `status: draft`) and a `---` rule between top-level sections.

## The rules that keep it honest

- **Read-only source.** Nothing in `1-SOURCES/` is ever modified; text is copied verbatim, orthography and all (Rules 1, 3).
- **Both files or neither** (Rule 5).
- **Citation chain.** The outputs live in `3-TRANSFORMATIONS/Adaptations/<id>-sa-bcad/` and count as *Adaptations*, so `2-RAILS/` files may never cite them — a rail needing this structure cites the original commentary's block IDs instead (Rule 7).
- **Always `status: draft`.** Only a human specialist promotes to `complete` (Rule 8).

## The verification pass (Step 6)

Before finishing, it re-reads both files and confirms: every block ID in File 1 appears in File 2; the numeric prefixes in File 2 match the block-ID segments exactly; no outline node was dropped; no source text was altered.

## Mental model

Think of it as a parser with a very specific grammar: the "tokens" are Tibetan enumeration phrases, the "grammar" is *announce-then-elaborate*, and the output is an abstract syntax tree serialised two ways — flat for machines, nested for humans. The `^TOC-…` IDs are the stable addresses that keep the whole thing wired to the rest of the vault.
