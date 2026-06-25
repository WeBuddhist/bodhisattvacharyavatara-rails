#!/usr/bin/env python3
"""Parallel batch runner for commentary segmentation (Stage 0 + Stage 1).

Processes an entire directory of Tibetan commentary .md files in parallel,
running preclean_commentary.py (Stage 0, optional) then segment_commentary.py
(Stage 1) on each file. Skips files whose output already exists unless
--force is passed.

Stage 1 segments purely by botok (WordTokenizer + sentence_tokenizer)
sentence boundaries. Install once before running:
    pip install botok

Note: botok is pure Python and builds a trie on first init (~10-15 s) in each
worker process. For large batches this startup cost is paid once per worker.

Usage:
    python3 batch_segment.py INPUT_DIR OUTPUT_DIR [options]

Options:
    --preclean          Also run Stage 0 (preclean) before segmentation.
    --workers N         Parallel worker processes (default: CPU count).
    --force             Re-process files even if output already exists.
    --ext EXT           File extension to glob (default: .md).
    --reports DIR       Directory for TSV reports (default: OUTPUT_DIR/reports).
    --dry-run           Parse and validate but do not write any files.

Output layout:
    OUTPUT_DIR/<stem>.segmented.md      Stage-1 output (always produced)
    OUTPUT_DIR/reports/<stem>.segreport.tsv
    OUTPUT_DIR/reports/<stem>.preclean.tsv  (only when --preclean)
    OUTPUT_DIR/batch_summary.tsv            one row per file
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
# process() functions directly instead of spawning subprocesses — eliminates
# per-file Python startup overhead.
# ---------------------------------------------------------------------------
_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))
import preclean_commentary as preclean  # noqa: E402
import segment_commentary as segment    # noqa: E402


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

def _process_one(args):
    """Called in a worker process. Returns a dict of results for this file."""
    (input_path, output_dir, reports_dir, do_preclean,
     dry_run, force) = args

    inp = Path(input_path)
    stem = inp.stem  # e.g. "khenpo-namdrol-ch1"

    out_segmented = Path(output_dir) / f"{stem}.segmented.md"
    out_preclean  = Path(output_dir) / f"{stem}.preclean.md"
    rep_preclean  = Path(reports_dir) / f"{stem}.preclean.tsv"
    rep_segment   = Path(reports_dir) / f"{stem}.segreport.tsv"

    # Skip if output already exists
    if not force and out_segmented.exists():
        return {
            "file": inp.name, "status": "skipped",
            "segments": 0,
            "elapsed_s": 0.0, "error": "",
        }

    t0 = time.perf_counter()
    try:
        text = unicodedata.normalize("NFC", inp.read_text(encoding="utf-8"))

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

        # ---- Stage 1 (botok) ----
        segmented, report = segment.process(stage1_input)
        segment.assert_no_loss(stage1_input, segmented)

        n_segments = len(report)

        if not dry_run:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            Path(reports_dir).mkdir(parents=True, exist_ok=True)
            out_segmented.write_text(segmented, encoding="utf-8")
            rep_segment.write_text(
                "index\ttrigger\tsyllables\tpreview\n" +
                "".join(
                    "{}\t{}\t{}\t{}\n".format(
                        i, r["trigger"], r["syllables"], r["preview"]
                    )
                    for i, r in enumerate(report, 1)
                ),
                encoding="utf-8",
            )

        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ok",
            "segments": n_segments,
            "elapsed_s": round(elapsed, 3), "error": "",
        }

    except SystemExit as e:
        # assert_no_loss calls sys.exit() on failure — catch it here
        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ABORT",
            "segments": 0,
            "elapsed_s": round(elapsed, 3),
            "error": str(e),
        }
    except Exception as e:
        elapsed = time.perf_counter() - t0
        return {
            "file": inp.name, "status": "ERROR",
            "segments": 0,
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
    args = ap.parse_args(argv[1:])

    input_dir  = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    reports_dir = Path(args.reports) if args.reports else output_dir / "reports"

    files = sorted(input_dir.glob(f"*{args.ext}"))
    if not files:
        sys.exit(f"No {args.ext} files found in {input_dir}")

    print(f"Found {len(files)} files. Workers: {args.workers}. "
          f"Preclean: {args.preclean}.")

    tasks = [
        (str(f), str(output_dir), str(reports_dir),
         args.preclean, args.dry_run, args.force)
        for f in files
    ]

    # Use a pool only when workers > 1 to keep tracebacks readable in single-
    # worker mode (common during testing).
    t_start = time.perf_counter()
    if args.workers == 1:
        results = [_process_one(t) for t in tasks]
    else:
        with multiprocessing.Pool(processes=args.workers) as pool:
            results = list(pool.imap_unordered(_process_one, tasks, chunksize=8))
    elapsed_total = time.perf_counter() - t_start

    # ---- Write batch summary ----
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        summary_path = output_dir / "batch_summary.tsv"

        with summary_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=[
                "file", "status", "segments", "elapsed_s", "error",
            ], delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(results)

    # ---- Print summary ----
    n_ok      = sum(1 for r in results if r["status"] == "ok")
    n_skip    = sum(1 for r in results if r["status"] == "skipped")
    n_abort   = sum(1 for r in results if r["status"] in ("ABORT", "ERROR"))
    n_seg     = sum(r["segments"] for r in results)

    print(f"\n=== Batch complete in {elapsed_total:.1f}s ===")
    print(f"  Processed : {n_ok}")
    print(f"  Skipped   : {n_skip}  (already done; use --force to redo)")
    print(f"  Errors    : {n_abort}")
    print(f"  Segments  : {n_seg}")
    if n_abort:
        print("\n  ERRORS -- files not written:")
        for r in results:
            if r["status"] in ("ABORT", "ERROR"):
                print(f"    {r['file']}: {r['error']}")
    if not args.dry_run:
        print(f"\n  Summary  : {output_dir}/batch_summary.tsv")
    return 0 if n_abort == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
