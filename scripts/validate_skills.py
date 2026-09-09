#!/usr/bin/env python3
"""Validate the repository's dependency-free Agent Skill packaging rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")


def parse_frontmatter(path: Path, text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing opening YAML frontmatter delimiter"]

    try:
        end = next(
            i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration:
        return {}, [f"{path}: missing closing YAML frontmatter delimiter"]

    values: dict[str, str] = {}
    current: str | None = None
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            value = (match.group(2) or "").strip()
            values[current] = "" if value in {">", "|"} else value.strip("\"'")
        elif current and line.startswith((" ", "\t")):
            values[current] = f"{values[current]} {line.strip()}".strip()

    for required in ("name", "description"):
        if not values.get(required):
            errors.append(f"{path}: missing or empty frontmatter field '{required}'")
    return values, errors


def validate_local_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            continue
        resolved = path.parent / unquote(target)
        if not resolved.exists():
            errors.append(f"{path}: broken local link '{raw_target}'")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append("skills/: no skill directories found")

    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{directory}: missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        fields, frontmatter_errors = parse_frontmatter(skill_file, text)
        errors.extend(frontmatter_errors)
        name = fields.get("name", "")
        if name and not NAME_PATTERN.fullmatch(name):
            errors.append(f"{skill_file}: invalid skill name '{name}'")
        if name and name != directory.name:
            errors.append(
                f"{skill_file}: frontmatter name '{name}' does not match folder "
                f"'{directory.name}'"
            )

        for markdown in directory.rglob("*.md"):
            errors.extend(
                validate_local_links(markdown, markdown.read_text(encoding="utf-8"))
            )

    for markdown in (
        ROOT / "README.md",
        ROOT / "README.ru.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
    ):
        if markdown.is_file():
            errors.extend(
                validate_local_links(markdown, markdown.read_text(encoding="utf-8"))
            )

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills and local Markdown links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
