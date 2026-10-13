#!/usr/bin/env python3
"""Per-segment context for the root text: Tibetan, aligned Sanskrit, aligned commentary passages.

Library:
    from segment_context import build_context
    ctx = build_context()          # {root_id: {"bo", "sa": [{"id","text"}], "commentaries": {cid: [{"id","text"}]}}}

CLI:
    python3 segment_context.py [--out context.json] [--show 6-33]

Bodhicaryāvatāra vault: there are no 1-SOURCES/Annotations files; the alignment is
the Obsidian transclusions already in the sources, never identical block numbers
(Tibetan and Sanskrit verse numbers differ in chapters 2, 5, 8 and 9).
- Sanskrit: the `![[1-SOURCES/Text/BCAV08_SH_sk.md#^id]]` lines above a Tibetan
  verse name its Sanskrit verse(s).
- Commentary: a `![[bo-བློ་ལྡན་ཤེས་རབ།#^id]]` line opens a passage that runs to the
  next transclusion. Consecutive transclusions with no text between them share
  the passage that follows (one comment on a group of verses). Each passage's
  `id` is the first root id it was attached to.
"""
import argparse
import json
import pathlib
import re

VAULT = pathlib.Path(__file__).resolve().parents[3]
ROOT_FILE = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
SA_FILE = "1-SOURCES/Text/BCAV08_SH_sk.md"
COMMENTARIES = {  # user choice 2026-10-07: three traditions, one compact
    "bo-kunpal": "1-SOURCES/Commentaries/Transcluded/BCAC19_KKP_bo_segmented.md",   # Khenpo Kunzang Palden, word commentary
    "bo-shenga": "1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md",              # Khenpo Shenga, interlinear notes
    "bo-gyaltsab": "1-SOURCES/Commentaries/Transcluded/BCAC14_GDR_bo_segmented.md",  # Gyaltsab Darma Rinchen
}
MARK = re.compile(r"\s*\^([0-9A-Za-z]+(?:-[0-9]+)*)\s*$")
TRANS = re.compile(r"^!\[\[([^\]#]*)#\^([^\]|]+)(?:\|[^\]]*)?\]\]\s*$")
LINK = re.compile(r"\[\[[^\]|]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]")


def body(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        return text[end + 4:] if end != -1 else text
    return text


def clean(line):
    line = line.replace("​", "").strip()
    line = re.sub(r"^#+\s*", "", line)
    line = LINK.sub(lambda m: m.group(1) if m.group(1) is not None else m.group(2).split("#")[0], line)
    return line.replace("**", "").strip()


def blocks(path, with_trans=False):
    """{id: text} in file order (multi-line blocks joined with spaces).
    with_trans: also {id: [transcluded ids]} from the transclusion lines just above each block."""
    out, above, pending, trans = {}, {}, [], []
    for raw in body((VAULT / path).read_text(encoding="utf-8")).splitlines():
        t = TRANS.match(raw.strip())
        if t:
            trans.append(t.group(2))
            continue
        line = clean(raw)
        if not line:
            continue
        m = MARK.search(line)
        if m:
            pending.append(line[: m.start()].strip())
            out[m.group(1)] = " ".join(p for p in pending if p)
            above[m.group(1)] = trans
            pending, trans = [], []
        else:
            pending.append(line)
    return (out, above) if with_trans else out


def commentary_passages(path):
    """{root_id: [ {id: first root id of the group, text: passage} ]} for one commentary."""
    root_stem = pathlib.Path(ROOT_FILE).stem
    out, group, cur = {}, [], None
    for raw in body((VAULT / path).read_text(encoding="utf-8")).splitlines():
        t = TRANS.match(raw.strip())
        if t and pathlib.Path(t.group(1)).stem == root_stem:
            if cur is not None and cur["text"]:  # text since the last transclusion closes that group
                group, cur = [], None
            rid = t.group(2)
            if cur is None:
                cur = {"id": rid, "text": ""}
            group.append(rid)
            out.setdefault(rid, []).append(cur)
            continue
        if cur is None:
            continue
        line = MARK.sub("", clean(raw)).strip()
        if line:
            cur["text"] = (cur["text"] + " " + line).strip()
    return out


def build_context(root=None):
    bo, above = blocks(ROOT_FILE, with_trans=True)
    sa = blocks(SA_FILE)
    comms = {cid: commentary_passages(p) for cid, p in COMMENTARIES.items()}
    ctx = {}
    for rid, text in bo.items():
        ctx[rid] = {
            "bo": text,
            "sa": [{"id": s, "text": sa[s]} for s in above.get(rid, []) if s in sa],
            "commentaries": {cid: [p for p in c[rid] if p["text"]] for cid, c in comms.items()
                             if rid in c and any(p["text"] for p in c[rid])},
        }
    return ctx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="ignored; kept for the Diamond Sutra interface")
    ap.add_argument("--out")
    ap.add_argument("--show")
    a = ap.parse_args()
    ctx = build_context()
    if a.out:
        pathlib.Path(a.out).write_text(json.dumps(ctx, ensure_ascii=False, indent=1), encoding="utf-8")
    verses = [k for k in ctx if re.fullmatch(r"\d+-[1-9]\d*", k)]
    n_sa = sum(1 for k in verses if ctx[k]["sa"])
    per_c = {}
    for k in verses:
        for cid in ctx[k]["commentaries"]:
            per_c[cid] = per_c.get(cid, 0) + 1
    print(f"root blocks={len(ctx)} verses={len(verses)} with_sanskrit={n_sa} with_commentary={per_c}")
    if a.show:
        print(json.dumps(ctx[a.show], ensure_ascii=False, indent=1)[:3000])


if __name__ == "__main__":
    main()
