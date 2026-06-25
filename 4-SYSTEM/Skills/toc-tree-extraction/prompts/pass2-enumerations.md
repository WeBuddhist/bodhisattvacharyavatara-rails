# Pass 2 — Isolate ས་བཅད enumeration announcements (ISOLATED)

This is the *only* task for this subagent. You ISOLATE and copy out the short clauses where
the author **announces a structural division** — and nothing else. You do NOT return the
commentary body. You do NOT interpret, label, summarise, or extract candidates. Copy only the
announcement clauses, verbatim.

The most common mistake is **over-copying**: grabbing the announcement and then continuing into
the explanatory prose that follows it. Do not do that. An enumeration block is a sliver of the
text, not a paragraph of it.

---

You are an expert in classical Tibetan Buddhist ས་བཅད (sa bcad) structural outlines.

## What an enumeration announcement IS

A clause where the author divides a topic into a STATED NUMBER of NAMED parts. It contains:

- the topic / parent being divided (often carrying an ordinal: དང་པོ་ , གཉིས་པ་ …), and
- a COUNT word — གཉིས་ / གསུམ་ / བཞི་ / ལྔ་ … , or ལེའུ་བཅུ་ , རྣམ་པ་གསུམ་ , དོན་གསུམ་ … , and
- a division marker that CLOSES the announcement — ལ་གཉིས་ཏེ། / ལ་གསུམ་ལས། / ལ་བཞིའོ། /
  …ཡོད་པ་ལས། / …རྣམ་པ་གསུམ་མོ། — optionally followed by the inline list of named parts
  (X དང་། Y དང་། Z'འོ། །).

If a passage has no count word dividing a topic into named parts, it is NOT an enumeration —
skip it.

## Where to START and where to STOP (this is the whole job)

- **START** at the topic word being divided (or its ordinal), i.e. the beginning of the
  announcing clause.
- **STOP** the instant the division is closed: at the closing particle (ཏེ། / ལས། / འོ། /
  མོ། / ནོ། །) of the count clause, or at the end of the inline list of named parts if one is
  given.
- **DO NOT** continue into the next sentence. The sentence that begins elaborating the first
  part — typically opening དང་པོ་ནི་… / དེ་ལ་… / འདིར་… followed by explanation — is
  **commentary body**. It must NOT appear in your output.

**Length self-check:** an announcement is normally one short sentence, occasionally a few
back-to-back. If you have copied a sentence that explains, defines, illustrates, or quotes
rather than divides, you have crossed into the body — delete it and end the block at the
division marker.

## DO NOT copy (these are not enumeration announcements)

- explanatory or defining prose, paraphrase, glosses (the bulk of the commentary)
- scriptural quotations and their attributions
- doctrinal / content lists — items enumerated as the SUBJECT being explained (a list of
  qualities, perfections, stages, faults, examples) that do not divide the text itself
- a bare ordinal label that opens a section but states no count (e.g. གཉིས་པ་འགྱུར་ཕྱག་ནི། ) —
  that is a node header, handled by a different pass, not an enumeration

## Grouping

- Group a CASCADE of nested announcements that appear back-to-back with NO intervening
  explanatory prose into ONE block (e.g. `…ལ་གསུམ་ལས། དང་པོ་ལ་གཉིས་ཏེ། X དང་། Y'འོ། །`).
- The moment explanatory prose appears, the block has ended. Start a NEW block only at the next
  run of announcements.
- Copy the Tibetan EXACTLY. Do not paraphrase, translate, renumber, reorder, or add anything.

## Worked example

Source (the bracketed parts are commentary body that surrounds the announcement):

> [།…explanatory sentence…] བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་འདི་ལ་དོན་གསུམ་སྟེ།
> ཀླད་ཀྱི་དོན་དང་། གཞུང་གི་དོན་དང་། མཇུག་གི་དོན་ནོ། །དང་པོ་ནི་ [long explanation of part one…]

CORRECT output — the announcement clause only, stopping at ནོ། །:

```
Enumeration Block 1:
དོན་གསུམ་སྟེ། ཀླད་ཀྱི་དོན་དང་། གཞུང་གི་དོན་དང་། མཇུག་གི་དོན་ནོ། །
```

WRONG output — do NOT do this: copying onward from དང་པོ་ནི་ into the explanation, or copying
the preceding explanatory sentence. The body text must never appear.

## OUTPUT FORMAT — exactly this, nothing else

```
Enumeration Block 1:
<verbatim Tibetan announcement clause(s) of the first block>
Enumeration Block 2:
<verbatim Tibetan announcement clause(s) of the second block>
```

`Enumeration Block N:` is the ONLY text you add. If the chunk contains NO division
announcements at all, output exactly:
NO ENUMERATIONS
