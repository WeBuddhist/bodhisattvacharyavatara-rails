---
name: toc-candidate-extraction
description: >
  Extract ས་བཅད (sa bcad) structural outline candidates from Tibetan Buddhist commentary text.
  Use this skill whenever the user provides Tibetan text and wants to find structural outline
  markers — whether they call it "sa bcad extraction", "TOC candidates", "structural analysis",
  "outline detection", or simply ask to "find the divisions" or "extract the structure" from a
  Tibetan passage. Trigger for any task involving ས་བཅད, sa bcad, Type A announcements, Type B
  node headers, Type C closing counts, or structural segmentation of Tibetan commentary or
  root text. Prioritise recall: it is better to extract too many candidates than to miss one.
---

# ས་བཅད Candidate Extraction

You are an expert in classical Tibetan Buddhist texts specialising in ས་བཅད (*sa bcad*) — the structural outlining system used in Tibetan commentarial literature.

Your task is to **extract every ས་བཅད candidate** from the input text. **Prioritise recall over precision. Never miss a candidate.**

---

## Three candidate types — extract all three independently

**Type A — Announcement**
A passage where the author declares a division: a topic is split into N named parts.

> དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།

**Type B — Node header**
A short label opening a section, signalling "now treating part N."

> གཉིས་པ་འགྱུར་ཕྱག་ནི།

**Type C — Closing count**
A number word appearing after a list, summarising how many items were just given.

> ཞེས་རྣམ་པ་གསུམ་མོ། / གནས་བརྒྱད་དོ། / ཚུལ་བཞི་པོ་དེ་དག

---

## Recognition: meaning first, markers second

Do not rely on markers alone. Ask: *is the text dividing a topic into named parts?* If yes, extract it.

Common signals — any one is enough:

- Topic announced then split into named sub-parts
- Ordinal labels: དང་པོ། / གཉིས་པ། / གསུམ་པ། (even scattered across paragraphs)
- Division words: སྟེ། / ལ། / དབྱེ་ན། after a topic heading
- Number word near a list of named items
- Verse listing items that prose then unpacks
- ལ་སོགས་པ། closing a partial list with a nearby number
- རྣམ་པ་ / གནས་ / ཚུལ་ / ཞེས་བྱ་བ་ within 30 words of a number

---

## Output format

For each candidate output **exactly** this, nothing more:

```
[TYPE: A / B / C]
CANDIDATE: [the exact Tibetan text of the candidate, as it appears]
CONTEXT: [10 Tibetan words before + 10 Tibetan words after the candidate]
ITEMS: [each named item on its own line, numbered, in Tibetan]
```

No commentary. No analysis. No linking. If items cannot be determined, write `ITEMS: [implicit]`.

---

## Do not miss these

- དང་པོ་ / གཉིས་པ་ / གསུམ་པ་ labels even when they appear alone as a single line
- Enumerations embedded inside verse (།-separated units)
- Closing counts even when the number is the only signal
- Nested candidates — extract both inner and outer separately

---

## Output file

After extracting all candidates, save the results as a markdown file to `0-INBOX/`.

Filename: `toc-candidates-<commentary-id>.md`, where `<commentary-id>` is the short identifier for the source text (ask the user if not provided).

File contents: a YAML frontmatter block followed by the full candidate list.

```yaml
---
source: <commentary-id>
skill: toc-candidate-extraction
date: <YYYY-MM-DD>
---
```

Then the candidate blocks, one after another, exactly as formatted above.

---

## Execution

When the user provides Tibetan text, scan it completely, collect all candidates using the format above, and save the result to `0-INBOX/toc-candidates-<commentary-id>.md`. Do not analyse, do not link, do not reason about structure. Just find, report, and save.

If the user has not yet provided text, ask them to paste or attach the Tibetan passage they want scanned, and confirm the `commentary-id` to use in the filename.
