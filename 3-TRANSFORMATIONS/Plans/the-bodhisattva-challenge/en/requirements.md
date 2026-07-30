---
title: "Requirements — The Bodhisattva Challenge (English stream)"
lang_tag: en
plan: the-bodhisattva-challenge
status: draft
---

# Requirements — English stream

Style contract for `en/Days/`. This file did not exist until Chapter 2 day 31; the skills `english-plan-generator`, `english-plan-from-tibetan`, and `english-plan-evaluator` all referenced it. It is written from what days 15–31 actually do, so it describes existing practice rather than imposing a new one.

---

## 1. Two formats exist. Know which one you are writing.

**Compact format — current, use this.** Days 15 onward (`Chapter-2 D15-D40/` and later). Four `##` sections, in this order and with this exact wording:

```
## Today's Verse
## 1) Introduction to Today's Practice
## 2) Commentary Explanation
## 3) Today's Practice
```

**Liturgy format — legacy, Chapter 1 only.** Days 1–14 use a six-section shape with `## Opening`, `## Renewing the Bodhisattva Vow`, `## Today's Verses`, `## From the Tradition`, `## Aspiration and Dedication`, `## Today's Practice`, plus a `# Day N — …` title and a `> **Notification**` block. Do not extend this format to new chapters without a human decision. The liturgy blocks live in `en/assets/liturgy.md`.

Filename in the compact format: `<N>-ch<C>-v<start>-<end>-eng.md`, no zero-padding.

---

## 2. Frontmatter

Minimum, as in days 15–25:

```yaml
day: 26
chapter: 2
verse: "28-29"
```

From day 26 onward also record the grounding, which is what makes the citation chain auditable:

```yaml
status: draft
context_packages:
  - "2-RAILS/Verses/2-28-summary.md"
  - "2-RAILS/Verses/2-29-summary.md"
generation_note: "…which rails, which commentators and block IDs, any correction made, anything uncorroborated."
```

Never set `status: complete`. A domain specialist does that.

---

## 3. Grounding — the rule that matters most

Content comes from `2-RAILS/Verses/<C>-<N>-summary.md`. These exist for all of Chapter 2 and carry eight commentators each with block-ID citations, a metaphors section, main teaching points, key terms, and a synthesis.

Do **not** build a day by translating the Tibetan day file in `3-TRANSFORMATIONS/Plans/Dalai Lama/` on its own. That file is itself a compressed digest of the same commentaries. Working from it alone produces two failures seen in the first pass at days 26–31: gaps get filled by the writer's own reasoning rather than by the commentary, and attributions get bundled onto whoever the digest names last. The Tibetan day file is legitimate context — it tells you the day's chosen angle and the practice — but the rails are the source.

If a claim cannot be traced to a cited rail passage, leave it out. If you keep something that only the Dalai Lama plan file supports, say so in `generation_note`.

**Never flatten a divergence.** Where the rails mark ⚑, carry both readings and say who holds each.

---

## 4. Section by section

### Today's Verse

One block-quote per verse, verbatim from `1-SOURCES/Translations/translation-ai/bo-en-translation/bca-en-plain.md`, located by block ID, each ending `^<C>-<N>`. Reproduce the source's own punctuation, including curly apostrophes. No paraphrase, no re-lineation.

### 1) Introduction to Today's Practice

80–115 words, one paragraph. Opens with "Today's practice is based on verse(s) … from the … chapter of the _Bodhicaryāvatāra_." Says plainly what the verses do and what the day asks of the reader. Note a chapter or section change when there is one.

### 2) Commentary Explanation

The substance of the day. **180–220 words**, prose paragraphs, no bullets. Days 15–25 average 195. This is a hard ceiling, not a target to grow into.

Build it around **the one thing the commentary adds that a careful reader of the verses alone would not reach** — a distinction, a mechanism, a stage-analysis, a concrete example. **One idea, not three.** Follow whatever point the Tibetan day file's `༤། འགྲེལ་བཤད།` leads with, so the language streams stay aligned with the Tibetan one.

> ⚠️ **Learned the hard way on days 26–31.** The first rails-based rebuild ran to 320–401 words and named up to **seven** Tibetan commentators in one section. It was accurate and nearly unreadable. Grounding a claim and putting it on the page are different decisions: the rails carry far more than a daily reader can absorb, and the surplus belongs in `generation_note` and in the rails, where a specialist can find it. Days 15–25 name **zero** Tibetan commentators and work fine.

Rules:

- **At most one named Tibetan commentator per section.** Two only when a ⚑ divergence genuinely needs both. Otherwise write "the commentaries". Days 15–25 use only "Master Shantideva" and "the commentaries" / "Spiritual teachers explain".
- Name a commentator once, then "he".
- Show the mechanism in steps. Do not assert importance with "great", "profound", "vast".
- Say who a consequence falls on.
- Short sentences, readable first time by a non-native speaker. No idioms that fail if read literally. No rhetorical question-and-answer.
- Use the term, do not paraphrase it: samsara, bodhicitta, karma, merit, refuge, bardo. No diacritics in prose (Shantideva, not Śāntideva).
- No em-dashes in body prose. No emojis. Light bold only, a phrase at most.

### 3) Today's Practice

Two labelled parts, exactly as days 15–31:

```
**Actual Practice:** [one sentence, first person, one doable action]

**Explanation:** _(Category)_ [120–160 words]
```

The action must match the Tibetan day file's `ཉམས་ལེན་དངོས།`. The category label renders the source's parenthetical: `སྡིག་པ་མི་བྱ་བ།` → _(Avoiding wrongdoing)_, `དགེ་བ་བྱ་བ།` → _(Doing good)_, `རང་སེམས་འདུལ་བ།` → _(Taming the mind)_. Patience and generosity days use _(Patience Practice)_ and _(Generosity Practice)_.

The explanation names a real situation, gives the reason from the verses, and stays a gentle invitation rather than an assignment. **Check the two previous days and make the action different** — the confession and offering verses run in long stretches and the practices drift into repetition.

---

## 5. Reader

A lay Buddhist, new to the philosophy, time-poor, sceptical of formulaic spiritual writing. Many are not native English speakers. One real idea to carry into the day. Where a rule and the reader conflict, serve the reader.

---

## 6. Before saving

- [ ] Verses verbatim from `bca-en-plain.md`, block IDs contiguous and matching `verse:`.
- [ ] Verse range matches `Tibetan-schedule-corrected.md`.
- [ ] Four headings, exact wording, right order.
- [ ] Every claim in §2 traceable to a cited rail; `context_packages` and `generation_note` filled.
- [ ] Divergences preserved, not flattened.
- [ ] Practice matches the Tibetan `ཉམས་ལེན་དངོས།` and differs from the two previous days.
- [ ] No em-dashes in prose, no diacritics, no invented names or bare names without their story.
- [ ] `status: draft`.
