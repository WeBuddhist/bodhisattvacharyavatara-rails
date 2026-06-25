#!/usr/bin/env python3
"""Parallel batch runner for commentary segmentation (Stage 0 + Stage 1).

Processes an entire directory of Tibetan commentary .md files in parallel,
running preclean_commentary.py (Stage 0, optional) then segment_commentary.py
(Stage 1) on each file. Skips files whose output already exists unless
--force is passed.

Usage:
    python3 batch_segment.py INPUT_DIR OUTPUT_DIR [options]

Options:
    --preclean          Also run Stage 0 (preclean) before segmentation.
    --max-syllables N   Syllable cap passed to segment_commentary (default 40).
    --workers N         Parallel worker processes (default: CPU count).
    --force             Re-process files even if output already exists.
    --ext EXT           File extension to glob (default: .md).
    --reports DIR       Directory for TSV reports (default: OUTPUT_DIR/reports).
    --dry-run           Parse and validate but do not write any files.

Output layout:
    OUTPUT_DIR/<stem>.md                Stage-1 output (same name as source)
    OUTPUT_DIR/reports/<stem>.segreport.tsv
    OUTPUT_DIR/reports/<stem>.preclean.tsv  (only when --preclean)
    OUTPUT_DIR/batch_summary.tsv            one row per file
    OUTPUT_DIR/batch_flagged.tsv            only STAGE2_REVIEW rows, all files
"""
from __future__ import annotations

import argparse
import csv
import multiprocessing
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Import the two stage modules from the same directory so we can call their
# process() functions directly instead of spawning subprocesses -- eliminates
# per-file Python startup overhead.
# Always load from .py source (bypasses stale __pycache__ .pyc files).
# ---------------------------------------------------------------------------
import types as _types

def _load_source(name, path):
    """Load a module from a .py file, bypassing __pycache__."""
    src = Path(path).read_text(encoding="utf-8")
    mod = _types.ModuleType(name)
    mod.__file__ = str(path)
    exec(compile(src, str(path), "exec"), mod.__dict__)
    return mod

_HERE = Path(__file__).parent
preclean = _load_source("preclean_commentary", _HERE / "preclean_commentary.py")
segment  = _load_source("segment_commentary",  _HERE / "segment_commentary.py")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^(---\r?\n)(.*?)(^---\r?\n)", re.DOTALL | re.MULTILINE)

def _inject_status(text: str, status: str = "segmented") -> str:
    """Add or update 'status: <value>' in the YAML front matter."""
    m = _FM_RE.match(text)
    if m:
        fence_open, body, fence_close = m.group(1), m.group(2), m.group(3)
        if re.search(r"^status\s*:", body, re.MULTILINE):
            body = re.sub(r"^status\s*:.*$", f"status: {status}", body,
                          flags=re.MULTILINE)
        else:
            body = body.rstrip("\n") + f"\nstatus: {status}\n"
        return fence_open + body + fence_close + text[m.end():]
    else:
        return f"---\nstatus: {status}\n---\n\n" + text


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

def _process_one(args):
    """Called in a worker process. Returns a dict of results for this file."""
    (input_path, output_dir, reports_dir, do_preclean,
     max_syllables, dry_run, force) = args

    inp = Path(input_path)
    stem = inp.stem

    out_segmented = Path(output_dir) / f"{stem}.md"
    out_preclean  = Path(output_dir) / f"{stem}.preclean.md"
    rep_preclean  = Path(reports_dir) / f"{stem}.preclean.tsv"
    rep_segment   = Path(reports_dir) / f"{stem}.segreport.tsv"

    if not force and out_segmented.exists():
        return {
            "file": inp.name, "status": "skipped",
            "segments": 0, "flagged": 0,
            "quote_open": 0, "quote_close": 0, "quote_status": "",
            "elapsed_s": 0.0, "error": "",
        }

    t0 = time.perf_counter()
    try:
        text = unicodedata.normalize("NFC", inp.read_text(encoding="utf-8", errors="replace"))

        # ---- Stage 0 (optional) ----
        if do_preclean:
            cleaned, blocks, stats, expected_body = preclean.process(text)
            preclean.assert_no_loss(expected_body, cleaned)
            if not dry_run:
                Path(reports_dir).mkdir(parents=True, exist_ok=True)
                rep_preclean.write_text(
                    "index\tkind\tsyllables\tpreview\n" +
                    "".join(
                        "{}\t{}\t{}\t{}\n".format(
                            i, kind,
                            preclean.count_syllables(txt),
                            txt.strip()[:80].replace("\t", " ").replace("\n", "/")
                        )
                        for i, (kind, txt) in enumerate(blocks, 1)
                    ),
                    encoding="utf-8",
                )
            stage1_input = cleaned
        else:
            stage1_input = text

        # ---- Stage 1 ----
        segmented, report = segment.process(stage1_input, max_syllables)
        segment.assert_no_loss(stage1_input, segmented)

        n_segments   = len(report)
        n_flagged    = sum(1 for r in report if r["flag"])
        n_quote_open = sum(1 for r in report if r["trigger"].startswith("quote-open"))
        n_quote_close= sum(1 for r in report if r["trigger"].startswith("quote-close"))
        quote_status = "OK" if n_quote_open == n_quote_close else "MISMATCH"

        if not dry_run:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            Path(reports_dir).mkdir(parents=True, exist_ok=True)
            out_segmented.write_text(_inject_status(segmented), encoding="utf-8")
            rep_segment.write_text(
                "index\ttrigger\tsyllables\tflag\tpreview\n" +
                "".join(
                    "{}\t{}\t{}\t{}\t{}\n".format(
                        i, r["trigger"], r["syllables"], r["flag"], r["preview"]
                    )
                    for i, r in enumerate(report, 1)
                ) +
                f"SUMMARY\tquote-balance\t{n_quote_open}\t{quote_status}"
                f"\topen={n_quote_open} close={n_quote_close}\n",
                encoding="utf-8",
            )

        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ok",
            "segments": n_segments, "flagged": n_flagged,
            "quote_open": n_quote_open, "quote_close": n_quote_close,
            "quote_status": quote_status,
            "elapsed_s": round(elapsed, 3), "error": "",
            "_report": report,
        }

    except SystemExit as e:
        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ABORT",
            "segments": 0, "flagged": 0,
            "quote_open": 0, "quote_close": 0, "quote_status": "",
            "elapsed_s": round(elapsed, 3),
            "error": str(e),
        }
    except Exception as e:
        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ERROR",
            "segments": 0, "flagged": 0,
            "quote_open": 0, "quote_close": 0, "quote_status": "",
            "elapsed_s": round(elapsed, 3),
            "error": repr(e),
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input_dir",  help="Directory of .md commentary files to process")
    ap.add_argument("output_dir", help="Directory to write segmented output files")
    ap.add_argument("--preclean",       action="store_true",
                    help="Run Stage 0 (preclean) before segmentation")
    ap.add_argument("--max-syllables",  type=int, default=40,
                    help="Syllable cap for segment_commentary (default 40)")
    ap.add_argument("--workers", "-j",  type=int,
                    default=max(1, (os.cpu_count() or 1)),
                    help="Parallel worker processes (default: all CPUs)")
    ap.add_argument("--force",          action="store_true",
                    help="Re-process files even if output already exists")
    ap.add_argument("--ext",            default=".md",
                    help="File extension to glob (default: .md)")
    ap.add_argument("--reports",        default=None,
                    help="Directory for TSV reports (default: OUTPUT_DIR/reports)")
    ap.add_argument("--dry-run",        action="store_true",
                    help="Validate but do not write any output files")
    ap.add_argument("--files", nargs="+", metavar="FILENAME",
                    help="Process only these filenames (names only, not paths)")
    args = ap.parse_args(argv[1:])

    input_dir  = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    reports_dir = Path(args.reports) if args.reports else output_dir / "reports"

    files = sorted(input_dir.glob(f"*{args.ext}"))
    if args.files:
        wanted = set(args.files)
        files = [f for f in files if f.name in wanted]
    if not files:
        sys.exit(f"No {args.ext} files found in {input_dir}")

    print(f"Found {len(files)} files. Workers: {args.workers}. "
          f"Preclean: {args.preclean}. Max syllables: {args.max_syllables}.")

    tasks = [
        (str(f), str(output_dir), str(reports_dir),
         args.preclean, args.max_syllables, args.dry_run, args.force)
        for f in files
    ]

    t_start = time.perf_counter()
    if args.workers == 1:
        results = [_process_one(t) for t in tasks]
    else:
        with multiprocessing.Pool(processes=args.workers) as pool:
            results = list(pool.imap_unordered(_process_one, tasks, chunksize=8))
    elapsed_total = time.perf_counter() - t_start

    flagged_rows = []
    for res in results:
        if res.get("_report"):
            for i, r in enumerate(res["_report"], 1):
                if r["flag"]:
                    flagged_rows.append({
                        "file": res["file"], "index": i,
                        "trigger": r["trigger"], "syllables": r["syllables"],
                        "flag": r["flag"], "preview": r["preview"],
                    })

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        summary_path = output_dir / "batch_summary.tsv"
        flagged_path = output_dir / "batch_flagged.tsv"

        with summary_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=[
                "file", "status", "segments", "flagged",
                "quote_open", "quote_close", "quote_status",
                "elapsed_s", "error",
            ], delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(results)

        with flagged_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=[
                "file", "index", "trigger", "syllables", "flag", "preview",
            ], delimiter="\t")
            w.writeheader()
            w.writerows(flagged_rows)

    n_ok      = sum(1 for r in results if r["status"] == "ok")
    n_skip    = sum(1 for r in results if r["status"] == "skipped")
    n_abort   = sum(1 for r in results if r["status"] in ("ABORT", "ERROR"))
    n_flagged = sum(r["flagged"] for r in results)
    n_seg     = sum(r["segments"] for r in results)
    mismatches= [r["file"] for r in results if r.get("quote_status") == "MISMATCH"]

    print(f"\n=== Batch complete in {elapsed_total:.1f}s ===")
    print(f"  Processed : {n_ok}")
    print(f"  Skipped   : {n_skip}  (already done; use --force to redo)")
    print(f"  Errors    : {n_abort}")
    print(f"  Segments  : {n_seg}")
    print(f"  STAGE2_REVIEW flags : {n_flagged}")
    if mismatches:
        print(f"  Quote MISMATCHES ({len(mismatches)}) -- check citations:")
        for f in mismatches[:20]:
            print(f"    {f}")
        if len(mismatches) > 20:
            print(f"    ... and {len(mismatches)-20} more (see batch_summary.tsv)")
    if n_abort:
        print("\n  ERRORS -- files not written:")
        for r in results:
            if r["status"] in ("ABORT", "ERROR"):
                print(f"    {r['file']}: {r['error']}")
    if not args.dry_run:
        print(f"\n  Summary  : {output_dir}/batch_summary.tsv")
        print(f"  Flagged  : {output_dir}/batch_flagged.tsv")
    return 0 if n_abort == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
