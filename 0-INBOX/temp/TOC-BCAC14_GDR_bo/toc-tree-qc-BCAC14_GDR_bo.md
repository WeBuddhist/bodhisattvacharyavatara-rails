---
source: BCAC14_GDR_bo
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-06-26
model: gemini-flash-latest
repaired: true
issues_before: 93
issues_after: 40
---

# TOC tree QC report

## Issues found (before repair)

- L201: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.2.1.3.1.2.2)
- L201: duplicate decimal 1.3.2.2.2.2.1.2.1.3.1.2.2 (also at L199)
- L202: indent 36 spaces != expected 33 for depth 12 (1.3.2.2.2.2.1.2.1.3.1.3)
- L203: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.2.1.3.1.3.1)
- L204: indent 39 spaces != expected 33 for depth 12 (1.3.2.2.2.2.1.2.1.3.1.2)
- L204: duplicate decimal 1.3.2.2.2.2.1.2.1.3.1.2 (also at L192)
- L328: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.2.2.1.1.3.1.1.4)
- L368: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.1.2.3.1.3)
- L368: duplicate decimal 1.3.2.2.2.2.1.1.1.1.2.3.1.3 (also at L88)
- L411: Tibetan ordinal = 2 but decimal last segment = 3  ->  1.3.2.2.2.2.2.2.3 གཉིས་པ་ལེའུའི་མཚན་
- L480: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.3.2 གཉིས་པ་རྩོད་པ་སྤང་བ་
- L494: indent 51 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.2.1.2.4.1)
- L528: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.3.2.2.2.2.2.3.1.1.2.2 གཉིས་པ་འདོད་པའི་གེགས་བྱེད་པ་ལ་ཁྲོ་བ་དགག་
- L555: indent 39 spaces != expected 27 for depth 10 (1.3.2.2.2.2.2.3.2.2)
- L556: indent 42 spaces != expected 30 for depth 11 (1.3.2.2.2.2.2.3.2.2.1)
- L557: indent 45 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.3.2.2.1.1)
- L558: indent 45 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.3.2.2.1.2)
- L559: indent 42 spaces != expected 30 for depth 11 (1.3.2.2.2.2.2.3.2.2.2)
- L560: indent 45 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.3.2.2.2.1)
- L561: indent 45 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.3.2.2.2.2)
- L562: indent 42 spaces != expected 30 for depth 11 (1.3.2.2.2.2.2.3.2.2.3)
- L563: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.4.3.1)
- L564: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1 (also at L435)
- L565: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1.1 (also at L436)
- L566: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1.2 (also at L437)
- L567: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1.3 (also at L438)
- L568: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2 (also at L445)
- L569: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2.1 (also at L446)
- L570: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2.2 (also at L463)
- L572: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3 (also at L464)
- L573: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.1 (also at L465)
- L574: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.1.1 (also at L466)
- L575: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.1.2 (also at L467)
- L578: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.1.3 (also at L468)
- L582: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.2 (also at L469)
- L583: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.3.2 (also at L518)
- L607: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.1.3 གསུམ་པ་ལེའུའི་མཚན་
- L624: indent 48 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2)
- L625: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.1)
- L626: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.2)
- L627: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3)
- L628: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.4)
- L629: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3 (also at L627)
- L632: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2 (also at L624)
- L633: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.1 (also at L625)
- L634: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.2 (also at L626)
- L635: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3 (also at L627)
- L636: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.4 (also at L628)
- L652: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.4.1)
- L685: indent 54 spaces != expected 51 for depth 18 (1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2.3)
- L686: indent 51 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2)
- L687: indent 54 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2.1)
- L688: indent 54 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2.2)
- L689: indent 54 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2.3)
- L690: indent 54 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2.4)
- L694: indent 54 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.1.1.2.2.2.2.2.5)
- L695: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2.3 (also at L685)
- L715: duplicate decimal 1.3.2.2.2.2.2.3.2.2 (also at L555)
- L736: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2 (also at L484)
- L737: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2.1 (also at L485)
- L739: indent 54 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1)
- L739: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1 (also at L435)
- L740: indent 54 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2)
- L740: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2 (also at L445)
- L741: indent 54 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3)
- L741: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3 (also at L464)
- L743: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2.2 (also at L486)
- L850: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.1.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- L857: duplicate decimal 1.3.2.2.2.2.2.3.1.1.2.2.2.1.1.4.2 (also at L545)
- L911: duplicate decimal 1.3.2.2.2.2.2.3.3.1.2.1.2.2.2 (also at L744)
- L1017: unparseable tree line: * 1.3.2.2.2.2.2.3.4.
- children of 1.3.2.2.2.2.1.1.1.1.2.3.1: numbered [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], expected [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- children of 1.3.2.2.2.2.1.2.1.3.1: numbered [1, 2, 2, 3], expected [1, 2, 3, 4]
- children of 1.3.2.2.2.2.1.2.1.3.1.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1: numbered [1, 1, 1, 2, 2, 2, 3, 3, 3], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.1: numbered [1, 1, 2, 2, 3, 3, 4, 5], expected [1, 2, 3, 4, 5, 6, 7, 8]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.2: numbered [1, 1, 2, 2, 3], expected [1, 2, 3, 4, 5]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3: numbered [1, 1, 2, 2, 3], expected [1, 2, 3, 4, 5]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.1: numbered [1, 1, 2, 2, 3, 3], expected [1, 2, 3, 4, 5, 6]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2: numbered [1, 1, 2, 2, 3, 4], expected [1, 2, 3, 4, 5, 6]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2.4: numbered [2], expected [1]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.3: numbered [1, 2, 2, 3], expected [1, 2, 3, 4]
- children of 1.3.2.2.2.2.2.3.1.1.2.2.2.1.1.4: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2: numbered [1, 1, 2, 2, 3, 3, 3, 4, 4], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.3.3.4: numbered [2, 3, 4], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2: numbered [1, 3, 3], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.1.1.2.2.2.2: numbered [2], expected [1]
- children of 1.3.2.2.2.2.2.3.3.1.2.1.2.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.3.1.3.2.2.1.1.1: numbered [1, 3, 4, 5], expected [1, 2, 3, 4]
- children of 1.3.2.2.2.2.2.3.3.1.3.2.3.2: numbered [1, 3], expected [1, 2]

## Issues remaining after repair

- L33: indent 30 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.4.2.1.4.2)
- L56: Tibetan ordinal = 4 but decimal last segment = 2  ->  1.3.2.2.2.2.1.2.1.1.4.2 བཞི་པ་མཇུག་བསྡུས་ཏེ་བསྔགས་པ་
- L123: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.4.2 (also at L33)
- L165: duplicate decimal 1.3.2.2.2.2.1.2.1.1.4.2 (also at L56)
- L202: indent 36 spaces != expected 33 for depth 12 (1.3.2.2.2.2.1.2.1.3.1.3)
- L203: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.2.1.3.1.3.1)
- L204: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.2.1.3.1.3.2)
- L328: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.2.2.1.1.3.1.1.4)
- L411: Tibetan ordinal = 2 but decimal last segment = 3  ->  1.3.2.2.2.2.2.2.3 གཉིས་པ་ལེའུའི་མཚན་
- L480: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.3.2 གཉིས་པ་རྩོད་པ་སྤང་བ་
- L494: indent 51 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.2.1.2.4.1)
- L528: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.3.2.2.2.2.2.3.1.1.2.2 གཉིས་པ་འདོད་པའི་གེགས་བྱེད་པ་ལ་ཁྲོ་བ་དགག་
- L607: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.1.3 གསུམ་པ་ལེའུའི་མཚན་
- L624: indent 48 spaces != expected 45 for depth 16 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2)
- L625: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.1)
- L626: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.2)
- L627: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3)
- L628: indent 51 spaces != expected 48 for depth 17 (1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.4)
- L629: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3 (also at L627)
- L632: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2 (also at L624)
- L633: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.1 (also at L625)
- L634: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.2 (also at L626)
- L635: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.3 (also at L627)
- L636: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2.4 (also at L628)
- L652: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.4.1)
- L685: indent 54 spaces != expected 51 for depth 18 (1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2.3)
- L695: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2.3 (also at L685)
- L850: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.1.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- L857: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.3.1.2.1.2.2.2)
- L857: duplicate decimal 1.3.2.2.2.2.2.3.3.1.2.1.2.2.2 (also at L744)
- children of 1.3.2.2.2.1.1.2.1.1: numbered [1, 3], expected [1, 2]
- children of 1.3.2.2.2.2.1.1.1.4.2.1.4: numbered [1, 2, 2, 3, 4], expected [1, 2, 3, 4, 5]
- children of 1.3.2.2.2.2.1.2.1.1.4: numbered [1, 2, 2, 3, 4], expected [1, 2, 3, 4, 5]
- children of 1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.2.4: numbered [2], expected [1]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.1.2.2: numbered [1, 1, 2, 2, 3, 3, 3, 4, 4], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]
- children of 1.3.2.2.2.2.2.3.2.1.2.1.2.3.3.4: numbered [2, 3, 4], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.2.1.2.2.2.2: numbered [1, 2, 3, 3], expected [1, 2, 3, 4]
- children of 1.3.2.2.2.2.2.3.3.1.2.1.2.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.3.1.3.2.2.1.1.1: numbered [1, 3, 4, 5], expected [1, 2, 3, 4]
