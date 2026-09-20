# Removing `type: title` segments from BCA content

Policy (2026-09-19, carried over from the liturgy corpus): heading titles do not
belong in an edition's `content`. They belong in the table of contents. Every
BCA edition uploaded before that policy carries its headings as ordinary content
plus a `type: title` segment over each one.

This toolchain removes them with `PATCH /v2/editions/{id}/content`
`{"type": "delete", "start": S, "end": E}` — one call per title segment — and
proves, before and after, that nothing else moved.

**Status: staged test executed and verified 2026-09-20 — see
[`test-run-2026-09-20.md`](test-run-2026-09-20.md). Three titles removed from the
Tibetan root; 126 ops across 10 editions remain.**

---

## Scope

The whole BCA family on `library.webuddhist.com` is 10 texts / 10 editions.
That is the complete job: **129 delete calls**, not the ~650 the liturgy sweep
needed.

| edition | lang | what it is | segments | titles |
|---|---|---|---|---|
| `3rCvwAoWrzKGlIQdtLjCu` | bo | Tibetan root (Ngok Loden Sherab et al.) | 941 | 14 |
| `oPhp5eN2PkvMoiq9pReuu` | sa | Sanskrit root | 934 | 12 |
| `nzztsifbIVhBlBHm2QWsT` | bo | commentary (BCAC14_NTS) | 1351 | 13 |
| `2AWdQyWXlLjIqMqLosTXV` | en | Plain English (AI) | 941 | 14 |
| `KR8O5cLLsJ6pJ7w63PDvG` | en | David Karma Choephel | 940 | 12 |
| `ru8JW2ztLc2dNEEibTXra` | en | Wallace | 942 | 11 |
| `UeXaNlPycKnnUpTnyXnas` | zh | 蔣揚仁欽譯師 | 925 | 11 |
| `gz0jVjcJJ7IHFQiSRp9to` | hi | Plain Hindi (AI) | 941 | 14 |
| `YJRbRrAWPXC8TDr8doccI` | mr | Marathi, scholarly (AI) | 941 | 14 |
| `AVGM32fuCApuhpmw7oa5q` | mr | Marathi, children's (AI) | 941 | 14 |

Only one commentary is uploaded so far. The rest of the vault's commentaries are
not on the backend and need nothing here.

In the Tibetan root the 14 titles are: the work title, `0. ཀླད་ཀྱི་དོན།`, the ten
chapter headings, and the two colophon headings `མཛད་བྱང།` / `འགྱུར་བྱང།`.

---

## Why bottom-up, and why it is sound

Backend `database/span_database.py`, `_adjust_span_for_delete` (commit
`cd1c205`, live as API v2 2.11.2). Branch order matters:

```python
if del_end <= start:   return (start - del_len, end - del_len)   # after  -> shifts
if del_start >= end:   return (start, end)                       # before -> UNTOUCHED
if del_start <= start and del_end >= end:  return None           # covered -> DETACH DELETE
```

Title spans are pairwise disjoint. Deleting title *k* therefore leaves every
title still queued — all of which lie strictly before it — on branch 2, with its
original coordinates intact. So **the whole op list can be computed from one
snapshot and executed without recomputing anything**, provided it runs in
descending order of `start`.

Going top-down would work too, but every later offset would have to be
recomputed after each call against a server that cannot be safely re-read
mid-sequence if a write's response is lost. Bottom-up removes that class of
error entirely.

A second, unplanned benefit: the validator checks `max_end <= content_length`,
and descending order submits the **largest offset first**. If the stored
`content_length` were ever stale, the very first call fails cleanly with 422
instead of the run corrupting an edition halfway through.

### Three facts that make BCA easier than the liturgy corpus

1. **Content contains no newlines at all.** Segments tile the content exactly —
   contiguous, no gaps, no overlaps, last `end` == `len(content)`. Deleting a
   title's exact span leaves a clean join with no orphaned separator.
2. **Offsets are Unicode code points**, confirmed by the backend validator's own
   error text and by the snapshot (`len(content)` in Python matches the last
   segment's `end`).
3. **No title segment is aligned to anything.** All 8,686 alignment pairs across
   all 8 pair lists were checked by segment id: zero of the 129 deletion targets
   appears in any of them. So unlike the liturgy corpus — where deleting the
   title dropped its `0->0` pair in every list and left orphan titles on the
   untouched side — here **no alignment pair can be affected**, and the editions
   are fully independent of one another. There is no "patch both sides" ordering
   constraint.

### The table of contents

New relative to the liturgy run: BCA editions have real TOCs, and
`TableOfContentsSection` spans are adjusted by the same function and are in the
same `DETACH DELETE` label list as Segments. A title span that fully covered a
TOC section would silently destroy that TOC node.

Simulated for all 129 ops: **no TOC section is deleted; all spans shift
correctly.** TOC section spans sit *between* the title spans (a chapter's
section starts where its heading ends), so no title covers one.

`ru8JW2ztLc2dNEEibTXra` (Wallace) has a pre-existing degenerate TOC section with
a zero-length span `[38,38)`. It survives — branch 1 or 2 catches it before the
"fully encompassed" test. It is worth a separate look as a data-quality matter,
but it is not a risk here. It is also why `spanmath.py` vendors the backend
function verbatim instead of paraphrasing it: an approximation that ignores
branch order reports that section as destroyed, which is wrong.

---

## The tools

| file | what it does |
|---|---|
| `api.py` | thin v2 client. GETs retry; **writes never do** |
| `spanmath.py` | verbatim copy of the backend's `_adjust_span_for_delete`, with a sha256 drift check against the real source |
| `snapshot.py` | captures content, segments, TOC, alignment links and every pair list, per edition |
| `plan_removal.py` | builds the descending op list, runs structural checks, and **simulates the whole sequence** to predict the exact after-state |
| `remove_titles.py` | executes the plan, one PATCH per title, re-checking live state before each |
| `compare.py` | holds the real after-snapshot against the prediction and writes a report |

### Run order

```bash
set -a; source /path/to/.env.local; set +a        # WEBUDDHIST_API_KEY — PATCH is key-gated
export TSR_SNAPSHOTS=/somewhere/snapshots

python3 snapshot.py before --seed 3rCvwAoWrzKGlIQdtLjCu \
                           --seed ru8JW2ztLc2dNEEibTXra \
                           --seed KR8O5cLLsJ6pJ7w63PDvG
python3 plan_removal.py --snapshot before --only <edition> --first 2
python3 remove_titles.py --plan "$TSR_SNAPSHOTS/plan-before-first2.json" --dry-run
python3 remove_titles.py --plan "$TSR_SNAPSHOTS/plan-before-first2.json" --execute
python3 snapshot.py after
python3 compare.py --before before --after after \
                   --plan "$TSR_SNAPSHOTS/plan-before-first2.json" --report report.md
```

`--first N` keeps only the **last** N titles of each edition — the first N to be
deleted — which is how the staged test is scoped.

---

## Safety rules, each earned

1. **A content PATCH is not idempotent, so writes are never retried.** A delete
   whose response was lost in transit has still been applied; re-sending it eats
   the *next* `end - start` characters. This destroyed 27 characters of a
   liturgy edition on 2026-09-19 and needed a manual `insert` repair.
   `remove_titles.py` stops the edition on any write failure and leaves it for a
   human.
2. **Every op re-reads live state immediately before writing** and refuses
   unless the target is still `type: title` with the planned span *and* the
   planned text. That makes the run idempotent and resumable — an op already
   applied fails its precheck and is skipped rather than repeated.
3. **Ops run sequentially**, and the ledger is flushed after every single call.
4. **`--execute` is required.** Everything else is a dry run.

### The one failure mode that is not fully self-healing

`routers/editions.py` adjusts spans in Neo4j **first**, then writes S3. If the
S3 write fails it compensates with the inverse span operation — but a
compensating `insert` restores *spans*, not a `DETACH DELETE`d Segment node. So
a failed S3 write would leave the content still holding its title with no
segment covering it: an unsegmented gap, recoverable but needing manual repair.
Unlikely, and it is a gap rather than corruption, but it is the reason step 1
above exists.

---

## Staged test, 2026-09-20 — result

Three titles deleted from the Tibetan root `3rCvwAoWrzKGlIQdtLjCu`, bottom-up:
`འགྱུར་བྱང།` [108526,108536), `མཛད་བྱང།` [108444,108452), and the chapter-10
heading `10. ལེའུ་བཅུ་པ། བསྔོ་བ།` [101082,101105). Three PATCHes, three 204s.
The other nine editions were deliberately left alone as controls.

**Every prediction held, to the byte.**

- **Content** — 108979 → 108938, exactly the predicted −41. The live after-content
  reconstructs as `before[:101082] + before[101105:108444] + before[108452:108526]
  + before[108536:]` — byte-identical, so nothing outside the three spans moved.
  None of the three deleted strings occurs anywhere in the new content.
- **Segments** — 941 → 938. Exactly the three targeted ids vanished; **no new
  segment id appeared**, so the segmentation was edited in place rather than
  rebuilt. Every survivor kept its node id, reference and type, and landed on its
  predicted span. The segmentation still tiles the content with no gaps.
- **Table of contents** — all 14 sections survive. Chapter 10's section moved
  [101105,108444) → [101082,108421) and keeps its title string; it now opens on
  chapter 10's first verse and closes on its colophon, which is correct. Nothing
  was DETACH DELETEd.
- **Alignments** — all 7 links intact, and all 8 pair lists (8,686 pairs) compared
  entry by entry: **byte-identical**. As predicted, since no title is aligned.
- **Controls** — all nine untouched editions byte-identical on content, segments,
  TOC and pairs.

The chapter-9 colophon now joins directly to chapter 10's opening verse, with no
separator artifact — the content has no newlines, so the join is clean.

### What this licenses

The remaining 126 ops are the same operation in the same conditions. The staged
run confirmed the mechanism (in-place segmentation edit, correct TOC shifting,
no alignment collateral) rather than anything specific to those three headings.
Remaining work: 11 titles on the Tibetan root, and all titles on the other nine
editions.

The table of contents must be regenerated afterwards regardless — the TOC
sections survived correctly, but their titles are now the only place the heading
text lives.
