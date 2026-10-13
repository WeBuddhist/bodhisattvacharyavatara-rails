#!/usr/bin/env python3
"""gm_verify.py — deterministic checks on a Gemini track. No API calls.

Run after a corpus run (and after any re-run) to state, from the files rather
than from anyone's summary, whether the track is whole:

  * the last corpus report: texts, blocks done/total, calls, stopped-or-not
  * ledgers: one per source text, every block recorded, none without line parity
  * rendered files: blocks_translated == blocks_total, no placeholders, a
    researched title and the generator's site stamped
  * block ids: identical to the Tibetan, one for one, in every file
  * stray script: Tibetan or CJK characters inside translation lines (an
    ornament copied from the source, an untranslated fragment)

Exit status 0 when everything holds, 1 otherwise, so a driver can chain it.

Usage:
    gm_verify.py --lang-tag hi
    gm_verify.py --lang-tag mn --quiet     # only the verdict line
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parents[3]

sys.path.insert(0, str(HERE))
from gm_translate import DEFAULT_TRACK_ROOT  # noqa: E402

TIBETAN = re.compile(r"[ༀ-࿿]")
CJK = re.compile(r"[一-鿿]")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lang-tag", required=True)
    ap.add_argument("--track", default=None)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    tag = args.lang_tag
    track = pathlib.Path(args.track or VAULT / DEFAULT_TRACK_ROOT / tag)
    say = (lambda *a, **k: None) if args.quiet else print
    problems = []

    reps = sorted(glob.glob(str(track / "work" / "_corpus-run-*.json")))
    if reps:
        rep = json.load(open(reps[-1], encoding="utf-8"))
        say(f"last report : {os.path.basename(reps[-1])}  texts {rep['texts_attempted']}/{rep['texts_planned']}, "
            f"blocks {rep['blocks_done']}/{rep['blocks_total']}, calls {rep['calls']}, "
            f"stopped={rep['stopped']}")
        if rep["stopped"]:
            problems.append(f"last corpus run stopped early ({rep['stopped']})")

    # ledgers
    n_blocks, no_parity, texts = 0, [], 0
    for led in sorted((track / "work").glob(f"*-{tag}.jsonl")):
        texts += 1
        latest = {}
        for line in led.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                latest[r["block_id"]] = r
        n_blocks += len(latest)
        for b, r in latest.items():
            if r.get("line_parity") is False:
                no_parity.append((led.name[: -(len(tag) + 7)], b,
                                  len(r["source"].split("\n")), len(r["translation"].split("\n"))))
    say(f"ledgers     : {texts} texts, {n_blocks} blocks; {len(no_parity)} without line parity")
    for x in no_parity:
        say(f"              {x[0][:40]} ^{x[1]} source {x[2]} -> output {x[3]}")
    if no_parity:
        problems.append(f"{len(no_parity)} block(s) without line parity")

    # rendered files
    files = sorted(track.glob(f"*-{tag}.md"))
    short, placeholder, untitled, unsited = [], [], [], []
    for f in files:
        t = f.read_text(encoding="utf-8")
        a = re.search(r"^blocks_translated: (\d+)", t, re.M)
        b = re.search(r"^blocks_total: (\d+)", t, re.M)
        if not a or not b or a.group(1) != b.group(1):
            short.append(f.name)
        if "*[not yet translated]*" in t:
            placeholder.append(f.name)
        # FORK(21-taras-rails): the work's title lives in `title` (what the vault
        # linter uploads); a title that is still the "<x> — Gemini zero-shot" composite
        # means no researched title was ever seeded.
        if not re.search(r"^title: (?!.*zero-shot).+\S", t, re.M):
            untitled.append(f.name)
        if not re.search(r"^source: https?://", t, re.M):
            unsited.append(f.name)
    say(f"rendered    : {len(files)} files; short {len(short)}, placeholders {len(placeholder)}, "
        f"untitled {len(untitled)}, no source site {len(unsited)}")
    for name, lst in (("short", short), ("placeholder", placeholder), ("untitled", untitled), ("no site", unsited)):
        for x in lst[:5]:
            say(f"              {name}: {x}")
        if lst:
            problems.append(f"{len(lst)} file(s) {name}")

    # block ids vs source
    mismatches = []
    for f in files:
        stem = f.name[: -(len(tag) + 4)]
        src = VAULT / "1-SOURCES" / "Text" / f"{stem}.md"
        if not src.exists():
            mismatches.append((f.name, "no source"))
            continue
        ids_src = re.findall(r"\^([A-Za-z0-9-]+)\s*$", src.read_text(encoding="utf-8"), re.M)
        ids_out = re.findall(r"\^([A-Za-z0-9-]+)\s*$", f.read_text(encoding="utf-8"), re.M)
        if ids_src != ids_out:
            mismatches.append((f.name, f"{len(ids_src)} vs {len(ids_out)}"))
    say(f"block ids   : {len(mismatches)} file(s) differ from the Tibetan")
    for x in mismatches[:5]:
        say(f"              {x}")
    if mismatches:
        problems.append(f"{len(mismatches)} file(s) with block-id mismatch")

    # stray script
    stray = []
    for f in files:
        body = f.read_text(encoding="utf-8").split("\n---\n", 1)[1]
        for line in body.split("\n"):
            # `![[…#^id]]` is a transclusion of the Tibetan, not a translation line.
            if line.startswith((">", "#", "![[")) or not line.strip():
                continue
            # FORK(21-taras-rails): CJK is the target script for zh/ja/lzh tracks.
            if TIBETAN.search(line) or (tag not in ("zh", "ja", "lzh") and CJK.search(line)):
                stray.append((f.name[:32], line[:50]))
    say(f"stray script: {len(stray)} translation line(s) with Tibetan or CJK characters")
    for x in stray[:8]:
        say(f"              {x}")
    if stray:
        problems.append(f"{len(stray)} translation line(s) with stray script")

    verdict = "OK" if not problems else "PROBLEMS: " + "; ".join(problems)
    print(f"{tag}: {verdict}")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
