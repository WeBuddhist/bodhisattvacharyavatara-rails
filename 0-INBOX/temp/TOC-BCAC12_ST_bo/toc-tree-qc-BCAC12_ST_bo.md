---
source: BCAC12_ST_bo
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-09-25
model: gemini-flash-latest
repaired: true
issues_before: 44
issues_after: 27
---

# TOC tree QC report

## Issues found (before repair)

- L105: duplicate decimal 2.3.2.2.3.3 (also at L101)
- L116: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  2.3.2.3 རྗེས་མཇུག་
- L187: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.1.2.2.3.2.3.4 བཞི་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L256: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 3, 4)  ->  2.4.2.3.1.1.3.6 དྲུག་པ་སྐབས་བསྡུ་བ་
- L267: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.2.3.2.1.1 དང་པོ་གཡོ་བ་མེད་པ་
- L277: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.2.3)
- L278: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.2.4)
- L279: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.2.5)
- L280: indent 18 spaces != expected 15 for depth 6 (2.4.2.3.2.3)
- L281: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.1)
- L282: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.2)
- L283: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.3)
- L284: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.1)
- L285: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.2)
- L286: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.3)
- L287: indent 24 spaces != expected 18 for depth 7 (2.4.2.3.2.3.4)
- L349: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.3.2.1.4.2.1.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- L421: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  2.4.3.2.1.4.3.2.2.3.1.1 དང་པོ་ཕན་འདོགས་ཆེ་བ་
- L580: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.5.2.1.3.4 བཞི་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L636: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.5.2.2.4.2.3.3.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L647: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.6.2.1.2.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L680: duplicate decimal 2.4.6.2.1.1 (also at L643)
- L692: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.6.2.1.1.2.4.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L696: duplicate decimal 2.4.6.2.1.2 (also at L644)
- L697: duplicate decimal 2.4.6.2.1.2.1 (also at L645)
- L698: duplicate decimal 2.4.6.2.1.2.2 (also at L646)
- L699: duplicate decimal 2.4.6.2.1.2.3 (also at L647)
- L699: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.6.2.1.2.3 གསུམ་པ་ལུང་བཀར་བསྒྲུབ་པ་
- L700: duplicate decimal 2.4.6.2.1.2.3.1 (also at L648)
- L701: duplicate decimal 2.4.6.2.1.2.3.2 (also at L649)
- L712: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  2.4.6.2.1.2.5 ལྔ་པ་སྐབས་ཀྱི་དོན་བསྡུ་བ་
- L713: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 5)  ->  2.4.6.2.1.2.6 དྲུག་པ་ཐེག་པ་ཆེན་པོའི་ལུང་བཀར་བསྒྲུབ་པའི
- L716: duplicate decimal 2.4.6.2.1.3 (also at L650)
- L717: duplicate decimal 2.4.6.2.1.3.1 (also at L651)
- L718: duplicate decimal 2.4.6.2.1.3.2 (also at L652)
- L719: duplicate decimal 2.4.6.2.1.3.3 (also at L657)
- L744: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.6.3.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- L751: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 3, 4, 6)  ->  2.4.6.3.1.3.1.5 ལྔ་པ་རྩོད་པ་སྤང་བ་
- L752: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.6.3.1.3.1.6 དྲུག་པ་དོན་བསྡུ་བ་
- children of 2.3.2.2.3: numbered [1, 2, 3, 3], expected [1, 2, 3, 4]
- children of 2.4.6.2.1: numbered [1, 1, 2, 2, 3, 3], expected [1, 2, 3, 4, 5, 6]
- children of 2.4.6.2.1.2: numbered [1, 1, 2, 2, 3, 3, 4, 5, 6], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]
- children of 2.4.6.2.1.2.3: numbered [1, 1, 2, 2], expected [1, 2, 3, 4]
- children of 2.4.6.2.1.3: numbered [1, 1, 2, 2, 3, 3, 4], expected [1, 2, 3, 4, 5, 6, 7]

## Issues remaining after repair

- L187: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.1.2.2.3.2.3.4 བཞི་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L256: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 3, 4)  ->  2.4.2.3.1.1.3.6 དྲུག་པ་སྐབས་བསྡུ་བ་
- L267: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.2.3.2.1.1 དང་པོ་གཡོ་བ་མེད་པ་
- L279: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.2.5)
- L280: indent 18 spaces != expected 15 for depth 6 (2.4.2.3.2.3)
- L281: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.1)
- L282: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.2)
- L283: indent 21 spaces != expected 18 for depth 7 (2.4.2.3.2.3.3)
- L284: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.1)
- L285: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.2)
- L286: indent 24 spaces != expected 21 for depth 8 (2.4.2.3.2.3.3.3)
- L287: indent 24 spaces != expected 18 for depth 7 (2.4.2.3.2.3.4)
- L349: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.3.2.1.4.2.1.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- L367: indent 36 spaces != expected 33 for depth 12 (2.4.3.2.1.4.2.1.1.3.6.1)
- L368: indent 36 spaces != expected 33 for depth 12 (2.4.3.2.1.4.2.1.1.3.6.2)
- L369: indent 36 spaces != expected 33 for depth 12 (2.4.3.2.1.4.2.1.1.3.6.3)
- L382: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 3, 4)  ->  2.4.3.2.1.4.2.1.2.3.6 དྲུག་པ་སྐབས་བསྡུ་བ་
- L421: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  2.4.3.2.1.4.3.2.2.3.1.1 དང་པོ་ཕན་འདོགས་ཆེ་བ་
- L580: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.5.2.1.3.4 བཞི་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L636: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.5.2.2.4.2.3.3.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L647: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.6.2.1.2.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L692: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.4.6.2.2.1.2.4.3 གསུམ་པ་དེ་ལ་རྩོད་པ་སྤང་བ་
- L712: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  2.4.6.2.2.2.5 ལྔ་པ་སྐབས་ཀྱི་དོན་བསྡུ་བ་
- L744: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.6.3.1.2.2.3 གསུམ་པ་དོན་བསྡུ་བ་
- L751: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 3, 4, 6)  ->  2.4.6.3.1.3.1.5 ལྔ་པ་རྩོད་པ་སྤང་བ་
- L752: ordinal 6 (དྲུག་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.4.6.3.1.3.1.6 དྲུག་པ་དོན་བསྡུ་བ་
- children of 2.4.2.3.2.2: numbered [1, 2, 5], expected [1, 2, 3]
