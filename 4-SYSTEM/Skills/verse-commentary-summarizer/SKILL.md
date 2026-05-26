---
name: verse-commentary-summarizer
description: Create a verse-specific summary file under 3-TRANSFORMATIONS/Translations/ by extracting the verse's commentary explanations from provided commentary sources, summarizing each commentary individually, and generating a combined synthesis.
---

# verse-commentary-summarizer

This skill automates the creation of verse-by-verse commentary summary files. Given a verse ID, it extracts the relevant explanation blocks from one or more classical commentary files in `1-SOURCES/Commentaries/`, generates a concise summary of the explanation for each commentary, synthesizes them into a combined summary, and outputs the resulting file in the `3-TRANSFORMATIONS/Translations/` directory (typically under a specific translation track's `Verses/` folder).

This process ensures that the translator has a consolidated, multi-source reference of traditional interpretations for each verse, preventing misinterpretation and grounding the translation in authentic commentaries.

---

## Inputs

- **Verse ID** — The ID of the verse in `chapter-verse` format (e.g., `1-1`, `1-10`).
- **Commentary Files** — One or more commentary filenames from `1-SOURCES/Commentaries/` (e.g., `zh-賈曹傑 入菩薩行論廣解.md`, `bo-དངུལ་ཆུ་ཐོགས་མེད།.md`).
- **Output Path/Track** — The target directory under `3-TRANSFORMATIONS/Translations/` (e.g., `en-plain-english/Verses/` or `en-ai/Verses/`).

---

## Output

A new markdown file named `<verse-id>.md` (e.g., `1-1.md`) created at:

```
3-TRANSFORMATIONS/Translations/<track-name>/Verses/<verse-id>.md
```

If the file already exists, read it first and update it in place, preserving any manual refinements.

---

## Output File Format

```markdown
---
verse_id: <e.g. 1-1>
commentaries:
  - <commentary-1-filename>
  - <commentary-2-filename>
output_track: <e.g. en-plain-english>
status: draft
---

# Verse <verse-id> Commentary Summary & Synthesis

## Verse Text
![[1-SOURCES/Text/sk-dev.md#^<verse-id>]]

## Commentary Explanations

### [[<commentary-1-filename>]]
![[1-SOURCES/Commentaries/<commentary-1-filename>#^<block-id-1>]]
![[1-SOURCES/Commentaries/<commentary-1-filename>#^<block-id-2>]]

### [[<commentary-2-filename>]]
![[1-SOURCES/Commentaries/<commentary-2-filename>#^<block-id-1>]]

## Per-Commentary Summaries

### [[<commentary-1-filename>]] Summary
<A concise, accurate summary of the explanation from Commentary 1 in the target language (e.g., English). Keep it focused on key points, definitions, analogies, and structural divisions.>

### [[<commentary-2-filename>]] Summary
<A concise, accurate summary of the explanation from Commentary 2 in the target language.>

## Combined Commentary Synthesis
<A synthesized summary that integrates the insights from all commentaries. Highlight consensus interpretations, major terminological mappings, and any notable divergences or unique doctrinal points raised by different commentators.>
```

---

## Rules

1. **Locate Commentary Blocks via Transclusion Markers:** In the commentary files, the explanation for a verse is located immediately after the transclusion marker of that verse, e.g., `![[1-SOURCES/Text/sk-dev.md#^1-1]]`. Extract all blocks between this marker and the next transclusion marker (e.g., `![[1-SOURCES/Text/sk-dev.md#^1-2]]`) or the next heading.
2. **Use Transclusions for Explanations:** In the "Commentary Explanations" section, transclude the raw source blocks using `![[1-SOURCES/Commentaries/<file>#^<block-id>]]` instead of copying the text, so the user can easily click through to the full source.
3. **Preserve Doctrinal and Terminology Precision:** In the summaries, maintain the exact technical terms or note key translations (e.g., *bodhicitta*, *Sugata*).
4. **Draft in Target Language:** The summaries and combined synthesis should be drafted in the target language of the translation track (defaulting to English unless specified otherwise).
5. **No Hallucination:** Rely strictly on the extracted commentary blocks. If a commentary does not contain an explanation for the verse, clearly state that it is not covered.

---

## Procedure

1. **Locate the Verse:** Identify the target `verse_id` (e.g., `1-1`).
2. **Scan Commentary Files:** For each provided commentary file in `1-SOURCES/Commentaries/`:
   - Open the file and locate the transclusion marker for the verse: `![[1-SOURCES/Text/sk-dev.md#^<verse-id>]]` (or matching root text file).
   - Collect all block IDs (e.g. `^1-1`, `^1-2`) of the paragraphs that follow this marker up to the next transclusion marker or heading.
3. **Draft the Commentary Explanations:** Create a section with subheadings for each commentary, transcluding the collected blocks.
4. **Generate Per-Commentary Summaries:** Read the extracted blocks for each commentary and write a concise, clear summary of how that commentator explains the verse (e.g., what terms are defined, what divisions are made, what analogies are used).
5. **Generate the Combined Synthesis:** Synthesize the summaries. Identify what the commentators agree on (Consensus) and any unique insights or differences in their interpretations (Divergences).
6. **Set Frontmatter & Save:** Add the YAML frontmatter, set `status: draft`, and write the file to `3-TRANSFORMATIONS/Translations/<track-name>/Verses/<verse-id>.md`.

---

## Example

### Example Invocation
> "Run `verse-commentary-summarizer` for verse `1-1` using commentaries `zh-賈曹傑 入菩薩行論廣解.md` and `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` for track `en-plain-english`."

### Example Output File (`3-TRANSFORMATIONS/Translations/en-plain-english/Verses/1-1.md`)
```markdown
---
verse_id: 1-1
commentaries:
  - zh-賈曹傑 入菩薩行論廣解.md
  - bo-དངུལ་ཆུ་ཐོགས་མེད།.md
output_track: en-plain-english
status: draft
---

# Verse 1-1 Commentary Summary & Synthesis

## Verse Text
![[1-SOURCES/Text/sk-dev.md#^1-1]]

## Commentary Explanations

### [[zh-賈曹傑 入菩薩行論廣解.md]]
![[1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md#^1-1]]
![[1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md#^1-2]]
![[1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md#^1-3]]
![[1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md#^1-4]]
![[1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md#^1-5]]

### [[bo-དངུལ་ཆུ་ཐོགས་མེད།.md]]
![[1-SOURCES/Commentaries/bo-དངུལ་ཆུ་ཐོགས་མེད།.md#^1-1]]

## Per-Commentary Summaries

### [[zh-賈曹傑 入菩薩行論廣解.md]] Summary
Gyaltsab Je structures the homage (worship) into three parts: purpose, condensed meaning, and word meaning.
- **Purpose:** Paying homage purifies obstacles to composing the treatise and enables the author and others to accumulate merit.
- **Word Meaning of Sugata:** Explained in terms of both abandonment (graceful leaving of afflictions, not returning to cyclic existence, and abandoning non-afflictive ignorance) and realization (directly knowing the two types of selflessness).
- **The Three Jewels:** The Buddha Jewel is the Sugata; the Dharma Jewel is the naturally pure Dharmakaya; the Sons of the Sugatas are the noble Bodhisattvas (the Sangha Jewel). Homage is also paid to preceptors, masters, etc.

### [[bo-དངུལ་ཆུ་ཐོགས་མེད།.md]] Summary
Thokme Zangpo explains that the homage is performed to the Sugatas, their Sons, and the Dharmakaya to clear obstacles and generate merit. He defines *Sugata* as "one who has gone to bliss" and explains that the Bodhisattvas are the "Sons of the Victorious."

## Combined Commentary Synthesis
Both commentators agree that the opening verse of homage (worship) is dedicated to the Three Jewels—the Buddhas (Sugatas), the Dharma (Dharmakaya), and the Sangha (Sons of the Sugatas)—to purify obstacles and accumulate merit for the composition.
- **Consensus:** *Sugata* is defined in terms of supreme realization and abandonment of afflictions, while the Bodhisattvas are recognized as the spiritual heirs (Sons) of the Buddhas.
- **Unique Insights:** Gyaltsab Je provides a highly detailed scholastic breakdown of the term *Sugata*, distinguishing its aspects of abandonment and realization from non-Buddhist ascetics, Hinayana disciples, and solitary realizers, respectively.
```

---

## Completion Check

- [ ] YAML frontmatter is complete with `verse_id`, `commentaries`, `output_track`, and `status: draft`.
- [ ] Verse text section correctly transcludes the root text verse.
- [ ] Commentary Explanations section transcludes all relevant blocks from the specified commentaries.
- [ ] Per-Commentary Summaries section contains a focused summary of each commentary's explanation.
- [ ] Combined Commentary Synthesis successfully integrates the commentaries, highlighting consensus and differences.
- [ ] Output is written to the correct path under `3-TRANSFORMATIONS/Translations/`.
