#!/usr/bin/env python3
"""Check that the ten public invocation contracts remain documented."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FILES = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
TEXT = "\n".join(path.read_text(encoding="utf-8") for path in FILES)

SCENARIOS = {
    "1 initialize before code": [r"Do not write product code during discovery", r"start discovery"],
    "2 creator workflow is discovered": [r"Creator: inspiration", r"actual sequence"],
    "3 derive unknown features": [r"infer candidates", r"long-term records"],
    "4 no visual reference": [r"three distinct directions", r"visual"],
    "5 screenshot without copying": [r"not copied logos", r"three runnable"],
    "6 real cross-device sync": [r"two accounts", r"computer create"],
    "7 daily use implies release": [r"stable URL", r"PWA"],
    "8 automation feasibility": [r"API, RSS", r"scheduled"],
    "9 incremental feature": [r"implement incrementally", r"migration"],
    "10 redesign preserves data": [r"visual redesign", r"preserve"],
}


def main() -> int:
    failed = []
    for name, patterns in SCENARIOS.items():
        missing = [pattern for pattern in patterns if not re.search(pattern, TEXT, re.IGNORECASE)]
        if missing:
            failed.append((name, missing))
            print(f"FAIL: {name}: missing {', '.join(missing)}")
        else:
            print(f"PASS: {name}")
    if failed:
        return 1
    print(f"OK: {len(SCENARIOS)} scenario contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
