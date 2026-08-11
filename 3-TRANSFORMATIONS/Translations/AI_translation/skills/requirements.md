---
title: "AI_translation — workspace requirements"
file_role: requirements
scope: AI_translation/
status: active
doc_language: en
source_text: "AI_translation/bo-བློ་ལྡན་ཤེས་རབ།_split_chapters/"
audience_profiles:
  - AI_translation/audience_profile/children.md
  - AI_translation/audience_profile/plain.md
  - AI_translation/audience_profile/scholars.md
skills_dir: AI_translation/skills/
---

# AI_translation — workspace requirements

The governing contract for everything under `AI_translation/`. Read before creating, extending, or auditing any file in this folder.

This workspace is a **self-contained translation pipeline** running directly off the Tibetan root text. It is not the vault's rails pipeline: nothing here consumes `2-RAILS/`, and nothing here is bound by the `3-TRANSFORMATIONS/` per-track contract convention. Terminology authority comes from a termbase built empirically from the source, not from the commentary tradition. If a translation needs commentary-grounded authority, it belongs in `3-TRANSFORMATIONS/Translations/`, not here.

---

## 1. Audience level — the one option the user chooses

Every artifact in this workspace is produced **for exactly one audience level**. The level is chosen by the user before any work begins, and it is the single parameter that legitimately changes the output. Everything else — source text, segment IDs, line structure — is invariant.

The three levels are defined in `audience_profile/`. **These files are the source of truth for register. Do not restate their content in a translation prompt; read the file.**

| Level | Slug | Profile | Reader | Priority order (from the profile) |
|---|---|---|---|---|
| Children's | `children` | `audience_profile/children.md` | Ages ~8–12, no Buddhist background | Understanding → Simplicity → Core meaning → Accuracy |
| Plain | `plain` | `audience_profile/plain.md` | Little or no Buddhist background | Understanding → Accuracy → Readability → Consistency |
| Scholars' | `scholars` | `audience_profile/scholars.md` | Buddhologists, Indologists, Tibetologists, advanced students | Accuracy → Terminological precision → Fidelity to source syntax → Readability |

The slug is `scholars`, plural — it must match the profile filename exactly, because it becomes part of every output filename.

### What the level actually decides

| Decision | `children` | `plain` | `scholars` |
|---|---|---|---|
| Register | Simple, warm, short sentences | Clear, modern, natural, smooth | Formal, academic |
| Technical terms | Rendered into everyday words | Rendered into ordinary target-language words | **Retained in transliteration at first occurrence with a target-language gloss** — e.g. *bodhicitta* (बोधिचित्त) |
| Transliteration standard | n/a | n/a | IAST for Sanskrit, Wylie for Tibetan |
| Syntax | Recast freely for comprehension | Idiomatic target-language syntax | Literal, close to the source's syntax |
| Explanatory additions | Minor clarification through wording permitted; **never add information absent from the source** | Same | **None.** No clarifying words, no paraphrase beyond what the source states |
| Genuine source ambiguity | Resolve toward the plainer reading | Resolve toward the plainer reading | **Preserve the ambiguity — do not resolve it silently** |
| Philosophical distinctions | May be simplified in wording, never collapsed in meaning | May be simplified in wording | **Never simplified** — e.g. aspirational vs. engaged bodhicitta stay distinct |

The transliteration row is the sharpest divergence: the same pipeline run at `scholars` produces a file that would be a rule violation at `plain`, and vice versa. Never carry a wording decision across levels.

### Adding a fourth level

Write a new `audience_profile/<slug>.md` with the same five sections (Audience, Translation Goal, Style, Explanatory Additions, Priority). Add a row to both tables above. Do not introduce an audience level that exists only inside a prompt.

---

## 2. Two paths, and which to use

Both paths produce a translation. They differ in whether terminology is locked first.

**Zero-shot path** — one skill, no termbase:

```
split-file-by-markers  →  zeroshot-translator
```

Use for a first draft, an exploratory pass, a single chapter, or a comparison. Word choice is the translator's own judgment, consistent within the piece but not locked. Re-running it legitimately produces different wording — that is expected, not drift to chase.

**Rails path** — four skills, termbase-locked:

```
split-file-by-markers → [keyword extraction] → keyword-equivalence-mapper
                      → word-sense-grouper → termbase-builder → rails-verse-translator
```

Use when the whole text is being translated and terminology must hold across all ten chapters. Requires an existing target-language translation to map keywords against — in practice, the zero-shot output of the same language + level. That is the intended relationship between the two paths: zero-shot first, then rails built from what it revealed.

**Keyword extraction is a prerequisite, not a pipeline step.** `keywords-by-reference-tibetan-only.md` and `tib_chapter_keywords/` already exist and are reusable for every language and level. No skill in `skills/` produces them.

**The rails translation is written fresh.** `rails-verse-translator` is explicit that a zero-shot file must not be copied and then structurally validated — even when the termbase was built from that very file. Shared vocabulary is not the same as having applied the termbase.

---

## 3. Pacing — one chapter per turn

Every skill in this workspace that touches chapters states this independently, so it is a workspace rule, not a per-skill quirk:

- Translate, map, or verify **one chapter per turn**. Present it, then wait for explicit approval before the next.
- **Never dispatch chapters in parallel**, including via subagents.
- The reason is cost of rework: a register or structural fault caught after chapter 1 costs one chapter. Caught after chapter 8, it costs eight — and the tokens were already spent on unreviewed material.

---

## 4. Structural invariants — true at every level, on both paths

These are not stylistic preferences. A file that violates one is wrong regardless of how well it reads.

1. **Segment IDs are preserved exactly**, in the same position as the source — normally at the end of the segment's last line. No renumbering, no additions, no omissions.
2. **Per-segment line count mirrors the source.** A four-line source verse gets four target lines, each carrying its own source line's content. Not collapsed into prose, not word-wrapped to a count. A segment with an atypical line count (2 or 5 in a mostly-4 chapter) matches **its own** count, not the chapter's pattern.
3. **One blank line between segments**, always — even where the source uses two. Blank-line spacing is formatting, not structure; normalize it.
4. **No structural additions** — no new sub-headers, no reordering, no filler.
5. **Nothing is added that the source does not state.** At `children` and `plain`, clarification may happen through word choice. At `scholars`, not even that.

### The source's ID scheme

| Region | ID form | Example |
|---|---|---|
| Title line | `^0` | `^0` |
| Introduction | `^I-N` | `^I-0` … `^I-3` |
| Chapter heading | `^N-0` | `^1-0` |
| Verse | `^chapter-verse` | `^1-1`, `^10-58` |
| Author's colophon | `^a-N` | `^a-0`, `^a-1` |
| Translators' colophon | `^b-N` | `^b-0` … `^b-3` |

Numbers are never zero-padded.

---

## 5. Every file in this workspace — what it is and what it needs

### Inputs (shared, language-independent)

| File | What it is | Needs | Produced by |
|---|---|---|---|
| `bo-བློ་ལྡན་ཤེས་རབ།_split_chapters/` | The Tibetan source, split into `intro.md`, `ch1.md`–`ch10.md`, `colophon.md`, `frontmatter.txt` | — | `split-file-by-markers` |
| `keywords-by-reference-tibetan-only.md` | Every source keyword, one line per segment ID: `[id] word1, word2, …` | — | Prerequisite; not produced by any skill here |
| `tib_chapter_keywords/` | The same keyword list split per chapter | `keywords-by-reference-tibetan-only.md` | `split-file-by-markers` |
| `audience_profile/<level>.md` | Register contract for one audience level | — | Written by hand |

### Per-language, per-level artifacts

All live in `<language>/`, named with the **full language name** (`english`, not `en`) and the audience slug.

| File | What it is | Needs | Produced by |
|---|---|---|---|
| `<text>-<language>-<level>-zeroshot_split_chapters/` | Zero-shot translation, one file per chapter. **This is the required output of the zero-shot path** | Source chapters + audience profile | `zeroshot-translator` |
| `keywords-by-reference-tibetan-<language>-<level>.md` | Source keywords aligned to their equivalent in this translation: `[id] word=equivalent, …` | Tibetan keyword file + a translation with the same segment IDs | `keyword-equivalence-mapper` |
| `tibetan-word-<language>-senses-<level>.md` | Same data regrouped **by source word**, equivalents clustered into senses: `word: {sense_tag: term_a / term_b; sense_tag2: term_c}` | The keywords-by-reference file above | `word-sense-grouper` |
| `tibetan-<language>-termbase-<level>.md` | The locked termbase — **exactly one term per sense**, no ` / ` alternates: `word: {sense_tag: chosen_term}` | The senses file + the audience profile | `termbase-builder` |
| `<text>-<language>-<level>.md` | The merged rails translation, with frontmatter. **No `-zeroshot` marker — its absence is what marks this as termbase-guided** | Source chapters + locked termbase + audience profile | `rails-verse-translator` |
| `commentary-fact-check-report-<commentary-id>-<translation>.md` | Verse-by-verse audit against a Tibetan commentary | A finished translation | `commentary-fact-check` (vault skill, `4-SYSTEM/Skills/`) |

`<text>` is the source-text slug — `bca` in this project.

### Notes on the format-critical files

- **Sense tags are always English**, whatever the target language, because they exist to distinguish meanings at a glance, not to translate. When the target language *is* English, a tag must still be a description, not a copy of the value — `what use: what use` is a duplicated translation, not a gloss.
- **`(no direct equivalent)` belongs in the keywords-by-reference file only.** By the senses file it must be gone: a word whose only attested sense is "no equivalent" is dropped entirely; a word with real senses alongside it keeps only the real ones. A sense value is always actual target-language text.
- **The senses file and the termbase file have the same shape but are not the same file.** The senses file may carry `term_a / term_b` alternates; the termbase must not. The word set and sense set are identical between them — `termbase-builder` narrows candidates, it never adds or drops a word or a sense.

### Merged-file frontmatter

Every merged translation (`<text>-<language>-<level>.md`) carries frontmatter recording at minimum: `title`, `source_text` (path), `target_language`, `translation_approach` (`zeroshot` or rails, stated explicitly), `audience_profile` (**path**, plus a one-line summary), `termbase` (path, or a statement that none was used), `verse_id_format`, `segment_id_coverage`, and `license`. This is what makes the file self-documenting later without reconstructing how it was made. **Paths in frontmatter must resolve** — see §7.

### Scripts

`skills/scripts/` holds the mechanical helpers, invoked by the skills rather than run ad hoc: `split_chapters.py` (cutting), `lint_translation.py` (frontmatter + segment-ID + formatting validation, exit 1 on any ERROR), `add_transclusions.py` and `add_transclusions_from_root.py`.

---

## 6. Naming rules

- **Full language name, never a short tag.** `english`, `hindi`, `marathi` — not `en`, `hi`, `mr`. This applies to folder names and to every filename component.
- **The audience slug is used bare**, exactly as the profile file names it: `-plain`, not `-plain-english-version`.
- **`-zeroshot` marks the fast path**, and only ever appears on the split-chapters folder. Its absence marks a rails output. Never omit it from a zero-shot folder; never add it to a rails file.
- **The audience slug appears on every per-language artifact**, including files whose content is not itself audience-dependent (the keywords-by-reference and senses files). Those files trace back to one audience's translation, and a different audience's run would legitimately attach different equivalents. Without the slug, one silently overwrites the other.
- **No `_before` suffixes as a versioning scheme.** `hindi/*_before.md` are historical; do not create more. Use git.

---

## 7. Verification before anything is called done

Per chapter:

- [ ] Every source segment ID present, none added, none duplicated, in order.
- [ ] Per-segment line count matches the source, checked segment by segment — including the atypical ones.
- [ ] Exactly one blank line between segments.
- [ ] Register matches the audience profile across the whole chapter, not just the opening verses.
- [ ] At `scholars`: technical terms transliterated and glossed at first occurrence; no explanatory additions anywhere.

On merge:

- [ ] The **whole merged document** re-verified against the full source — not a re-read of per-chapter passes. Seam faults (a dropped blank line, a skipped or duplicated segment at a chapter boundary) only show up here.
- [ ] `lint_translation.py` exits 0.
- [ ] Frontmatter complete per §5, and **every path in it resolves to a file that exists**.
- [ ] Termbase, if one was used, contains no ` / ` alternates.

### Checking for uncollapsed termbase values

A termbase row is `word: {tag: value; tag2: value2}`. **A sense tag may legitimately contain ` / `** — it is a gloss, and `Avalokiteśvara / lord` is a valid tag. Only a ` / ` in the **value** means `termbase-builder` failed to collapse. So grepping for ` / ` gives false positives; split on the **last** colon in each clause and test the value:

```python
import re, glob
for path in sorted(glob.glob('*/tibetan-*termbase*.md')):
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        m = re.match(r'^(.*?):\s*\{(.*)\}\s*$', line.rstrip())
        if not m: continue
        for clause in m.group(2).split(';'):
            if ':' in clause and ' / ' in clause.rsplit(':', 1)[1]:
                print(path, n, m.group(1), clause.strip())
```

All eight termbases pass this check as of 2026-08-06.

### Line endings

The merged translation files use **CRLF**. Any scripted edit must preserve them — a `sed` pattern anchored with `$` will silently fail to match, and a careless rewrite will reflow the whole file into a spurious diff.

### Known drift (as of 2026-08-06)

Resolved:

- ~~`english/bca-english-plain.md` pointed at a nonexistent `tibetan-word-english-termbase-plain.md`~~ — corrected to `tibetan-english-termbase-plain.md`.
- ~~`hindi/bca-hindi-plain_before.md` pointed at `sanskrit-english/english_keyword/output/tibetan-hindi-termbase.md`, outside this workspace~~ — corrected to `AI_translation/hindi/tibetan-hindi-termbase-plain_before.md`.
- ~~`hindi/bca-hindi-children.md` used a bare `hindi/…` path~~ — normalized to the `AI_translation/…` prefix used everywhere else. Every `termbase:` path in every merged file now resolves.

Open — **`དབང་ཕྱུག` is under-split into one sense in three termbases.** The word carries two unrelated referents in this text: Avalokiteśvara (the bodhisattva, at `2-13`, via `འཇིག་རྟེན་དབང་ཕྱུག`/Lokeśvara) and Īśvara (the theistic creator-god Śāntideva **refutes** at `9-118`–`9-125`). The Marathi scholars mapping file attests both correctly — 6× `ईश्वर`, 3× `अवलोकितेश्वर` — but `word-sense-grouper` merged them under one tag, and `termbase-builder` then locked a single term:

| File | Locked as | Consequence if applied |
|---|---|---|
| `marathi/tibetan-marathi-termbase-scholars.md` | `{Avalokiteśvara / lord: अवलोकितेश्वर}` | Ch. 9 refutation of Īśvara reads as a refutation of Avalokiteśvara |
| `hindi/tibetan-hindi-termbase-plain.md` | `{Avalokiteśvara/lord: अवलोकितेश्वर}` | Same |
| `marathi/tibetan-marathi-termbase-children.md` | `{Lord/Ishvara/almighty: ईश्वर}` | Inverse — Avalokiteśvara at `2-13` becomes ईश्वर |

Both English termbases split it correctly and are the model to follow. At `scholars` this is also a direct profile violation ("no simplification of philosophical distinctions"). The Marathi scholars *translation* is unaffected because it is a zero-shot pass and never applied the termbase — it renders `9-119` as `ते ईश्वर असू शकत नाहीत` and `2-13` as `अवलोकितेश्वरादींना`, both correct. The risk is to any future rails pass built on these termbases.

Open — **`marathi/tibetan-marathi-termbase-plain.md` carries a `(no direct equivalent): (no direct equivalent)` sense** on `དབང་ཕྱུག`. `word-sense-grouper` §4 forbids this: a sense value must always be actual target-language text, and the clause should have been dropped because the word has real senses alongside it.

Both open items are **locked-termbase edits**, which `termbase-builder` requires be surfaced rather than made quietly. They are recorded here and await a decision.

Open — coverage is uneven: `english` and `hindi` have `children` + `plain`; `marathi` additionally has `scholars`. No language has all three levels complete on both paths.

---

## 8. What this workspace does not do

- It does not read `2-RAILS/`. A translation needing commentary authority belongs in `3-TRANSFORMATIONS/Translations/`, under that folder's `requirements.md` / `termbase.md` / `audience.md` contract.
- It does not modify `1-SOURCES/`.
- It does not set `status: complete` on anything. A domain specialist does that.
