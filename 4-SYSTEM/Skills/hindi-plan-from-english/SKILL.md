---
name: hindi-plan-from-english
description: Translate an existing English Bodhisattva Challenge day-plan file into plain, conversational Hindi, rendering only the Opening/Introduction, From the Tradition, and Today's Practice sections into everyday Devanagari Hindi while reproducing the liturgy, Tibetan verses, English verse translation, notification, and all section headings verbatim. Saves to 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/.
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
| **Source-context files** | The rails/commentary the English plan was generated from. Read these for context so the Hindi captures the full meaning behind the English prose. Locate them from the day file's frontmatter (`verses`, `generation_note`) — they are the same sources the English plan was built on. | See "Source-context files" below |

Notes on locating the source:
- English day files live in chapter subfolders such as `Chapter-1 D1-D14/` and `Chapter-2 D15-D40/`. A given day number may also have variant files (`11-option-a.md`, `12-option-1.md`, etc.). Translate the canonical `<DAY_NUMBER>.md` unless the user names a specific variant.
- If you cannot find a clean `<DAY_NUMBER>.md`, stop and ask which file to translate rather than picking a variant on your own.

### Source-context files

The English plan was generated from source rails. Reading them gives you the reasoning and commentary behind the English prose, which lets you choose accurate Hindi renderings and avoid flattening doctrinal points. Pull the verse IDs from the day file's `verses` frontmatter field, then read whichever of these exist for those verses:

| Context file | What it gives you | Path |
|---|---|---|
| **Verse context package (preferred)** | Disambiguated restatement + commentary synthesis in the original language. | `2-RAILS/Verses/<verse-id>.md` (use when `status: complete`) |
| **Interim commentary summaries** | Combined commentary summaries (Gyaltsab Darma Rinchen, Sazang Mati Panchen, Ngulchu Thokme Zangpo). The day file's `generation_note` says when these were the source. | `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` |
| **AI English verse translation** | The English rendering of each verse, by block ID — context for the "From the Tradition" note. | `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md` |
| **Tibetan root text** | The canonical Tibetan verses. | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |

These files are **read-only context**. They sharpen the translation; they do not change what gets translated. The Hindi prose must still match the English day file in content (see Rules 4 and 9) — context guides word choice and meaning, never adds new claims the English does not make. If none of the context files exist for a verse, proceed from the English alone and note this; do not block on it.

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
4. **Accuracy in plain, everyday Hindi.** The Hindi must say what the English says — no additions, no omissions, no softening of doctrinal claims — but it must read like a friend explaining over chai, not like a textbook. Plainness is a hard requirement, not a nicety: testers found the earlier Hindi too hard and too technical. See "Language and register" below.
5. **Preserve cultural and Buddhist meaning.** Where the English names a specific commentator's distinction, a doctrinal point, or a precise condition, carry it across exactly. Never collapse a precise point into a generic spiritual statement.
5a. **Use the source context to translate faithfully, not to expand.** Read the source rails/commentary (step 3) so you understand the full meaning behind the English prose and can pick the right Hindi term or phrasing. The context disambiguates; it never licenses adding claims, examples, or detail the English day file does not contain. The Hindi must still match the English in content.
6. **Prefer plain Hindi over technical terms; gloss the rest.** Do not reach for heavy Sanskritized vocabulary. Use everyday Hindustani words people actually speak (इंसान, भलाई, सुकून, जरिया, सोच, नमन, शरण). Terms that are already everyday Hindi can stay as-is (कर्म, धर्म, संसार, बुद्ध, पुण्य). For more technical terms, lead with a plain description and only attach the term lightly if useful: bodhicitta → "सबके भले के लिए जागने का संकल्प (बोधिचित्त)"; bodhisattva → "जो सबकी भलाई में जुटे रहते हैं" rather than बोधिसत्त्व as a bare title. Never use lofty titles like महान प्राणी or प्रबुद्ध वीर. Be consistent within and across day files. Do not consult or modify any vault termbase for this skill.
7. **Keep proper names in standard Hindi forms.** शांतिदेव (Shantideva); for the commentators, transliterate to Devanagari on first use and keep the one-clause identification the English gives (e.g. who they are / when they lived) so the Hindi reader gets the same context.
8. **Preserve formatting within translated prose.** Paragraph breaks, the absence of bullet lists, prose-only structure, and the no-em-dash convention of the source all carry over. Do not introduce lists or sub-headers that were not in the source.
9. **Do not invent or "improve" content.** If the English says something, translate it. If it does not, do not add it. This skill translates; it does not re-author.
10. **Write only inside `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/`.** Never edit the English source, the liturgy assets, or any `1-SOURCES/` file.

---

## Language and register — the "Chai" rule

This is the most important quality bar for the translated prose, and the reason this skill was revised. Testers said the Hindi was too hard and too technical. Fix that by writing the way an Indian friend would explain the idea to you over chai: warm, natural, human, in the Hindi people actually speak.

- **Conversational Hindustani, not literary/Sanskritized Hindi.** Short, clear sentences, one idea at a time. If a sentence has to be re-read, split it or simplify it.
- **Use everyday words.** Reach for इंसान, भलाई, सुकून, चैन, जरिया, सोच, असल में, नमन, शरण, भरोसा, कमाल की सोच — the vocabulary of normal speech. Avoid stiff, bookish, or over-Sanskritized choices when a plain word exists.
- **Explain the meaning, don't translate the words.** Read the English, understand the point, then say it in Hindi the way you'd explain it to a friend. Free, natural, sense-for-sense rendering is the goal; a literal word-for-word translation is exactly what makes it sound stiff and technical. It is fine to recast a sentence completely, as long as the meaning, the doctrinal point, and any commentator attribution are fully preserved.
- **Don't repeat the same word.** When a key word starts piling up in one passage (e.g. भरोसा appearing five times, or मन, अभ्यास over and over), vary it with natural synonyms (भरोसा / यक़ीन / हौसला for faith, trust, confidence) or fold it into a pronoun (ये तीनों, एक-दूसरे को). Repetition is one of the fastest ways to make plain Hindi sound clumsy.
- **Name the thing; don't leave referents vague.** A bare इसे, यह, उसे, or यह सब often leaves the reader unsure what is meant. If "this/it" could be unclear, name it plainly — e.g. for "writing this," say यह किताब लिखने से, not इसे लिखने से. The reader should never have to guess what a pronoun points to. (English sources lean on "this/it" because the surrounding verses make the referent obvious; in the standalone Hindi sentence it often is not, so spell it out.)
- **No jargon dumps and no lofty titles.** Don't stack Buddhist technical terms or honorifics (महान प्राणी, प्रबुद्ध वीर, बोधिसत्त्व as a bare title). Describe the thing plainly first; attach a term only if it genuinely helps, with a one-clause plain gloss.
- **Keep the warmth and the precision.** Plain does not mean vague. The doctrinal point and the commentator's specific distinction must still be exactly there (Rules 4, 5, 5a) — just said in plain words.

Quick contrast (illustrative):

| Too technical / stiff | Plain "chai" Hindi |
|---|---|
| अपने चित्त को प्रशिक्षित करने हेतु | अपने मन को सँवारने के लिए |
| कर्मों के फलविपाक में आस्था | यह भरोसा कि हम जो करते हैं उसका असर होता है |
| बोधिसत्त्व के संवर में प्रवेश | जो सबकी भलाई के रास्ते पर चलते हैं, उनके संकल्प में उतरना |
| ...भरोसा... भरोसा... भरोसा... भरोसा... (एक ही शब्द बार-बार) | भरोसा... यक़ीन... हौसला... ये तीनों (शब्द बदलते हुए) |

The reference register comes from the verse-summary Hindi skill the team already trusts; match that voice, while keeping the plan's need to name commentators and preserve their specific point. The bar is the team's approved sample: a short, warm, everyday-Hindi explanation a person would actually say out loud, with no word repeating and no stiff vocabulary.

---

## Procedure

1. **Resolve the source file.** From the day number, locate `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/<Chapter-folder>/<DAY_NUMBER>.md`. If multiple candidates exist or the canonical file is absent, stop and ask the user which to translate.
2. **Read the source in full.** Note the exact frontmatter, the day title, the notification block, every `##` heading and its exact wording (record which header variant is used for Opening and for Practice), and the verbatim liturgy and verse blocks.
3. **Gather the source context.** Read the day file's `verses` field to get the verse IDs, and its `generation_note` to learn which source was used. Then read the available source-context files (see "Source-context files") for those verses — verse rails preferred, interim commentary summaries otherwise, plus the AI English verse translation. Hold this context in mind so the meaning behind the English prose is fully understood before you translate, especially for the "From the Tradition" note, which compresses a specific commentator's point.
4. **Identify the three translatable bodies.** Capture the prose under Opening/Introduction, under From the Tradition, and under Today's Practice(/Challenge). If the Opening section contains a `*Push notification:*` / notification line above the intro prose, that line stays English; translate only the introductory prose beneath it.
5. **Translate each of the three bodies into Hindi**, one at a time, applying Rules 4–9 and using the source context from step 3 to choose accurate Hindi renderings and preserve doctrinal precision. After each, re-read the English and the Hindi side by side to confirm nothing was added, dropped, or softened, and that every doctrinal point and commentator attribution survived.
6. **Assemble the output file.** Start from an exact copy of the source. Replace only the three translated bodies. Leave the headings in English. Add `translated_from: "en/Days/<Chapter-folder>/<DAY_NUMBER>.md"` to the frontmatter and keep `status: draft`. Preserve any existing `generation_note` verbatim.
7. **Create directories if needed** and save to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md`.
8. **Diff against the source.** Confirm that the only lines that differ are: the three translated bodies, the added `translated_from:` frontmatter line, and nothing else. If any verbatim region changed, fix it before reporting completion.

---

## Completion check

- [ ] Source English day file located and read in full; header variants for Opening and Practice recorded.
- [ ] Source-context files read for the day's verse IDs (verse rails preferred, else interim commentary summaries, plus the AI English verse translation); used to inform renderings without adding content.
- [ ] Exactly three section bodies translated into Hindi: Opening/Introduction, From the Tradition, Today's Practice(/Challenge).
- [ ] All `##` section headings left in English and in original order.
- [ ] Frontmatter, day title, notification text, liturgy block-quotes, and Tibetan + English verse block-quotes reproduced verbatim.
- [ ] `translated_from:` added to frontmatter; `status: draft`; existing `generation_note` preserved.
- [ ] Hindi reads in plain, conversational "chai" register — everyday Hindustani, short clear sentences, no heavy Sanskritized vocabulary, no lofty titles or jargon dumps; technical terms glossed plainly.
- [ ] Translated sense-for-sense, not word-for-word; sentences recast freely for natural flow while keeping the meaning and attribution intact.
- [ ] No key word repeats awkwardly within a passage (varied with synonyms or pronouns).
- [ ] Commentator names transliterated with the source's one-clause identification preserved.
- [ ] Hindi prose adds nothing and omits nothing relative to the English; no doctrinal point flattened despite the plainer wording.
- [ ] No bullet lists or sub-headers introduced; no em-dashes added to body prose.
- [ ] Saved to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md`; no English source or `1-SOURCES/` file modified.
- [ ] Diff against source shows only the three translated bodies and the added `translated_from:` line changed.
