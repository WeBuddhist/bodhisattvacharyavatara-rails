---
name: Transclusion-rootext-into-commentaries
description: Transclude root-text verses into a Tibetan commentary and format the placement/spacing around each transclusion. Runs a three-stage pipeline — (1) insert `![[root#^N-V]]` right before each verse's first full inline quotation in the commentary, (2) reposition that transclusion to sit right before the verse's own sa-bcad (ས་བཅད) block when the verse has one, otherwise leave it right before the verse, (3) normalize spacing to exactly one blank line before and after every transclusion. TRIGGER whenever a user asks to transclude root verses into a commentary and/or to fix the placement or blank-line spacing of verse transclusions relative to sa-bcad structure, in any phrasing or language.
---

# Transclusion-rootext-into-commentaries

This skill places root-text verse transclusions inside a Tibetan master's commentary, positions each transclusion correctly relative to the sa-bcad (ས་བཅད) structure that introduces its verse, and normalizes the blank-line spacing around it so the outline reads correctly in Obsidian.

It bundles three deterministic Python scripts that run as an ordered pipeline. Each stage has a dry-run mode (default) and an `--apply` mode. Always dry-run, review the report, then apply.

Transclusions are navigation aids added to `1-SOURCES/` files — never interpretive content. Beyond inserting `![[...]]` lines, moving them, and managing the blank lines immediately around them, **no commentary text is ever added, removed, reordered, or rephrased.**

> **Filename note.** Stage 2's script is still called `02_remove_blank_before_transclusions.py` and Stage 3's is still called `03_blank_before_sachad.py`, but their behavior has changed (see below) — the names are legacy and kept only so existing notes/commands referencing them still work. Rename them (`02_reposition_before_sachad.py`, `03_blank_around_transclusions.py`) next time you have shell access to the vault, if you want the filenames to match what they do now.

---

## When to use

- "Transclude the root verses into commentary X" → run Stage 1.
- "Put the transclusion before the verse's sa-bcad, not after it" / "reposition the transclusions relative to sa-bcad" → run Stage 2.
- "Add blank lines around the transclusions" / "space out the transclusions" → run Stage 3.
- "Do the whole transclusion pass on commentary X" → run Stages 1 → 2 → 3 in order.

Stages 2 and 3 assume the transclusions already exist (Stage 1 has run, or they were added previously).

---

## Inputs

| Field | Description | Example |
|---|---|---|
| `root` | Full vault-relative path to the root text / translation to transclude from. Must use `verse_id_format: chapter-verse` block IDs (`^N-V`). | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| `commentary` | Full vault-relative path to the Tibetan commentary to modify in place. | `1-SOURCES/Commentaries/Raw/BCAC20_NKW_bo_segmented.md` |
| `link-base` | The base of the transclusion link, exactly as it should appear inside `![[ … #^N-V]]`. The skill uses the short Obsidian link form. | `bo-བློ་ལྡན་ཤེས་རབ།` |
| `chapter` | Optional. A single chapter label to scope the run, or `all` (default). Accepts a plain chapter number or a Roman-numeral front-matter label (see below). | `1`, `I`, `all` |

**Chapter labels aren't always numeric.** Some root files in this vault give the pre-chapter-1 front matter (Sanskrit title line, Tibetan title line, opening homage) Roman-numeral block IDs — `^I-1`, `^I-2`, `^I-3` — instead of the generic `^0-N` convention. All three scripts recognize `^[IVXLCDM]+-N` alongside `^N-V`, and `--chapter` accepts either form (`--chapter I` scopes to the Roman-numeral front matter). Roman-numeral chapters sort before chapter 1 in reports.

---

## Output

The commentary file is modified in place. The only changes are:

1. inserted `![[link-base#^N-V]]` transclusion lines (Stage 1),
2. the transclusion line moved up to sit right before the verse's own sa-bcad block, when it has one (Stage 2),
3. exactly one blank line inserted/normalized immediately before and immediately after each transclusion, wherever it now sits (Stage 3).

No new files are created. No existing commentary text is changed.

---

## The three stages

### Stage 1 — Transclude verses (`scripts/01_transclude_verses.py`)

For each root verse stanza, the script finds the **first full inline quotation** of that stanza in the commentary and inserts `![[link-base#^N-V]]` on the line immediately before the stanza's first line. This stage always places the transclusion right before the verse text itself — Stage 2 decides whether it should move.

- **Full quotation preferred.** When a verse is quoted in more than one place, the occurrence where the most stanza lines match wins (ties → earliest). A 2-line illustrative citation inside an earlier verse's commentary loses to the full 4-line stanza in the verse's own section.
- **Variant-tolerant.** Lines are matched with a character-overlap ratio (≥ 0.80) plus containment, so minor orthographic variants are absorbed (e.g. `བསྒོམ`/`སྒོམ`, `དེང`/`དེ`, `ཟློག`/`བཟློག`). Matching anchors on *any* stanza line, so a variant first line does not block the match.
- **Passing single lines are not enough.** A one-line match is accepted only when followed by a citation closer (`ཞེས་པ་ནི།`, `ཅེས་པ་ནི།`, …) — i.e. a genuine short citation, never a line echoed mid-prose.
- **Single-line root segments (titles, the opening homage, colophon lines) get a second look.** The main matcher only searches for a match starting at the beginning of a commentary line, which is right for a block-quoted verse stanza but misses a short root line that a commentary paraphrases mid-sentence. For any root segment that is only one line long, a fallback pass additionally scans every commentary line for that text appearing *anywhere* inside it (exact equality or full containment). This is what lets a segment like the Sanskrit/Tibetan title lines or the opening homage (`^I-1`–`^I-3` in this vault's numbering) get placed even though no commentary quotes them on their own dedicated line. It still won't force a match where the commentary only paraphrases the idea without the actual words — that stays `UNPLACED` for a human to place, same as always.
- **Idempotent.** Verses already transcluded are skipped.
- **No blank-line management.** Stage 1 no longer touches blank lines at all — that is entirely Stage 3's job now.

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

### Stage 2 — Reposition before the verse's own sa-bcad (`scripts/02_remove_blank_before_transclusions.py`)

Decides, per verse, whether the transclusion belongs right before that verse's own **sa-bcad (ས་བཅད) block** or right before the **verse** itself, and moves it there:

- **If the verse has its own sa-bcad** — the line immediately above the transclusion is structural (an ordinal, a heading, an enumeration opener/member — see classification below) — the transclusion is moved up to sit immediately before the **first line of that sa-bcad block** (walking up through any enumeration so the block starts at a genuine opener/heading/ordinal, exactly as it used to only for blank-line placement).
- **If the verse has no sa-bcad** — the line above is ordinary prose, a connector, a commentary conclusion, or a root-verse fragment — the transclusion is **left exactly where Stage 1 put it**, right before the verse.

Only the `![[...]]` line itself moves. No blank lines are touched here (that's Stage 3), and no commentary text is added, removed, reordered, or rephrased.

```
python3 scripts/02_remove_blank_before_transclusions.py --commentary "<comm>.md" --report   # dry run, shows every decision
python3 scripts/02_remove_blank_before_transclusions.py --commentary "<comm>.md" --apply
```

### Stage 3 — Blank line before and after every transclusion (`scripts/03_blank_before_sachad.py`)

Normalizes spacing so exactly **one blank line** sits immediately before and immediately after every transclusion, wherever Stage 2 left it:

```
<preceding line>

![[link-base#^N-V]]

<following line>
```

Multiple existing blank lines touching a transclusion are collapsed to one; a missing blank is inserted. A transclusion at the very start or end of the file gets no leading/trailing blank (nothing to separate it from). Nothing else in the file is touched.

```
python3 scripts/03_blank_before_sachad.py --commentary "<comm>.md"          # dry run
python3 scripts/03_blank_before_sachad.py --commentary "<comm>.md" --apply
```

---

## Sa-bcad classification (used by Stage 2 to decide placement)

A line counts as **structural** (part of a sa-bcad block) when it is one of:

- an **ordinal-led** line: starts with `དང་པོ`, `གཉིས་པ`, `གསུམ་པ`, … `བཅུ་པ` — **checked first, and this alone is enough regardless of what else the same block contains** (see note below);
- a **heading**: ends in `ནི།` / `ནི། །` (a "this is X" announcement), short (≤ 60 collapsed syllables);
- an **enumeration opener**: ends in `ལ།`, `ལ་ཡང་།`, `ལས།`, `ཏེ།`, `སྟེ།`, short;
- an **enumeration member / closer**: ends in `དང་།` / `དང༌།`, or a closing member `…པའོ། །` / `…བའོ། །` / `…ནོ། །` / `…ལོ། །`, or a count word (`…གསུམ།`, `…གཉིས།`, …), short.

A line is **not** structural (and stops the upward walk) when it is:

- ordinary commentary prose (long sentences);
- a connector: `དེའི་རྗེས་སུ།`, `དེའི་འཐད་པར།`, `དེའི་འཐད་པ་ནི།`;
- a quotation or commentary conclusion (contains `ཞེས` / `ཅེས`, e.g. `…ཞེས་པའོ། །`, `…ཞེས་གསུངས།`) — **unless the line is ordinal-led (see above)**;
- a **root-verse fragment** (ends in `དང་། །` / `དང་ནི། །`) — these are verse lines, not sa-bcad.

**Why the ordinal check runs first.** Some commentaries fold a sa-bcad announcement and its own extended explanation into a single block instead of keeping them as separate lines — e.g. `བཞི་པ་སྤྲོ་བ་བསྐྱེད་པ་ནི། <several sentences unpacking the point> ཞེས་པའི་དོན་ནོ། །` all as one paragraph. Classifying by the line's *ending* alone would see the trailing `ཞེས་པའི་དོན་ནོ` and call the whole block a prose conclusion, missing the `བཞི་པ་...ནི།` sa-bcad announcement sitting at its front. Checking `starts_ord` before the quotation/conclusion test means an ordinal-led block is always recognized as its verse's own sa-bcad, no matter how much explanation follows in the same paragraph.

**Block start.** Walk up the contiguous run of structural lines above the transclusion; trim any leading member-only lines so the block begins at a genuine opener/heading/ordinal. The transclusion moves to right before that first line. If the run contains no opener/heading/ordinal (e.g. a lone `…པའོ། །` prose conclusion), it is not a real sa-bcad block → the transclusion is not moved.

**"Immediately above" skips blank lines, not just literal adjacency.** This vault's segmented commentaries put every clause on its own paragraph, separated by a blank line - so the walk looks at the nearest *non-blank* line above the transclusion (and the nearest non-blank line above that, and so on), not literally `line[i-1]`. Reading it as strict line-adjacency would see a blank line everywhere and never find a sa-bcad at all. A markdown heading line (`##`–`########`, ending in its own block ID like `^1-2-1-0`) is never itself treated as structural — it always reads as `none` and stops the walk - only a plain-prose sa-bcad *announcement* sentence counts, even when it sits right below a heading that restates the same point.

---

## Worked example (verse ^1-4)

After Stage 1 (transclusion right before the verse, blank lines not yet normalized):

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

After Stage 2 — the transclusion **moves up** to right before the **first line of the sa-bcad block** (not just before the immediate `དང་པོ་ནི།`):

```
… ཡོད་པར་འགྱུར་རོ་ཞེས་པའོ། །
![[bo-བློ་ལྡན་ཤེས་རབ།#^1-4]]
གཉིས་པ་བརྩམ་བྱ་…དངོས་བཤད་པ་ལ།
… (enumeration unchanged) …
དང་པོ་ནི།
<verse text follows>
```

After Stage 3 — one blank line is added on each side of the transclusion:

```
… ཡོད་པར་འགྱུར་རོ་ཞེས་པའོ། །

![[bo-བློ་ལྡན་ཤེས་རབ།#^1-4]]

གཉིས་པ་བརྩམ་བྱ་…དངོས་བཤད་པ་ལ།
… (enumeration unchanged) …
དང་པོ་ནི།
<verse text follows>
```

Contrast: where the line above the transclusion is a connector (`དེའི་འཐད་པར།`) or commentary prose (`…ཞེས་གསུངས།`), Stage 2 leaves the transclusion right before the verse, and Stage 3 still wraps it with one blank line on each side.

---

## Rules

1. **Read-only except for navigation links, their position, and their spacing.** `1-SOURCES/` files may receive block IDs, frontmatter, internal navigation links (transclusions qualify), and `[Ed:…]` notes only. This skill inserts `![[…]]` lines, moves them relative to sa-bcad structure, and manages the blank lines immediately around them — nothing else.
2. **Short link form.** Transclusions use the short Obsidian form `![[link-base#^N-V]]` (matching the precedent in the target commentary). If a vault requires full vault-relative paths, pass that full path as `--link-base`.
3. **Never duplicate a transclusion.** Stage 1 skips any verse whose `^N-V` is already transcluded.
4. **Never modify existing commentary text.** Every stage only inserts, moves, or removes `![[…]]` lines and the blank lines immediately around them.
5. **Always dry-run first.** Run each stage without `--apply` (`--report` for Stage 2, plain dry-run for Stages 1 and 3), read the report, then apply. For Stage 1, hand-resolve every `UNPLACED` verse before moving on. A single-line root segment (title lines, the opening homage, a colophon line) that stays `UNPLACED` after the fallback pass usually means the commentary only paraphrases it rather than using its actual wording - place it by hand right before the passage that discusses it (prefer the line that most directly restates or quotes it; if that passage opens with its own heading, placing the transclusion right before the heading is also reasonable for a front-matter segment with no verse-style prose exposition of its own).
6. **Run the stages in order** (1 → 2 → 3) for a fresh commentary. Stages 2 and 3 may be run independently on a commentary that already has transclusions.
7. **Lenient read, clean write.** The scripts read the commentary leniently (so a stray truncated final byte does not abort a run) and re-validate the UTF-8 decode after writing. If a prior tool clipped the final colophon byte, repair the last line from a known-good backup before applying.
8. **Idempotent end-to-end.** Running Stages 2 and 3 again on an already-processed commentary makes no further changes.

---

## Procedure

1. Confirm `root` is a `1-SOURCES/` root/translation file with `^chapter-verse` block IDs, and `commentary` is a `1-SOURCES/` Tibetan commentary.
2. **Stage 1** — dry-run per chapter; review placements and `UNPLACED`; apply; hand-place any split/variant verses. After all chapters, confirm: transclusion count = unique verse-id count = root verse count.
3. **Stage 2** — `--report`; spot-check the sa-bcad decisions (especially multi-line enumeration blocks) — confirm each "moves before sa-bcad" verse genuinely has its own sa-bcad, and each "stays before verse" verse genuinely doesn't; apply.
4. **Stage 3** — dry-run; apply. Confirm every transclusion now has exactly one blank line immediately before and after it, and nothing else changed.
5. **Verify integrity** — compare non-blank lines before/after each apply; they must be byte-identical except for the transclusion lines themselves (present, possibly moved) and the blank lines directly touching them. Confirm the file still decodes as UTF-8 and ends correctly.

---

## Completion check

- [ ] Root confirmed to have `^N-V` (or `^[Roman numeral]-V` front-matter) block IDs; commentary confirmed in `1-SOURCES/`
- [ ] Stage 1: every verse placed (by the matcher or, for a single-line title/homage/colophon segment, by hand) or explicitly left `UNPLACED` with a reason; transclusions = unique ids = root verse count; no duplicates
- [ ] Stage 2: every transclusion sits right before its verse's own sa-bcad block when one exists, and right before the verse otherwise; no sa-bcad block wrongly identified or missed
- [ ] Stage 3: exactly one blank line immediately before and after every transclusion; no blank lines added or removed anywhere else
- [ ] Every inserted transclusion uses the agreed link form
- [ ] No commentary text deleted, reordered, or rephrased (non-blank, non-transclusion lines byte-identical)
- [ ] File decodes as UTF-8 and ends with the intact colophon
