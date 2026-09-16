#!/usr/bin/env python3
"""Initialize durable Personal Workbench Builder state without overwriting it."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--project-name")
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: project root is not a directory: {root}", file=sys.stderr)
        return 2

    destination = root / ".personal-workbench"
    if destination.exists() and any(destination.iterdir()):
        print(f"error: refusing to overwrite existing state: {destination}", file=sys.stderr)
        return 3

    template = Path(__file__).resolve().parent.parent / "assets" / "state-template"
    required = {
        "requirements.md",
        "workflow.md",
        "feature-map.md",
        "design-choice.md",
        "decisions.md",
        "project-state.json",
    }
    missing = sorted(required - {item.name for item in template.iterdir()})
    if missing:
        print(f"error: state template is incomplete: {', '.join(missing)}", file=sys.stderr)
        return 4

    destination.mkdir(exist_ok=True)
    name = args.project_name or root.name
    now = utc_now()
    for source in template.iterdir():
        target = destination / source.name
        if source.suffix == ".json":
            data = json.loads(source.read_text(encoding="utf-8"))
            data["project_name"] = name
            data["created_at"] = now
            data["updated_at"] = now
            target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            content = source.read_text(encoding="utf-8").replace("{{PROJECT_NAME}}", name)
            content = content.replace("{{CREATED_AT}}", now)
            target.write_text(content, encoding="utf-8")

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
