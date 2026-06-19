import json, re

data = json.load(open('batch_01.json', encoding='utf-8'))
by_idx = {d['tsv_idx']: d for d in data}

# decisions: tsv_idx -> split point marker (the substring right BEFORE which to insert \n\n)
# We specify the exact substring that starts the second block.
splits = {}

# [0] 592 syll62 - single clause "...mi zad" - no clean internal break (subject...verb chain). keep
# [1] 593 syll43 - keep, single sentence
# [2] 619 syll52 - keep (list continues with dang in next block presumably)
# [3] 622 syll74 - two images joined by dang/: "...dri ma thams cad gzhom pa dang/" - could split at "nam mkha' nas mar..." simile clause. Actually whole thing is one continuous simile sentence. keep
# [4] 623 syll44 - keep, single sentence
# [5] 630 syll47 - keep
# [6] 659 syll54 - keep (single descriptive clause then restated)
#   Actually "zhes pa..." restates - could split before "zhes pa sangs rgyas..." Let's check: 
#   text: "...byug par bgyi zhes pa sangs rgyas dang byang chub sems dpa'..." This explains what was just stated (verse gloss -> prose explanation). Good split candidate.
splits[659] = "ཞེས་པ་སངས་རྒྱས་"
# [7] 660 syll41 - keep
# [8] 664 syll51 - keep (one long list, single sentence, list continues into next block)
# [9] 666 syll94 - long: two parts - flower offering action + aspiration (smon lam). Split before "ces de lta bu'i me tog phul ba'i bsod nams kyis"
splits[666] = "ཞེས་དེ་ལྟ་བུའི་མེ་ཏོག་ཕུལ་བའི་བསོད་ནམས་ཀྱིས་"
# [10] 670 syll59 - keep, single sentence
# [11] 676 syll42 - keep
# [12] 689 syll46 - keep
# [13] 694 syll81 - long, describes palace+goddesses+praise, one continuous descriptive clause modifying "rang bzhin can" at the end (continues to next block). Hard to cut cleanly mid-description. Try split at "lha'i bu mo mdzes ma yid du 'ong ba de dag rnams kyis" (subject shift from palace to goddesses)
splits[694] = "ལྷའི་བུ་མོ་མཛེས་མ་ཡིད་དུ་འོང་བ་དེ་དག་རྣམས་ཀྱིས་"
# [14] 696 syll43 - keep
# [15] 697 syll67 - has "zhes" reason clause then resumes offering. "blos dpag par mi nus pas na" gives reason for "blos dpag pa las mtha' yas..." Try split before "blos dpag pa las mtha' yas shing"
splits[697] = "བློས་དཔག་པ་ལས་མཐའ་ཡས་ཤིང་"
# [16] 698 syll42 - keep
# [17] 707 syll52 - keep
# [18] 715 syll46 - keep
# [19] 728 syll41 - keep
# [20] 730 syll45 - keep (single sentence with comparison)
# [21] 735 syll62 - long: aspiration content + label "...ni smon lam stobs kyi mchod pa ste" Split before "ces bya ba ni smon lam"
splits[735] = "ཅེས་བྱ་བ་ནི་སྨོན་ལམ་སྟོབས་ཀྱི་མཆོད་པ་སྟེ"
# [22] 753 syll43 - keep
# [23] 774 syll41 - keep
# [24] 776 syll48 - keep (single causal clause)
# [25] 790 syll44 - keep
# [26] 793 syll42 - keep
# [27] 800 syll41 - keep
# [28] 811 syll45 - keep
# [29] 827 syll57 - keep (list continues to next block with "tshangs pa dang dbang phyug dang")
# [30] 837 syll60 - keep (single long conditional clause, continues with zhing)
# [31] 849 syll41 - keep
# [32] 854 syll47 - keep (single gloss sentence)
# [33] 860 syll98 - LONG, two ideas: (1) describing rejoicing in others' sins as equally faulty (2) restating that as fault now seen. Split before "de lta bu'i nyes pa dang nongs pa'am 'khrul ba mi dge ba'i las de dag thams cad ni nyes pa yin pa"
splits[860] = "དེ་ལྟ་བུའི་ཉེས་པ་དང་ནོངས་པའམ་འཁྲུལ་བ་མི་དགེ་བའི་ལས་དེ་དག་ཐམས་ཅད་ནི་ཉེས་པ་ཡིན་པ་"
# [34] 863 syll58 - keep (single confession sentence, ends with quote marker zhes dang)
# [35] 880 syll46 - keep
# [36] 884 syll67 - long: self-description + quoted speech "...'gyur du mchi zhes bya ba gus tshig gi sgo nas nga shi ba'i nyen kha 'dug ces" Split before "zhes bya ba gus tshig"
splits[884] = "ཞེས་བྱ་བ་གུས་ཚིག་གི་སྒོ་ནས་"
# [37] 886 syll75 - long quoted supplication, single continuous quote - "ji ltar na ngas...gsol ba btab pa'o" all one quoted sentence. keep whole (it's a single quotation)
# [38] 891 syll54 - keep (single statement about death's inevitability + epithet, continues into next block "dgra 'dul ba")
# [39] 899 syll48 - keep
# [40] 904 syll46 - keep (list continues)
# [41] 911 syll54 - keep (single summary statement)
# [42] 927 syll46 - keep (list of examples, single sentence)
# [43] 929 syll42 - keep
# [44] 931 syll61 - long: two parts - (1) list of sins (2) statement they exist as latent imprints in mind. Split before "rang nyid kyi sems kyi mdun na ste"
splits[931] = "རང་ཉིད་ཀ�ྱི་སེམས་ཀྱི་མདུན་ན་སྟེ"
# need exact substring check - will verify and fix below
# [45] 934 syll49 - keep (single clause "ma gyur pas...mun mug ma rig pa dang" continues to next block)
# [46] 947 syll49 - keep (single descriptive scene)
# [47] 951 syll41 - keep
# [48] 954 syll47 - keep (single conditional)
# [49] 956 syll43 - keep
# [50] 975 syll46 - keep
# [51] 980 syll43 - keep
# [52] 994 syll63 - long: rhetorical question chain, single continuous thought ("re ba skyes nas" at end leads into next block). keep whole - hard to cut without breaking flow
# [53] 1000 syll43 - keep
# [54] 1019 syll51 - keep (continues list with "dang" - part of refuge formula)
# [55] 1021 syll53 - keep (single refuge-taking sentence)
# [56] 1025 syll65 - long: fear of samsara's suffering + offering body to Samantabhadra. Split before "sangs rgyas thams cad kyi smon lam grub pa'i rang gzugs"
splits[1025] = "སངས་རྒྱས་ཐམས་ཅད་ཀྱི་སྨོན་ལམ་གྲུབ་པའི་རང་གཟུགས་"
# [57] 1026 syll51 - keep (single offering sentence)
# [58] 1041 syll77 - long: description of Yama's emissaries + their victims fleeing. Split before "sems can dmyal ba pa rnams la sdang zhing gsod bcom rdung rdeg btang bar gyur pa de rnams thams cad kyang"
splits[1041] = "སེམས་ཅན་དམྱལ་བ་པ་རྣམས་ལ་སྡང་ཞིང་གསོད་བཅོམ་རྡུང་རྡེག་བཏང་བར་གྱུར་པ་དེ་རྣམས་ཐམས་ཅད་ཀྱང་"
# [59] 1045 syll59 - keep (single long temporal clause, continues with "la")
# [60] 1048 syll67 - long: supplication content + label "...zhes zhus pa ni sdig pa bshags pa'i rten gyi stobs kyi sgo nas..." Split before "zhes zhus pa ni"
splits[1048] = "ཞེས་ཞུས་པ་ནི་སྡིག་པ་བཤགས་པའི་རྟེན་གྱི་སྟོབས་ཀྱི་སྒོ་ནས་"
# [61] 1057 syll58 - keep (single conditional clause, continues to next block "yin na")
# [62] 1058 syll53 - keep (single comparison: dharma as medicine vs ordinary medicine)
# [63] 1062 syll61 - keep (single clause about nature of medicine/dharma, continues "ma gtogs")
# [64] 1067 syll46 - keep (single conditional)
# [65] 1068 syll76 - long: cause (negative karma) + result (hell realm duration). Split before "skye ba phyi ma la dpag tshad stong phrag nyi shu la sogs pa'i sa'i 'og dmyal ba tsha dmyal mnar med la sogs pa'i gnas de nyid la zag nas"
splits[1068] = "སྐྱེ་བ་ཕྱི་མ་ལ་དཔག་ཚད་སྟོང་ཕྲག་ཉི་ཤུ་ལ་སོགས་པའི་སའི་འོག་དམྱལ་བ་ཚ་དམྱལ་མནར་མེད་ལ་སོགས་པའི་གནས་དེ་ཉིད་ལ་ཟག་ནས་"
# [66] 1069 syll66 - long: duration of suffering + resulting caution needed. Split before "dge sgrub sdig spong gi las la yang nas yang du 'bad par bya dgos pa'am"
splits[1069] = "དགེ་སྒྲུབ་སྡིག་སྤོང་གི་ལས་ལ་ཡང་ནས་ཡང་དུ་འབད་པར་བྱ་དགོས་པའམ་"
# [67] 1072 syll51 - keep (single clause)
# [68] 1082 syll48 - keep (single rhetorical clause)

print(json.dumps(splits, ensure_ascii=False, indent=1))
