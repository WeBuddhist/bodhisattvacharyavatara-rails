---
name: toc-candidate-extraction
description: 'Extract ས་བཅད (sa bcad) structural outline candidates from Tibetan Buddhist commentary text. Use this skill whenever the user provides Tibetan text and wants to find structural outline markers — whether they call it "sa bcad extraction", "TOC candidates", "structural analysis", "outline detection", or simply ask to "find the divisions" or "extract the structure" from a Tibetan passage. Trigger for any task involving ས་བཅད, sa bcad, Type A announcements, Type B node headers, Type C closing counts, or structural segmentation of Tibetan commentary or root text. Prioritise recall: it is better to extract too many candidates than to miss one.'
---

# ས་བཅད Candidate Extraction

You are an expert in classical Tibetan Buddhist texts specialising in ས་བཅད (*sa bcad*) — the structural outlining system used in Tibetan commentarial literature.

Your task is to **extract every ས་བཅད candidate** from the input text. **Prioritise recall over precision. Never miss a candidate.**

---

## Step 1 — Chunk the file

Large files must be processed in chunks so nothing is missed. Run the bundled script:

```bash
python 4-SYSTEM/Skills/toc-candidate-extraction/scripts/chunk_file.py \
  "<path-to-input-file>" \
  --chunk-size 150 \
  --overlap 25 \
  --output-dir /tmp/toc-chunks-<commentary-id>
```

This produces numbered chunk files (`chunk_000.md`, `chunk_001.md`, …) plus a `manifest.txt`. The 25-line overlap ensures candidates at chunk boundaries appear in full in at least one chunk.

---

## Step 2 — Create the per-chunk output folder

Before processing any chunk, create the staging folder:

**Path:** `0-INBOX/temp/<commentary-id>/`

This folder will hold one result file per chunk. Do not create the final combined file yet.

---

## Step 3 — Extract from each chunk and save

Read each chunk file in order. For every chunk, apply your full understanding of Tibetan Buddhist commentarial structure to identify every ས་བཅད candidate.

Save the results for each chunk as its own file:

**Path:** `0-INBOX/temp/<commentary-id>/chunk_NNN.md`

File contents — a small header followed by the candidates:

```
<!-- chunk NNN | lines START–END | source: <commentary-id> -->

[candidate blocks here]
```

If a chunk contains no candidates, write:

```
<!-- chunk NNN | lines START–END | source: <commentary-id> -->
<!-- no candidates -->
```

Save the file before moving to the next chunk. This way, if the process is interrupted, completed chunks are not lost and the run can resume from the first missing chunk file.

---

## Step 4 — Combine into the final output file

Once all chunk files are saved, combine them into a single file:

**Path:** `0-INBOX/toc-candidates-<commentary-id>.md`

Structure:

```yaml
---
source: <commentary-id>
skill: toc-candidate-extraction
date: <YYYY-MM-DD>
total_candidates: <N>
---
```

Then concatenate all chunk files in order, preserving their `<!-- chunk NNN -->` headers so each candidate's position in the source is traceable.

---

## Three candidate types — extract all three independently

**Type A — Announcement**
A passage where the author declares a division: a topic is split into N named parts.

> དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།

**Type B — Node header**
A short label opening a section, signalling "now treating part N."

> གཉིས་པ་འགྱུར་ཕྱག་ནི།

**Type C — Closing count**
A number word appearing after a list, summarising how many items were just given.

> ཞེས་རྣམ་པ་གསུམ་མོ། / གནས་བརྒྱད་དོ། / ཚུལ་བཞི་པོ་དེ་དག

---

## Recognition: meaning first, markers second

Do not pattern-match on surface markers alone. For each passage ask: *is this text dividing a topic into named parts, labelling a sub-section, or counting items just listed?* If yes — regardless of exact wording — extract it.

Common signals — any one is enough:

- Topic announced then split into named sub-parts
- Ordinal labels: དང་པོ། / གཉིས་པ། / གསུམ་པ། (even scattered across paragraphs)
- Division words: སྟེ། / ལ། / དབྱེ་ན། following a topic heading
- Number word near a list of named items
- Verse listing items that prose then unpacks
- ལ་སོགས་པ། closing a partial list with a nearby number
- རྣམ་པ་ / གནས་ / ཚུལ་ / ཞེས་བྱ་བ་ within 30 words of a number

---

## Candidate output format

For each candidate output **exactly** this block, nothing more:

```
[TYPE: A / B / C]
CANDIDATE: [exact Tibetan text as it appears in the source]
CONTEXT: [10 Tibetan words before + 10 Tibetan words after the candidate]
ITEMS: [each named item on its own line, numbered, in Tibetan]
```

No commentary. No analysis. No linking. If items cannot be determined, write `ITEMS: [implicit]`.

---

## Do not miss these

- དང་པོ་ / གཉིས་པ་ / གསུམ་པ་ labels even when they appear alone as a single line
- Enumerations embedded inside verse (།-separated units)
- Closing counts even when the number is the only signal
- Nested candidates — extract both inner and outer separately
- Candidates in the overlap zone — extract once only, in the earlier chunk

---

## Execution summary

1. Confirm `commentary-id` with the user if not obvious from the filename.
2. Run `chunk_file.py` to split the input file.
3. Create `0-INBOX/temp/<commentary-id>/`.
4. For each chunk in order: read → extract → save to `chunk_NNN.md` in the temp folder.
5. Combine all chunk files into `0-INBOX/toc-candidates-<commentary-id>.md`.
6. Report total candidates found and the output file path.

If the user has not yet provided a file path, ask for it and confirm the `commentary-id`.
