#!/usr/bin/env python3
"""Validate durable state files and phase-gate consistency."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


PHASES = [
    "discovery",
    "proposal",
    "feature_confirmed",
    "ui_prototypes",
    "ui_confirmed",
    "implementation",
    "integration",
    "release",
    "qa",
    "operational",
]
FILES = ["requirements.md", "workflow.md", "feature-map.md", "design-choice.md", "decisions.md"]


def valid_timestamp(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    args = parser.parse_args()
    state_dir = args.project_root.expanduser().resolve() / ".personal-workbench"
    errors: list[str] = []

    for name in FILES + ["project-state.json"]:
        path = state_dir / name
        if not path.is_file():
            errors.append(f"missing {name}")
        elif path.stat().st_size == 0:
            errors.append(f"empty {name}")

    state_path = state_dir / "project-state.json"
    if errors and not state_path.is_file():
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid project-state.json: {exc}")
        return 1

    required = {
        "schema_version",
        "project_name",
        "phase",
        "created_at",
        "updated_at",
        "primary_scenario",
        "primary_device",
        "data_mode",
        "feature_confirmation",
        "ui_confirmation",
        "third_party_dependencies",
        "deployment",
        "pwa",
        "qa",
    }
    for key in sorted(required - state.keys()):
        errors.append(f"missing field: {key}")

    phase = state.get("phase")
    if state.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(state.get("project_name"), str) or not state.get("project_name", "").strip():
        errors.append("project_name must be a non-empty string")
    if phase not in PHASES:
        errors.append(f"phase must be one of: {', '.join(PHASES)}")
    for key in ("created_at", "updated_at"):
        if not valid_timestamp(state.get(key)):
            errors.append(f"{key} must be an ISO-8601 timestamp")
    if state.get("primary_device") not in {"mobile", "desktop", "both", "unknown"}:
        errors.append("invalid primary_device")
    if state.get("data_mode") not in {"undecided", "local", "cloud-sync"}:
        errors.append("invalid data_mode")
    if not isinstance(state.get("third_party_dependencies"), list):
        errors.append("third_party_dependencies must be an array")

    feature = state.get("feature_confirmation", {})
    ui = state.get("ui_confirmation", {})
    if not isinstance(feature, dict) or not isinstance(feature.get("confirmed"), bool):
        errors.append("feature_confirmation.confirmed must be boolean")
    if not isinstance(ui, dict) or not isinstance(ui.get("confirmed"), bool):
        errors.append("ui_confirmation.confirmed must be boolean")
    if phase in PHASES and PHASES.index(phase) >= PHASES.index("feature_confirmed") and not feature.get("confirmed"):
        errors.append(f"phase {phase} requires confirmed features")
    if phase in PHASES and PHASES.index(phase) >= PHASES.index("ui_confirmed") and not ui.get("confirmed"):
        errors.append(f"phase {phase} requires confirmed UI")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {state_dir} ({phase})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
