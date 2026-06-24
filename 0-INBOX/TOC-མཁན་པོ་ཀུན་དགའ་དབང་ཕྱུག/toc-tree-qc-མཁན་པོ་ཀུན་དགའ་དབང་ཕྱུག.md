---
source: མཁན་པོ་ཀུན་དགའ་དབང་ཕྱུག
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-06-23
model: gemini-flash-latest
repaired: true
issues_before: 56
issues_after: 10
---

# TOC tree QC report

## Issues found (before repair)

- L16: Tibetan ordinal = 2 but decimal last segment = 4  ->  1.1.1.2.2.4 གཉིས་པ་མཚན་བཏགས་པའི་དགོས་པ་
- L154: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.2.2.2.3.1.2.2 གཉིས་པ་གཉེན་པོ་ཀུན་ཏུ་སྤྱོད་པའི་སྟོབས་ཀྱ
- L179: duplicate decimal 1.2.2.1.1.1.2.2.2 (also at L44)
- L182: indent 27 spaces != expected 24 for depth 9 (1.2.2.1.1.1.2.2.3)
- L183: indent 21 spaces != expected 18 for depth 7 (1.2.2.1.1.1.3)
- L184: indent 24 spaces != expected 18 for depth 7 (1.2.2.1.1.1.1)
- L184: duplicate decimal 1.2.2.1.1.1.1 (also at L28)
- L185: indent 24 spaces != expected 18 for depth 7 (1.2.2.1.1.1.2)
- L185: duplicate decimal 1.2.2.1.1.1.2 (also at L31)
- L186: indent 27 spaces != expected 18 for depth 7 (1.2.2.1.1.1.1)
- L186: duplicate decimal 1.2.2.1.1.1.1 (also at L28)
- L187: indent 30 spaces != expected 18 for depth 7 (1.2.2.1.1.1.1)
- L187: duplicate decimal 1.2.2.1.1.1.1 (also at L28)
- L188: indent 30 spaces != expected 18 for depth 7 (1.2.2.1.1.1.2)
- L188: duplicate decimal 1.2.2.1.1.1.2 (also at L31)
- L189: indent 33 spaces != expected 21 for depth 8 (1.2.2.1.1.1.2.1)
- L189: duplicate decimal 1.2.2.1.1.1.2.1 (also at L32)
- L190: indent 33 spaces != expected 21 for depth 8 (1.2.2.1.1.1.2.2)
- L190: duplicate decimal 1.2.2.1.1.1.2.2 (also at L42)
- L191: indent 36 spaces != expected 24 for depth 9 (1.2.2.1.1.1.2.2.1)
- L191: duplicate decimal 1.2.2.1.1.1.2.2.1 (also at L43)
- L192: indent 36 spaces != expected 0 for depth 1 (2)
- L193: indent 36 spaces != expected 0 for depth 1 (3)
- L194: indent 30 spaces != expected 9 for depth 4 (1.2.1.3)
- L194: duplicate decimal 1.2.1.3 (also at L22)
- L195: indent 30 spaces != expected 9 for depth 4 (1.2.1.4)
- L195: duplicate decimal 1.2.1.4 (also at L23)
- L196: indent 27 spaces != expected 18 for depth 7 (1.2.2.1.1.1.2)
- L196: duplicate decimal 1.2.2.1.1.1.2 (also at L31)
- L197: indent 30 spaces != expected 21 for depth 8 (1.2.2.1.1.1.2.1)
- L197: duplicate decimal 1.2.2.1.1.1.2.1 (also at L32)
- L198: indent 30 spaces != expected 21 for depth 8 (1.2.2.1.1.1.2.2)
- L198: duplicate decimal 1.2.2.1.1.1.2.2 (also at L42)
- L242: indent 36 spaces != expected 0 for depth 1 (2)
- L242: duplicate decimal 2 (also at L192)
- L243: indent 36 spaces != expected 0 for depth 1 (3)
- L243: duplicate decimal 3 (also at L193)
- L248: indent 36 spaces != expected 0 for depth 1 (2)
- L248: duplicate decimal 2 (also at L192)
- L257: Tibetan ordinal = 2 but decimal last segment = 1  ->  1.2.2.3.3.1.2.1.1.1.1 གཉིས་པ་དབྱེ་བ་
- L258: Tibetan ordinal = 3 but decimal last segment = 2  ->  1.2.2.3.3.1.2.1.1.1.2 གསུམ་པ་གྲངས་ངེས་
- L259: Tibetan ordinal = 4 but decimal last segment = 3  ->  1.2.2.3.3.1.2.1.1.1.3 བཞི་པ་དབྱེ་བའི་ངོ་བོ་
- L260: Tibetan ordinal = 5 but decimal last segment = 4  ->  1.2.2.3.3.1.2.1.1.1.4 ལྔ་པ་སྒྲ་དོན་
- L261: Tibetan ordinal = 6 but decimal last segment = 5  ->  1.2.2.3.3.1.2.1.1.1.5 དྲུག་པ་རྟོགས་བྱེད་ཀྱི་བློ་
- L262: Tibetan ordinal = 7 but decimal last segment = 6  ->  1.2.2.3.3.1.2.1.1.1.6 བདུན་པ་རྟོགས་ཚུལ་གྱི་དབང་དུ་བྱས་ན་
- L263: Tibetan ordinal = 8 but decimal last segment = 7  ->  1.2.2.3.3.1.2.1.1.1.7 བརྒྱད་པ་བདེན་གཉིས་སོ་སོར་རྟོགས་པའི་གང་ཟག
- L271: indent 33 spaces != expected 0 for depth 1 (2)
- L271: duplicate decimal 2 (also at L192)
- L314: indent 33 spaces != expected 0 for depth 1 (2)
- L314: duplicate decimal 2 (also at L192)
- L330: Tibetan ordinal = 2 but decimal last segment = 1  ->  1.2.2.4.1.2.1.1.2.1 གཉིས་པ་དམིགས་བསལ་དུད་འགྲོ་དང་ཡི་དྭགས་སོག
- children of (root): numbered [1, 2, 2, 2, 2, 2, 3, 3], expected [1, 2, 3, 4, 5, 6, 7, 8]
- children of 1.2.1: numbered [1, 2, 3, 3, 4, 4], expected [1, 2, 3, 4, 5, 6]
- children of 1.2.2.1.1.1: numbered [1, 1, 1, 1, 2, 2, 2, 2, 3], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]
- children of 1.2.2.1.1.1.2: numbered [1, 1, 1, 2, 2, 2, 3], expected [1, 2, 3, 4, 5, 6, 7]
- children of 1.2.2.1.1.1.2.2: numbered [1, 1, 2, 2, 3], expected [1, 2, 3, 4, 5]

## Issues remaining after repair

- L16: Tibetan ordinal = 2 but decimal last segment = 4  ->  1.1.1.2.2.4 གཉིས་པ་མཚན་བཏགས་པའི་དགོས་པ་
- L257: Tibetan ordinal = 2 but decimal last segment = 1  ->  1.2.2.3.3.1.2.1.1.1.1 གཉིས་པ་དབྱེ་བ་
- L258: Tibetan ordinal = 3 but decimal last segment = 2  ->  1.2.2.3.3.1.2.1.1.1.2 གསུམ་པ་གྲངས་ངེས་
- L259: Tibetan ordinal = 4 but decimal last segment = 3  ->  1.2.2.3.3.1.2.1.1.1.3 བཞི་པ་དབྱེ་བའི་ངོ་བོ་
- L260: Tibetan ordinal = 5 but decimal last segment = 4  ->  1.2.2.3.3.1.2.1.1.1.4 ལྔ་པ་སྒྲ་དོན་
- L261: Tibetan ordinal = 6 but decimal last segment = 5  ->  1.2.2.3.3.1.2.1.1.1.5 དྲུག་པ་རྟོགས་བྱེད་ཀྱི་བློ་
- L262: Tibetan ordinal = 7 but decimal last segment = 6  ->  1.2.2.3.3.1.2.1.1.1.6 བདུན་པ་རྟོགས་ཚུལ་གྱི་དབང་དུ་བྱས་ན་
- L263: Tibetan ordinal = 8 but decimal last segment = 7  ->  1.2.2.3.3.1.2.1.1.1.7 བརྒྱད་པ་བདེན་གཉིས་སོ་སོར་རྟོགས་པའི་གང་ཟག
- L330: Tibetan ordinal = 2 but decimal last segment = 1  ->  1.2.2.4.1.2.1.1.2.1 གཉིས་པ་དམིགས་བསལ་དུད་འགྲོ་དང་ཡི་དྭགས་སོག
- children of 1.2.2.2.2.1.2.3: numbered [2, 3], expected [1, 2]
