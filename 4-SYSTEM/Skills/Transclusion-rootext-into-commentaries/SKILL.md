---
name: Transclusion-rootext-into-commentaries
description: Transclude root-text verses into a Tibetan commentary and format the spacing around each transclusion. Runs a three-stage pipeline — (1) insert `![[root#^N-V]]` before each verse's first full inline quotation in the commentary, (2) remove the blank line between the preceding commentary line and the transclusion, (3) add a blank line before the sa-bcad (ས་བཅད) block that introduces the verse. TRIGGER whenever a user asks to transclude root verses into a commentary and/or to fix the blank-line spacing around verse transclusions (sa-bcad spacing), in any phrasing or language.
---

# Transclusion-rootext-into-commentaries

This skill places root-text verse transclusions inside a Tibetan master's commentary and then formats the blank-line spacing around each transclusion so that the structural outline (ས་བཅད, *sa-bcad*) reads correctly in Obsidian.

It bundles three deterministic Python scripts that run as an ordered pipeline. Each stage has a dry-run mode (default) and an `--apply` mode. Always dry-run, review the report, then apply.

Transclusions are navigation aids added to `1-SOURCES/` files — never interpretive content. Beyond inserting `![[...]]` lines and the blank lines around them, **no commentary text is ever added, removed, reordered, or rephrased.**

---

## When to use

- "Transclude the root verses into commentary X" → run Stage 1.
- "Remove the blank lines between the commentary and the verse transclusions" → run Stage 2.
- "Add a blank line before the sa-bcad of each verse transclusion" → run Stage 3.
- "Do the whole transclusion-and-spacing pass on commentary X" → run Stages 1 → 2 → 3 in order.

Stages 2 and 3 assume the transclusions already exist (Stage 1 has run, or they were added previously).

---

## Inputs

| Field | Description | Example |
|---|---|---|
| `root` | Full vault-relative path to the root text / translation to transclude from. Must use `verse_id_format: chapter-verse` block IDs (`^N-V`). | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| `commentary` | Full vault-relative path to the Tibetan commentary to modify in place. | `1-SOURCES/Commentaries/Raw/BCAC20_NKW_bo_segmented.md` |
| `link-base` | The base of the transclusion link, exactly as it should appear inside `![[ … #^N-V]]`. The skill uses the short Obsidian link form. | `bo-བློ་ལྡན་ཤེས་རབ།` |
| `chapter` | Optional. A single chapter number to scope the run, or `all` (default). | `1`, `all` |

---

## Output

The commentary file is modified in place. The only changes are:

1. inserted `![[link-base#^N-V]]` transclusion lines (Stage 1),
2. removal / insertion of blank lines immediately around those transclusion lines (Stages 2–3).

No new files are created. No existing commentary text is changed.

---

## The three stages

### Stage 1 — Transclude verses (`scripts/01_transclude_verses.py`)

For each root verse stanza, the script finds the **first full inline quotation** of that stanza in the commentary and inserts `![[link-base#^N-V]]` on the line immediately before the stanza's first line.

- **Full quotation preferred.** When a verse is quoted in more than one place, the occurrence where the most stanza lines match wins (ties → earliest). A 2-line illustrative citation inside an earlier verse's commentary loses to the full 4-line stanza in the verse's own section.
- **Variant-tolerant.** Lines are matched with a character-overlap ratio (≥ 0.80) plus containment, so minor orthographic variants are absorbed (e.g. `བསྒོམ`/`སྒོམ`, `དེང`/`དེ`, `ཟློག`/`བཟློག`). Matching anchors on *any* stanza line, so a variant first line does not block the match.
- **Passing single lines are not enough.** A one-line match is accepted only when followed by a citation closer (`ཞེས་པ་ནི།`, `ཅེས་པ་ནི།`, …) — i.e. a genuine short citation, never a line echoed mid-prose.
- **Idempotent.** Verses already transcluded are skipped.

Verses the script cannot place are listed under `UNPLACED`. These are usually **split quotations** (the commentator breaks the stanza across prose explanation) or large variants. Resolve each by hand: locate the first line of the verse's quotation and insert `![[link-base#^N-V]]` on the line immediately before it.

```
python3 scripts/01_transclude_verses.py \
  --root "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md" \
  --commentary "1-SOURCES/Commentaries/Raw/<comm>.md" \
  --link-base "bo-བློ་ལྡན་ཤེས་རབ།" \
  --chapter 1            # dry run
# review, then:
python3 scripts/01_transclude_verses.py ... --chapter 1 --apply
```

### Stage 2 — Remove blank line before transclusions (`scripts/02_remove_blank_before_transclusions.py`)

Removes the single blank line directly above each `![[...]]` line, so the layout becomes:

```
<commentary line / sa-bcad>
![[link-base#^N-V]]
<verse text>
```

Only the one blank line immediately preceding a transclusion is removed; nothing else is touched.

```
python3 scripts/02_remove_blank_before_transclusions.py --commentary "<comm>.md"          # dry run
python3 scripts/02_remove_blank_before_transclusions.py --commentary "<comm>.md" --apply
```

### Stage 3 — Blank line before the sa-bcad block (`scripts/03_blank_before_sachad.py`)

Inserts one blank line before the **sa-bcad (ས་བཅད) block** that introduces each verse, per these rules:

1. If the line immediately above the transclusion is a sa-bcad, add a blank line **before that sa-bcad**.
2. If a sa-bcad **enumeration** (a contiguous run of openers + member lines) sits right before the immediate sa-bcad, add the blank before the **first line of that whole enumeration**, not before the immediate sa-bcad.
3. If there is **no immediate sa-bcad** above the transclusion (the line above is ordinary commentary prose, a connector, a commentary conclusion, or a root-verse fragment), add **nothing**.

```
python3 scripts/03_blank_before_sachad.py --commentary "<comm>.md" --report   # show every decision
python3 scripts/03_blank_before_sachad.py --commentary "<comm>.md" --apply
```

---

## Sa-bcad classification (Stage 3 rules)

A line counts as **structural** (part of a sa-bcad block) when it is one of:

- an **ordinal-led** line: starts with `དང་པོ`, `གཉིས་པ`, `གསུམ་པ`, … `བཅུ་པ`;
- a **heading**: ends in `ནི།` / `ནི། །` (a "this is X" announcement), short (≤ 60 collapsed syllables);
- an **enumeration opener**: ends in `ལ།`, `ལ་ཡང་།`, `ལས།`, `ཏེ།`, `སྟེ།`, short;
- an **enumeration member / closer**: ends in `དང་།` / `དང༌།`, or a closing member `…པའོ། །` / `…བའོ། །` / `…ནོ། །` / `…ལོ། །`, or a count word (`…གསུམ།`, `…གཉིས།`, …), short.

A line is **not** structural (and stops the upward walk) when it is:

- ordinary commentary prose (long sentences);
- a connector: `དེའི་རྗེས་སུ།`, `དེའི་འཐད་པར།`, `དེའི་འཐད་པ་ནི།`;
- a quotation or commentary conclusion (contains `ཞེས` / `ཅེས`, e.g. `…ཞེས་པའོ། །`, `…ཞེས་གསུངས།`);
- a **root-verse fragment** (ends in `དང་། །` / `དང་ནི། །`) — these are verse lines, not sa-bcad.

**Block start.** Walk up the contiguous run of structural lines above the transclusion; trim any leading member-only lines so the block begins at a genuine opener/heading/ordinal. The blank goes before that first line. If the run contains no opener/heading/ordinal (e.g. a lone `…པའོ། །` prose conclusion), it is not a real sa-bcad block → no blank.

---

## Worked example (verse ^1-4)

Before Stage 3 (the block reads bottom-up to the transclusion):

```
… ཡོད་པར་འགྱུར་རོ་ཞེས་པའོ། །              ← prose conclusion (stops the walk)
གཉིས་པ་བརྩམ་བྱ་…དངོས་བཤད་པ་ལ།            ← block FIRST line (ordinal + ལ། opener)
…ལེའུ་གསུམ།  /  …ལ་ཡང་།  /  …དང༌།          ← enumeration members
…
ལུས་རྟེན་…ཚུལ་དང་།
སེམས་རྟེན་…ཚུལ་ལོ། །
དང་པོ་ནི།                                  ← the immediate sa-bcad
![[bo-བློ་ལྡན་ཤེས་རབ།#^1-4]]
```

After Stage 3 — the blank goes before the **first line of the enumeration**, not before `དང་པོ་ནི།`:

```
… ཡོད་པར་འགྱུར་རོ་ཞེས་པའོ། །

གཉིས་པ་བརྩམ་བྱ་…དངོས་བཤད་པ་ལ།
… (enumeration unchanged) …
དང་པོ་ནི།
![[bo-བློ་ལྡན་ཤེས་རབ།#^1-4]]
```

Contrast: where the line above the transclusion is a connector (`དེའི་འཐད་པར།`) or commentary prose (`…ཞེས་གསུངས།`), **no** blank is added.

---

## Rules

1. **Read-only except for navigation links and their spacing.** `1-SOURCES/` files may receive block IDs, frontmatter, internal navigation links (transclusions qualify), and `[Ed:…]` notes only. This skill inserts/removes `![[…]]` lines and the blank lines immediately around them — nothing else.
2. **Short link form.** Transclusions use the short Obsidian form `![[link-base#^N-V]]` (matching the precedent in the target commentary). If a vault requires full vault-relative paths, pass that full path as `--link-base`.
3. **Never duplicate a transclusion.** Stage 1 skips any verse whose `^N-V` is already transcluded.
4. **Never modify existing text.** Every stage is insertion/removal of `![[…]]` lines and surrounding blank lines only.
5. **Always dry-run first.** Run each stage without `--apply`, read the report, then apply. For Stage 1, hand-resolve every `UNPLACED` verse before moving on.
6. **Run the stages in order** (1 → 2 → 3) for a fresh commentary. Stages 2 and 3 may be run independently on a commentary that already has transclusions.
7. **Lenient read, clean write.** The scripts read the commentary leniently (so a stray truncated final byte does not abort a run) and re-validate the UTF-8 decode after writing. If a prior tool clipped the final colophon byte, repair the last line from a known-good backup before applying.

---

## Procedure

1. Confirm `root` is a `1-SOURCES/` root/translation file with `^chapter-verse` block IDs, and `commentary` is a `1-SOURCES/` Tibetan commentary.
2. **Stage 1** — dry-run per chapter; review placements and `UNPLACED`; apply; hand-place any split/variant verses. After all chapters, confirm: transclusion count = unique verse-id count = root verse count.
3. **Stage 2** — dry-run; apply. Confirm no transclusion is preceded by a blank line.
4. **Stage 3** — `--report`; spot-check the sa-bcad decisions (especially multi-line enumeration blocks); apply.
5. **Verify integrity** — compare non-blank lines before/after each apply; they must be byte-identical except for the inserted `![[…]]` lines. Confirm the file still decodes as UTF-8 and ends correctly.

---

## Completion check

- [ ] Root confirmed to have `^N-V` block IDs; commentary confirmed in `1-SOURCES/`
- [ ] Stage 1: every verse placed or hand-resolved; transclusions = unique ids = root verse count; no duplicates
- [ ] Stage 2: no transclusion preceded by a blank line
- [ ] Stage 3: blank precedes the first line of each sa-bcad block; no blank where the line above is prose/connector/conclusion; no prose swept into a block
- [ ] Every inserted transclusion uses the agreed link form
- [ ] No commentary text deleted, reordered, or rephrased (non-blank lines byte-identical)
- [ ] File decodes as UTF-8 and ends with the intact colophon
