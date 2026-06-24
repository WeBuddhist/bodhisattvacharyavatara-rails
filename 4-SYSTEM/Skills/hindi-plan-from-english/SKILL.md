---
name: hindi-plan-from-english
description: Translate an existing English Bodhisattva Challenge day-plan file into Hindi, rendering only the Opening/Introduction, From the Tradition, and Today's Practice sections into Devanagari Hindi while reproducing the liturgy, Tibetan verses, English verse translation, notification, and all section headings verbatim. Saves to 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/.
---

# hindi-plan-from-english

This skill produces the Hindi stream of the 365-day Bodhisattva Challenge by translating a finished English day file (from the `en/Days/` tree) into Hindi. It is a **partial translation**: only three prose sections are rendered into Hindi — the Opening/Introduction, From the Tradition, and Today's Practice — and everything else in the file is copied through byte-for-byte. This boundary is the whole point of the skill: the fixed liturgy, the Tibetan root verses, the factual English verse translation, the push-notification text, and the `##` section headings must survive unchanged so the Hindi file stays structurally identical to its English source. The translation must be accurate to the English and must preserve the Buddhist and cultural meaning, never flattening a doctrinal point into a vague paraphrase.

Correct output looks like a full day file, identical in structure and ordering to the English source, in which exactly three section bodies now read as natural Devanagari Hindi and nothing else has moved.

---

## Inputs

Gather these before starting. If an input is missing, stop and ask the human contributor — never guess or invent content.

| Input | Description | Path / format |
|---|---|---|
| **Source English day file** | The finished English day file to translate. Read it in full. | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/<Chapter-folder>/<DAY_NUMBER>.md` |
| **Day number** | Which day to translate (1–365). Used to locate the source file and name the output. | e.g. `1`, `45` — no zero-padding |

Notes on locating the source:
- English day files live in chapter subfolders such as `Chapter-1 D1-D14/` and `Chapter-2 D15-D40/`. A given day number may also have variant files (`11-option-a.md`, `12-option-1.md`, etc.). Translate the canonical `<DAY_NUMBER>.md` unless the user names a specific variant.
- If you cannot find a clean `<DAY_NUMBER>.md`, stop and ask which file to translate rather than picking a variant on your own.

---

## Output

One file per day, mirroring the English source's location under the `hi/` tree:

`3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md`

- Use the **same chapter subfolder name** as the English source (e.g. `Chapter-1 D1-D14`). Create the `hi/` and `hi/Days/<Chapter-folder>/` directories if they do not yet exist.
- Filename: `<DAY_NUMBER>.md` — no zero-padding.
- This skill writes only into `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/`. It never modifies the English source or anything in `1-SOURCES/`.

---

## Output file format

The Hindi file is a structural copy of the English source. Frontmatter, the day title, the notification block, every `##` heading (kept in English), the liturgy block-quotes, and the Tibetan + English verse block-quotes are reproduced **exactly** as in the source. Only the body prose of the three translatable sections is replaced with Hindi.

Translate the body of these sections (match whichever header variant the source uses):

| Section to translate | Header variants seen in source files |
|---|---|
| Opening | `## Opening` or `## Introduction` |
| From the Tradition | `## From the Tradition` |
| Today's Practice | `## Today's Practice Challenge` or `## Today's Practice` |

Reproduce verbatim (no translation):

- YAML frontmatter (add a single `translated_from:` line — see Procedure).
- The `# Day N — …` title line.
- The notification block / `*Push notification:*` line (this is delivery text; keep it in English).
- `## Renewing the Bodhisattva Vow` and its liturgy block-quote.
- `## Today's Verses` and its Tibetan + English block-quotes.
- `## Aspiration` / `## Aspiration and Dedication` and its liturgy block-quote.
- All `##` section headings themselves (English), in their original order.

Skeleton (headers kept English; only the three marked bodies become Hindi):

```markdown
---
day: [N]
chapter: [C]
verses: "[…]"
status: draft
translated_from: "en/Days/<Chapter-folder>/[N].md"
generation_note: "[copied verbatim from source if present]"
---

# Day [N] — [ENGLISH TITLE, VERBATIM]

> **Notification**            ← verbatim (or *Push notification:* line, verbatim)
> ...

## Opening                     ← header kept English
[INTRODUCTION PROSE IN HINDI]

## Renewing the Bodhisattva Vow
[LITURGY — VERBATIM]

## Today's Verses
[TIBETAN + ENGLISH — VERBATIM]

## From the Tradition          ← header kept English
[COMMENTARY NOTE IN HINDI]

## Aspiration                  ← header kept English
[LITURGY — VERBATIM]

## Today's Practice Challenge   ← header kept English (use source's variant)
[PRACTICE INSTRUCTION IN HINDI]
```

---

## Rules

1. **Translate only the three named section bodies.** Opening/Introduction, From the Tradition, and Today's Practice(/Challenge). Every other line in the file is copied byte-for-byte from the English source.
2. **Keep all `##` headings in English.** Do not translate, transliterate, or reorder section headings.
3. **Reproduce fixed content verbatim.** The frontmatter, day title, notification text, liturgy block-quotes, and the Tibetan + English verse block-quotes must be identical to the source. Do not translate the English verse translation, even though a Hindi reader will see English there — that boundary is intentional and set by the requester.
4. **Accuracy over fluency, but fluent where possible.** The Hindi must say what the English says — no additions, no omissions, no softening of doctrinal claims. Then make it read naturally to a Hindi-speaking lay Buddhist.
5. **Preserve cultural and Buddhist meaning.** Where the English names a specific commentator's distinction, a doctrinal point, or a precise condition, carry it across exactly. Never collapse a precise point into a generic spiritual statement.
6. **Render key Buddhist terms in standard Devanagari Hindi/Sanskrit forms.** Use common, widely-understood spellings: बोधिचित्त (bodhicitta), संसार (samsara), कर्म (karma), बोधिसत्त्व (bodhisattva), धर्म (dharma), बुद्ध (buddha), संघ (sangha), पुण्य (merit), शरण (refuge), निर्वाण (nirvana). Be consistent within and across day files. Do not consult or modify any vault termbase for this skill.
7. **Keep proper names in standard Hindi forms.** शांतिदेव (Shantideva); for the commentators, transliterate to Devanagari on first use and keep the one-clause identification the English gives (e.g. who they are / when they lived) so the Hindi reader gets the same context.
8. **Preserve formatting within translated prose.** Paragraph breaks, the absence of bullet lists, prose-only structure, and the no-em-dash convention of the source all carry over. Do not introduce lists or sub-headers that were not in the source.
9. **Do not invent or "improve" content.** If the English says something, translate it. If it does not, do not add it. This skill translates; it does not re-author.
10. **Write only inside `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/`.** Never edit the English source, the liturgy assets, or any `1-SOURCES/` file.

---

## Procedure

1. **Resolve the source file.** From the day number, locate `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/<Chapter-folder>/<DAY_NUMBER>.md`. If multiple candidates exist or the canonical file is absent, stop and ask the user which to translate.
2. **Read the source in full.** Note the exact frontmatter, the day title, the notification block, every `##` heading and its exact wording (record which header variant is used for Opening and for Practice), and the verbatim liturgy and verse blocks.
3. **Identify the three translatable bodies.** Capture the prose under Opening/Introduction, under From the Tradition, and under Today's Practice(/Challenge). If the Opening section contains a `*Push notification:*` / notification line above the intro prose, that line stays English; translate only the introductory prose beneath it.
4. **Translate each of the three bodies into Hindi**, one at a time, applying Rules 4–9. After each, re-read the English and the Hindi side by side to confirm nothing was added, dropped, or softened, and that every doctrinal point and commentator attribution survived.
5. **Assemble the output file.** Start from an exact copy of the source. Replace only the three translated bodies. Leave the headings in English. Add `translated_from: "en/Days/<Chapter-folder>/<DAY_NUMBER>.md"` to the frontmatter and keep `status: draft`. Preserve any existing `generation_note` verbatim.
6. **Create directories if needed** and save to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md`.
7. **Diff against the source.** Confirm that the only lines that differ are: the three translated bodies, the added `translated_from:` frontmatter line, and nothing else. If any verbatim region changed, fix it before reporting completion.

---

## Completion check

- [ ] Source English day file located and read in full; header variants for Opening and Practice recorded.
- [ ] Exactly three section bodies translated into Hindi: Opening/Introduction, From the Tradition, Today's Practice(/Challenge).
- [ ] All `##` section headings left in English and in original order.
- [ ] Frontmatter, day title, notification text, liturgy block-quotes, and Tibetan + English verse block-quotes reproduced verbatim.
- [ ] `translated_from:` added to frontmatter; `status: draft`; existing `generation_note` preserved.
- [ ] Key Buddhist terms in standard Devanagari forms, consistent; commentator names transliterated with the source's one-clause identification preserved.
- [ ] Hindi prose adds nothing and omits nothing relative to the English; no doctrinal point flattened.
- [ ] No bullet lists or sub-headers introduced; no em-dashes added to body prose.
- [ ] Saved to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md`; no English source or `1-SOURCES/` file modified.
- [ ] Diff against source shows only the three translated bodies and the added `translated_from:` line changed.
