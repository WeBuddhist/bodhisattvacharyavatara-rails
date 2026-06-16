#!/usr/bin/env python3
"""Upload an alignment annotation to the reading-app API.


python3 alignment_upload.py --instance-id <INSTANCE_ID> \
    --target-manifestation-id <MNF_ID> --dry-run   # preview payload
python3 alignment_upload.py --instance-id <INSTANCE_ID> \
    --target-manifestation-id <MNF_ID> --api-key <KEY>


Reads a reader JSON file produced by ``build_reader_json.py`` (with an
``alignment`` array of
``{"alignment_annotation": {"span": {...}}, "target_annotation": [{"span": {...}}, ...]}``
entries) and POSTs an alignment annotation payload to::

    POST {base-url}/v2/annotations/{instance-id}/annotation

Field mapping from the reader JSON to the API payload:

- ``"alignment"``                                  -> ``type: "alignment"``
- ``--target-manifestation-id``                    -> ``target_manifestation_id``
- ``alignment[*].target_annotation[*].span``       -> ``target_annotation``
  (deduplicated, each given a sequential ``index``)
- ``alignment[*].alignment_annotation.span``       -> ``alignment_annotation``
  (each given a sequential ``index`` and the ``alignment_index`` values of
  its corresponding ``target_annotation`` entries)
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
DEFAULT_PREVIEW_OUTPUT = Path(__file__).resolve().parent / "payloads/alignment_preview.json"


def _alignment_span(entry: dict) -> dict | None:
    """Return the root span for one alignment entry.

    Reader JSON may store ``alignment_annotation`` as either a single
    ``{"span": ...}`` object (translation alignments) or a list of span
    objects (commentary alignments with multiple root verses).  Lists are
    merged to min-start / max-end.
    """
    aa = entry.get("alignment_annotation")
    if isinstance(aa, list):
        spans = [item["span"] for item in aa if item.get("span")]
        if not spans:
            return None
        return {
            "start": min(s["start"] for s in spans),
            "end": max(s["end"] for s in spans),
        }
    if isinstance(aa, dict) and aa.get("span"):
        return dict(aa["span"])
    return None


def build_payload(document: dict, *, target_manifestation_id: str) -> dict:
    alignment = document.get("alignment", [])

    target_annotation: list[dict] = []
    target_index_by_span: dict[tuple[int, int], int] = {}
    alignment_annotation: list[dict] = []

    for align_index, entry in enumerate(alignment):
        alignment_index: list[int] = []

        for target in entry.get("target_annotation", []):
            span = target["span"]
            key = (span["start"], span["end"])
            target_index = target_index_by_span.get(key)
            if target_index is None:
                target_index = len(target_annotation)
                target_index_by_span[key] = target_index
                target_annotation.append({"span": span, "index": target_index})
            alignment_index.append(target_index)

        span = _alignment_span(entry)
        if span is None:
            continue

        alignment_annotation.append(
            {
                "span": span,
                "index": align_index,
                "alignment_index": alignment_index,
            }
        )

    return {
        "type": "alignment",
        "target_manifestation_id": target_manifestation_id,
        "target_annotation": target_annotation,
        "alignment_annotation": alignment_annotation,
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
        "/v2/annotations/<instance-id>/annotation",
    )
    parser.add_argument(
        "--target-manifestation-id",
        required=True,
        help="The 'target_manifestation_id' field (e.g. MNF12345678)",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"API base URL (default: {DEFAULT_BASE_URL})",
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
        target_manifestation_id=args.target_manifestation_id,
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

    url = f"{args.base_url.rstrip('/')}/v2/annotations/{args.instance_id}/annotation"
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
