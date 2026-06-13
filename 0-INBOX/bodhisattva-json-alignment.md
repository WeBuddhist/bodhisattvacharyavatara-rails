---
title: Alignment check — scripts/data/bodhisattva.json vs 1-SOURCES/Text/sk-dev.md
status: draft
---

# Verse-to-segment alignment

`scripts/data/bodhisattva.json` stores a single `content` string (78,274 chars) plus a `segments` array of 920 character-span IDs. `1-SOURCES/Text/sk-dev.md` has 917 block IDs (916 verse/content blocks + headings).

After normalizing both (stripping whitespace, danda/double-danda, virama, line breaks) and globally diffing, the texts match at **98%** character similarity. Of 916 sk-dev verse blocks:

- **887** map 1:1 to a single json segment
- **13** map to 2 json segments (verse split across two spans)
- a handful of blocks show apparent 0- or multi-segment counts — these are **not missing text**, just off-by-one block assignment from the automated aligner (see below). The underlying segment text is present and in order.

A draft mapping (`<chapter-verse>` → `[segment ids]`) was generated and saved to the outputs scratch folder; it is ~97% correct as-is but the ranges below need a manual re-split before it can be trusted as a rail.

## Known issues to resolve before treating the mapping as final

1. **First 2 segments of `bodhisattva.json` are not in sk-dev.** They contain an alternate title/homage (`बोधिसत्त्वचर्यावतारनाम नमो बुद्ध बोधित्त्वेभ्यः`) that doesn't correspond to sk-dev's `^0-1` (`ॐ नमो बुद्धाय`). Conversely, sk-dev's `^0-1` has no counterpart in the json. These should be excluded/handled separately, not forced into the verse mapping.

2. **Chapter 8, verses ~79–84**: json segment count (5) doesn't match sk-dev verse count (6, `8-79`…`8-84`) in that span — off by one. Likely caused by issue 3 below shifting the local alignment; needs manual re-check of `8-79`–`8-83`.

3. **An "extra verse" literally appears in the json content** at two places, embedded mid-segment with the English marker text `"extra verse"`:
   - inside the segment landing near `8-186`
   - inside the segment landing near `9-168`
   
   These look like editorial insertions in the json source that have no corresponding verse in sk-dev. They should be stripped/flagged, and everything downstream in those chapters re-checked for an off-by-one shift (chapter 9 ranges `9-12`–`9-21` and `9-133`–`9-168` show the same kind of 1-segment drift, but content checks confirm the actual verse text is present and in order — just assigned to the neighboring block ID by the aligner).

4. **Chapter 10, verse `10-22`: the json contains the verse text twice** (segment text for `आरोग्यं रोगिणामस्तु...` is duplicated). This duplication likely also causes `10-16` to show as empty (one verse re-numbered due to the upstream duplicate). Needs manual confirmation against sk-dev — sk-dev has this verse only once at `^10-22`.

## Recommendation

Given the issues above are concentrated in a few small ranges (ch.8 ~79-84, ch.9 ~12-21 and ~133-168, ch.10 ~16-23) plus the title/intro mismatch, the cleanest fix is a manual pass over just those ranges (re-splitting/re-assigning segment IDs verse-by-verse) rather than trusting the automated global alignment there. The remaining ~870 verses (chapters 1–7, most of 8–10) are reliably 1:1 or 1:2 and don't need rework.
