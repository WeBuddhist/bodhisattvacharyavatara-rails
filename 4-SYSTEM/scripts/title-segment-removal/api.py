#!/usr/bin/env python3
"""Thin client for the OpenPecha v2 library API (library.webuddhist.com).

Shared by snapshot.py / plan_removal.py / remove_titles.py / compare.py.

THE ONE RULE THAT MATTERS: reads are retried, writes are NEVER retried.
A content PATCH is not idempotent. A `delete` op whose response was lost in
transit has still been applied on the server, so re-sending it deletes the
*next* N characters instead. That happened once on the liturgy corpus
(2026-09-19, edition kIBLisYhjyIOw2NUno2Ul) and cost a manual repair. A failed
write is therefore left for the operator: re-running the planner re-reads the
live segmentation and decides again, which is the only safe resolution.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

BASE = os.environ.get("WEBUDDHIST_BASE", "https://library.webuddhist.com")


class ApiError(RuntimeError):
    def __init__(self, status, body, method, path):
        super().__init__(f"{method} {path} -> {status} {body[:200]}")
        self.status = status
        self.body = body


def request(method, path, body=None, timeout=90, attempts=4):
    """Perform one API call. Returns (status, parsed_json_or_None)."""
    idempotent = method == "GET"
    data = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    last = None
    for attempt in range(attempts):
        req = urllib.request.Request(BASE + path, data=data, method=method)
        if data:
            req.add_header("Content-Type", "application/json")
        key = os.environ.get("WEBUDDHIST_API_KEY", "")
        if key:
            req.add_header("X-API-Key", key)
        app = os.environ.get("WEBUDDHIST_APP", "")
        if app:
            req.add_header("X-Application", app)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read().decode()
                return r.status, (json.loads(raw) if raw.strip() else None)
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            if idempotent and e.code >= 500 and attempt < attempts - 1:
                last = ApiError(e.code, detail, method, path)
                time.sleep(1.5 * (attempt + 1))
                continue
            raise ApiError(e.code, detail, method, path) from None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            if idempotent and attempt < attempts - 1:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
    raise last


def get(path, **kw):
    return request("GET", path, **kw)[1]


def paged(path, limit=500):
    """Walk a `{items, has_more, offset, limit}` list endpoint to exhaustion."""
    out, offset = [], 0
    sep = "&" if "?" in path else "?"
    while True:
        d = get(f"{path}{sep}limit={limit}&offset={offset}")
        items = d["items"] if isinstance(d, dict) else d
        out.extend(items)
        if not isinstance(d, dict) or not d.get("has_more"):
            return out
        offset += len(items)
        if not items:
            return out


# --- resource helpers -------------------------------------------------------

def edition(eid):
    return get(f"/v2/editions/{eid}")


def content(eid):
    d = get(f"/v2/editions/{eid}/content")
    return d if isinstance(d, str) else (d or {}).get("content", "")


def segments(eid):
    return paged(f"/v2/editions/{eid}/segmentation/segments")


def segment_content(sid):
    d = get(f"/v2/segments/{sid}/content")
    return d if isinstance(d, str) else (d or {}).get("content", "")


def alignments(eid):
    return get(f"/v2/editions/{eid}/alignments") or []


def pairs(src, tgt):
    return paged(f"/v2/editions/{src}/alignments/{tgt}")


def text(tid):
    return get(f"/v2/texts/{tid}")


def toc(eid):
    return get(f"/v2/editions/{eid}/table-of-contents")


def delete_span(eid, start, end):
    """PATCH one delete op. NOT retried — see module docstring."""
    return request("PATCH", f"/v2/editions/{eid}/content",
                   {"type": "delete", "start": start, "end": end}, attempts=1)[0]


def insert_text(eid, position, text_):
    """PATCH one insert op — the repair path for a damaged edition."""
    return request("PATCH", f"/v2/editions/{eid}/content",
                   {"type": "insert", "position": position, "text": text_}, attempts=1)[0]
