#!/usr/bin/env python3
"""Copy the optional starter into a new empty directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent / "assets" / "react-vite-pwa-starter"
    destination = args.destination.expanduser().resolve()
    if not source.is_dir():
        print(f"error: starter is missing: {source}", file=sys.stderr)
        return 2
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        print(f"error: destination must be an empty directory: {destination}", file=sys.stderr)
        return 3

    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
