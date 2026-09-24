#!/usr/bin/env python3
"""Recompute an edition's table of contents from its source, and replace it.

Needed because the 2026-09-20 sweep took every heading out of the uploaded
content and segmentation. The TOC that is live was built when headings still
occupied characters, so its section spans no longer describe the text.

WHAT A SECTION'S SPAN IS NOW

Content is a single line — no newlines at all — and the segments tile it
exactly. A heading occupies no characters, so a section runs from where its
own body starts to where the next heading of the same or higher level starts:

    [heading.pos, next same-or-higher heading.pos)     last one: to content end

Only content segments fall inside that range; the heading's own text is not in
the content at all. It travels as the section's `title` instead, which is the
whole point of the policy.

NESTING follows heading depth: `#` is a section, each `##` under it is a
subsection of that section, each `###` a subsection of the `##`, and so on.
A parent's span therefore covers all of its children's.

THE BLOCK ID HAS NOWHERE TO GO IN THE PAYLOAD. `TableOfContentsSectionInput`
is {title, summary, span, subsections} with `additionalProperties: false`, so
an extra key is rejected. `AnnotationMetadata` holds only `name`. `title` and
`summary` are LocalizedString maps, and the backend validates every key as a
real language code (NomenDatabase.create_with_transaction ->
validate_language_codes_exist), so a pseudo-language key is rejected too.
`SegmentInput` *does* carry `reference` — the same field on a TOC section is
the clean fix and worth asking the backend for. Until then this script writes
the mapping to a local ledger: backend section id <-> vault block id.

ORDER OF OPERATIONS. The old TOC is deleted and a new one posted. That is two
calls with a window in between, and neither is idempotent, so:

  * the content check must pass FIRST — if the source no longer reproduces the
    live content byte for byte, the spans would describe a different string,
    and the script refuses before touching anything;
  * the payload is built and fully validated BEFORE the delete, so the delete
    only happens once there is something correct to put back;
  * a failed POST after a successful DELETE leaves the edition with no TOC.
    The payload is written to disk first, so it can be re-posted by hand.

Usage:
    rebuild_toc.py --edition <id> --dry-run
    rebuild_toc.py --edition <id> --execute
    rebuild_toc.py --all --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import api
import preflight_toc as pf

HERE = Path(__file__).resolve().parent
PAYLOAD_DIR = HERE / "toc-payloads"
LEDGER = HERE / "toc-reference-ledger.json"


def headings_for(mod, src, kind):
    """(content, headings, header_levels) with headings in document order."""
    fm, body = mod._read_source(src)
    blocks = mod._extract_blocks(body)
    doc_default = "paragraph" if kind == "commentary" else "verse"
    content, segs, headings = mod._build_content_and_segmentation(blocks, doc_default)
    if kind == "commentary":
        content, segs, headings = mod._strip_verse_ids(content, segs, headings)
    return content, headings, mod._extract_header_levels(body), fm


def build_sections(headings, levels, content_len, lang_tag, mod):
    """Nest headings by depth. Returns (sections, flat) where flat is in the
    same order the backend will return them, each with its block id."""
    nodes = [{
        "ref": h["reference"],
        "level": levels.get(h["reference"], 1),
        "start": h["pos"],
        "title": mod._wylie_to_unicode(h["title"], lang_tag),
    } for h in headings]

    for i, n in enumerate(nodes):
        end = content_len
        for j in range(i + 1, len(nodes)):
            if nodes[j]["level"] <= n["level"]:
                end = nodes[j]["start"]
                break
        n["end"] = end

    flat = []

    def nest(idx, parent_level):
        out = []
        i = idx
        while i < len(nodes):
            n = nodes[i]
            if n["level"] <= parent_level:
                break
            if n["level"] == parent_level + 1:
                sec = {"title": {lang_tag: n["title"]},
                       "span": {"start": n["start"], "end": n["end"]}}
                flat.append(n)
                subs, i = nest(i + 1, n["level"])
                if subs:
                    sec["subsections"] = subs
                out.append(sec)
            else:
                i += 1
        return out, i

    top = nodes[0]["level"] if nodes else 1
    sections, _ = nest(0, top - 1)
    return sections, flat


def validate(sections, content_len):
    """Structural checks. Returns a list of problems."""
    problems = []

    def walk(secs, parent=None, depth=0):
        prev_end = None
        for s in secs:
            a, b = s["span"]["start"], s["span"]["end"]
            title = next(iter(s["title"].values()), "?")
            if not (0 <= a <= b <= content_len):
                problems.append(f"{title!r}: span [{a},{b}) outside [0,{content_len}]")
            if parent is not None:
                pa, pb = parent["span"]["start"], parent["span"]["end"]
                if a < pa or b > pb:
                    problems.append(f"{title!r}: span [{a},{b}) escapes parent [{pa},{pb})")
            if prev_end is not None and a < prev_end:
                problems.append(f"{title!r}: span [{a},{b}) overlaps previous sibling ending {prev_end}")
            prev_end = b
            walk(s.get("subsections", []), s, depth + 1)

    walk(sections)
    if sections:
        if sections[0]["span"]["start"] != 0:
            problems.append(f"first section starts at {sections[0]['span']['start']}, not 0")
        if sections[-1]["span"]["end"] != content_len:
            problems.append(f"last section ends at {sections[-1]['span']['end']}, not {content_len}")
    else:
        problems.append("no sections")
    return problems


def count(sections):
    return sum(1 + count(s.get("subsections", [])) for s in sections)


def process(eid, execute, live_check=True):
    rel, kind = pf.EDITIONS[eid]
    src = pf.VAULT / rel
    mod = pf.load(f"_m_{kind}", pf.ROOT_PARSER if kind == "root" else pf.COMM_PARSER)
    content, headings, levels, fm = headings_for(mod, src, kind)
    lang_tag = fm.get("lang_tag") or "en"

    print(f"\n=== {eid}  {Path(rel).name}  [{lang_tag}]")

    if live_check:
        live_content = api.content(eid)
        same = hashlib.sha256(content.encode()).hexdigest() == \
               hashlib.sha256(live_content.encode()).hexdigest()
        print(f"  source reproduces live content: {'yes' if same else 'NO'} "
              f"(source {len(content)}, live {len(live_content)})")
        if not same:
            print("  REFUSING: spans would describe a different string than the backend holds.")
            return None, ["source/live content mismatch"]
        content_len = len(live_content)
    else:
        content_len = len(content)

    sections, flat = build_sections(headings, levels, content_len, lang_tag, mod)
    problems = validate(sections, content_len)
    print(f"  headings {len(headings)} -> {count(sections)} sections "
          f"({len(sections)} top-level), content {content_len} chars")
    for s in sections:
        print(f"    [{s['span']['start']},{s['span']['end']}) "
              f"{next(iter(s['title'].values()))[:44]}")
        for ss in s.get("subsections", []):
            print(f"      [{ss['span']['start']},{ss['span']['end']}) "
                  f"{next(iter(ss['title'].values()))[:40]}")
    for p in problems:
        print(f"    !! {p}")
    if problems:
        return None, problems

    payload = {"sections": sections}
    PAYLOAD_DIR.mkdir(exist_ok=True)
    out = PAYLOAD_DIR / f"{eid}.toc.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  payload written: {out.relative_to(pf.VAULT)}")

    existing = api.toc(eid) or []
    old_ids = [t["id"] for t in existing if isinstance(t, dict) and t.get("id")]
    print(f"  existing TOC(s) to delete: {old_ids or 'none'}")

    if not execute:
        print("  DRY RUN — nothing sent.")
        return {"sections": sections, "flat": flat, "old_ids": old_ids}, []

    for tid in old_ids:
        status, _ = api.request("DELETE", f"/v2/table-of-contents/{tid}", attempts=1)
        print(f"  DELETE /v2/table-of-contents/{tid} -> {status}")
    status, created = api.request("POST", f"/v2/editions/{eid}/table-of-contents",
                                  payload, attempts=1)
    print(f"  POST  /v2/editions/{eid}/table-of-contents -> {status}")
    return {"sections": sections, "flat": flat, "created": created, "old_ids": old_ids}, []


def record_refs(eid, flat, created=None):
    """Persist backend section id <-> vault block id, since the payload cannot.

    Always re-reads the TOC from the API rather than trusting the POST body:
    the create response does not carry the nested sections, so reading it back
    is the only way to learn the ids the backend assigned.
    """
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    docs = api.toc(eid) or []
    want = (created or {}).get("id") if isinstance(created, dict) else None
    live = next((d for d in docs if d.get("id") == want), docs[0] if docs else {})
    got = []

    def walk(secs):
        for s in secs or []:
            got.append(s)
            walk(s.get("subsections"))

    walk((live or {}).get("sections"))
    if len(got) != len(flat):
        ledger[eid] = {"error": f"section count {len(got)} != expected {len(flat)}"}
    else:
        ledger[eid] = {
            "toc_id": (live or {}).get("id"),
            "sections": [{"section_id": g.get("id"), "block_id": f["ref"],
                          "title": f["title"], "span": [f["start"], f["end"]]}
                         for g, f in zip(got, flat)],
        }
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=1), encoding="utf-8")
    return ledger[eid]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--ledger-only", action="store_true",
                    help="re-read the live TOC and (re)write the block-id ledger, no writes")
    args = ap.parse_args(argv)

    if args.execute and args.dry_run:
        print("--execute and --dry-run are mutually exclusive"); return 2
    if args.execute and not os.environ.get("WEBUDDHIST_API_KEY"):
        print("WEBUDDHIST_API_KEY is not set; DELETE/POST are key-gated. Refusing.")
        return 2

    eids = list(pf.EDITIONS) if args.all else args.edition
    if args.ledger_only:
        for eid in eids:
            rel, kind = pf.EDITIONS[eid]
            mod = pf.load(f"_m_{kind}", pf.ROOT_PARSER if kind == "root" else pf.COMM_PARSER)
            content, headings, levels, fm = headings_for(mod, pf.VAULT / rel, kind)
            _, flat = build_sections(headings, levels, len(api.content(eid)),
                                     fm.get("lang_tag") or "en", mod)
            rec = record_refs(eid, flat)
            print(f"{eid}: " + (rec["error"] if "error" in rec
                                else f"{len(rec['sections'])} sections mapped, toc {rec['toc_id']}"))
        return 0
    if not eids:
        print("give --edition <id> (repeatable) or --all"); return 2
    print(("EXECUTE" if args.execute else "DRY RUN") + f": {len(eids)} edition(s) on {api.BASE}")

    bad = []
    for eid in eids:
        try:
            res, problems = process(eid, args.execute)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR {e!r}"[:300]); bad.append(eid); continue
        if problems:
            bad.append(eid); continue
        if args.execute and res:
            rec = record_refs(eid, res["flat"], res.get("created"))
            if "error" in rec:
                print(f"  !! ledger: {rec['error']}"); bad.append(eid)
            else:
                print(f"  ledger: {len(rec['sections'])} section ids mapped to block ids")

    print(f"\n{len(eids) - len(bad)}/{len(eids)} ok" + (f"; problems: {bad}" if bad else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
