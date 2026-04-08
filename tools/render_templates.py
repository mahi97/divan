#!/usr/bin/env python3
"""Render placeholder tokens in template files.

Replaces {{KEY}} placeholders with provided values in text files.
Skips binary files.
"""

from __future__ import annotations

import datetime
import os
from pathlib import Path

# Default placeholder values
DEFAULTS = {
    "PROJECT_NAME": "my_project",
    "OWNER": "myorg",
    "DESCRIPTION": "A new project",
    "PRIMARY_LANGUAGE": "Python",
    "PYTHON_VERSION": "3.12",
    "LICENSE": "MIT",
    "YEAR": str(datetime.date.today().year),
}

# File extensions considered text (safe to render)
TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".ps1", ".toml", ".yaml", ".yml",
    ".json", ".cfg", ".ini", ".editorconfig", ".gitignore", ".gitattributes",
    ".template", ".html", ".css", ".js", ".ts", ".rst",
}

# Files that are always text regardless of extension
TEXT_NAMES = {
    ".editorconfig", ".gitignore", ".gitattributes", "Makefile",
    "LICENSE", "Dockerfile",
}


def is_text_file(path: Path) -> bool:
    """Check if a file should be treated as text."""
    if path.name in TEXT_NAMES:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def render_string(content: str, values: dict[str, str]) -> str:
    """Replace all {{KEY}} placeholders in a string."""
    result = content
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def render_file(path: Path, values: dict[str, str], dry_run: bool = False) -> int:
    """Render placeholders in a single file. Returns count of replacements."""
    if not is_text_file(path):
        return 0

    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0

    rendered = render_string(content, values)
    if rendered == content:
        return 0

    count = sum(
        content.count("{{" + key + "}}") for key in values if "{{" + key + "}}" in content
    )

    if not dry_run:
        path.write_text(rendered, encoding="utf-8")

    return count


def render_directory(directory: Path, values: dict[str, str], dry_run: bool = False) -> dict[str, int]:
    """Render placeholders in all text files under a directory.

    Returns a dict mapping file paths to replacement counts.
    """
    results = {}
    for root, _dirs, files in os.walk(directory):
        for name in files:
            path = Path(root) / name
            count = render_file(path, values, dry_run=dry_run)
            if count > 0:
                results[str(path)] = count
    return results


def build_values(
    project_name: str | None = None,
    owner: str | None = None,
    description: str | None = None,
    primary_language: str | None = None,
    python_version: str | None = None,
    license_type: str | None = None,
    year: str | None = None,
) -> dict[str, str]:
    """Build a placeholder values dict, falling back to defaults."""
    values = dict(DEFAULTS)
    if project_name is not None:
        values["PROJECT_NAME"] = project_name
    if owner is not None:
        values["OWNER"] = owner
    if description is not None:
        values["DESCRIPTION"] = description
    if primary_language is not None:
        values["PRIMARY_LANGUAGE"] = primary_language
    if python_version is not None:
        values["PYTHON_VERSION"] = python_version
    if license_type is not None:
        values["LICENSE"] = license_type
    if year is not None:
        values["YEAR"] = year
    return values


def check_remaining_placeholders(directory: Path) -> list[tuple[str, list[str]]]:
    """Find files that still contain unreplaced {{...}} placeholders."""
    import re

    pattern = re.compile(r"\{\{[A-Z_]+\}\}")
    results = []

    for root, _dirs, files in os.walk(directory):
        for name in files:
            path = Path(root) / name
            if not is_text_file(path):
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            found = pattern.findall(content)
            if found:
                results.append((str(path), sorted(set(found))))

    return results
