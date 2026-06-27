---
ref: <chapter-verse, e.g. 1-1>
unit_type: single        # single | group | template | instance
unit_verses: [<ref>]     # list all verses if this is a group/template
commentary_coverage: []  # registered_ids or book_ids of commentaries used
tradition_coverage: []   # e.g. [nyingma, gelug]
concepts_in_verse: []    # བོད་སྐད་ term (gloss) — concepts the verse introduces
concepts_in_commentary: []   # བོད་སྐད་ term (gloss) — further concepts the commentaries raise
stories: []              # names of narratives the commentaries attach to this verse
layer_order: [chendrel, word-disambiguation, concepts, stories, metaphors, quotations, commentary-synthesis]
status: draft            # LLM always leaves draft; only a domain specialist sets complete
---

<!-- HOW TO USE: copy this file to <ref>.md (e.g. 1-1.md). Fill every section.
 REQUIRED sections (never delete): Source Text, Disambiguated Restatement, and the merged
 Traditional Interpretation & AI Overview. OPTIONAL sections (delete the heading if no cited material
 exists for this verse): Chendrel, Word-by-word Disambiguation, Key Concepts, Stories,
 Metaphors, Quotations. Language: Traditional Interpretation is English; everything else
 is Tibetan. Every claim ends with a (1-SOURCES/.../<file>.md#^<block>) citation.
 Full rules: 2-RAILS/About Rails.md §5 · generation procedure + AI-Overview prompt:
 4-SYSTEM/Skills/verse-context/SKILL.md -->

## 1. Source Text

### Sanskrit
![[1-SOURCES/Text/BCAV08_SH_sk.md#^<ref>]]

### Tibetan
![[1-SOURCES/Text/<bo-root-text>.md#^<ref>]]

**Variants**
[Ed: <cross-edition / cross-language variant, with citation — or delete this block>]

## 2. Chendrel — ཚིག་འགྲེལ

<!-- Optional. Running Tibetan word-commentary from an annotation (mchan-'grel) source:
 each phrase of the root verse in [**brackets**] followed by its inline gloss. Delete if no
 word-commentary source covers this verse. -->
[**<root phrase>**] <gloss> — [**<root phrase>**] <gloss> …
(1-SOURCES/Commentaries/<mchan-grel-file>.md#^<block>)

## 3. Word-by-word Disambiguation (ཚིག་དོན་གསལ་བཤད།)

<!-- Optional. Only tokens where a commentary makes a NON-OBVIOUS choice. Delete if none. -->
- **<root word/phrase>** — <Tibetan disambiguating gloss: sense / compound / referent>
  (1-SOURCES/Commentaries/<file>.md#^<block>)

## 4. Key Concepts (ཆོས་ཀྱི་གནད་ཚིག)

### ཚིགས་བཅད་ནང་གི་གནད་ཚིག — concepts the verse introduces
- **<term>** (<gloss>) — <one-line Tibetan note>
  (1-SOURCES/Commentaries/<file>.md#^<block>) · [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]

### འགྲེལ་པ་ནས་འབྱུང་བའི་གནད་ཚིག — further concepts the commentaries raise
- **<term>** (<gloss>) — <one-line Tibetan note>
  (1-SOURCES/Commentaries/<file>.md#^<block>) · [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]

## 5. Stories (སྒྲུང་།)

<!-- Optional. From gtam-rgyud / sgrung-'grel story commentaries. Delete if none. -->
- **<story name>** — <Tibetan précis; which phrase of the verse it illustrates>
  (1-SOURCES/Commentaries/<story-file>.md#^<block>)

## 6. Metaphors (དཔེ།)

<!-- Optional. Figures in the verse or developed by the commentaries. Delete if none. -->
- **<image>** → <tenor / what it illustrates>. <how the commentary develops it.>
  (1-SOURCES/Commentaries/<file>.md#^<block>)

## 7. Quotations (ལུང་།)

<!-- Optional. Verbatim Tibetan scripture the commentaries adduce on this verse/topic.
 Delete if no commentary block quotes scripture verbatim here. -->
> <verbatim Tibetan quotation>
> — <scripture as named by the commentary>
> (1-SOURCES/Commentaries/<file>.md#^<block>)

## 8. Disambiguated Restatement (Tibetan)

<Short Tibetan rewrite of the verse with every ambiguity the synthesis resolved made
explicit (referents fixed, senses chosen, compounds parsed). Cite the blocks that
authorise each choice. This is what transformation skills consume.>
(1-SOURCES/Commentaries/<file>.md#^<block>)

## 9. Concept Links
- [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]

## 10. Traditional Interpretation & AI Overview (བསྡུས་དོན།)

<!-- The cited per-commentary reading (English) plus its Tibetan AI-Overview synthesis,
 together. Every claim in the synthesis must trace to a paraphrase below it. -->

### <commentary-id> — <Commentary full name> (<language>)
<English paraphrase of this commentary's reading; every claim cited.>
(1-SOURCES/Commentaries/<file>.md#^<block>)

<!-- repeat one ### subsection per commentary -->

### Divergences
<Only where commentaries genuinely disagree. Attribute each position, flag ⚑. Delete if none.>

### AI Overview — བསྡུས་དོན།

**ངོ་སྤྲོད་མདོར་བསྡུས།** <one–two Tibetan sentences answering "what does this verse say," in a single synthetic voice drawn from the paraphrases above.>
(1-SOURCES/Commentaries/<file>.md#^<block>)

**གནད་དོན་གཙོ་བོ།**
- <key point in Tibetan> (1-SOURCES/Commentaries/<file>.md#^<block>)
- <key point in Tibetan> (1-SOURCES/Commentaries/<file>.md#^<block>)
<!-- 3–6 bullets; ⚑ + cite both sides on any point the commentaries split. -->
