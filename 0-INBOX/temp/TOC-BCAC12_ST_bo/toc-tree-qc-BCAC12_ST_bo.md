---
source: BCAC12_ST_bo
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-09-25
model: gemini-flash-latest
repaired: true
issues_before: 12
issues_after: 18
---

# TOC tree QC report

## Issues found (before repair)

- L13: Tibetan ordinal = 1 but decimal last segment = 2  ->  1.2.2 དང་པོ་གཞི་རྟེན་གྱི་གང་ཟག་
- L33: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 5)  ->  1.2.3.1.4.2 གཉིས་པ་མཚན་ཉིད་
- L89: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.2.3.2.1.1.3.1.3.5 ལྔ་པ་དོན་བསྡུ་བ་
- L112: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2.3.2.1.1.5 ལྔ་པ་བསྐུལ་བ
- L265: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 6)  ->  1.2.4.2.3.1.1.3.3 གསུམ་པ་རྩོད་པ་སྤང་བ
- L268: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.2.4.2.3.1.1.3.6 དྲུག་པ་སྐབས་བསྡུ་བ
- L289: indent 24 spaces != expected 21 for depth 8 (1.2.4.2.3.2.2.3)
- L290: indent 24 spaces != expected 21 for depth 8 (1.2.4.2.3.2.2.4)
- L291: indent 24 spaces != expected 21 for depth 8 (1.2.4.2.3.2.2.5)
- L292: duplicate decimal 1.2.4.2.3.2.2.3 (also at L289)
- L361: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.2.4.3.2.1.4.2.1.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- children of 1.2.4.2.3.2.2: numbered [1, 2, 3, 3, 4, 5], expected [1, 2, 3, 4, 5, 6]

## Issues remaining after repair

- L13: Tibetan ordinal = 1 but decimal last segment = 2  ->  1.2.2 དང་པོ་གཞི་རྟེན་གྱི་གང་ཟག་
- L33: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 5)  ->  1.2.3.1.4.2 གཉིས་པ་མཚན་ཉིད་
- L89: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.2.3.2.1.1.3.1.3.5 ལྔ་པ་དོན་བསྡུ་བ་
- L160: indent 24 spaces != expected 21 for depth 8 (1.2.4.1.2.2.2.3)
- L166: indent 21 spaces != expected 18 for depth 7 (1.2.4.1.2.2.3)
- L175: duplicate decimal 1.2.4.1.2.2.2.3 (also at L160)
- L180: duplicate decimal 1.2.4.1.2.2.3 (also at L166)
- L241: indent 18 spaces != expected 15 for depth 6 (1.2.4.2.2.3)
- L244: duplicate decimal 1.2.4.2.2.3 (also at L241)
- L305: indent 27 spaces != expected 24 for depth 9 (1.2.4.2.3.2.1.2.2)
- L359: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.2.4.3.2.1.4.2.1.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- children of 1.2.4.1.2.2.2: numbered [1, 2, 3, 3], expected [1, 2, 3, 4]
- children of 1.2.4.1.2.2: numbered [1, 2, 3, 3, 4], expected [1, 2, 3, 4, 5]
- children of 1.2.4.1.2.2.1: numbered [1, 2, 4], expected [1, 2, 3]
- children of 1.2.4.2.2: numbered [1, 2, 3, 3], expected [1, 2, 3, 4]
- children of 1.2.4.2.2.2: numbered [1, 2, 4, 5], expected [1, 2, 3, 4]
- children of 1.2.4.2.3.3.2.1.2: numbered [1, 3, 4], expected [1, 2, 3]
- children of 1.2.4.2.3.2.1.2: numbered [2], expected [1]
