#!/usr/bin/env python3
"""Upload a root-text translation to the backend API.

Usage:
    python3 upload_root_text_translation.py <source.md> [--output-dir <parser_output_dir>]

Example:
    python3 4-SYSTEM\\scripts\\upload_root_text_translation.py \
        "1-SOURCES\\Translations\\bo-བློ་ལྡན་ཤེས་རབ།.md"

Upload order:
    1. text     → POST /v2/texts                          → save text_id to source file
    2. edition  → POST /v2/texts/{text_id}/editions       → save edition_id to source file
    3. toc      → POST /v2/editions/{edition_id}/table-of-contents → save toc_id to source file
    4. alignment → POST /v2/editions/{edition_id}/alignments/{root_edition_id}
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

API_BASE = "http://13.250.189.160/v2"
DEFAULT_OUTPUT_DIR = Path(__file__).parent / "parser-root-text" / "output"

YAML_PROPS_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_yaml(path: Path) -> dict:
    try:
        import yaml
    except ImportError:
        raise SystemExit("PyYAML required: pip install pyyaml")
    text = path.read_bytes().replace(b"\x00", b"").decode("utf-8", errors="replace")
    m = YAML_PROPS_RE.match(text)
    if not m:
        raise ValueError(f"No YAML frontmatter in {path}")
    return yaml.safe_load(m.group(1)) or {}, text, m


def _patch_source_file(path: Path, updates: dict):
    """Write key: value pairs into the YAML frontmatter of a source .md file."""
    raw_bytes = path.read_bytes().replace(b"\x00", b"")
    content = raw_bytes.decode("utf-8", errors="replace").lstrip("﻿")

    lines = content.splitlines(keepends=True)

    # Find opening ---
    if not lines or lines[0].rstrip("\r\n") != "---":
        print(f"  WARN could not patch {path.name} — no YAML frontmatter found")
        return

    # Find closing ---
    close_idx = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            close_idx = i
            break
    if close_idx is None:
        print(f"  WARN could not patch {path.name} — no closing --- found")
        return

    # Detect line ending
    nl = "\r\n" if lines[0].endswith("\r\n") else "\n"

    # Update existing keys or collect new ones to append
    pending = {}
    for key, value in updates.items():
        found = False
        for i in range(1, close_idx):
            if re.match(rf"^{re.escape(key)}\s*:", lines[i]):
                lines[i] = f"{key}: {value}{nl}"
                found = True
                break
        if not found:
            pending[key] = value

    # Append new keys before closing ---
    for key, value in pending.items():
        lines.insert(close_idx, f"{key}: {value}{nl}")
        close_idx += 1

    path.write_bytes("".join(lines).encode("utf-8"))
    for key, value in updates.items():
        print(f"  PATCHED {path.name}: {key} = {value}")


def _resolve_path(val: str, from_path: Path) -> Path | None:
    """Resolve a relative vault path from the source file's location."""
    p = Path(val)
    for base in [from_path.parent, *from_path.parents]:
        candidate = base / p
        if candidate.exists():
            return candidate
    for base in from_path.parents:
        matches = list(base.rglob(p.name))
        if matches:
            return matches[0]
    return None


def _post(url: str, data: dict) -> dict:
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} {e.reason}\n{body_text}") from e


def _put(url: str, data: dict) -> dict:
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} {e.reason}\n{body_text}") from e


def _load_json(path: Path) -> dict:
    return json.loads(path.read_bytes().replace(b"\x00", b"").decode("utf-8", errors="replace"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Upload root-text translation to API")
    parser.add_argument("source", help="Path to the source .md file")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help=f"Parser output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"ERROR source file not found: {source_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)
    stem = source_path.stem

    # Locate parser output files
    text_file    = output_dir / f"{stem}.text.json"
    edition_file = output_dir / f"{stem}.edition.json"
    toc_file     = output_dir / f"{stem}.toc.json"
    align_file   = output_dir / f"{stem}.alignment.json"

    for f in [text_file, edition_file, toc_file, align_file]:
        if not f.exists():
            print(f"ERROR missing parser output: {f}", file=sys.stderr)
            print("Run the linter and parser first.", file=sys.stderr)
            sys.exit(1)

    # Read source YAML to get root_text path and its edition_id
    fm, _, _ = _read_yaml(source_path)
    root_text_val = fm.get("root_text")
    if not root_text_val:
        print("ERROR source file has no root_text property", file=sys.stderr)
        sys.exit(1)

    root_path = _resolve_path(str(root_text_val), source_path)
    if not root_path:
        print(f"ERROR could not resolve root_text: {root_text_val}", file=sys.stderr)
        sys.exit(1)

    root_fm, _, _ = _read_yaml(root_path)
    root_edition_id = root_fm.get("edition_id")
    if not root_edition_id:
        print(f"ERROR root text {root_path.name} has no edition_id — upload the root text first", file=sys.stderr)
        sys.exit(1)

    print(f"Source : {source_path}")
    print(f"Root   : {root_path.name}  (edition_id: {root_edition_id})")
    print()

    # -----------------------------------------------------------------------
    # 1. Upload text
    # -----------------------------------------------------------------------
    print("── 1. Uploading text ──────────────────────────────────────────")
    text_data = _load_json(text_file)
    try:
        resp = _post(f"{API_BASE}/texts", text_data)
        text_id = resp.get("id") or resp.get("text_id")
        if not text_id:
            raise RuntimeError(f"No id in response: {resp}")
        print(f"OK  text_id = {text_id}")
        _patch_source_file(source_path, {"text_id": text_id})
    except Exception as exc:
        print(f"ERROR uploading text: {exc}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # 2. Upload edition
    # -----------------------------------------------------------------------
    print()
    print("── 2. Uploading edition ───────────────────────────────────────")
    edition_data = _load_json(edition_file)
    try:
        resp = _post(f"{API_BASE}/texts/{text_id}/editions", edition_data)
        edition_id = resp.get("id") or resp.get("edition_id")
        if not edition_id:
            raise RuntimeError(f"No id in response: {resp}")
        print(f"OK  edition_id = {edition_id}")
        _patch_source_file(source_path, {"edition_id": edition_id})
    except Exception as exc:
        print(f"ERROR uploading edition: {exc}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # 3. Upload TOC
    # -----------------------------------------------------------------------
    print()
    print("── 3. Uploading TOC ───────────────────────────────────────────")
    toc_data = _load_json(toc_file)
    try:
        resp = _post(f"{API_BASE}/editions/{edition_id}/table-of-contents", toc_data)
        toc_id = resp.get("id") or resp.get("toc_id")
        if not toc_id:
            raise RuntimeError(f"No id in response: {resp}")
        print(f"OK  toc_id = {toc_id}")
        _patch_source_file(source_path, {"toc_id": toc_id})
    except Exception as exc:
        print(f"ERROR uploading TOC: {exc}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # 4. Upload alignment
    # -----------------------------------------------------------------------
    print()
    print("── 4. Uploading alignment ─────────────────────────────────────")
    align_data = _load_json(align_file)
    align_url = f"{API_BASE}/editions/{edition_id}/alignments/{root_edition_id}"
    print(f"  PUT {align_url}")
    try:
        resp = _put(align_url, align_data)
        print(f"OK  alignment uploaded")
        align_id = resp.get("id") or resp.get("alignment_id")
        if align_id:
            print(f"    alignment_id = {align_id}")
    except Exception as exc:
        print(f"ERROR uploading alignment: {exc}", file=sys.stderr)
        sys.exit(1)

    print()
    print("Done.")


if __name__ == "__main__":
    main()
