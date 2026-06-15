#!/usr/bin/env python3
"""Upload a commentary reader document to the reading-app API.


python3 commentary_upload.py --instance-id <INSTANCE_ID> --dry-run   # preview payload
python3 commentary_upload.py --instance-id <INSTANCE_ID> --author-person-id P12345678 --api-key <KEY>


Reads a reader JSON file produced by ``build_reader_json.py`` (with
``metadata``, ``content``, and ``verse`` fields) and POSTs a commentary
payload to::

    POST {base-url}/v2/instances/{instance-id}/commentary

Field mapping from the reader JSON to the API payload:

- ``metadata.language``               -> ``language``
- ``content``                         -> ``content``
- ``metadata.title[language|en|*]``   -> ``title``
- ``metadata.cbeta`` / contributions  -> ``source`` (best-effort citation)
- ``--author-person-id`` (or the      -> ``author``
  ``author`` contribution's
  ``person_id``)
- ``verse[*].span``                   -> ``segmentation`` (``id`` dropped)
- ``metadata.copyright``              -> ``copyright``
- ``metadata.license``                -> ``license``
- ``--category-id`` (or               -> ``category_id``
  ``metadata.category_id``)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover - dependency check
    requests = None

DEFAULT_INPUT = (
    Path(__file__).resolve().parent.parent / "data/zh-隆蓮法師a.json"
)
DEFAULT_BASE_URL = "https://api-aq25662yyq-uc.a.run.app"
DEFAULT_PREVIEW_OUTPUT = Path(__file__).resolve().parent / "payloads/commentary_preview.json"


def _pick_title(metadata: dict) -> str | None:
    title = metadata.get("title")
    if isinstance(title, str):
        return title
    if isinstance(title, dict):
        language = metadata.get("language")
        if language and language in title:
            return title[language]
        if "en" in title:
            return title["en"]
        if title:
            return next(iter(title.values()))
    return None


def _pick_source(metadata: dict) -> str | None:
    parts: list[str] = []

    title = _pick_title(metadata)
    if title:
        parts.append(title)

    for contribution in metadata.get("contributions", []):
        if contribution.get("role") == "translator":
            name = contribution.get("name")
            if name:
                parts.append(name)

    if cbeta := metadata.get("cbeta"):
        parts.append(f"CBETA {cbeta}")

    if not parts:
        return None

    return ", ".join(parts)


def _pick_author(metadata: dict, person_id: str | None) -> dict | None:
    if person_id:
        return {"person_id": person_id}

    for contribution in metadata.get("contributions", []):
        if contribution.get("role") == "author":
            if author_person_id := contribution.get("person_id"):
                return {"person_id": author_person_id}
            if name := contribution.get("name"):
                return {"name": name}

    return None


def build_payload(
    document: dict,
    *,
    author_person_id: str | None = None,
    title: str | None = None,
    source: str | None = None,
    category_id: str | None = None,
) -> dict:
    metadata = document.get("metadata", {})

    payload: dict = {
        "language": metadata.get("language"),
        "content": document.get("content", ""),
    }

    if resolved_title := (title or _pick_title(metadata)):
        payload["title"] = resolved_title

    if resolved_source := (source or _pick_source(metadata)):
        payload["source"] = resolved_source

    if author := _pick_author(metadata, author_person_id):
        payload["author"] = author

    payload["segmentation"] = [
        {"span": verse["span"]} for verse in document.get("verse", [])
    ]

    if "copyright" in metadata:
        payload["copyright"] = metadata["copyright"]
    if "license" in metadata:
        payload["license"] = metadata["license"]

    if resolved_category_id := (category_id or metadata.get("category_id")):
        payload["category_id"] = resolved_category_id

    return _drop_empty_strings(payload)


def _drop_empty_strings(payload: dict) -> dict:
    """Remove top-level string fields that are empty.

    The API rejects empty strings (e.g. ``"source": ""``) with a 422
    "String should have at least 1 character" error, so any field that
    would otherwise resolve to ``""`` is omitted entirely instead.
    """
    return {
        key: value
        for key, value in payload.items()
        if not (isinstance(value, str) and value == "")
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Source reader JSON file (default: {DEFAULT_INPUT.name})",
    )
    parser.add_argument(
        "--instance-id",
        required=True,
        help="Target instance id, e.g. the value in "
        "/v2/instances/<instance-id>/commentary",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"API base URL (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--author-person-id",
        help="Override/author person id for the 'author' field "
        "(e.g. P12345678)",
    )
    parser.add_argument(
        "--title",
        help="Override the 'title' field (default: derived from metadata.title)",
    )
    parser.add_argument(
        "--source",
        help="Override the 'source' field (default: derived from metadata)",
    )
    parser.add_argument(
        "--category-id",
        help="Override the 'category_id' field "
        "(default: derived from metadata.category_id, e.g. CAT12345678)",
    )
    parser.add_argument(
        "--api-key",
        help="Bearer token / API key, sent as 'Authorization: Bearer <key>'",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write the payload as JSON instead of sending the request",
    )
    parser.add_argument(
        "--preview-output",
        type=Path,
        default=DEFAULT_PREVIEW_OUTPUT,
        help=f"Where to write the --dry-run payload JSON "
        f"(default: {DEFAULT_PREVIEW_OUTPUT})",
    )
    args = parser.parse_args()

    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
    except OSError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    payload = build_payload(
        document,
        author_person_id=args.author_person_id or None,
        title=args.title or None,
        source=args.source or None,
        category_id=args.category_id or None,
    )

    if args.dry_run:
        args.preview_output.parent.mkdir(parents=True, exist_ok=True)
        args.preview_output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote payload preview to {args.preview_output}")
        return

    if requests is None:
        print(
            "The 'requests' package is required to send the upload "
            "(install it, or use --dry-run to inspect the payload).",
            file=sys.stderr,
        )
        sys.exit(1)

    url = f"{args.base_url.rstrip('/')}/v2/instances/{args.instance_id}/commentary"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    if args.api_key:
        headers["Authorization"] = f"Bearer {args.api_key}"

    response = requests.post(url, headers=headers, json=payload)
    print(f"POST {url} -> {response.status_code}")
    try:
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(response.text)

    response.raise_for_status()


if __name__ == "__main__":
    main()
