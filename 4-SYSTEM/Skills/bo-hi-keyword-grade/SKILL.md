---
name: bo-hi-keyword-grade
description: Enriches the existing English-Tibetan keyword JSON with Hindi translations and audience-grade classifications, producing three separate output files (beginner / intermediate / advanced). Reads Tibetan verse text from the canonical source and Hindi translations from a user-supplied annotated Hindi file. Triggers on: "Tibetan Hindi keyword", "grade-level keywords", "bo-hi keyword", "audience grade enrichment".
---

# bo-hi-keyword-grade

This skill extends the existing verse-keyword JSON
(`4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json`)
with three new fields per verse (`bo_text`, `hi_text`) and two new fields per keyword (`hi`, `grade`),
then splits the result into three audience-graded output files.

The Hindi verse translations come from a **user-supplied annotated Hindi file** — Claude does not
invent them. Each keyword's Hindi meaning and grade are assigned by Claude using the grade rules below.

---

## Inputs

Gather all of these before starting. If any is missing, stop and ask — never guess or invent content.

| Input | Description | Path / format |
|---|---|---|
| **Tibetan source** | Canonical Tibetan verse text. Verse IDs are marked `^verse_id` at end of each verse block. | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| **Existing keyword JSON** | English verse text + keywords already enriched with Tibetan (`bo` field). | `4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json` |
| **Annotated Hindi file** | User-supplied Hindi translation file with grade annotations per verse. Format described below. | Path provided by user at run time |

### Annotated Hindi file format

The user's Hindi file marks each verse's translation with a grade level using the tag
`[grade:beginner]`, `[grade:intermediate]`, or `[grade:advanced]` on the line immediately before the
Hindi verse text. A single verse may have up to three variants (one per grade). Example:

```
^1-1
[grade:beginner]
बुद्ध और बोधिसत्त्वों को प्रणाम करके, मैं संक्षेप में बोधिसत्त्व के आचरण का वर्णन करूँगा।

[grade:intermediate]
सुगत, उनके पुत्रों और धर्मकाय सहित सभी वन्दनीयों को प्रणाम करके, मैं बोधिसत्त्वों के संवर में प्रवेश का वर्णन करूँगा।

[grade:advanced]
सुगत, सधर्मकाय ससुतान् और समस्त वन्द्यों को आदरपूर्वक प्रणिपात कर, सुगतात्मजसंवरावतार का यथागम संक्षेप में वर्णन करूँगा।
```

If a verse has only one grade variant, use it for all three output files (adapting the register
slightly when building the other grades — see "Adapting missing grades" below).

---

## Grade levels

| Grade | Audience | Language style | Keyword rank cutoff |
|---|---|---|---|
| `beginner` | General public, new to Buddhism | Plain modern Hindi, everyday words, no Sanskrit jargon. E.g. "जो सबकी भलाई के लिए जागना चाहता है।" | rank ≤ 200 (high-frequency core terms only) |
| `intermediate` | Students with basic Buddhist knowledge | Mix of Hindi and common Sanskrit Buddhist terms. | rank ≤ 500 |
| `advanced` | Scholars, monks, serious practitioners | Sanskrit-rich, technical Abhidharma / Madhyamaka vocabulary. | all keywords (full rank range) |

### Grade classification — keywords

Assign `grade` to each keyword based on its Buddhist depth:

**beginner** — terms a newcomer understands after one teaching:
> buddha, dharma, karma, compassion, virtue, mind, suffering, teacher, monk, prayer, body, death,
> birth, joy, peace, love, kindness, help, practice, vow, faith

**intermediate** — terms requiring study of basic Buddhist philosophy:
> bodhichitta, bodhisattva, emptiness, samsara, nirvana, skandhas, merit, refuge, precepts,
> mindfulness, attachment, afflictions, wisdom, samadhi, dedication, renunciation, generosity,
> patience, diligence, meditative stabilisation, ethical discipline

**advanced** — technical Abhidharma, Madhyamaka, or tantric terminology:
> alayavijnana, dharmakaya, tathagatagarbha, dependent origination (as technical term), two truths,
> non-self, trikaya, mantra, mudra, vajra, bodhisatvacarya, prajnaparamita, madhyamaka, yogacara,
> shamatha, vipashyana (as technical terms), any transliterated Sanskrit/Tibetan term

When a keyword sits on a boundary, assign the lower (more accessible) grade.

### Hindi keyword meanings — grade-differentiated examples

| English keyword | beginner `hi` | intermediate `hi` | advanced `hi` |
|---|---|---|---|
| compassion | दया | करुणा | करुणा / अनुकम्पा |
| emptiness | खालीपन | शून्यता | शून्यता (सर्वधर्मनिःस्वभावता) |
| merit | पुण्य | पुण्य / कुशल | कुशलकर्म |
| bodhichitta | सबके लिए जागने का संकल्प | बोधिचित्त | बोधिचित्त (संवोधिचित्त) |
| suffering | दुःख | दुःख / कष्ट | दुःख (सर्वसंस्कारदुःखता) |

Match the Buddhist context, not a generic dictionary meaning. Keep `hi` values short (1–5 words).

---

## Adapting missing grades

When a verse has no annotation for a target grade, adapt the nearest available version:

- **beginner missing** → take the `intermediate` Hindi and simplify: replace Sanskrit terms with
  plain Hindi equivalents, shorten complex sentences, remove technical vocabulary.
- **advanced missing** → take the `intermediate` Hindi and formalize: add appropriate Sanskrit
  technical terms in parentheses, increase precision of doctrinal language.
- **only one grade provided** → use it as `intermediate`, then derive beginner and advanced as above.
- Never leave `hi_text` empty.

---

## Output format

Same JSON structure as the input, with new fields added. Three separate files, one per grade:

```json
{
  "verse_id": {
    "text": "...",           // English — keep unchanged
    "bo_text": "...",        // Tibetan lines for this verse — ADD
    "hi_text": "...",        // Hindi translation at this grade level — ADD
    "keywords": [
      {
        "key": "...",        // English keyword — keep
        "rank": 0,           // keep
        "score": 0.0,        // keep
        "count": 0,          // keep
        "bo": "...",         // Tibetan meaning — keep
        "hi": "...",         // Hindi meaning at this grade — ADD
        "grade": "beginner"  // target grade for this file — ADD
      }
    ]
  }
}
```

**Keyword filtering per file:**
- `beginner` file: include only keywords with `rank ≤ 200`
- `intermediate` file: include only keywords with `rank ≤ 500`
- `advanced` file: include all keywords regardless of rank

---

## Output files

Save all three files to:

```
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_beginner.json
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_intermediate.json
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_advanced.json
```

This skill writes only to `4-SYSTEM/scripts/english_keyword/output/`. It never modifies
`1-SOURCES/`, the existing enriched JSON, or the user's annotated Hindi file.

---

## Procedure

1. **Read all inputs in full.**
   - Parse Tibetan source (`bo-བློ་ལྡན་ཤེས་རབ།.md`): extract `{verse_id → bo_text}` by collecting
     the Tibetan lines above each `^verse_id` marker, stripping the `![[...]]` transclusion lines,
     and keeping the verse lines only.
   - Parse the annotated Hindi file: extract `{verse_id → {grade → hi_text}}` by reading the
     `^verse_id` markers and the `[grade:X]` tags above each Hindi text block.
   - Load the existing keyword JSON: this is the base — keep every field unchanged.

2. **For each verse, build the three grade outputs in parallel:**
   a. Set `bo_text` from the parsed Tibetan source. If a verse ID is absent from the Tibetan source,
      set `bo_text: ""` and note it.
   b. Set `hi_text` at each grade level from the parsed Hindi file. Apply the "Adapting missing
      grades" rules if a grade variant is absent.
   c. For each keyword in the verse:
      - Assign `grade` using the classification rules above.
      - Assign `hi` (the Hindi meaning at the target grade level).
      - Include the keyword in a grade's output file only if `rank ≤ cutoff` for that grade
        (or grade is `advanced`, which takes all).

3. **Process in batches of 50 verses** to avoid context overflow. After each batch, write / merge
   results to all three output files before moving on. Print progress:
   `Batch N done — verses [first_id]–[last_id] (X / 929 total)`

4. **Never leave `hi` or `hi_text` empty.** If a keyword's Hindi is genuinely uncertain, use the
   best Buddhist-context equivalent and continue. Do not stall.

5. **Verify the output files parse as valid JSON** after the final batch.

---

## Completion check

- [ ] Tibetan source parsed: `{verse_id → bo_text}` built for all verses.
- [ ] Annotated Hindi file parsed: `{verse_id → {grade → hi_text}}` built; missing grades adapted.
- [ ] Existing keyword JSON loaded; all original fields kept unchanged.
- [ ] `bo_text` added to every verse (empty string with note if verse absent from Tibetan source).
- [ ] `hi_text` added at the correct grade level for every verse in each of the three output files.
- [ ] Every keyword has `hi` (Hindi meaning at target grade) and `grade` fields.
- [ ] Keyword rank cutoff applied: beginner ≤ 200, intermediate ≤ 500, advanced = all.
- [ ] Three output files saved to `4-SYSTEM/scripts/english_keyword/output/`.
- [ ] All three output files parse as valid JSON.
- [ ] No `1-SOURCES/` file or the existing enriched JSON modified.
