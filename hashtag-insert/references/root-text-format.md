# Root-text verse format (real example)

Source pattern seen in this project's vault for root-text translations (e.g. `bo-བློ་ལྡན་ཤེས་རབ།.md`, the Tibetan canonical translation of the Bodhicaryavatara).

```markdown
---
title: བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།
...
verse_id_format: chapter-verse
root_text: 1-SOURCES/Text/BCAV08_SH_sk.md
covers_verses: 1-1–10-61
...
---
# ༄༅། །བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་བཞུགས་སོ། ། ^0

## 0. ཀླད་ཀྱི་དོན། ^I-0

༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་ཙརྱ་ཨ་བ་ཏཱ་ར། ^I-1

བོད་སྐད་དུ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། ^I-2

## 1. ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ། ^1-0

![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]

བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །
བདེ་གཤེགས་སྲས་ཀྱི་སྡོམ་ལ་འཇུག་པ་ནི། །
ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། ། ^1-1

![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-2]]

སྔོན་ཆད་མ་བྱུང་བ་ཡང་འདིར་བརྗོད་མེད། །
...
```

And at the very end, after the last chapter, a colophon:

```markdown
## འགྱུར་བྱང། ^b-0

རྒྱ་གར་གྱི་མཁན་པོ་སརྦ་ཛྙཱ་དེ་བ་དང་། ... ^b-1
...
```

## What counts as a "root verse" here

- Real numbered root verses end their block in `^<chapter>-<verse>` where **both parts are plain digits**, e.g. `^1-1`, `^6-14`, `^10-58`. These are what `extract_verses.py` returns and what this skill tags.
- A verse's text is normally 4 pada lines (occasionally fewer/more), each ending in Tibetan double-shad punctuation (`། །`), immediately preceded by a `![[...]]` transclusion embed pointing at the corresponding line in the Sanskrit/source root text, and followed by a blank line before the next transclusion.
- Chapter headings (`## N. <chapter title> ^N-0`) mark the start of each chapter and are used only to track the current chapter number — they are not verses.
- **Non-numeric anchors are structural, not verses**, and are deliberately excluded:
  - Front-matter/homage material before chapter 1 uses anchors like `^I-1`, `^I-2`, `^I-3` (roman-numeral chapter marker).
  - The closing colophon uses anchors like `^b-1`, `^b-2`, `^b-3`.
  - Don't tag these — they're translator's notes/homages, not root verses subject to thematic tagging.
- Check the frontmatter's `covers_verses` field as a sanity check on the expected verse range, but don't be alarmed if the parsed count differs slightly (e.g. some source verses are combined under one anchor) — spot-check against the raw file if the discrepancy is large.
