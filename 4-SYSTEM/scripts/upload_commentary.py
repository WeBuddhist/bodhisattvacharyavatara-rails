#!/usr/bin/env python3
"""Upload a commentary to the backend API (parser-commentary payloads).

Usage:
    python3 upload_commentary.py <source.md> [--output-dir <dir>] [--dry-run] [--resume]

Example:
    python3 4-SYSTEM/scripts/upload_commentary.py \
        "1-SOURCES/Commentaries/formated_commentary/BCAC10_PKM_bo_segmented 1.md" --dry-run

Prerequisites:
    - linter-commentary/lint_commentary.py and parser-commentary/parser_commentary.py
      have been run, so <stem>.{text,edition,toc,alignment}.json exist
    - the commentary's `root_text` file already has an `edition_id` (upload it first)

Upload order (same as upload_root_text_translation.py):
    1. text      -> POST /v2/texts                                        -> text_id
    2. edition   -> POST /v2/texts/{text_id}/editions                     -> edition_id
    3. toc       -> POST /v2/editions/{edition_id}/table-of-contents      -> toc_id
    4. alignment -> PUT  /v2/editions/{edition_id}/alignments/{root_edition_id}

Each returned id is written back to the commentary's frontmatter.

Safety:
    - Refuses files whose file_type is not `commentary`.
    - Refuses if text_id / edition_id / toc_id are already set (a re-run would create
      duplicate records). Use --resume to continue a partly finished upload: steps whose
      id is already in the frontmatter are skipped.
    - --dry-run checks everything and prints the plan without calling the API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from upload_root_text_translation import (
    API_BASE,
    _load_json,
    _patch_source_file,
    _post,
    _put,
    _read_yaml,
    _resolve_path,
)

DEFAULT_OUTPUT_DIR = Path(__file__).parent / "parser-commentary" / "output"


def _fail(msg: str) -> None:
    print(f"ERROR {msg}", file=sys.stderr)
    sys.exit(1)


def _blank(val) -> bool:
    return val is None or str(val).strip() == ""


def main():
    ap = argparse.ArgumentParser(description="Upload a commentary to the API")
    ap.add_argument("source", help="Path to the commentary source .md file")
    ap.add_argument(
        "--output-dir",
        default=None,
        help=f"Parser output directory (default: {DEFAULT_OUTPUT_DIR}/<stem>/ if it exists, else {DEFAULT_OUTPUT_DIR})",
    )
    ap.add_argument("--dry-run", action="store_true", help="Validate and print the plan; no API calls")
    ap.add_argument("--resume", action="store_true", help="Skip steps whose id is already in the frontmatter")
    args = ap.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        _fail(f"source file not found: {source_path}")

    stem = source_path.stem
    if args.output_dir:
        output_dir = Path(args.output_dir)
    elif (DEFAULT_OUTPUT_DIR / stem).is_dir():
        output_dir = DEFAULT_OUTPUT_DIR / stem
    else:
        output_dir = DEFAULT_OUTPUT_DIR
    files = {
        "text": output_dir / f"{stem}.text.json",
        "edition": output_dir / f"{stem}.edition.json",
        "toc": output_dir / f"{stem}.toc.json",
        "alignment": output_dir / f"{stem}.alignment.json",
    }
    for f in files.values():
        if not f.exists():
            print(f"ERROR missing parser output: {f}", file=sys.stderr)
            _fail("run lint_commentary.py and parser_commentary.py first")

    fm, _, _ = _read_yaml(source_path)
    if fm.get("file_type") != "commentary":
        _fail(f"file_type is {fm.get('file_type')!r}, expected 'commentary' "
              "(use upload_root_text_translation.py for other types)")

    ids = {k: fm.get(k) for k in ("text_id", "edition_id", "toc_id")}
    already = [k for k, v in ids.items() if not _blank(v)]
    if already and not args.resume:
        _fail(f"{', '.join(already)} already set in frontmatter — re-uploading would create duplicates. "
              "Use --resume to continue a partial upload.")

    text_data = _load_json(files["text"])
    if _blank(text_data.get("commentary_of")):
        _fail("text.json has no commentary_of — set root_text in the frontmatter and re-run the linter and parser")

    root_text_val = fm.get("root_text")
    if _blank(root_text_val):
        _fail("source file has no root_text property")
    root_path = _resolve_path(str(root_text_val), source_path)
    if not root_path:
        _fail(f"could not resolve root_text: {root_text_val}")
    root_fm, _, _ = _read_yaml(root_path)
    root_edition_id = root_fm.get("edition_id")
    if _blank(root_edition_id):
        _fail(f"root text {root_path.name} has no edition_id — upload the root text first")

    print(f"Source : {source_path}")
    print(f"Root   : {root_path.name}  (edition_id: {root_edition_id})")
    print(f"API    : {API_BASE}")
    print(f"Payload: {output_dir}")
    print(f"commentary_of: {text_data['commentary_of']}")
    print()

    plan = [
        ("text", ids["text_id"]),
        ("edition", ids["edition_id"]),
        ("toc", ids["toc_id"]),
        ("alignment", None),
    ]
    if args.dry_run:
        print("Dry run — no API calls. Would perform:")
        for name, existing in plan:
            action = "SKIP (id already set)" if not _blank(existing) else "UPLOAD"
            print(f"  {action:22} {name}  <- {files[name].name}")
        return

    # 1. text
    text_id = ids["text_id"]
    if _blank(text_id):
        print("── 1. Uploading text ──────────────────────────────────────────")
        try:
            resp = _post(f"{API_BASE}/texts", text_data)
            text_id = resp.get("id") or resp.get("text_id")
            if not text_id:
                raise RuntimeError(f"No id in response: {resp}")
        except Exception as exc:
            _fail(f"uploading text: {exc}")
        print(f"OK  text_id = {text_id}")
        _patch_source_file(source_path, {"text_id": text_id})
    else:
        print(f"── 1. text: skipped (text_id = {text_id})")

    # 2. edition
    edition_id = ids["edition_id"]
    if _blank(edition_id):
        print("── 2. Uploading edition ───────────────────────────────────────")
        try:
            resp = _post(f"{API_BASE}/texts/{text_id}/editions", _load_json(files["edition"]))
            edition_id = resp.get("id") or resp.get("edition_id")
            if not edition_id:
                raise RuntimeError(f"No id in response: {resp}")
        except Exception as exc:
            _fail(f"uploading edition: {exc}")
        print(f"OK  edition_id = {edition_id}")
        _patch_source_file(source_path, {"edition_id": edition_id})
    else:
        print(f"── 2. edition: skipped (edition_id = {edition_id})")

    # 3. toc
    toc_id = ids["toc_id"]
    if _blank(toc_id):
        print("── 3. Uploading TOC ───────────────────────────────────────────")
        try:
            resp = _post(f"{API_BASE}/editions/{edition_id}/table-of-contents", _load_json(files["toc"]))
            toc_id = resp.get("id") or resp.get("toc_id")
            if not toc_id:
                raise RuntimeError(f"No id in response: {resp}")
        except Exception as exc:
            _fail(f"uploading TOC: {exc}")
        print(f"OK  toc_id = {toc_id}")
        _patch_source_file(source_path, {"toc_id": toc_id})
    else:
        print(f"── 3. toc: skipped (toc_id = {toc_id})")

    # 4. alignment (PUT is idempotent, so it always runs)
    print("── 4. Uploading alignment ─────────────────────────────────────")
    align_url = f"{API_BASE}/editions/{edition_id}/alignments/{root_edition_id}"
    print(f"  PUT {align_url}")
    try:
        resp = _put(align_url, _load_json(files["alignment"]))
    except Exception as exc:
        _fail(f"uploading alignment: {exc}")
    print("OK  alignment uploaded")
    align_id = resp.get("id") or resp.get("alignment_id")
    if align_id:
        print(f"    alignment_id = {align_id}")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
