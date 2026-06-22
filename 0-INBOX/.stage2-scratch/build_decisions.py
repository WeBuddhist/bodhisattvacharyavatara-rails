import json, re

data = json.load(open('batch_01.json', encoding='utf-8'))

splits = {
"659": ("ཞེས་པ་སངས་རྒྱས་", "verse-gloss -> prose explanation of who is anointed"),
"666": ("ཞེས་དེ་ལྟ་བུའི་མེ་ཏོག་ཕུལ་བའི་བསོད་ནམས་ཀྱིས་", "offering act -> resulting aspiration (smon lam)"),
"694": ("ལྷའི་བུ་མོ་མཛེས་མ་ཡིད་དུ་འོང་བ་དེ་དག་རྣམས་ཀྱིས་", "topic shift: palace description -> goddesses' praise-singing"),
"697": ("བློས་དཔག་པ་ལས་མཐའ་ཡས་ཤིང་", "reason clause -> main descriptive statement"),
"735": ("ཅེས་བྱ་བ་ནི་སྨོན་ལམ་སྟོབས་ཀྱི་མཆོད་པ་སྟེ", "aspiration content -> closing classification label"),
"860": ("དེ་ལྟ་བུའི་ཉེས་པ་དང་ནོངས་པའམ་འཁྲུལ་བ་མི་དགེ་བའི་ལས་དེ་དག་ཐམས་ཅད་ནི་ཉེས་པ་ཡིན་པ་", "describing the rejoicing-in-sin fault -> restating it as a fault now directly seen"),
"884": ("ཞེས་བྱ་བ་གུས་ཚིག་གི་སྒོ་ནས་", "quoted inner thought -> narrator's framing of the quote"),
"931": ("རང་ཉིད་ཀྱི་སེམས་ཀྱི་མདུན་ན་སྟེ", "list of sins committed -> statement that they remain as latent imprints"),
"1025": ("སངས་རྒྱས་ཐམས་ཅད་ཀྱི་སྨོན་ལམ་གྲུབ་པའི་རང་གཟུགས་", "fear of samsara's suffering -> act of offering body to Samantabhadra"),
"1041": ("སེམས་ཅན་དམྱལ་བ་པ་རྣམས་ལ་སྡང་ཞིང་གསོད་བཅོམ་རྡུང་རྡེག་བཏང་བར་གྱུར་པ་དེ་རྣམས་ཐམས་ཅད་ཀྱང་", "description of Yama's tormentors -> victims' fear and flight"),
"1048": ("ཞེས་ཞུས་པ་ནི་སྡིག་པ་བཤགས་པའི་རྟེན་གྱི་སྟོབས་ཀྱི་སྒོ་ནས་", "supplication content -> closing classification label"),
"1068": ("སྐྱེ་བ་ཕྱི་མ་ལ་དཔག་ཚད་སྟོང་ཕྲག་ཉི་ཤུ་ལ་སོགས་པའི་སའི་འོག་དམྱལ་བ་ཚ་དམྱལ་མནར་མེད་ལ་སོགས་པའི་གནས་དེ་ཉིད་ལ་ཟག་ནས་", "cause (negative karma) -> resulting hell-realm rebirth/duration"),
"1069": ("དགེ་སྒྲུབ་སྡིག་སྤོང་གི་ལས་ལ་ཡང་ནས་ཡང་དུ་འབད་པར་བྱ་དགོས་པའམ་", "duration of suffering described -> resulting exhortation to vigilant practice"),
}

keep_reasons = {
"592": "single continuous clause (confession of past misdeeds), no internal break point",
"593": "single sentence stating a vow, indivisible",
"619": "single list of offering substances, continues into next block",
"622": "single extended simile clause (rain image), cannot be cut without breaking sense",
"623": "single sentence describing dissolution of offerings into light",
"630": "single aspirational sentence",
"660": "single sentence: merit dedicated to an aspiration",
"664": "single list of objects of offering, continues into next block",
"670": "single sentence describing incense smoke offering",
"676": "single sentence listing food offerings",
"689": "single sentence describing offering of ground/land",
"698": "single sentence: merit dedicated to an aspiration",
"707": "single sentence describing continual offering",
"715": "single sentence: merit dedicated to an aspiration",
"728": "single comparative clause, continues into next block",
"730": "single sentence comparing one's offering to bodhisattvas' offerings",
"753": "single sentence describing prostration to stupas",
"774": "single causal clause explaining motivation for taking refuge in Dharma",
"776": "single causal clause on refuge in the Buddha",
"790": "single causal clause on compassion-motivated refuge",
"793": "single causal clause on refuge for others' sake",
"800": "single sentence defining bodhicitta vow of aspiration",
"811": "single sentence on protective benefit of taking refuge",
"827": "single sentence defining the lay vow-holder, list continues into next block",
"837": "single long conditional clause, continues with further prohibition into next block",
"849": "single list clause of buddhas in the ten directions, continues into next block",
"854": "single explanatory gloss on 'I did not know'",
"863": "single confession sentence, closes with quotation marker",
"880": "single confession sentence addressed to buddhas and bodhisattvas",
"886": "single continuous quoted supplication, indivisible as one direct-speech unit",
"891": "single statement on inevitability of death, continues with epithet into next block",
"899": "single sentence: request for purification through blessing",
"904": "single causal clause, list continues into next block",
"911": "single summary statement on universality of death",
"927": "single list of examples of deceased relatives/friends",
"929": "single causal clause on harmful acts done out of attachment",
"934": "single sentence on ignorance of impermanence, continues into next block",
"947": "single descriptive scene of deathbed",
"951": "single causal sentence urging swift confession",
"954": "single conditional clause describing one bound for lower rebirth",
"956": "single rhetorical statement: relatives cannot help at death",
"975": "single conditional clause describing judicial punishment, continues into next block",
"980": "single conditional/comparative clause on fear before human law",
"994": "single rhetorical question chain expressing rising hope for a protector",
"1000": "single sentence on directly witnessing one's karmic destiny",
"1019": "single clause continuing refuge formula (Dharma jewel description), continues into next block",
"1021": "single sentence on taking refuge in the Three Jewels",
"1026": "single sentence: offering body/mind to Manjushri",
"1041": None,  # handled in splits
"1045": "single long temporal clause, continues into next block",
"1057": "single conditional clause on the power of affliction, continues into next block",
"1058": "single comparison: Dharma medicine vs ordinary medicine",
"1062": "single clause on the nature of the Dharma as medicine, continues with exception clause",
"1067": "single conditional clause on caution with minor wounds",
"1072": "single rhetorical clause on false complacency about death",
"1082": "single rhetorical clause on failure to practice Dharma",
}

decisions = []
for d in data:
    tsv_idx = d['tsv_idx']
    text = d['text']
    if tsv_idx in splits:
        marker, reason = splits[tsv_idx]
        pos = text.index(marker)
        new_text = text[:pos].rstrip() + "\n\n" + text[pos:]
        action = "split"
    else:
        new_text = text
        reason = keep_reasons.get(tsv_idx, "no clean internal cut without breaking sense; left whole")
        action = "keep"
    decisions.append({
        "tsv_idx": tsv_idx,
        "block_idx": d['block_idx'],
        "action": action,
        "original": text,
        "new": new_text,
        "reason": reason,
    })

# Verification pass
fail = 0
for dec in decisions:
    a = re.sub(r'\s+', '', dec['new'])
    b = re.sub(r'\s+', '', dec['original'])
    if a != b:
        fail += 1
        print("MISMATCH", dec['tsv_idx'])
        print("orig:", b[:50], '...', b[-50:])
        print("new :", a[:50], '...', a[-50:])

print("Total:", len(decisions), "Fails:", fail)
print("Split count:", sum(1 for d in decisions if d['action']=='split'))
print("Keep count:", sum(1 for d in decisions if d['action']=='keep'))

if fail == 0:
    with open('decisions_01.json', 'w', encoding='utf-8') as f:
        json.dump(decisions, f, ensure_ascii=False, indent=1)
    print("WROTE decisions_01.json")
else:
    print("NOT WRITING due to failures")
