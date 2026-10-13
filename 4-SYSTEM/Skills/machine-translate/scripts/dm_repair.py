#!/usr/bin/env python3
"""dm_repair.py — finish and repair a DharmaMitra track against its Tibetan sources.

Two passes over every source text in the track:

  MISSING  a source block with no ledger record        -> translate it
  MISSHAPEN a block whose translation has a different  -> re-translate it alone,
           number of non-blank lines than its source      with the exact required
                                                          line count stated

A repair is sent on its own (never batched) so the model has one job, and the
result is ACCEPTED ONLY IF the line count actually matches. If no attempt
matches, the original record is left untouched and the block is reported for
human review -- a wrong answer is never silently swapped for another wrong one.

The ledger is append-only: a repaired block is appended and supersedes the older
record at render time. No earlier attempt is destroyed.

Usage:
  dm_repair.py --report-only                      # what would change, no API calls
  dm_repair.py                                    # repair everything
  dm_repair.py --only-text "ཆགས་མེད་བདེ་སྨོན།"     # one text
  dm_repair.py --attempts 4 --accept-closest      # try harder, take best effort
"""

import argparse
import datetime as _dt
import importlib.util
import json
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("dm_translate", HERE / "dm_translate.py")
dm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dm)

# Two repair protocols, tried in order.
#
# NUMBERED is the good one: the source goes out with "1| ", "2| " prefixes and the
# model returns the same prefixes, so line N of the output provably translates line
# N of the source. Matching a line COUNT is not the same as matching line for line
# -- a count-only repair will happily cram two source lines into one output line and
# leave another nearly empty. The numbered form pins each line to its source.
NUMBERED_CLAUSE = (
    "\n\nLINE-BY-LINE (strict): the source has {n} numbered lines, each prefixed "
    "'1| ', '2| ' and so on. Output exactly {n} lines carrying the SAME prefixes. "
    "Line N of your output must translate line N of the source and nothing else: do "
    "not move content between lines, and do not merge or split lines. Output only "
    "the numbered lines -- no heading, no blank lines, no commentary."
)

# COUNT is the fallback when the model will not hold the numbering.
COUNT_CLAUSE = (
    "\n\nLINE COUNT (strict): the source segment has exactly {n} line(s). Your "
    "translation must have exactly {n} line(s) -- one output line for each source "
    "line, in the same order. Do not add, merge, split or drop line breaks. Do not "
    "output blank lines, a heading, a number, or any commentary."
)

NUM_RE = re.compile(r"^[ \t]*(\d+)[ \t]*\|[ \t]?(.*)$")


class Abort(Exception):
    """A hard API failure -- exhausted 429 backoff. Stop; do not keep calling."""


def number_source(lines):
    return "\n".join(f"{i}| {l}" for i, l in enumerate(lines, 1))


def parse_numbered(text, n):
    """Strip 'N| ' prefixes, or None if the numbering did not come back intact.

    Strict on purpose: any non-empty line without a prefix, any duplicate or
    out-of-order index, any empty line body -> None, and the caller falls back.
    Alignment is never guessed at.
    """
    got, order = {}, []
    for line in text.split("\n"):
        if not line.strip():
            continue
        m = NUM_RE.match(line)
        if not m:
            return None
        idx, body = int(m.group(1)), m.group(2).strip()
        if idx in got or not body:
            return None
        got[idx] = body
        order.append(idx)
    if order != list(range(1, n + 1)):
        return None
    return "\n".join(got[i] for i in range(1, n + 1))


def nlines(text):
    """Non-blank line count -- the shape that has to match."""
    return len([l for l in text.split("\n") if l.strip()])


def tidy(text):
    """Drop blank lines and trailing space; what gets stored for a repaired block."""
    return "\n".join(l.rstrip() for l in text.split("\n") if l.strip())


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--track", default="3-TRANSFORMATIONS/Translations/Dharmamitra/en")
    p.add_argument("--sources", default="1-SOURCES/Text")
    p.add_argument("--lang", default="english")
    p.add_argument("--lang-tag", default="en")
    p.add_argument("--source-language", default="tibetan", choices=sorted(dm.SOURCE_LANG_FIELDS))
    p.add_argument("--focus", default="tibetan")
    p.add_argument("--attempts", type=int, default=3, help="tries per misshapen block")
    p.add_argument("--context-blocks", type=int, default=3)
    p.add_argument("--context-cap", type=int, default=3000)
    p.add_argument("--sleep", type=float, default=7.0,
                   help="seconds between calls; repair makes up to 4 calls per block, "
                        "so it trips the ~10/min public limit sooner than a batch run")
    p.add_argument("--timeout", type=int, default=90)
    p.add_argument("--retries", type=int, default=6)
    p.add_argument("--layout", default="parallel", choices=["parallel", "translation-only"])
    p.add_argument("--only-text", default=None, help="substring of one source filename")
    p.add_argument("--limit", type=int, default=0, help="stop after N repaired blocks")
    p.add_argument("--accept-closest", action="store_true",
                   help="if no attempt matches exactly, keep the closest instead of the original")
    p.add_argument("--redo-count-repairs", action="store_true",
                   help="also redo blocks last fixed by the weaker count-only protocol")
    p.add_argument("--report-only", action="store_true", help="list the work, make no API calls")
    args = p.parse_args()

    track = pathlib.Path(args.track)
    work = track / "work"
    if not work.is_dir():
        sys.exit(f"no ledger folder at {work}")

    style_md = track / "style.md"
    args.style = (style_md.read_text(encoding="utf-8").strip()
                  if style_md.exists() else dm.DEFAULT_STYLE)
    ch = track / "context-header.md"
    header_default = ch.read_text(encoding="utf-8").strip() if ch.exists() else ""

    # batching fields render() reports in frontmatter; repairs are always solo
    args.batch, args.batch_max_chars, args.payload_cap = 1, 0, 0

    srcs = sorted(pathlib.Path(args.sources).glob("*.md"))
    if args.only_text:
        srcs = [f for f in srcs if args.only_text in f.name]
        if not srcs:
            sys.exit(f"no source matched {args.only_text!r}")

    plan, fixed, failed, done_n = [], [], [], 0
    aborted = None

    for f in srcs:
        meta, units = dm.parse_source(f)
        blocks = [u for u in units if u["kind"] == "block" and u["id"]]
        led_path = work / f"{f.stem}-{args.lang_tag}.jsonl"
        recs = []
        if led_path.exists():
            recs = [json.loads(l) for l in
                    led_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        latest = {}
        for r in recs:
            latest[r["block_id"]] = r

        todo = []
        for b in blocks:
            r = latest.get(b["id"])
            want = nlines(b["text"])
            if r is None:
                todo.append((b, "missing", want, 0))
            elif nlines(r["translation"]) != want:
                todo.append((b, "misshapen", want, nlines(r["translation"])))
            elif (args.redo_count_repairs and r.get("repair_of")
                  and r.get("repair_protocol") != "numbered"):
                todo.append((b, "recount", want, nlines(r["translation"])))
        if todo:
            plan.append((f, led_path, meta, units, blocks, latest, todo))

    n_missing = sum(1 for _, _, _, _, _, _, t in plan for x in t if x[1] == "missing")
    n_shape = sum(1 for _, _, _, _, _, _, t in plan for x in t if x[1] == "misshapen")
    print(f"texts scanned      : {len(srcs)}")
    print(f"texts needing work : {len(plan)}")
    print(f"missing blocks     : {n_missing}")
    print(f"misshapen blocks   : {n_shape}")
    if args.report_only:
        for f, _, _, _, _, _, todo in plan:
            print(f"\n{f.name}")
            for b, kind, want, got in todo:
                print(f"   ^{b['id']:<5} {kind:10s} source {want} line(s), translation {got}")
        return
    if not plan:
        print("nothing to do")
        return

    for f, led_path, meta, units, blocks, latest, todo in plan:
        if aborted:
            break
        print(f"\n=== {f.name}  ({len(todo)} block(s)) ===")
        for b, kind, want, got in todo:
            if aborted or (args.limit and done_n >= args.limit):
                if not aborted:
                    print("limit reached")
                break
            prior = [latest[x["id"]] for x in blocks
                     if x["id"] in latest and x["id"] != b["id"]]
            header = header_default or (
                f"Work: {meta.get('title_in_english') or meta.get('title') or f.stem}. "
                f"A canonical Tibetan text; the blocks are translated in order.")
            ctx = dm.build_context(header, prior, b, [], args.context_blocks, args.context_cap)

            src_lines = [l for l in b["text"].split("\n") if l.strip()]
            best, best_gap, method, el = None, None, None, 0.0

            def attempt(protocol):
                """One call. Returns (translation, n_lines) or (None, None)."""
                nonlocal el
                if protocol == "numbered":
                    payload = number_source(src_lines)
                    clause = NUMBERED_CLAUSE.format(n=want)
                else:
                    payload, clause = b["text"], COUNT_CLAUSE.format(n=want)
                body = {"input_tibetan": "", "input_chinese": "", "input_pali": "",
                        "input_sanskrit": "", "context": ctx, "focus": args.focus,
                        "target_language": args.lang,
                        "style_instruction": args.style + clause}
                body[dm.SOURCE_LANG_FIELDS[args.source_language]] = payload
                t0 = time.time()
                try:
                    raw = dm.call_api(body, args.timeout, args.retries)
                except dm.DailyQuotaExceeded as exc:
                    raise Abort(f"DAILY QUOTA: {exc}") from exc
                except RuntimeError as exc:
                    raise Abort(str(exc)) from exc
                el = time.time() - t0
                out = parse_numbered(raw, want) if protocol == "numbered" else tidy(raw)
                if out is None:
                    return None, None
                return out, nlines(out)

            try:
              for protocol in ("numbered", "count"):
                tries = args.attempts if protocol == "numbered" else 1
                for k in range(1, tries + 1):
                    print(f"  ^{b['id']:<5} {kind:10s} want {want}, have {got}  "
                          f"{protocol}{k} … ", end="", flush=True)
                    out, n = attempt(protocol)
                    if out is None:
                        print(f"{el:.1f}s -> protocol not honoured")
                    else:
                        print(f"{el:.1f}s -> {n} line(s) {'OK' if n == want else ''}")
                        gap = abs(n - want)
                        if best is None or gap < best_gap:
                            best, best_gap, method = out, gap, protocol
                        if n == want:
                            break
                    if args.sleep:
                        time.sleep(args.sleep)
                if best is not None and best_gap == 0:
                    break
            except Abort as exc:
                aborted = str(exc)
                print(f"\n\nSTOPPED: {exc}\n"
                      "The ledger is intact and everything fixed so far is saved.\n"
                      "Wait a few minutes and re-run; repaired blocks are skipped.",
                      file=sys.stderr)
                break

            if best is None:
                failed.append((f.name, b["id"], want, got, "no response"))
                continue

            accept = (best_gap == 0) or (kind == "missing") or args.accept_closest
            if not accept:
                failed.append((f.name, b["id"], want, got, f"best attempt {nlines(best)} lines"))
                print(f"         kept original (no attempt matched {want} lines)")
                if args.sleep:
                    time.sleep(args.sleep)
                continue

            rec = {
                "block_id": b["id"], "heading": b["heading"], "source": b["text"],
                "translation": best, "target_language": args.lang, "focus": args.focus,
                "style_instruction": args.style + (
                    NUMBERED_CLAUSE if method == "numbered" else COUNT_CLAUSE
                ).format(n=want),
                "context": ctx, "endpoint": dm.ENDPOINT,
                "batch_size": 1, "batch_block_ids": [b["id"]], "batch_fallback": False,
                "repair_of": kind, "repair_target_lines": want,
                "repair_result_lines": nlines(best), "repair_protocol": method,
                "elapsed_s": round(el, 2),
                "ts": _dt.datetime.now().isoformat(timespec="seconds"),
            }
            with led_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            latest[b["id"]] = rec
            fixed.append((f.name, b["id"], want, got, nlines(best)))
            done_n += 1
            if args.sleep:
                time.sleep(args.sleep)

        # re-render this text from its updated ledger
        base = meta.get("title_in_english") or f.stem
        import re as _re
        slug = _re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:40] or \
            _re.sub(r'[/\\:*?"<>|]', "", f.stem).strip() or "text"
        ordered = [latest[b["id"]] for b in blocks if b["id"] in latest]
        dm.render(track / f"{slug}-{args.lang_tag}.md", units, ordered, meta, args,
                  f"1-SOURCES/Text/{f.name}")
        print(f"  re-rendered {slug}-{args.lang_tag}.md")

    print(f"\n=== repair summary ===")
    if aborted:
        print(f"RUN STOPPED EARLY     : {aborted}")
    print(f"blocks fixed          : {len(fixed)}")
    print(f"blocks left unfixed   : {len(failed)}")
    for r in failed:
        print(f"   {r[0][:34]:36s} ^{r[1]:<5} source {r[2]} lines — {r[4]}")


if __name__ == "__main__":
    main()
