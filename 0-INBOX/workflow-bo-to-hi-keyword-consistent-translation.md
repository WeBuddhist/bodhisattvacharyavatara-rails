---
title: Workflow — Tibetan root text → keyword-consistent Hindi translation (×3 audiences)
status: draft
location: 0-INBOX (scratch / design note — not cited from elsewhere)
inputs:
  - 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md   # Tibetan root (verse-aligned)
  - 1-SOURCES/Translations/en-David_Karma_Choephel.md
  - 1-SOURCES/Translations/en-Padmakara_2006.md
  - 1-SOURCES/Translations/en-Wallace.md
audiences: [8th-grade, general, scholar]
target_language: hi (Hindi)
---

# Goal

Translate the Tibetan root text into Hindi with two guarantees:

1. **Vocabulary consistency** — every keyword renders the same way everywhere.
2. **Audience adaptation** — the rendering is tuned to 8th-grade, general, and scholar readers.

The principle: **keyword *identity* is fixed once (on the Tibetan side); only the *rendering* varies by audience.**

---

# The workflow (as requested)

| # | Step | Input | Output |
|---|------|-------|--------|
| 1 | Extract English keywords (TF-IDF) | EN translation(s) | EN keyword list |
| 2 | Bo–En keyword glossary via verse alignment | Bo root + EN keywords + block-ID alignment | `bo-en` keyword glossary: *term · verse-id · frequency* |
| 3 | Zero-shot Hindi translation, audience-tuned | Bo root | 3 Hindi drafts (one per audience) |
| 4 | Extract Hindi keywords against Tibetan | 3 Hindi drafts + Bo root + step-2 glossary | `bo-hi` keyword glossary |
| 5 | Build termbase per audience | `bo-hi` glossary | 3 termbases (one locked rendering per term) |
| 6 | Apply termbase → final translation | termbase + step-3 drafts | 3 keyword-consistent Hindi files |

---

# Issues found in the workflow as drafted

**A. The existing `hi-बोधिचर्यावतारः.md` is Sanskrit (Devanagari), not Hindi.** It cannot be used as a Hindi reference. There is currently **no** human Hindi translation in the vault, which is exactly why the zero-shot bootstrap in step 3 is justified.

**B. TF-IDF on a single translation imports that translator's bias.** TF-IDF surfaces *statistically distinctive* words, not necessarily *doctrinal keywords* (e.g. it may rank a rare proper noun above བྱང་ཆུབ་སེམས་ / bodhicitta, which appears so often it looks "uninteresting" to TF-IDF). Recommendation: run TF-IDF across **all** EN translations and intersect, and union the result with the vault's already-built `2-RAILS/Bilingual-Glossaries/bo-en.md` and `2-RAILS/Local-Wiki/` term list, which are the *authoritative* keyword anchors.

**C. English→Tibetan mapping needs word-level, not verse-level, alignment.** "We already have verse alignment" (shared block IDs) tells you which *verse* a keyword is in, but a verse has ~20–30 Tibetan words. The vault already solves this with **`interlinear-gloss`** (token-level `\gla/\glb/\glc` alignment). Use it instead of guessing the Tibetan counterpart from verse co-occurrence.

**D. Why pivot through English at all?** If the only target is Hindi, the English step is a *bridge* to decide which Tibetan terms count as keywords. The vault already has that keyword set (`bo-en.md` + Local-Wiki), so the English/TF-IDF detour is largely redundant — keep it only as a *candidate generator*, not the source of truth.

**E. Audience handling.** Steps 3–6 fan out ×3. Keep the **keyword set audience-independent** (one anchored list of Tibetan terms); only the **rendering column** differs per audience. Extracting Hindi keywords separately from three independently zero-shot drafts (step 4) risks three different term *sets* — anchor all three to the same Tibetan lemma list instead.

**F. Order of locking.** The vault's rails are *termbase-first* (prescriptive), then translate. The requested order is *draft-first* (zero-shot), then harvest, then lock, then re-translate. The draft-first bootstrap is fine **because no Hindi reference exists** — but step 6 should be a **full regeneration under the locked termbase**, not a find-and-replace patch of step-3 drafts (patching produces ungrammatical Hindi where a term's case/agreement changes).

**G. Consistency must be verified, not assumed.** Add a final lint/QA pass that programmatically checks every termbase term renders identically across all output (the vault's planned `translation-qa` / `style-consistency-check`).

---

# Optimized workflow (mapped to existing vault skills)

The vault already contains most of this machinery. Reuse it rather than rebuilding:

```
0.  interlinear-gloss   : Bo root × each EN translation → token-aligned gloss      [exists]
1.  glossary-extract-raw: each gloss → raw bo-en glossary                          [exists]
2.  glossary-combine    : merge → 2-RAILS/Bilingual-Glossaries/bo-en.md            [exists, file present]
        ↳ keyword anchor set = (TF-IDF candidates) ∪ (bo-en glossary) ∪ (Local-Wiki terms)
        ↳ each entry carries: Bo lemma · EN rendering(s) · verse-id(s) · frequency
3.  zero-shot translate : Bo root → 3 Hindi drafts (8th-grade / general / scholar)
4.  interlinear-gloss    (Bo × each Hindi draft) → glossary-extract-raw
        → 2-RAILS/Bilingual-Glossaries/bo-hi.md  (Bo lemma ↔ Hindi rendering, per audience)
5.  glossary-select     : per audience, pick ONE Hindi rendering per Bo lemma,
        guided by that track's requirements.md → 3 termbase.md files               [exists]
        ↳ 3-TRANSFORMATIONS/Translations/hi-8th-grade|general|scholar/termbase.md
6.  translate-section   : REGENERATE each Hindi track under its locked termbase     [planned]
7.  translation-qa + style-consistency-check : verify term consistency             [planned]
```

Net changes vs. the drafted workflow:
- Replace ad-hoc TF-IDF+verse-cooccurrence with `interlinear-gloss` for word-level alignment; keep TF-IDF only to *propose* candidate keywords.
- Anchor the keyword set on the **Tibetan** lemma once; never let three drafts define three term sets.
- Make step 6 a **regeneration** under the termbase, plus a QA lint, not a string replace.
- Land outputs in the canonical `3-TRANSFORMATIONS/Translations/<track>/` layout (requirements.md · termbase.md · audience.md · translation files).

---

# Decisions (locked 2026-06-29)

1. **Keyword source = fresh TF-IDF only** (user choice). Extract keywords from the EN translation(s) by TF-IDF; do not pre-seed from `bo-en.md`/Local-Wiki.
   - ⚠️ Mitigations to apply anyway: run TF-IDF over *all* EN translations (not just Choephel) and intersect, to dampen single-translator bias; and for the Bo↔En mapping in step 2, use word-level alignment (`interlinear-gloss`), since TF-IDF gives the English keyword but verse-level alignment alone won't pin the exact Tibetan lemma.
2. **Shared Tibetan keyword set, three renderings** (user choice). One anchored Bo lemma list; only the Hindi rendering column differs per audience.
3. **Step 6 = full regeneration under the locked termbase** (user choice). No find-and-replace patching.
4. **Do not run yet** (user choice). This is design-only; build is deferred.

# Still to confirm before a build

- Hindi register per audience (e.g. scholar = Sanskrit/tatsama-heavy; 8th-grade = colloquial Hindustani).
- Scope of first run when greenlit: pilot chapter vs. whole text (1-1–10-61).
