#!/usr/bin/env python3
"""Lint source text/edition document info against the API schemas.

On success: writes a valid JSON payload to output/<stem>.json.
On failure: writes a failure report to output/<stem>.errors.json.

Usage:
    python lint_text_input.py [path/to/file.md ...]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from constants import (
    load_languages, LANGUAGE_VALUES, LANGUAGE_CODE_TO_NAME, LANG_TAG_MAP,
)
from validate import validate_text_input, validate_edition, validate_toc, resolve_language
from build import write_output, write_edition_output

YAML_PROPS_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


def extract_doc_info(path):
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("PyYAML is required: pip install pyyaml") from exc
    text = path.read_text(encoding="utf-8", errors="replace")
    match = YAML_PROPS_RE.match(text)
    if not match:
        return None, None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from exc
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise ValueError("document info must be a YAML mapping")
    body = text[match.end():]
    return data, body


def patch_source_file(path, updates):
    text = path.read_text(encoding="utf-8", errors="replace")
    match = YAML_PROPS_RE.match(text)
    if not match:
        return []
    block = match.group(1)
    block_start = 4  # len("---\n")
    changes = []
    new_block = block
    for field, value in updates.items():
        field_re = re.compile(r'^(' + re.escape(field) + r'\s*:)(.*)$', re.MULTILINE)
        existing = field_re.search(new_block)
        if existing:
            old_val = existing.group(2).strip()
            new_line = f"{existing.group(1)} {value}"
            new_block = new_block[:existing.start()] + new_line + new_block[existing.end():]
            changes.append(f"{field}: {old_val!r} -> {value!r}")
        else:
            new_block = new_block + f"\n{field}: {value}"
            changes.append(f"{field}: (missing) -> {value!r}")
    if not changes:
        return []
    new_text = text[:block_start] + new_block + text[block_start + len(block):]
    path.write_text(new_text, encoding="utf-8", errors="replace")
    return changes


def _resolve_root_text_path(val, source_path):
    val_path = Path(val)
    for base in [source_path.parent, *source_path.parents]:
        candidate = base / val_path
        if candidate.exists():
            return candidate
    name = val_path.name
    for base in source_path.parents:
        matches = list(base.rglob(name))
        if matches:
            return matches[0]
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate source document against the TextInput / Edition schema."
    )
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to lint")
    args = parser.parse_args(argv)
    if not args.paths:
        parser.print_help()
        return 0

    load_languages()
    had_errors = False

    for path in args.paths:
        if not path.exists():
            print(f"ERROR {path}: file not found", file=sys.stderr)
            had_errors = True
            continue
        try:
            doc_info, body = extract_doc_info(path)
        except ValueError as exc:
            print(f"ERROR {path}: {exc}", file=sys.stderr)
            had_errors = True
            continue
        if doc_info is None:
            print(f"ERROR {path}: no YAML properties block found", file=sys.stderr)
            had_errors = True
            continue

        file_type = doc_info.get("file_type", "")

        # For translations: resolve root_text -> translation_of, category_id before validation
        if file_type == "translation" and not doc_info.get("translation_of"):
            root_text_val = doc_info.get("root_text")
            if root_text_val:
                resolved_root = _resolve_root_text_path(str(root_text_val), path)
                if resolved_root:
                    try:
                        root_info, _ = extract_doc_info(resolved_root)
                        if root_info:
                            root_file_type = root_info.get("file_type", "")
                            if root_file_type:
                                doc_info["_root_file_type"] = root_file_type
                                print(f"  INFO root_text file_type: {root_file_type!r}")
                            else:
                                print(f"  WARN root_text {resolved_root.name}: file_type not set", file=sys.stderr)
                            trans_of = root_info.get("text_id")
                            if trans_of:
                                doc_info["translation_of"] = str(trans_of)
                            else:
                                print(f"  WARN root_text {resolved_root.name}: no text_id found to set translation_of", file=sys.stderr)
                            if not doc_info.get("category_id"):
                                cat_id = root_info.get("category_id")
                                if cat_id:
                                    doc_info["category_id"] = str(cat_id)
                    except (ValueError, OSError) as exc:
                        print(f"  WARN root_text: could not read {resolved_root}: {exc}", file=sys.stderr)
                else:
                    print(f"  WARN root_text: {root_text_val!r} could not be resolved to a file", file=sys.stderr)

        if file_type in ("root-text", "edition", "translation"):
            items = validate_text_input(doc_info)
            items += validate_edition(doc_info, body)
            items += validate_toc(doc_info, body)
            out_path, person_warnings, resolved_author, resolved_title, resolved_bdrc_work_id = \
                write_edition_output(path, doc_info, items)
            errors = [(l, m) for l, m in items if l == "ERROR"]
            infos  = [(l, m) for l, m in items if l == "INFO"]
            warns  = [(l, m) for l, m in items if l == "WARN"]

            patches = {}
            raw_lang = doc_info.get("language", "")
            vault_tag = doc_info.get("lang_tag")
            code, _ = resolve_language(raw_lang) if raw_lang else (None, None)
            if code:
                if raw_lang in LANGUAGE_VALUES:
                    patches["language"] = LANGUAGE_CODE_TO_NAME[code]
                if not vault_tag or vault_tag != code:
                    patches["lang_tag"] = code
            elif vault_tag and vault_tag in LANGUAGE_VALUES:
                patches["language"] = LANGUAGE_CODE_TO_NAME[vault_tag]
            raw_author = (
                doc_info.get("author")
                or doc_info.get("author in English")
                or doc_info.get("author_in_english")
            )
            if resolved_author and raw_author and resolved_author.strip() != str(raw_author).strip():
                patches["author"] = resolved_author
            if resolved_bdrc_work_id and not doc_info.get("bdrc_work_id") and not doc_info.get("bdrc"):
                patches["bdrc_work_id"] = resolved_bdrc_work_id
            source_changes = patch_source_file(path, patches)

            if errors:
                had_errors = True
                print(f"FAIL  {path}  ->  {out_path}")
                for _, msg in errors:
                    print(f"  ERROR {msg}")
            else:
                print(f"OK    {path}  ->  {out_path}")
                for _, msg in infos:
                    print(f"  INFO {msg}")
            for _, msg in warns:
                print(f"  WARN {msg}")
            if source_changes:
                print(f"  PATCHED source: {', '.join(source_changes)}")
            if person_warnings:
                for w in person_warnings:
                    print(f"  WARN {w}")
        else:
            items = validate_text_input(doc_info)
            out_path, person_warnings, resolved_author, resolved_title, resolved_bdrc_work_id = \
                write_output(path, doc_info, items)

            errors = [(l, m) for l, m in items if l == "ERROR"]
            infos  = [(l, m) for l, m in items if l == "INFO"]

            patches = {}
            raw_lang = doc_info.get("language", "")
            vault_tag = doc_info.get("lang_tag")
            code, _ = resolve_language(raw_lang) if raw_lang else (None, None)
            if code:
                if raw_lang in LANGUAGE_VALUES:
                    patches["language"] = LANGUAGE_CODE_TO_NAME[code]
                if not vault_tag or vault_tag != code:
                    patches["lang_tag"] = code
            elif vault_tag and vault_tag in LANGUAGE_VALUES:
                patches["language"] = LANGUAGE_CODE_TO_NAME[vault_tag]
            raw_author = (
                doc_info.get("author")
                or doc_info.get("author in English")
                or doc_info.get("author_in_english")
            )
            if resolved_author and raw_author and resolved_author.strip() != str(raw_author).strip():
                patches["author"] = resolved_author
            if resolved_bdrc_work_id and not doc_info.get("bdrc_work_id") and not doc_info.get("bdrc"):
                patches["bdrc_work_id"] = resolved_bdrc_work_id
            source_changes = patch_source_file(path, patches)

            if errors:
                had_errors = True
                print(f"FAIL  {path}  ->  {out_path}")
                for _, msg in errors:
                    print(f"  ERROR {msg}")
            else:
                print(f"OK    {path}  ->  {out_path}")
                for _, msg in infos:
                    print(f"  INFO {msg}")
            if source_changes:
                print(f"  PATCHED source: {', '.join(source_changes)}")
            if person_warnings:
                for w in person_warnings:
                    print(f"  WARN {w}")

    sys.exit(1 if had_errors else 0)


if __name__ == "__main__":
    main()
