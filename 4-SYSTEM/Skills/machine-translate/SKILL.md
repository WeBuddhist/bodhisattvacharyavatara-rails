---
name: machine-translate
description: >
  Produce a zero-shot machine-baseline translation of a block-ID'd source text
  by calling a translation API on small batches of adjacent blocks, threading the
  document's own preceding translations back in as context, and writing a translation
  file whose block IDs match the source exactly.

  Trigger on "machine translate this", "run the baseline translation", "translate this
  with Gemini", "run DharmaMitra on this", "get me a rough translation of this file",
  "translate this into Hindi/Nepali/Mongolian/Vietnamese".

  This is a **baseline**, not a finished translation — it is the starting point a human
  or `translate-commentary` improves, and `translation-qa` grades.
---

# Machine baseline translation, block-ID aligned

Two engines, same contract:

| Engine | Strength | Needs |
|---|---|---|
| 1 — Gemini | Any display language (Hindi, Nepali, Mongolian, Vietnamese, …) | A Google API key |
| 2 — DharmaMitra | Buddhist-domain Tibetan/Sanskrit → English; trained on this literature | `cat-translate` API: anonymous (400 calls/day), or unlimited with `DHARMAMITRA_API_KEY` |

**Prefer DharmaMitra for Tibetan or Sanskrit into English** — it is trained on exactly
this material and gets technical vocabulary right that a general model paraphrases.
**Use Gemini for every other target language**, where DharmaMitra has no coverage.

**The contract both engines share, and which matters more than the engine choice:**

- **Block IDs are preserved exactly.** The output file's IDs match the source's
  one-for-one. A translation whose IDs drifted cannot be aligned, QA'd, or cited, and
  the damage is invisible until something downstream tries to use it.
- **Small batches of adjacent blocks**, with the document's own preceding
  translations threaded back in as context, so terminology stays consistent across
  the file rather than resetting every call.
- **No termbase is applied here.** Locking terminology is `bilingual-glossary` Phase
  4 plus `zeroshot-translate` / `translate-commentary`. Mixing a termbase into the
  baseline hides which decisions the machine made and which the termbase forced.

---

## Engine 1 — Gemini

Block-ID-aligned batches into any display language.

The sibling of `dharmamitra-translate` for languages DharmaMitra's `cat-translate` endpoint does not serve well or at all. It reuses that skill's parser, context builder and renderer (`dm_translate.py` is imported, not copied), keeps the same per-text append-only ledger and the same track layout. Two things are different, and both are the point:

- **Transport.** Gemini is asked for a JSON object holding one array of lines per block, under a response schema. No marker protocol: the response is split by block *and by line* without guessing.
- **Line parity is enforced, not hoped for.** Every block's line count is checked against its source before it is recorded. A wrong count triggers a solo re-run with the required count stated (up to `--parity-attempts`, default 3). Anything still divergent is recorded with `line_parity: false` and listed in the run report.

The output is a **machine baseline**: `track_type: machine-baseline`, `rails_used: none`, `status: draft`, never cited by any other `3-TRANSFORMATIONS/` output, never promoted past draft by an LLM.

This engine assumes a vault that serves **one text**. A collection vault translating many short texts at once needs corpus drivers this skill does not carry — a title registry and a batch launcher — because its unit of work is the corpus, not the file. Everything Engine 2 states under **Conventions** (track layout, output filename, transclusion layout, the headings flag, preserved frontmatter, the warning in the `note:` key, and publishing via `translation-upload`) applies here unchanged.

---

### Source language and provenance — read this first

**The source is always the Tibetan in `1-SOURCES/Text/`.** `root_text`, `translation_of_text_id` and the segment alignment always point at the Tibetan text, and block `^N` of the output renders block `^N` of the Tibetan.

An existing machine translation may be threaded into the prompt as **reference** with `--reference-track <folder>` (e.g. the DharmaMitra English track). It is recorded on every ledger record (`reference_used`) and in the frontmatter (`reference_translation`), but it is context, not source. **Default is no reference** — a true zero-shot from the Tibetan. The six imported tracks were all produced without a reference.

### Inputs

| Input | Description | Required |
|---|---|---|
| **Source file** | A block-ID'd note under `1-SOURCES/Text/`. Blocks without ` ^<id>` are skipped; headings are handled by `--headings`. | yes |
| **Target language** | A language **label** (`hindi`, `nepali`, `mongolian`, `vietnamese`), not an ISO code. The tag comes from the label table or `--lang-tag`. | yes |
| **Model** | `--model`, default `gemini-3.1-pro-preview`. `--thinking low|medium|high` (default: the model's default). Temperature is left at the model default unless `--temperature` is given. | no |
| **Style instruction** | `<track>/style.md`, seeded per language on first run and read back **verbatim** thereafter as the system prompt, followed by the fixed output contract. Edit the file, never the script. | no |
| **Context header** | `<track>/context-header.md`, a work-neutral preamble; the per-text `Work:` line is derived from each source and appended at call time. | no |
| **Reference track** | `--reference-track`, see above. | no |
| **Glossary** | `<track>/glossary.tsv` (auto-loaded when present) or `--glossary`: `Tibetan term<TAB>rendering` lines; entries whose term occurs in the batch join that call's context as fixed terminology. The four imported tracks carry the name glossaries pinned in the Liturgy vault. | no |
| **Extra frontmatter** | `--extra-fm <file.json>`: keys to seed or override on render. | no |

### Output

```
3-TRANSFORMATIONS/Translations/Gemini/<tag>/
├── about.md                        # what this track is and is not (seeded)
├── style.md                        # system prompt, verbatim (seeded, editable)
├── context-header.md               # work-neutral preamble (seeded, editable)
├── glossary.tsv                    # optional fixed terminology, auto-loaded
├── <source stem>-<tag>.md          # rendered, block-ID aligned, transclusion above each block
└── work/
    └── <source stem>-<tag>.jsonl   # append-only ledger, one record per block / heading
```

Ledger records carry the DharmaMitra fields plus `model`, `model_version`, `thinking`, `temperature`, `line_parity`, `parity_attempts`, `reference_used` and token `usage`. The frontmatter adds `model`, `thinking`, `temperature`, `response_format`, `reference_translation`, `glossary` and `line_parity_failures`, and its `generator` is the model version that actually answered.

#### Seeded style per language

| tag | Script and vocabulary the seed asks for | Mantras | Names |
|---|---|---|---|
| `hi` | Devanagari; Sanskrit-derived Hindi Buddhist vocabulary | Devanagari transliteration of the Sanskrit | Sanskrit names in Devanagari; Tibetan names transliterated |
| `ne` | Devanagari, standard Nepali (not Hindi); Nepal's Buddhist usage | Devanagari | as Hindi, plus forms current in Nepal (गुरु रिन्पोछे, लामा) |
| `mn` | Cyrillic, Khalkha; the Tibetan-derived Mongolian Buddhist lexicon | Cyrillic as recited (Ум мани бадмэ хум) | established Mongolian deity names (Дарь эх, Жанрайсиг, …) |
| `vi` | Vietnamese with diacritics; Sino-Vietnamese Buddhist vocabulary | romanized Sanskrit (Om Mani Padme Hum) | established Vietnamese forms (Quán Thế Âm, Văn Thù, Liên Hoa Sanh) |

---

### Rules

1. **Never write to `1-SOURCES/`.**
2. **Never write into a non-baseline track.** The script refuses a folder that holds a `file_type: translation` file without `track_type: machine-baseline`.
3. **Never guess a split.** A response whose ids or shape do not match the batch is discarded and the batch is re-run one block per call. A block whose line count is wrong is re-run alone. Parity failures are reported, never padded or trimmed by hand.
4. **Every source block ID appears exactly once in the output**, in source order, unaltered.
5. **Source is the Tibetan.** A reference track is context and is recorded as such.
6. **The ledger is append-only.** To change a rendering, edit `style.md` (or add a `glossary.tsv` line) and re-run the block with `--force --only <id>`; the newer record supersedes at render time.
7. **Rate limits are handled, quotas are not fought.** 429s back off; a per-day quota 429 aborts the run at once. The ledger makes any re-run a resume.
8. **Report a partial run as partial.**
9. **Wrathful and exorcistic texts are liturgy.** Safety thresholds are `BLOCK_NONE`; a `finishReason` other than `STOP` is a failed call, retried singly, and reported if it still fails.

---

### Procedure

Scripts live in `4-SYSTEM/Skills/machine-translate/scripts/`. All commands run from the vault root with `GEMINI_API_KEY` in the environment (`source ~/.zshrc`).

#### Step 1 — Confirm inputs, spend nothing

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --list
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --limit 3 --dry-run
```

`--dry-run` prints the exact request bodies so the style and the `Work:` line can be read before a call is made.

#### Step 2 — Pilot, then run

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --limit 6
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label>
```

Read the pilot back block by block against the Tibetan: line parity, script, mantras transliterated, names consistent, register recitable, imperatives/optatives (`ཤོག`, `གྱུར་ཅིག`) rendered as aspirations. A **systematic** defect means editing `style.md`; a **recurring term-level** error means a line in `glossary.tsv`; then re-run the affected blocks with `--force --only <ids>`.

#### Step 3 — Translate the section headings

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --headings
```

All `##` headings go in one JSON call (each is a one-line block, so the parity check applies). A `HEADINGS:` clause narrows the track's `style.md` for the call; the records are `kind: heading` and the renderer puts them into the `##` lines. The H1 is never sent.

#### Step 4 — Verify

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_verify.py --lang-tag <tag>
```

No API calls: every ledger's parity flags, every rendered file's counts and title, block ids against the Tibetan one for one, and a scan for Tibetan or CJK characters inside translation lines (transclusion lines are skipped). Exit 0 means the track is whole. Also confirm `headings_translated` equals the number of `##` headings.

#### Step 5 — Upload (separate decision)

Never from here. The `translation-upload` skill lints, parses, checks the live root and asks for confirmation before sending. The backend must know the language first (`GET /v2/languages`; `hi`, `mn`, `ne`, `vi` are all registered as of 2026-09-17).

---

### Completion check

- [ ] Target language stated or confirmed; tag matches the backend's language code
- [ ] `--dry-run` request read once; `Work:` line names the text being translated
- [ ] Pilot read back block by block; `style.md` / `glossary.tsv` adjusted if needed
- [ ] Section headings translated with `--headings` and read back
- [ ] `gm_verify.py --lang-tag <tag>` exits 0; `about.md` carries the run history
- [ ] Every source block ID appears exactly once in the rendered file, in source order
- [ ] Frontmatter carries `track_type: machine-baseline`, `rails_used: none`, `status: draft`, and names the model version that answered
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or any other track was modified

---

## Engine 2 — DharmaMitra

Buddhist-domain API for Tibetan/Sanskrit → English.

Translates a source file from `1-SOURCES/` into any target language by calling DharmaMitra's public `cat-translate` endpoint on **a small batch of adjacent block IDs** — three stanzas, say — and threading the preceding blocks of the same document back into each call as context, so terminology and register stay coherent across the text. Batched blocks are separated by `[[n]]` marker lines that the model echoes back, and the response is split apart on those markers; each block still gets its own ledger record and its own block ID. The output is a **machine baseline**: raw API output, block-ID aligned, no `2-RAILS/` involvement and no termbase, written to its own track folder and marked `status: draft`. It never touches `1-SOURCES/` and never overwrites a rails-governed or human translation.

Correct output is a track folder whose translation file carries one target-language block per source block ID, in source order, with every block ID preserved exactly and an Obsidian transclusion of the Tibetan block above each one; plus an append-only JSONL ledger recording the exact request behind every line, so any rendering can be traced to the call that produced it.

The failure mode it prevents: silently mixing machine output into the vault's cited translation chain. Everything this skill writes is labelled `track_type: machine-baseline`, `rails_used: none`, and is explicitly ineligible to be cited by any `3-TRANSFORMATIONS/` output or marked `complete`.

The behaviour that is specific to a single-text vault — the default track root, the rendered filename rule, the warning written into the `note:` key, and heading handling — is marked `SINGLE-TEXT VAULT` in `4-SYSTEM/Skills/machine-translate/scripts/dm_translate.py` and summarised under **Conventions** below. A collection vault overrides those four points and leaves the rest.

---

### Conventions (read first)

| Topic | Rule here |
|---|---|
| Track folder | `3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/` (the Liturgy layout; the old `<tag>-dharmamitra-zeroshot` folders were retired on 2026-09-17). |
| Rendered file | `<source stem>-<tag>.md`, e.g. `bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en.md`. Never an English slug: the vault linter, parser and uploader derive the source from this filename. |
| Ledger | `work/<source stem>-<tag>.jsonl`, one record per block (and one per translated heading, `kind: heading`). |
| Layout | `--layout transclusion` (default): `![[<source stem>#^<id>]]` above each translated block — the form the vault parser reads the alignment from. `parallel` (blockquote copy) and `translation-only` still exist. |
| Headings | `##` section headings are translated **separately** with `--headings` (one call each, under `HEADING_STYLE`, never batched with verse). Until then the Tibetan heading is reproduced verbatim. The H1 is never machine-translated: it is the work's title from the frontmatter. |
| Frontmatter | What the vault linter expects of `file_type: translation` (`title` in the target language, `root_text`, `language`, `lang_tag`, `category_id`, `license`, `source`, `edition_type`) plus the provenance keys. Keys the renderer cannot know — researched title, backend ids, import provenance (`PRESERVE_FM_KEYS`) — are carried over from the file being overwritten and can be seeded with `--extra-fm <json>`. There is **no separate stamping pass** in this vault. |
| Warning callout | Lives in the frontmatter `note:` key, not in the body — the linter requires every non-transclusion body block to end in a block id. |
| Upload | Never from this skill. See `translation-upload` (`4-SYSTEM/scripts/upload_translation.py`). |
| Authentication | `DHARMAMITRA_API_KEY`, sent as the `X-API-Key` header, lifts the daily quota. The script reads it from the environment or from a `DHARMAMITRA_API_KEY=…` line in the vault's **git-ignored** `4-SYSTEM/scripts/.env`, and prints only where it came from (`auth : X-API-Key from …`). See **Authentication and parallel runs** below. |

---

### Authentication and parallel runs

**The key.** With `DHARMAMITRA_API_KEY` set, every call carries `X-API-Key: <key>` and the public quota (400 calls per day, shared by everyone on the same IP) no longer applies. The key is a credential the vault owner was given privately:

- Keep it **only** in `4-SYSTEM/scripts/.env` (`DHARMAMITRA_API_KEY=<key>`), which `.gitignore` excludes. Check with `git check-ignore -v 4-SYSTEM/scripts/.env` before creating it.
- Never write it into this skill, a script, a ledger, a commit, a prompt for another agent, or a command line. Never print it. Never copy it into another vault or into the shared skill library: each vault owner adds it to their own `.env`.
- The ledger records the endpoint, not the key.

**Parallel runs (key required).** Two levels, combinable:

| Level | How | Notes |
|---|---|---|
| Across files | Run one `dm_translate.py` process per source × target pair, concurrently (e.g. one background shell per file). | Each pair has its own ledger. **Never run two processes on the same ledger** (same source and same `--lang-tag`). |
| Within a file | `--workers N` (default 1; 4 is a good value). The remaining batches are cut into N contiguous lanes of similar source size; each lane runs in order with its own rolling context. With `--headings`, N headings are in flight at once. | A lane's first batch sees only context that earlier lanes or runs already finished — a small loss at N−1 cut points. Ledger writes are serialised; a stop in one lane stops the others after their current call, and re-running resumes. |

Without a key, `--workers > 1` is refused and the default `--sleep` stays 4 s; with a key the default `--sleep` is 0.5 s per lane.

---

### Inputs

| Input | Description | Required |
|---|---|---|
| **Source file** | A block-ID'd file under `1-SOURCES/` — root text or commentary. Every translatable block must end in ` ^<id>`. Blocks without an ID are skipped. | yes |
| **Target language** | A free-form language **label**, not an ISO code: `english`, `german`, `modern chinese`, `hindi`. Passed verbatim to the API as `target_language`. | yes |
| **Source language** | Which `input_*` field the blocks fill: `tibetan` (default), `sanskrit`, `chinese`, `pali`. | no |
| **Style instruction** | Free-form prose read **verbatim** by the API model. Lives at `<track>/style.md`; seeded on first run and human-editable thereafter. | no |
| **Context header** | A work-neutral preamble prepended to every call's `context`; the per-text `Work: <title> (author: …)` line is derived from the source's frontmatter and appended at call time. Lives at `<track>/context-header.md`. | no |
| **Glossary** *(optional)* | A file of `source term<TAB>target rendering` lines. Entries whose source term appears in the current block are added to that call's context. | no |
| **Extra frontmatter** *(optional)* | `--extra-fm <file.json>`: keys to seed or override on render (researched `title`, `text_id`, `imported_from`, …). | no |

If the target language is not stated in the user's request, ask before running. Do not default to English silently.

### Output

```
3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/
├── about.md                          # what this track is, and what it is not (seeded)
├── style.md                          # the style_instruction sent verbatim (seeded, editable)
├── context-header.md                 # work-neutral preamble (seeded, editable)
├── <source stem>-<tag>.md            # the rendered block-ID-aligned translation
└── work/
    ├── <source stem>-<tag>.jsonl     # append-only ledger: one record per block / heading
    └── extra-fm.json                 # (optional) seeded frontmatter keys
```

### Output file format

````markdown
---
title: Praises to the Twenty-One Tārās            # the work's title in the target language
track: DharmaMitra zero-shot (english)
title_original: སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།
language: English
lang_tag: en
file_type: translation
track_type: machine-baseline
root_text: 1-SOURCES/Text/<source stem>.md
translation_of_text_id: <root text_id>
translation_of_edition_id: <root edition_id>
text_id:                                          # this translation's own ids, filled by the uploader
edition_id:
toc_id:
category_id: <copied from the root>
license: public
translator: dharmamitra cat-translate v1
source: https://dharmamitra.org
edition_type: critical
source_language: tibetan
target_language: english
generator: dharmamitra cat-translate v1
endpoint: "https://dharmamitra.org/api-search/cat-translate/v1/translate"
focus: tibetan
context_blocks: 3
batching: "<=3 blocks/call, <=900 src chars, <=6000 payload chars"
style_instruction: "<verbatim string sent to the API>"
rails_used: none
generated: YYYY-MM-DD
blocks_translated: 32
blocks_total: 32
headings_translated: 4
note: Machine baseline — not a rails-governed translation. …
status: draft
---

## <title> ^0

### <translated heading, or the Tibetan heading until --headings has run> ^I-0

![[<source stem>#^I-1]]

<translation line> ^I-1

![[<source stem>#^1-1]]

<translation line 1>
<translation line 2>
<translation line 3>
<translation line 4> ^1-1
````

Rules the render obeys:

- Every source heading keeps its `^N-0` anchor; the H1 carries the frontmatter `title`.
- The block ID sits at the end of the **last line** of its translation — the same position the source uses.
- A block present in the source but absent from the ledger renders as `*[not yet translated]* ^<id>`, never as a silent gap.

One ledger record **per block** (`work/<source stem>-<tag>.jsonl`) — batching never collapses two blocks into one record — holding `block_id`, `heading`, `source`, `translation`, `target_language`, `focus`, `style_instruction`, the exact `context` string sent, `endpoint`, `elapsed_s`, `ts`, plus `batch_size`, `batch_block_ids` and `batch_fallback`. Heading records add `kind: heading`. Records imported from another vault add a `recut` object (see `4-SYSTEM/scripts/recut_liturgy_import.py`).

---

### Batching

DharmaMitra's own agent chunks source into **3–5 sentences (~80–150 source words)** per `cat-translate` call. This skill follows that guidance at block granularity. Latency is nearly all fixed overhead (one block ≈ 8 s, five blocks ≈ 8 s), so the batch size, not the text length, decides how long a run takes.

| Knob | Default | What it bounds |
|---|---|---|
| `--batch` | 3 | Blocks per call. `1` = one call per block. 5 is DharmaMitra's stated ceiling. |
| `--batch-max-chars` | 900 | Source characters in one batch. |
| `--batch-max-lines` | 32 | Source lines in one batch. |
| `--payload-cap` | 6000 | context + style_instruction + source for the whole call. |

A batch is also closed at a **heading boundary** — sections are never mixed — and any block that alone busts a cap is sent on its own. **Marker protocol:** for a batch of more than one block the source is sent as `[[1]]`, block, `[[2]]`, block, … and a clause is appended to the style instruction telling the model to reproduce every marker verbatim. If the markers do not come back as exactly `[[1]]`…`[[N]]`, in order, the response is discarded and the batch is re-run one block per call. Alignment is never inferred from line counts.

---

### Rules

1. **Never write to `1-SOURCES/`.** This skill reads it and nothing more.
2. **Never write into a non-baseline track.** If the target folder already holds a `file_type: translation` file without `track_type: machine-baseline`, stop and report it.
3. **Batch small, and never guess a split.** See Batching.
4. **Every block ID in the source appears exactly once in the output**, in source order, unaltered. Block IDs are never renumbered, merged, or invented.
5. **This output is never cited.** It may not be cited by any other `3-TRANSFORMATIONS/` output and must not be promoted past `status: draft` by an LLM. Its renderings may feed `2-RAILS/Bilingual-Glossaries/` only through `bilingual-glossary` (Phase 1).
6. **`target_language` is a label, never an ISO code** (`"german"`, not `"de"`). The tag (`de`) is used only for folder and file naming.
7. **Do not lower the 90 s timeout.** A Cloudflare cap at 100 s surfaces as HTTP 524.
8. **Anonymous calls have a DAILY quota** (400 requests per day per IP, observed 2026-08-27 and again 2026-10-04, when seven parallel jobs spent it mid-run). Count calls, not blocks; `--dry-run` prints the call count without spending any. A daily 429 aborts immediately; short-burst 429s back off 20 s → 180 s. **Without a key, never run several instances in parallel.** With `DHARMAMITRA_API_KEY` (see **Authentication and parallel runs**) the quota does not apply: run files concurrently and use `--workers`, but never two processes on one ledger.
9. **The ledger is append-only.** Never hand-edit it. To change a rendering, edit `style.md` and re-run that block with `--force --only <id>`; the newest record wins at render time.
10. **Report a partial run as partial.** `blocks_translated` / `blocks_total` must match reality.
11. **The API key is a secret.** It lives only in the git-ignored `4-SYSTEM/scripts/.env`; it is never printed, committed, passed on a command line, or handed to another agent or vault.

---

### Procedure

All commands run from the vault root.

#### Step 1 — Confirm the inputs (no calls)

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --list
```

Check the block count against the vault annex's addressing scheme. Confirm the target language. Confirm the target track folder holds no non-baseline translation.

#### Step 2 — Smoke-test six blocks

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> --limit 6
```

Six rather than three, so the smoke test exercises two real batches. This seeds `about.md`, `style.md` and `context-header.md` on first run. Read the translations back: line count per block equal to the source's, mantras and names transliterated, register as asked, no marker fallback on most batches. If anything is wrong, edit `<track>/style.md` and re-run the same blocks with `--force`.

#### Step 3 — Run the remaining blocks

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> [--workers 4]
```

Blocks already in the ledger are skipped, so this is also the resume command. Check the `auth :` line it prints first: `X-API-Key from …` means the key was found and `--workers` / concurrent files are allowed; `none` means the anonymous quota applies. Several files can run at the same time in separate processes when the key is present.

#### Step 3b — Translate the section headings

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> --headings [--workers 4]
```

One call per `##` heading (level ≥ 2) under `HEADING_STYLE`; the H1 is never sent. Read the four-or-so results back: a short label, numeral kept, nothing added. Re-run one with `--headings --force --only <id>` if needed. These become the section titles of the translation's table of contents on upload.

#### Step 4 — Verify the render

1. `blocks_translated == blocks_total` and `headings_translated` equals the number of `##` headings, or state the shortfall.
2. No `*[not yet translated]*` markers, no stray `[[n]]` markers:
   ```bash
   grep -n '\[\[[0-9]\+\]\]\|not yet translated' "3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/<stem>-<tag>.md" || echo clean
   ```
3. Block IDs match the source one-for-one (headings included):
   ```bash
   diff <(grep -o '\^[A-Za-z0-9-]*$' "1-SOURCES/Text/<file>.md") \
        <(grep -o '\^[A-Za-z0-9-]*$' "3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>/<stem>-<tag>.md") && echo IDS OK
   ```
4. Line parity per block and no Tibetan inside translation lines: `python3 4-SYSTEM/Skills/machine-translate/scripts/gm_verify.py --lang-tag <tag> --track 3-TRANSFORMATIONS/Translations/Dharmamitra/<tag>` (the checker is generator-agnostic).
5. Re-render at any time without calling the API: `--render-only` (add `--extra-fm work/extra-fm.json` to seed frontmatter keys).

#### Step 5 — Report

Blocks done / total, calls made, headings translated, the track path, the style instruction in force, any batch that fell back to one-block calls, and any block where the API's line count diverged from the source's. Do not mark anything `complete`.

#### Step 6 — Upload (separate decision)

Uploading is outward-facing and is done by the `translation-upload` skill, never from here: it lints, parses, checks the live root and asks for confirmation before sending.

---

### Completion check

- [ ] `--list` block count matches the source's addressing scheme in the vault annex
- [ ] Target language was stated by the user or explicitly confirmed
- [ ] Six-block smoke test read back and `style.md` adjusted if needed
- [ ] Section headings translated with `--headings` and read back
- [ ] Track folder contains `about.md`, `style.md`, `context-header.md`, `<stem>-<tag>.md`, `work/<stem>-<tag>.jsonl`
- [ ] Every source block ID (headings included) appears exactly once in the rendered file, in source order
- [ ] `blocks_translated` / `blocks_total` / `headings_translated` reported honestly
- [ ] Frontmatter carries `track_type: machine-baseline`, `rails_used: none`, `status: draft`, `root_text`, `title` in the target language
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or any other translation track was modified

---

## After this skill

Run `translation-qa` to grade the baseline, and `commentary-fact-check` to check it
against the commentary tradition. Neither should be skipped because the output "reads
well" — fluency is exactly what a machine baseline is best at and accuracy is what it
is worst at.
