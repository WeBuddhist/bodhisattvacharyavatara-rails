# Keyword Extraction Analysis — ཀུན་བཟང་བླ་མའི་ཞལ་ལུང (Words of My Perfect Teacher)

Analysis date: 2026-08-04

## Summary

Three keyword outputs exist: a scored phrase list (`en-normalized.json`, 5,767 entries), a flat single-word list (`en_termbase.json`, 8,673 words), and a TF-IDF file (`en-tfidf.md`). Against the human-made `glossary.md` (531 terms): **60% full coverage, 29% partial, 11% (60 terms) missing entirely**. The biggest failure is that the per-verse keyword files (`en_keyword_verses.json`, `en_verse_keywords.json`) are empty — that pipeline stage never ran. No Tibetan-side extraction exists; projecting glossary terms through the bo/en line alignment gives a 64% hit rate — the alignment itself is sound, but naive single-occurrence projection isn't reliable enough to build a Tibetan keyword list on its own.

## A. English keywords

**en-normalized.json vs en_termbase.json.** Only 25% of the termbase's 8,673 words also appear in the normalized phrase set. The termbase looks like a broad, low-precision intermediate vocabulary (confirmed by 32 leaked stopwords: *himself, ourselves, because, during,* etc.); `en-normalized.json` is the more usable, phrase-aware keyword ranking.

**Top-ranked entries.** Of the top 30 lowest-score (highest-importance) phrases, most are genuine text-specific terms (dharma, buddha, bodhicitta-adjacent phrases, dharma king trisong/songtsen), but about 6 are generic, low-signal words that shouldn't rank so high: *great, action, time, life, good, people*. One entry, "time lord buddha," looks like an n-gram stitching artifact rather than a real phrase. This suggests the scoring is frequency-driven without enough of an IDF/stopword penalty.

**Empty verse-keyword files.** `en_keyword_verses.json` and `en_verse_keywords.json` are both `{}`. The global extraction ran, but the verse-linking step that would make keywords usable in context never completed — the single biggest gap in the pipeline.

## B. Tibetan keywords

No Tibetan extraction file exists, so this tests projecting keywords via the en.md/bo.md line alignment. Both files have 5,383 lines with no blank-line mismatches — the alignment is structurally sound. Spot-checking 22 glossary terms (English term located in en.md, same line checked in bo.md for the matching Tibetan term) found the Tibetan term present **14/22 times (64%)**. Misses were mostly paraphrase (English uses a descriptive phrase, not the glossary headword, on that occurrence) or first-occurrence mismatch, not evidence of drift — so the line alignment is trustworthy, but a usable Tibetan keyword list would need multi-occurrence matching and Tibetan orthographic normalization to get reliability above ~80%.

## C. Glossary cross-check

All 531 glossary entries were checked against both keyword files (case-insensitive, word-by-word for multi-word terms).

| Coverage | Count | % |
|---|---|---|
| Full | 319 | 60.1% |
| Partial | 152 | 28.6% |
| Missing | 60 | 11.3% |

**Partial coverage** is mostly numbered doctrinal sets ("Four empowerments," "Five wisdoms," "Eight auspicious signs") where the head noun is caught but the cardinal qualifier isn't bound to it — a matching limitation, not a real content gap.

**Missing entirely** — 60 terms, split by priority:

<details>
<summary>C.1 Proper nouns / names / schools / texts (40 — lower priority)</summary>

| English | Tibetan |
|---|---|
| Akanishtha | འོག་མིན |
| Akshobhya | མི་བསྐྱོད་པ |
| Atisha | ཇོ་བོ་ཨ་ཏི་ཤ |
| Avalokiteshvara | སྤྱན་རས་གཟིགས |
| Brahma-world | ཚངས་པའི་འཇིག་རྟེན |
| Chamaradvipa | རྔ་ཡབ་གླིང |
| Chenrezi | སྤྱན་རས་གཟིགས |
| Darshaka | མཐོང་ལྡན |
| Destroyer-of-Samsara | འཁོར་བ་འཇིག |
| Dipamkara | — |
| Gelugpa | དགེ་ལུགས་པ |
| Gyelgong | རྒྱལ་འགོང |
| Kagyupa | བཀའ་བརྒྱུད་པ |
| Kashyapa | འོད་སྲུང |
| Krishnacharya | ནག་པོ་སྤྱོད་པ |
| Mahakashyapa | འོད་སྲུང་ཆེན་པོ |
| Manjushri | འཇམ་དཔལ་དབྱངས |
| Manjushrimitra | འཇམ་དཔལ་བཤེས་གཉེན |
| Nalanda | — |
| Once-Come-King | སྔོན་བྱུང་གི་རྒྱལ་པོ |
| Purnakashyapa | འོད་སྲུང་རྫོགས་བྱེད |
| Sakyapa | ས་སྐྱ་པ |
| Samvarasara | བདེ་མཆོག་སྙིང་པོ |
| Shakyamuni | ཤཱ་ཀྱ་ཐུབ་པ |
| Shankara | བདེ་བྱེད |
| Shantarakshita | ཞི་བ་འཚོ |
| Shantideva | ཞི་བ་ལྷ |
| Shariputra | ཤཱ་རིའི་བུ |
| Sarvanivaranavishkambhin | སྒྲིབ་པ་རྣམ་སེལ |
| Shavaripa | ཤ་བ་རི་པ |
| Smritijnana | — |
| Shri Singha | དཔལ་གྱི་སེང་གེ |
| Shrona | གྲོ་བཞིན་སྐྱེས |
| Sunakshatra | ལེགས་པའི་སྐར་མ |
| Vaishravana | རྣམ་ཐོས་སྲས |
| Vikramashila | — |
| Vipashyin | རྣམ་པར་གཟིགས |
| Amoghasiddhi | དོན་ཡོད་གྲུབ་པ |
| Angulimala | — |
| Anandagarbha | བདེ་མཆོག་སྙིང་པོ |

Shantideva, Manjushri, Shakyamuni, and Avalokiteshvara/Chenrezi are surprising misses given their centrality — likely a spelling-variant issue (e.g. "Chenrezig" vs. "Chenrezi") worth a manual check.

</details>

**C.2 Common Buddhist/doctrinal terms (20 — higher priority, should be fixed):**

| English | Tibetan |
|---|---|
| Circumambulation | སྐོར་བ |
| Daka | དཔའ་བོ |
| Demigod | ལྷ་མ་ཡིན |
| Dharmata | ཆོས་ཉིད |
| Doha | — |
| Egolessness | བདག་མེད |
| Gandharva | དྲི་ཟ |
| Garuda | ཁྱུང |
| Ground-of-all | ཀུན་གཞི |
| Kapala | ཀ་པ་ལ |
| Kshatriya | རྒྱལ་རིགས |
| Muni | ཐུབ་པ |
| Non-action | — |
| Pratimoksha | སོ་སོར་ཐར་པ |
| Rakshasa | སྲིན་པོ |
| Rishi | དྲང་སྲོང |
| Shastra | བསྟན་བཅོས |
| Shravaka | ཉན་ཐོས |
| Shravakayana | ཉན་ཐོས་ཀྱི་ཐེག་པ |
| Tsa-tsa | ཙ་ཙ |
| Yaksha | གནོད་སྦྱིན |
| Vaishakha | ས་ག་ཟླ་བ |

These are core doctrinal vocabulary a keyword system for this text should catch — their absence suggests either low frequency in this translation or an unhandled inflected/compound form.


