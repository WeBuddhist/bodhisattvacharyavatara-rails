---
title: "Hindi verse translation - style contract"
track: hi-poetic
transformation_type: translation
lang_tag: hi
language: hindi
status: draft
doc_language: en
doc_language_note: "CLAUDE.md §9 asks that requirements.md be written in the target language. Written in English at the explicit request of the vault owner, who does not read Hindi and must be able to audit this contract. Locked renderings and quoted verse lines stay in Devanagari."
base_style_source: "1-SOURCES/Translations/translation-ai/bca-hi-poetic.md (verses 1-1 to 2-24)"
---

# Style contract

This contract is **derived** from the pre-existing Hindi verse translation (1-1 through 2-24), not invented. New verses must read as continuous with the old ones.

---

## 1. Verse shape

- **Four lines** per verse. Never three, never five.
- Each line carries **one comma caesura** near the middle, splitting it into two half-lines:
  > `जितने भी हैं लोकों में सारे, धूल के छोटे-छोटे कण,`
- **Rhyme: AABB** — lines 1-2 rhyme, lines 3-4 rhyme. This is end-assonance, not strict metrical scansion; vowel agreement is enough (`सागर हैं / सागर हैं`, `करूँ / धरूँ`, `कण / झुकता हूँ`).
- Lines 1, 2, 3 end with **a single trailing space** (markdown line break). Line 4 ends with **`॥`**.
- Line 2 usually ends with **`।`** — the existing text is inconsistent about this. Follow it where natural; don't force it.

## 2. Verse numbering

- Header is **`**(Devanagari numeral)**`** — e.g. `**(२५)**`, alone on its own line.
- Numbering **restarts per chapter**. Chapter 2 counts from `(१)`.
- No blank line between the number and line 1; one blank line between verses.
- The block ID (`^2-25`) sits on its own line **after** line 4, separated by a blank line.

## 3. Register

- **Simplest possible Hindi.** Use a Sanskritic (*tatsama*) word only when that word is itself religiously necessary — बोधिचित्त, तथागत, स्तूप. Otherwise everyday Hindi: `तकलीफ़`, `नासमझ`, `भयानक`, `फ़ायदा`, `ज़ोर`.
- Common Urdu/Persian-origin words are fine and are already present in the base text: `ताकत`, `अंजाम`, `इंसान`, `खास`.
- **Parenthetical glosses sparingly** — only where meaning breaks without one: `सोने की मूठ (डंडी) वाले`. Never more than one per verse.
- **No footnotes, no English, no non-Devanagari script** in the verses themselves.

## 4. Spelling decisions (locked for chapter 2)

| Decision | Reason |
|---|---|
| **बोधिसत्व** (single त) | The spelling already used in chapter 2 (verses 2-21, 2-22). Chapter 1 uses `बोधिसत्त्व` — don't change it there, don't carry it here. |
| **बोधिचित्त** | Used throughout. |
| Nuqta optional | The base text is inconsistent; readability wins. |

## 5. Rails-based method (mandatory)

Same order, same inputs, for every verse:

1. **Tibetan root** (`1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`) — the basis of meaning.
2. **Sanskrit** (`1-SOURCES/Text/BCAV08_SH_sk.md`) — for disambiguation.
3. **The rail's `བསྡུས་དོན།` synthesis** (`2-RAILS/Verses/<id>-summary.md`) — this is what tells you *what the verse is saying*. Translate from this, not from the bare root line.
4. **The rail's `གནད་ཚིག` key-terms table** → resolved to a locked Hindi form via `termbase.md`.
5. **The rail's `⚑ Divergences`** → resolved by the rule in §6.
6. **The preceding 3 Hindi verses** — for continuity of metre and voice.

The three English translations (Padmakara, Wallace, Choephel) are **witnesses only**: where all three agree, a reading is confirmed; where they split, the rail's synthesis decides. **Never translate from the English.**

## 6. Divergence rule

Where commentators disagree (`⚑`), the verse takes the **broadest attested reading**:

- If one commentary gives a narrow taxonomy (e.g. `མཆོད་རྟེན` = eight specific stūpas) and another gives a wide sense (= any support of the Buddha's body, speech, or mind), take the **wide** one.
- The narrow reading must **not** appear in the verse, but must be recorded in `divergence-log.md` — which reading was taken, which were dropped, and the rail citation for each.
- **Never reconcile two readings by cramming both into one line.** Pick one, log the rest.
- Exception: if the rail itself states that two glosses are complementary rather than contradictory, both may be carried. Note it in the log.

## 7. Hard prohibitions

- **Add nothing** the rail's synthesis does not support — not even to complete a rhyme. Rhyme is subordinate to meaning.
- **No synonyms** for any lemma locked in `termbase.md`.
- **Never add, drop, merge, or split verses.** One verse in the Tibetan is one verse in Hindi.
- **No parametric knowledge** — no story, name, number, or taxonomy from the model's own memory.

## 8. Production process

- **5-6 verses per pass.** More than that and the metre degrades.
- QA after each pass: verse count, line count, termbase compliance, rhyme, rail fidelity.
- All output stays `status: draft`. Only a human subject-matter expert sets `complete`.
