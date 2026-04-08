#!/usr/bin/env python3
"""Fetch external skills listed in skills/external/manifest.yml.

Downloads SKILL.md files from GitHub or URLs into skills/external/<name>/.
Skips already-installed skills unless --force is used.

Usage:
    python tools/fetch_skills.py
    python tools/fetch_skills.py --force
    python tools/fetch_skills.py --dry-run
    python tools/fetch_skills.py --list
"""

from __future__ import annotations

import argparse
import sys
import urllib.request
from pathlib import Path


def find_divan_root() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_manifest(manifest_path: Path) -> list[dict]:
    """Parse a minimal YAML manifest without external dependencies."""
    content = manifest_path.read_text(encoding="utf-8")
    skills = []
    current: dict | None = None

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue

        if stripped == "skills:":
            continue

        if stripped.startswith("- name:"):
            if current:
                skills.append(current)
            current = {"name": stripped.split(":", 1)[1].strip()}
        elif current is not None and ":" in stripped:
            key, _, val = stripped.partition(":")
            current[key.strip()] = val.strip()

    if current:
        skills.append(current)

    return skills


def github_url_to_raw(location: str) -> str:
    """Convert a GitHub tree URL to a raw SKILL.md URL."""
    # https://github.com/org/repo/tree/main/skills/foo
    # → https://raw.githubusercontent.com/org/repo/main/skills/foo/SKILL.md
    loc = location.replace("https://github.com/", "https://raw.githubusercontent.com/")
    loc = loc.replace("/tree/", "/")
    if not loc.endswith("/SKILL.md"):
        loc = loc.rstrip("/") + "/SKILL.md"
    return loc


def fetch_skill(skill: dict, dest_base: Path, *, force: bool = False, dry_run: bool = False) -> str:
    """Fetch a single skill. Returns status string."""
    name = skill.get("name", "unknown")
    source = skill.get("source", "")
    location = skill.get("location", "")
    dest_dir = dest_base / name

    skill_file = dest_dir / "SKILL.md"

    if skill_file.exists() and not force:
        return "skipped (already installed)"

    if dry_run:
        return f"would fetch from {location}"

    if source == "github":
        raw_url = github_url_to_raw(location)
    elif source == "url":
        raw_url = location
    else:
        return f"unknown source type: {source}"

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(raw_url, timeout=10) as response:
            content = response.read().decode("utf-8")
        skill_file.write_text(content, encoding="utf-8")
        return "installed"
    except Exception as e:
        return f"FAILED: {e}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch external skills from manifest.yml"
    )
    parser.add_argument("--force", action="store_true", help="Re-download installed skills")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fetched")
    parser.add_argument("--list", action="store_true", help="List skills in manifest")
    args = parser.parse_args(argv)

    divan_root = find_divan_root()
    manifest_path = divan_root / "skills" / "external" / "manifest.yml"

    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}")
        return 1

    skills = parse_manifest(manifest_path)

    if args.list:
        print(f"Skills in manifest ({len(skills)} total):")
        for s in skills:
            installed = (divan_root / s.get("dest", "") / "SKILL.md").exists()
            status = "[installed]" if installed else "[not installed]"
            print(f"  {status} {s['name']} — {s.get('description', '')}")
        return 0

    if args.dry_run:
        print("[DRY RUN] Would fetch:")

    dest_base = divan_root / "skills" / "external"
    results = []
    for skill in skills:
        status = fetch_skill(skill, dest_base, force=args.force, dry_run=args.dry_run)
        results.append((skill["name"], status))
        print(f"  {skill['name']}: {status}")

    failed = [name for name, status in results if status.startswith("FAILED")]
    if failed:
        print(f"\n{len(failed)} skill(s) failed to fetch: {', '.join(failed)}")
        return 1

    print(f"\nDone. {len(results)} skill(s) processed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
