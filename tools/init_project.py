#!/usr/bin/env python3
"""Initialize the parent project from divan bootstrap files.

Divan lives INSIDE the target project at <project_root>/divan/.
This script copies bootstrap/common/ and a profile overlay to <project_root>/../
(i.e., the parent directory of divan).

Usage from inside divan/:
    python tools/init_project.py
    python tools/init_project.py --profile ml-research --backup
    python tools/init_project.py --dry-run
    python tools/init_project.py --target /path/to/other/project

Requires Python 3.8+, stdlib only.
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

PROFILES = ["base", "ml-research", "llm-research", "general-python"]

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")

TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".ps1", ".toml", ".yaml", ".yml",
    ".json", ".cfg", ".ini", ".editorconfig", ".gitignore", ".gitattributes",
    ".template", ".html", ".css", ".js", ".ts", ".rst", ".tex", ".bib",
    ".pbs",  # HPC PBS job scripts
}

TEXT_NAMES = {
    ".editorconfig", ".gitignore", ".gitattributes", "Makefile",
    "LICENSE", "Dockerfile",
}

# Files in profile dirs that should NOT be copied to the target
PROFILE_SKIP = {"README.md"}


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def find_divan_root() -> Path:
    """Find divan root — this script is in divan/tools/, so go up one."""
    return Path(__file__).resolve().parent.parent


def find_project_root(divan_root: Path, target: str | None) -> Path:
    """Find the parent project root.

    Default: the directory that contains divan/ (i.e., divan_root.parent).
    If --target is given, use that path instead.
    """
    if target:
        return Path(target).resolve()
    return divan_root.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_text_file(path: Path) -> bool:
    if path.name in TEXT_NAMES:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def infer_project_name(project_root: Path) -> str:
    return project_root.name


def build_values(
    project_name: str,
    owner: str,
    description: str,
    python_version: str,
    license_type: str,
    language: str,
) -> dict[str, str]:
    return {
        "PROJECT_NAME": project_name,
        "OWNER": owner,
        "DESCRIPTION": description,
        "PRIMARY_LANGUAGE": language,
        "PYTHON_VERSION": python_version,
        "LICENSE": license_type,
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
# Core
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
            "- Placeholders: " + ", ".join(
                f"{{{{{k}}}}}={v}" for k, v in sorted(values.items())
            ),
            f"- Errors: {len(self.errors) or 'none'}",
        ]
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
    # README.project.md → README.md
    if dst.name == "README.project.md":
        dst = dst.with_name("README.md")
    # Strip .template extension
    if dst.suffix == ".template":
        dst = dst.with_suffix("")

    rel = str(dst.relative_to(dst.parents[len(dst.parts) - 2]) if False else dst)
    try:
        rel = str(dst)
    except Exception:
        rel = str(dst)

    if dst.exists():
        if not force:
            result.skipped.append(str(dst))
            return
        if backup and not dry_run:
            bak = dst.with_suffix(dst.suffix + ".bak")
            shutil.copy2(dst, bak)
            result.backed_up.append(str(dst))
        result.overwritten.append(str(dst))
    else:
        result.created.append(str(dst))

    if dry_run:
        return

    dst.parent.mkdir(parents=True, exist_ok=True)

    if is_text_file(src):
        try:
            content = src.read_text(encoding="utf-8")
            rendered = render_string(content, values)
            dst.write_text(rendered, encoding="utf-8")
        except (UnicodeDecodeError, OSError) as e:
            result.errors.append(f"{dst}: {e}")
            shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)

    if os.access(src, os.X_OK):
        os.chmod(dst, dst.stat().st_mode | 0o111)


def init_project(
    divan_root: Path,
    project_root: Path,
    profile: str,
    values: dict[str, str],
    *,
    force: bool = False,
    backup: bool = False,
    dry_run: bool = False,
) -> InitResult:
    result = InitResult()

    if not dry_run:
        project_root.mkdir(parents=True, exist_ok=True)

    # Common files
    common_dir = divan_root / "bootstrap" / "common"
    if not common_dir.is_dir():
        result.errors.append(f"bootstrap/common/ not found: {common_dir}")
        return result

    for rel_path in collect_files(common_dir):
        src = common_dir / rel_path
        dst = project_root / rel_path
        copy_file(src, dst, values, result, force=force, backup=backup, dry_run=dry_run)

    # Profile overlay
    if profile != "base":
        profile_dir = divan_root / "bootstrap" / "profiles" / profile
        if not profile_dir.is_dir():
            result.errors.append(f"Profile not found: {profile_dir}")
        else:
            for rel_path in collect_files(profile_dir):
                if rel_path.name in PROFILE_SKIP:
                    continue
                src = profile_dir / rel_path
                dst = project_root / rel_path
                copy_file(src, dst, values, result, force=force, backup=backup, dry_run=dry_run)

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize parent project from divan bootstrap files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Run from inside divan/ or from the parent project root.

Examples:
  python tools/init_project.py
  python tools/init_project.py --profile ml-research
  python tools/init_project.py --dry-run
  python tools/init_project.py --backup --force
  python tools/init_project.py --target /path/to/other/project
        """,
    )
    parser.add_argument(
        "--target", default=None,
        help="Target project root (default: parent of divan/, i.e. ../)",
    )
    parser.add_argument(
        "--profile", default="ml-research", choices=PROFILES,
        help="Profile to apply (default: ml-research)",
    )
    parser.add_argument(
        "--project-name", default=None,
        help="Project name — inferred from target directory name if omitted",
    )
    parser.add_argument(
        "--owner", default="{{OWNER}}",
        help="Owner/username placeholder value",
    )
    parser.add_argument(
        "--description", default="An ML research project",
        help="Project description",
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
        help="Show what would happen without making changes",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--backup", action="store_true",
        help="Create .bak copies before overwriting (with --force)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    divan_root = find_divan_root()
    project_root = find_project_root(divan_root, args.target)

    project_name = args.project_name or infer_project_name(project_root)
    values = build_values(
        project_name=project_name,
        owner=args.owner,
        description=args.description,
        python_version=args.python_version,
        license_type=args.license,
        language=args.language,
    )

    if args.dry_run:
        print(f"[DRY RUN] Would initialize {project_root} with profile '{args.profile}'")
        print(f"  divan root: {divan_root}")
        print()

    result = init_project(
        divan_root=divan_root,
        project_root=project_root,
        profile=args.profile,
        values=values,
        force=args.force,
        backup=args.backup,
        dry_run=args.dry_run,
    )

    print(result.summary(project_root, args.profile, values))

    if args.dry_run and (result.created or result.skipped or result.overwritten):
        print()
        print("Would create:")
        for f in result.created:
            # Show path relative to project_root for readability
            try:
                rel = Path(f).relative_to(project_root)
            except ValueError:
                rel = Path(f)
            print(f"  + {rel}")
        if result.skipped:
            print("Would skip (exist):")
            for f in result.skipped[:10]:
                try:
                    rel = Path(f).relative_to(project_root)
                except ValueError:
                    rel = Path(f)
                print(f"  ~ {rel}")
            if len(result.skipped) > 10:
                print(f"  ... and {len(result.skipped) - 10} more")

    if result.errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
