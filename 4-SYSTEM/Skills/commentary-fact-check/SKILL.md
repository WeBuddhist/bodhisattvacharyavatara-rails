---
name: commentary-fact-check
description: >
  Audits an English BCA translation verse by verse against a Tibetan commentary
  that transcludes the root text, using a strict term-by-term alignment method
  (not a gist/comprehension check). For every content word the commentary
  explicitly glosses, it maps Tibetan lemma → commentary gloss → English word and
  flags any case where the English names the wrong thing — kaya/dharma/mind swaps,
  a precise term softened to a vague synonym, wrong named entity, wrong number or
  scope, wrong simile tenor, wrong agent, or wrong enumeration order — even when
  the English reads fluently. Use whenever the user asks to "fact-check the
  translation", "check the English against the commentary", "find mistranslations
  against BCAC14_NTS / BCAC19_KS / <any commentary>", "QA a verse against the
  commentary", or "run the commentary fact-check". Reports; does not edit the
  translation file.
---

# commentary-fact-check

Confirms that an already-written English translation says what the Tibetan
**commentary** says each verse means, checked **at the word level, not the gist
level**. This is the key design decision: a comprehension check ("does the English
convey roughly what the verse means?") silently passes errors like *chos kyi sku*
(dharmakāya, a buddha-**body**) rendered as "the dharma", because the three-jewels
gist survives even though the referent is wrong. To catch that class of error the
audit forces a term-by-term alignment against the commentary's own glosses and
withholds any verdict until every anchored term has been checked.

This skill **reports**; it never edits the translation file. Real discrepancies go
in the report (and to the user) for a separate editing pass to fix.

Companion to `translation-qa` (which scores wording/register against `2-RAILS/`
rails and `termbase.md`). This skill's ground truth is the **commentary**, because
it transcludes the whole root text and settles content questions — sutra
citations, similes, named entities, classification schemes, kāya distinctions —
that a bare verse line can't.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Commentary** | ✓ | Path to a Tibetan commentary in `1-SOURCES/Commentaries/Transcluded/` that transcludes the root via `![[…#^verse-id]]` markers (e.g. `BCAC14_NTS_bo_segmented.md` = Ngulchu Thokme; `BCAC19_KS_bo.md` = Khenpo Zhenga). One commentary per run — do not silently mix commentaries; if a verse is unclear from this one, say so rather than reaching for another. |
| **Translation** | ✓ | Path to the English translation file to audit (e.g. `1-SOURCES/Translations/translation-ai/bo-en-translation/bca-en-plain.md`, or a graded `3-TRANSFORMATIONS/.../bca-en-<grade>.md`). |
| **Scope** | ✓ | A chapter number, `colophon`, or an explicit verse range (e.g. `1-1 to 1-5`). Never default to "the whole text" — pick a bounded scope so each verse gets a full term-alignment pass. |

Report file: `<translation-dir>/commentary-fact-check-report-<commentary-id>-<translation-name>.md`
(one file per commentary×translation pair, so audits of the same text against
different commentaries never overwrite each other). Create on first use.

---

## Procedure

### Step 1 — Extract the commentary passages

```bash
python3 4-SYSTEM/Skills/commentary-fact-check/scripts/extract_commentary.py \
    <commentary-path> --json /tmp/commentary.json
```

Splits the file on its transclusion markers, attributing the Tibetan prose (and
block-quoted sutra citations — they are the commentary's own support and are worth
checking) between one marker and the next to that marker's verse. Read the coverage
summary. An empty bucket means its content was absorbed into the **next** verse's
bucket (a heading or citation sat flush against the marker) — recover it from the
following verse; do not report it as a translation defect. Watch for a **cascading
shift** where every bucket quietly holds the *next* verse's prose: if a bucket's
content plainly describes a different verse than its label, check the neighbor
before concluding the English is wrong, and note any confirmed shift in the report.

### Step 2 — Extract the target translation

```bash
python3 4-SYSTEM/Skills/commentary-fact-check/scripts/extract_translation.py \
    <translation-path> --chapter <N> --json /tmp/translation.json
```

### Step 3 — Term-by-term audit (the core method)

**Stance: assume the translation CONTAINS errors; your job is to find them, not to
confirm it reads well. A verse is not cleared until every anchored term is checked.**

For **each** verse in scope, build an alignment table before assigning any verdict:

1. **List the anchors.** From the commentary's prose for that verse, list every
   content word/phrase the commentary explicitly glosses, defines, etymologizes,
   names, counts, or illustrates (e.g. it spells out *chos kyi sku*, *sdom*,
   *bodhi = byang chub*; names a sutra/person; gives a number; states a simile).
   These glossed terms — not your own sense of what matters — are the mandatory
   checklist.
2. **One row per anchor:** `Tibetan (+Wylie) | commentary's gloss | English word used | MATCH / MISMATCH | one-line reason`.
3. **Verdict only after the table.** No verdict without the table.

**Flag as an ERROR (not a style note) any row where the English NAMES THE WRONG
THING, even if it reads fluently.** Scan specifically for:

- **kāya vs dharma vs mind:** *sku / chos sku / longs sku / sprul sku* must stay a
  "body/kāya" — never collapse to "dharma" (the teaching) or "mind".
- **precise term → vague near-synonym:** *dge ba* = virtue/goodness, not "kindness";
  *sdom* = vow/discipline, not "way of life"; *theg dman* = lesser vehicle, not
  merely "lower".
- **named entities:** sutras, teachers, bodhisattvas (Subāhu, Sudhana, Maitreya,
  Maitrībala…) — right name, right person.
- **number & scope:** singular/plural, one vs a few vs countless; *only / all /
  each / even / alone*.
- **simile tenor:** what illustrates what (lightning reveals **forms**, not "the
  sky"; *chu shing* = plantain).
- **grammatical role / agent:** who acts on whom; subject, object, case relations.
- **enumerations and their ORDER** (e.g. the three: virtue / friend / merit).

**Do NOT flag** elaboration the commentary adds that the verse needn't carry
(etymologies, sutra citations, sub-classifications, narrative illustrations).
Dropping supplementary detail is fine; renaming the referent is not. Keep a "style
/ softening" note separate from a hard ERROR so the editor can triage.

### Step 3a — Second pass on the highest-miss classes

After the first pass over the whole scope, do a **dedicated second sweep looking
ONLY for doctrinal-category swaps** — kāya↔dharma↔mind, wrong named entity, wrong
number/scope. A general pass averages over exactly these; a scoped pass catches
them. Report anything the second pass adds.

### Step 4 — Write the report

Create the report file if absent with a header and an empty progress table:

```markdown
# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `<commentary-path>`
- **Translation audited:** `<translation-path>`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
```

Append a `### Chapter <N>` (or range) subsection. Include, per verse, the ERROR and
MISMATCH rows (not the full alignment table — keep the report readable), then:

```markdown
### Chapter <N> — verses <a>–<b>

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-1 | ⚠ ERROR | ཆོས་ཀྱི་སྐུ (chos kyi sku) | dharmakāya, a buddha-body | "the dharma they embody" | dharmakāya / truth-body, not "dharma" |

**Result: <k>/<total> clean, <e> errors, <m> softening notes.**
```

Never overwrite an earlier subsection; append and extend the progress row.

### Step 4a — Verify the write landed

Re-read the report back (a fresh read) and confirm the new subsection is present as
written. This project's file mount has shown intermittent write/sync glitches; if
the re-read is missing or stale, redo the write once, then tell the user plainly if
it still doesn't stick (suggest the file may be open in Obsidian or under a sync
conflict).

### Step 5 — Report back

Tell the user: which commentary/translation/scope was checked, the clean/error
counts, and the full text of every ERROR row (with its Tibetan + commentary gloss)
so they can act without opening the file. Offer to apply the fixes.

---

## Completion check

- [ ] Commentary, translation file, and bounded scope all established before starting.
- [ ] Commentary extracted; empty-bucket / cascading-shift artifacts resolved, not mis-reported.
- [ ] Every verse got a term-alignment table anchored on the commentary's own glosses, before any verdict.
- [ ] Second pass on kāya/entity/number swaps completed.
- [ ] ERRORs (wrong referent) kept distinct from softening/style notes.
- [ ] Report appended (never overwritten) to the commentary×translation report file; write re-read and confirmed.
- [ ] Every ERROR surfaced to the user in chat with its Tibetan + commentary citation.
