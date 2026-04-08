#!/usr/bin/env python3
"""Initialize a sibling project from the divan template.

Copies bootstrap/common files, applies a profile overlay, and renders
placeholders. Supports dry-run, force, and backup modes.

Usage:
    python tools/init_project.py --target ../my_project --profile research-python \
        --project-name my_project --owner myorg

Requires Python 3.8+ and only standard library modules.
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import shutil
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROFILES = ["base", "research-python", "python-library", "llm-research"]

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")

TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".ps1", ".toml", ".yaml", ".yml",
    ".json", ".cfg", ".ini", ".editorconfig", ".gitignore", ".gitattributes",
    ".template", ".html", ".css", ".js", ".ts", ".rst",
}

TEXT_NAMES = {
    ".editorconfig", ".gitignore", ".gitattributes", "Makefile",
    "LICENSE", "Dockerfile",
}

# Files in profile dirs that should NOT be copied to the target
PROFILE_SKIP = {"README.md"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_text_file(path: Path) -> bool:
    if path.name in TEXT_NAMES:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def build_values(args: argparse.Namespace) -> dict[str, str]:
    return {
        "PROJECT_NAME": args.project_name,
        "OWNER": args.owner,
        "DESCRIPTION": args.description,
        "PRIMARY_LANGUAGE": args.language,
        "PYTHON_VERSION": args.python_version,
        "LICENSE": args.license,
        "YEAR": str(datetime.date.today().year),
    }


def render_string(content: str, values: dict[str, str]) -> str:
    result = content
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def collect_files(source_dir: Path) -> list[Path]:
    """Return all files under source_dir as relative paths."""
    files = []
    for root, _dirs, names in os.walk(source_dir):
        for name in names:
            full = Path(root) / name
            files.append(full.relative_to(source_dir))
    return sorted(files)


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

class InitResult:
    def __init__(self) -> None:
        self.created: list[str] = []
        self.skipped: list[str] = []
        self.overwritten: list[str] = []
        self.backed_up: list[str] = []
        self.errors: list[str] = []

    def summary(self, target: Path, profile: str, values: dict[str, str]) -> str:
        lines = [
            "## Initialization Report",
            f"- Target: {target}",
            f"- Profile: {profile}",
            f"- Files created: {len(self.created)}",
            f"- Files skipped (already exist): {len(self.skipped)}",
            f"- Files overwritten: {len(self.overwritten)}",
            f"- Files backed up: {len(self.backed_up)}",
            f"- Placeholders: " + ", ".join(
                f"{{{{{k}}}}} -> {v}" for k, v in sorted(values.items())
            ),
            f"- Errors: {len(self.errors) or 'none'}",
        ]
        if self.errors:
            for e in self.errors:
                lines.append(f"  - {e}")
        return "\n".join(lines)


def copy_file(
    src: Path,
    dst: Path,
    values: dict[str, str],
    result: InitResult,
    *,
    force: bool = False,
    backup: bool = False,
    dry_run: bool = False,
) -> None:
    """Copy a single file, rendering placeholders if text."""

    # Handle the special case where README.project.md -> README.md
    if dst.name == "README.project.md":
        dst = dst.with_name("README.md")

    # Handle .template extension (strip it)
    if dst.suffix == ".template":
        dst = dst.with_suffix("")

    rel = str(dst)

    if dst.exists():
        if not force:
            result.skipped.append(rel)
            return
        if backup and not dry_run:
            bak = dst.with_suffix(dst.suffix + ".bak")
            shutil.copy2(dst, bak)
            result.backed_up.append(rel)
        result.overwritten.append(rel)
    else:
        result.created.append(rel)

    if dry_run:
        return

    dst.parent.mkdir(parents=True, exist_ok=True)

    if is_text_file(src):
        try:
            content = src.read_text(encoding="utf-8")
            rendered = render_string(content, values)
            dst.write_text(rendered, encoding="utf-8")
        except (UnicodeDecodeError, OSError) as e:
            result.errors.append(f"{rel}: {e}")
            shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)

    # Preserve executable bit
    if os.access(src, os.X_OK):
        os.chmod(dst, dst.stat().st_mode | 0o111)


def init_project(
    template_root: Path,
    target: Path,
    profile: str,
    values: dict[str, str],
    *,
    force: bool = False,
    backup: bool = False,
    dry_run: bool = False,
) -> InitResult:
    result = InitResult()

    # Create target directory
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)

    # Copy common files
    common_dir = template_root / "bootstrap" / "common"
    if not common_dir.is_dir():
        result.errors.append(f"Common directory not found: {common_dir}")
        return result

    for rel_path in collect_files(common_dir):
        src = common_dir / rel_path
        dst = target / rel_path
        copy_file(src, dst, values, result, force=force, backup=backup, dry_run=dry_run)

    # Copy profile overlay (skip for 'base' which is common-only)
    if profile != "base":
        profile_dir = template_root / "bootstrap" / "profiles" / profile
        if not profile_dir.is_dir():
            result.errors.append(f"Profile directory not found: {profile_dir}")
        else:
            for rel_path in collect_files(profile_dir):
                if rel_path.name in PROFILE_SKIP:
                    continue
                src = profile_dir / rel_path
                dst = target / rel_path
                copy_file(src, dst, values, result, force=force, backup=backup, dry_run=dry_run)

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def find_template_root() -> Path:
    """Find the divan template root by looking relative to this script."""
    return Path(__file__).resolve().parent.parent


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a project from the divan template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --target ../my_project --profile research-python --project-name my_project --owner acme
  %(prog)s --target ../legacy --profile base --project-name legacy --owner acme --backup
  %(prog)s --target ../experiment --profile llm-research --project-name experiment --owner acme --dry-run
        """,
    )
    parser.add_argument(
        "--target", required=True,
        help="Path to the target project directory",
    )
    parser.add_argument(
        "--profile", default="base", choices=PROFILES,
        help="Profile to apply (default: base)",
    )
    parser.add_argument(
        "--project-name", required=True,
        help="Project name (used for {{PROJECT_NAME}} placeholder)",
    )
    parser.add_argument(
        "--owner", required=True,
        help="Owner name (used for {{OWNER}} placeholder)",
    )
    parser.add_argument(
        "--description", default="A new project",
        help="Project description (default: 'A new project')",
    )
    parser.add_argument(
        "--language", default="Python",
        help="Primary language (default: Python)",
    )
    parser.add_argument(
        "--python-version", default="3.12",
        help="Python version (default: 3.12)",
    )
    parser.add_argument(
        "--license", default="MIT",
        help="License type (default: MIT)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--backup", action="store_true",
        help="Create .bak copies before overwriting (requires --force)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    template_root = find_template_root()
    target = Path(args.target).resolve()
    values = build_values(args)

    if args.dry_run:
        print(f"[DRY RUN] Would initialize {target} with profile '{args.profile}'")
        print()

    result = init_project(
        template_root=template_root,
        target=target,
        profile=args.profile,
        values=values,
        force=args.force,
        backup=args.backup,
        dry_run=args.dry_run,
    )

    print(result.summary(target, args.profile, values))

    if args.dry_run:
        print()
        print("Files that would be created:")
        for f in result.created:
            print(f"  + {f}")
        if result.skipped:
            print("Files that would be skipped:")
            for f in result.skipped:
                print(f"  ~ {f}")
        if result.overwritten:
            print("Files that would be overwritten:")
            for f in result.overwritten:
                print(f"  ! {f}")

    if result.errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
