#!/usr/bin/env python3
"""Verbatim copy of the backend's span arithmetic, so the plan can be simulated
offline and the prediction checked against what the server actually did.

Source: webuddhist-library/openpecha-backend/database/span_database.py,
commit cd1c205 (the commit running live as OpenPecha API v2 2.11.2).
`verify_vendored_copy()` re-reads that file when the checkout is present and
raises if this copy has drifted — the whole method rests on these branches being
byte-identical to the server's, so a silent divergence must fail loudly.

Note the BRANCH ORDER. It is not a set of independent predicates: a zero-length
span sitting exactly on a delete boundary is caught by branch 1 or 2 and
survives, even though the "fully encompassed" test in branch 3 would also match
it. en-Wallace has exactly such a degenerate TOC section, so this is not
hypothetical.
"""

from __future__ import annotations

import hashlib
import os

# --- BEGIN verbatim block (span_database.py lines 31-47) --------------------

def _adjust_span_for_delete(start: int, end: int, del_start: int, del_end: int) -> tuple[int, int] | None:
    """Adjust span for DELETE. Returns None if fully encompassed."""
    del_len = del_end - del_start

    if del_end <= start:
        return (start - del_len, end - del_len)
    if del_start >= end:
        return (start, end)
    if del_start <= start and del_end >= end:
        return None
    if del_start <= start < del_end < end:
        return (del_start, end - del_len)
    if start < del_start < end <= del_end:
        return (start, del_start)
    if start < del_start and del_end < end:
        return (start, end - del_len)
    return (start, end)

# --- END verbatim block -----------------------------------------------------

VERBATIM_SHA256 = "ddf12eeb2644ffa035f5672e8f752403d2a90aa00b91acdc7d37170ddfe78208"

BACKEND_SRC = os.environ.get(
    "OPENPECHA_BACKEND_SRC",
    os.path.expanduser("~/Desktop/work/webuddhist-library/openpecha-backend/database/span_database.py"),
)


def verify_vendored_copy(path=None):
    """Return (ok, message). ok is None when the backend checkout is absent."""
    path = path or BACKEND_SRC
    if not os.path.exists(path):
        return None, f"backend source not found at {path} - vendored copy unverified"
    lines = open(path).read().splitlines(keepends=True)
    start = next((i for i, l in enumerate(lines) if l.startswith("def _adjust_span_for_delete")), None)
    if start is None:
        return False, "could not locate _adjust_span_for_delete in backend source"
    end = start
    while end + 1 < len(lines) and not lines[end + 1].startswith("def "):
        end += 1
    while end > start and not lines[end].strip():
        end -= 1
    block = "".join(lines[start:end + 1])
    got = hashlib.sha256(block.encode()).hexdigest()
    if got != VERBATIM_SHA256:
        return False, f"backend _adjust_span_for_delete has changed (sha {got[:16]}, expected {VERBATIM_SHA256[:16]})"
    return True, "vendored copy matches backend source"


def apply_delete(spans, del_start, del_end):
    """spans: {key: (start, end)}. Returns (new_spans, removed_keys)."""
    out, removed = {}, []
    for key, (s, e) in spans.items():
        adj = _adjust_span_for_delete(s, e, del_start, del_end)
        if adj is None:
            removed.append(key)
        else:
            out[key] = adj
    return out, removed


if __name__ == "__main__":
    ok, msg = verify_vendored_copy()
    print(("UNVERIFIED: " if ok is None else "OK: " if ok else "DRIFT: ") + msg)
    raise SystemExit(0 if ok is not False else 1)
