---
source: Commentary_Tibetan
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-06-24
model: gemini-flash-latest
repaired: true
issues_before: 109
issues_after: 25
---

# TOC tree QC report

## Issues found (before repair)

- L8: Tibetan ordinal = 3 but decimal last segment = 4  ->  1.1.4 གསུམ་པ་གྲུབ་པའི་དོན་
- L28: Tibetan ordinal = 4 but decimal last segment = 5  ->  1.1.5 བཞི་པ་སྒྲུབ་པར་རིགས་པ་
- L62: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 1)  ->  2.2.1.4 བཞི་པ་དགོས་པ་
- L78: Tibetan ordinal = 4 but decimal last segment = 5  ->  2.2.3.1.3.5 བཞི་པ་གཞུང་གིས་བསྟན་ཚུལ་
- L99: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.1.1.3.3.1.4.3 གཉིས་པ་ཐུན་མོང་དུ་བླང་ཚུལ་
- L167: indent 33 spaces != expected 30 for depth 11 (2.2.3.2.2.1.2.2.1.1.3)
- L172: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2, 4)  ->  2.2.3.2.2.1.2.2.1.3.1.1 དང་པོ་རྒྱུ་
- L174: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 1, 2)  ->  2.2.3.2.2.1.2.2.1.3.1.3 གསུམ་པ་ངོ་བོ་
- L176: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 2, 3, 4)  ->  2.2.3.2.2.1.2.2.1.3.1.5 ལྔ་པ་ཕན་ཡོན་
- L178: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.1.2.2.1.3.3 གཉིས་པ་གཞུང་དོན་
- L248: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  2.2.3.2.2.2.1.1 དང་པོ་གྲངས་ངེས་
- L261: Tibetan ordinal = 3 but decimal last segment = 10  ->  2.2.3.2.2.2.1.10 གསུམ་པ་ཕན་ཚུན་རྣམ་པར་ངེས་པ་
- L398: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.2.3 (also at L371)
- L405: indent 24 spaces != expected 27 for depth 10 (2.2.3.2.2.2.2.2.3.2)
- L406: indent 24 spaces != expected 27 for depth 10 (2.2.3.2.2.2.2.2.3.3)
- L408: duplicate decimal 2.2.3.2.2.2.2.2.3.2 (also at L405)
- L409: duplicate decimal 2.2.3.2.2.2.2.2.3.3 (also at L406)
- L410: indent 24 spaces != expected 27 for depth 10 (2.2.3.2.2.2.2.2.3.4)
- L411: indent 24 spaces != expected 27 for depth 10 (2.2.3.2.2.2.2.2.3.5)
- L412: indent 27 spaces != expected 30 for depth 11 (2.2.3.2.2.2.2.2.3.5.1)
- L413: duplicate decimal 2.2.3.2.2.2.2.2.5.1.1 (also at L275)
- L414: duplicate decimal 2.2.3.2.2.2.2.2.5.1.2 (also at L276)
- L415: duplicate decimal 2.2.3.2.2.2.2.2.5.1.3 (also at L312)
- L416: indent 27 spaces != expected 30 for depth 11 (2.2.3.2.2.2.2.2.3.5.2)
- L416: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.2.3.2.2.2.2.2.3.5.2 གཉིས་པ་སྒོམ་ཚུལ་
- L417: duplicate decimal 2.2.3.2.2.2.2.2.5.2.1 (also at L314)
- L418: duplicate decimal 2.2.3.2.2.2.2.2.5.2.1.1 (also at L315)
- L419: duplicate decimal 2.2.3.2.2.2.2.2.5.2.1.2 (also at L316)
- L420: duplicate decimal 2.2.3.2.2.2.2.2.5.2.1.3 (also at L336)
- L421: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2 (also at L337)
- L422: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.1 (also at L338)
- L423: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.2 (also at L339)
- L424: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.2.1 (also at L340)
- L429: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.1.1.2)
- L430: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.1.1.3)
- L431: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.2.1.4)
- L431: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.1.4 (also at L360)
- L432: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.2.1.5)
- L433: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.2.1.6)
- L446: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  2.2.3.2.2.2.2.2.5.2.2.3.2.2.1.2.2 གཉིས་པ་རྩོད་པ་སྤང་པ་
- L467: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.2.2 (also at L341)
- L468: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.1 (also at L354)
- L469: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2 (also at L355)
- L470: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.1 (also at L356)
- L471: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.2 (also at L361)
- L472: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.3 (also at L378)
- L473: duplicate decimal 2.2.3.2.2.2.2.2.5.2.2.3.2.2.4 (also at L395)
- L487: Tibetan ordinal = 2 but decimal last segment = 4  ->  2.2.3.2.2.2.2.2.5.2.2.2.4 གཉིས་པ་ཡིད་དུ་འོང་བའི་གེགས་ལ་བསྒོམ་པ་
- L499: Tibetan ordinal = 3 but decimal last segment = 5  ->  2.2.3.2.2.2.2.2.5.2.2.2.5 གསུམ་པ་གནོད་བྱེད་བཟོད་པའི་གྲོགས་སུ་བསྟེན
- L517: Tibetan ordinal = 3 but decimal last segment = 4  ->  2.2.3.2.2.2.2.2.5.2.2.2.5.6.4 གསུམ་པ་ཕན་ཡོན་
- L518: indent 27 spaces != expected 30 for depth 11 (2.2.3.2.2.2.2.2.3.5.3)
- L524: Tibetan ordinal = 2 but decimal last segment = 5  ->  2.2.3.2.2.2.2.4.5 གཉིས་པ་གཞུང་དོན་
- L547: Tibetan ordinal = 3 but decimal last segment = 1  ->  2.2.3.2.2.2.2.4.5.3.1 གསུམ་པགཉེན་པོ་
- L596: Tibetan ordinal = 2 but decimal last segment = 5  ->  2.2.3.2.2.2.2.5.5 གཉིས་པ་གཞུང་དོན་
- L603: Tibetan ordinal = 2 but decimal last segment = 1  ->  2.2.3.2.2.2.2.5.5.2.2.2.1 གཉིས་པ་བྱིས་པ་སྤང་པ་ལ་བཞི་ལས
- L604: Tibetan ordinal = 1 but decimal last segment = 2  ->  2.2.3.2.2.2.2.5.5.2.2.2.2 དང་པོ་ལ་ལྔ་ལས
- L605: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.5.5.2.2.2.3 གཉིས་པ་རྣམ་རྟོག་སྤང་ཚུལ་གཉིས་ལས
- L619: indent 48 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.2.5.2.2.3.2.1.2.3)
- L619: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.2.5.2.2.3.2.1.2.3 གཉིས་པ་གཞན་ལའང་དཔགས་ཏེ་ཆགས་པ་སྤང་པ་
- L628: indent 48 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2)
- L629: indent 51 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.1)
- L630: indent 51 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.2)
- L631: indent 51 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.3)
- L632: indent 51 spaces != expected 45 for depth 16 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.4)
- L633: indent 54 spaces != expected 48 for depth 17 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.4.1)
- L634: indent 54 spaces != expected 48 for depth 17 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.4.2)
- L635: indent 54 spaces != expected 48 for depth 17 (2.2.3.2.2.2.2.5.5.2.2.2.3.2.2.4.3)
- L636: indent 42 spaces != expected 36 for depth 13 (2.2.3.2.2.2.2.5.5.2.2.2.4)
- L636: Tibetan ordinal = 2 but decimal last segment = 4  ->  2.2.3.2.2.2.2.5.5.2.2.2.4 གཉིས་པ་དབེན་པ་ལ་དགའ་བ་བསྐྱེད་ཚུལ་ལ
- L637: indent 45 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.5.5.2.2.2.4.1)
- L638: indent 45 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.5.5.2.2.2.4.2)
- L639: indent 48 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.5.5.2.2.2.4.2.1)
- L640: indent 48 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.5.5.2.2.2.4.2.2)
- L685: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.5.5.3.2.1.2.4.1.2.3 གཉིས་པ་འགྲན་སེམས་བསྒོམ་ཚུལ་
- L686: Tibetan ordinal = 3 but decimal last segment = 4  ->  2.2.3.2.2.2.2.5.5.3.2.1.2.4.1.2.4 གསུམ་པ་ང་རྒྱལ་བསྒོམ་ཚུལ་
- L722: Tibetan ordinal = 2 but decimal last segment = 6  ->  2.2.3.2.2.2.2.6.3.2.1.1.6 གཉིས་པ་བསྒོམ་ཚུལ་
- L755: ordinal 4 (བཞི་པ) not attested for this title in candidates/enumerations (source attaches: 2, 3, 6)  ->  2.2.3.2.2.2.2.6.3.2.3.2.4 བཞི་པ་དབྱེ་བ་
- L758: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.2.3.2.2.2.2.6.3.2.3.2.5 ལྔ་པ་སྒྲུབ་ཚུལ་
- L759: Tibetan ordinal = 4 but decimal last segment = 6  ->  2.2.3.2.2.2.2.6.6 བཞི་པ་ཕན་ཡོན་
- L760: Tibetan ordinal = 2 but decimal last segment = 7  ->  2.2.3.2.2.2.2.6.7 གཉིས་པ་གཞུང་དོན་
- L790: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.6.7.2.1.1.3.2.2.3 གཉིས་པ་དོན་སེམས་གཉིས་མིན་དགག་པ་
- L791: Tibetan ordinal = 3 but decimal last segment = 4  ->  2.2.3.2.2.2.2.6.7.2.1.1.3.2.2.4 གསུམ་པ་དོན་བསྡུ་
- L792: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.6.7.2.1.1.3.2.3 གཉིས་པ་འཁྲུལ་གཞི་མེད་ན་འཁོར་འདས་མི་འབྱུང
- L818: Tibetan ordinal = 2 but decimal last segment = 1  ->  2.2.3.2.2.2.2.6.7.2.2.1 གཉིས་པ་བདག་མེད་གཉིས་ལ་འཇུག་ཚུལ་
- L854: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.7.2.2.3.2.1.1)
- L855: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.7.2.2.3.2.1.2)
- L856: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.5.2.2.3.2.1.3)
- L857: indent 48 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.6.5.2.2.3.2.2)
- L858: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.5.2.2.3.2.2.1)
- L859: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.5.2.2.3.2.2.2)
- L860: indent 51 spaces != expected 42 for depth 15 (2.2.3.2.2.2.2.6.5.2.2.3.2.2.3)
- L861: indent 48 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.6.5.2.2.3.2.3)
- L862: indent 48 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.6.5.2.2.3.2.4)
- L863: indent 48 spaces != expected 39 for depth 14 (2.2.3.2.2.2.2.6.5.2.2.3.2.5)
- children of 2.2.3.2.2.2.2.2.5.1: numbered [1, 1, 2, 2, 3, 3], expected [1, 2, 3, 4, 5, 6]
- children of 2.2.3.2.2.2.2.2.5.2: numbered [1, 1, 2, 2], expected [1, 2, 3, 4]
- children of 2.2.3.2.2.2.2.2.5.2.1: numbered [1, 1, 2, 2, 3, 3], expected [1, 2, 3, 4, 5, 6]
- children of 2.2.3.2.2.2.2.2.5.2.2: numbered [1, 1, 2, 2, 3], expected [1, 2, 3, 4, 5]
- children of 2.2.3.2.2.2.2.2.5.2.2.2: numbered [1, 1, 2, 2, 3, 4, 5], expected [1, 2, 3, 4, 5, 6, 7]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2: numbered [1, 1, 2, 2, 3], expected [1, 2, 3, 4, 5]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2.2: numbered [1, 1, 2, 2, 3, 3, 4, 4], expected [1, 2, 3, 4, 5, 6, 7, 8]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2.2.1: numbered [1, 2, 3, 4, 4, 5, 6], expected [1, 2, 3, 4, 5, 6, 7]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2.2.2: numbered [1, 2, 3, 3, 4, 5, 6, 7], expected [1, 2, 3, 4, 5, 6, 7, 8]
- children of 2.2.3.2.2.2.2.2.3: numbered [1, 2, 2, 3, 3, 4, 5], expected [1, 2, 3, 4, 5, 6, 7]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2.1.1: numbered [2, 3], expected [1, 2]
- children of 2.2.3.2.2.2.2.2.5.2.2.3.2.1.2: numbered [3], expected [1]
- children of 2.2.3.2.2.2.2.6: numbered [1, 2, 3, 6, 7], expected [1, 2, 3, 4, 5]
- children of 2.2.3.2.2.2.2.6.5.2.2.3.2.1: numbered [3], expected [1]
- children of 2.2.3.2.2.2.2.6.5.2.2.3.2: numbered [2, 3, 4, 5], expected [1, 2, 3, 4]

## Issues remaining after repair

- L8: Tibetan ordinal = 3 but decimal last segment = 4  ->  1.1.4 གསུམ་པ་གྲུབ་པའི་དོན་
- L28: Tibetan ordinal = 4 but decimal last segment = 5  ->  1.1.5 བཞི་པ་སྒྲུབ་པར་རིགས་པ་
- L62: Tibetan ordinal = 1 but decimal last segment = 4  ->  2.2.1.4 དང་པོ་དགོས་པ་
- L78: Tibetan ordinal = 4 but decimal last segment = 5  ->  2.2.3.1.3.5 བཞི་པ་གཞུང་གིས་བསྟན་ཚུལ་
- L99: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.1.1.3.3.1.4.3 གཉིས་པ་ཐུན་མོང་དུ་བླང་ཚུལ་
- L157: indent 33 spaces != expected 30 for depth 11 (2.2.3.2.2.1.2.2.1.1.3)
- L162: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2, 4)  ->  2.2.3.2.2.1.2.2.1.3.1.1 དང་པོ་རྒྱུ་
- L164: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 1, 2)  ->  2.2.3.2.2.1.2.2.1.3.1.3 གསུམ་པ་ངོ་བོ་
- L166: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 2, 3, 4)  ->  2.2.3.2.2.1.2.2.1.3.1.5 ལྔ་པ་ཕན་ཡོན་
- L168: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.1.2.2.1.3.3 གཉིས་པ་གཞུང་དོན་
- L238: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  2.2.3.2.2.2.1.1 དང་པོ་གྲངས་ངེས་
- L251: Tibetan ordinal = 3 but decimal last segment = 10  ->  2.2.3.2.2.2.1.10 གསུམ་པ་ཕན་ཚུན་རྣམ་པར་ངེས་པ་
- L263: Tibetan ordinal = 2 but decimal last segment = 5  ->  2.2.3.2.2.2.2.2.5 གཉིས་པ་གཞུང་དོན་
- L404: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4, 5)  ->  2.2.3.2.2.2.2.3.5.2 གཉིས་པ་སྒོམ་ཚུལ་
- L434: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  2.2.3.2.2.2.2.3.5.2.2.2.1.1.1.2.2 གཉིས་པ་རྩོད་པ་སྤང་པ་
- L475: Tibetan ordinal = 2 but decimal last segment = 4  ->  2.2.3.2.2.2.2.3.5.2.2.2.4 གཉིས་པ་ཡིད་དུ་འོང་བའི་གེགས་ལ་བསྒོམ་པ་
- L487: Tibetan ordinal = 3 but decimal last segment = 5  ->  2.2.3.2.2.2.2.3.5.2.2.2.5 གསུམ་པ་གནོད་བྱེད་བཟོད་པའི་གྲོགས་སུ་བསྟེན
- L505: Tibetan ordinal = 3 but decimal last segment = 4  ->  2.2.3.2.2.2.2.3.5.2.2.2.5.6.4 གསུམ་པ་ཕན་ཡོན་
- L516: Tibetan ordinal = 2 but decimal last segment = 5  ->  2.2.3.2.2.2.2.5.5 གཉིས་པ་གཞུང་དོན་
- L556: ordinal 3 (གསུམ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.2.3.2.2.2.2.5.5.2.2.2.1.2.1.3 གསུམ་པ་གཞན་ལའང་དཔགས་ཏེ་ཆགས་པ་སྤང་པ་
- L597: Tibetan ordinal = 3 but decimal last segment = 2  ->  2.2.3.2.2.2.2.5.5.3.2.1.1.2 གསུམ་པ་གདམས་པ་
- L701: ordinal 5 (ལྔ་པ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  2.2.3.2.2.2.2.6.3.2.3.2.5 ལྔ་པ་སྒྲུབ་ཚུལ་
- L703: Tibetan ordinal = 2 but decimal last segment = 5  ->  2.2.3.2.2.2.2.6.5 གཉིས་པ་གཞུང་དོན་
- L737: Tibetan ordinal = 2 but decimal last segment = 3  ->  2.2.3.2.2.2.2.6.5.2.1.1.1.3.2.3 གཉིས་པ་འཁྲུལ་གཞི་མེད་ན་འཁོར་འདས་མི་འབྱུང
- children of 2.2.3.2.2.2.2: numbered [1, 2, 3, 5, 6], expected [1, 2, 3, 4, 5]
