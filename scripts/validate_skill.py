#!/usr/bin/env python3
"""Validate the portable Agent Skills fields without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must begin with YAML frontmatter on the first line")
    try:
        closing = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is missing its closing delimiter") from exc

    fields: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = unquote(value)
    return fields, "\n".join(lines[closing + 1 :])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.skill_root.expanduser().resolve()
    skill_file = root / "SKILL.md"
    errors: list[str] = []

    if not skill_file.is_file():
        print(f"ERROR: missing {skill_file}")
        return 1

    text = skill_file.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    name = fields.get("name", "")
    description = fields.get("description", "")
    compatibility = fields.get("compatibility", "")
    if not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append("name must be 1-64 lowercase letters, digits, or single hyphens")
    if name != root.name:
        errors.append("name must match the parent directory name")
    if not description or len(description) > 1024:
        errors.append("description must be 1-1024 characters")
    if compatibility and len(compatibility) > 500:
        errors.append("compatibility must be at most 500 characters")
    if "TODO" in text or "[TODO" in text:
        errors.append("unfinished TODO marker found in SKILL.md")
    if not body.strip():
        errors.append("SKILL.md body must not be empty")

    for target in LINK_PATTERN.findall(body):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (root / target.split("#", 1)[0]).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            errors.append(f"link escapes the skill directory: {target}")
            continue
        if not resolved.is_file():
            errors.append(f"linked file does not exist: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: portable Agent Skill is valid: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
