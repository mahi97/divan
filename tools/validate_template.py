#!/usr/bin/env python3
"""Validate the divan template repository structure.

Checks that required files exist, profiles are well-formed, and placeholder
conventions are followed.

Usage:
    python tools/validate_template.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")
KNOWN_PLACEHOLDERS = {
    "{{PROJECT_NAME}}", "{{OWNER}}", "{{DESCRIPTION}}",
    "{{PRIMARY_LANGUAGE}}", "{{PYTHON_VERSION}}", "{{LICENSE}}", "{{YEAR}}",
}

REQUIRED_ROOT_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "TEMPLATE_USAGE.md",
    "PROJECT_INIT_PLAYBOOK.md",
    ".gitignore",
    ".editorconfig",
    ".gitattributes",
    "LICENSE",
    "Makefile",
]

REQUIRED_DOCS = [
    "docs/overview.md",
    "docs/workspace-model.md",
    "docs/standards/agent-standards.md",
    "docs/standards/coding-standards.md",
    "docs/standards/documentation-standards.md",
    "docs/standards/research-workflow.md",
    "docs/standards/project-lifecycle.md",
]

REQUIRED_TEMPLATES = [
    "docs/templates/architecture.md",
    "docs/templates/commands.md",
    "docs/templates/roadmap.md",
    "docs/templates/experiment-log.md",
    "docs/templates/literature-notes.md",
    "docs/templates/decision-record.md",
]

REQUIRED_COMMON = [
    "bootstrap/common/README.project.md",
    "bootstrap/common/AGENTS.md",
    "bootstrap/common/CLAUDE.md",
    "bootstrap/common/.gitignore",
    "bootstrap/common/.editorconfig",
    "bootstrap/common/.gitattributes",
    "bootstrap/common/docs/architecture.md",
    "bootstrap/common/docs/commands.md",
    "bootstrap/common/docs/roadmap.md",
    "bootstrap/common/docs/decisions/README.md",
    "bootstrap/common/docs/experiments/README.md",
    "bootstrap/common/docs/literature/README.md",
    "bootstrap/common/scripts/check.sh",
    "bootstrap/common/scripts/check.ps1",
    "bootstrap/common/scripts/test.sh",
    "bootstrap/common/scripts/test.ps1",
    "bootstrap/common/scripts/lint.sh",
    "bootstrap/common/scripts/lint.ps1",
    "bootstrap/common/.claude/settings.json",
    "bootstrap/common/.codex/config.toml",
]

REQUIRED_SKILLS_CLAUDE = [
    "bootstrap/common/.claude/skills/repo-onboarding/SKILL.md",
    "bootstrap/common/.claude/skills/legacy-rewrite/SKILL.md",
    "bootstrap/common/.claude/skills/experiment-runner/SKILL.md",
    "bootstrap/common/.claude/skills/literature-scan/SKILL.md",
]

REQUIRED_SKILLS_AGENTS = [
    "bootstrap/common/.agents/skills/repo-onboarding/SKILL.md",
    "bootstrap/common/.agents/skills/legacy-rewrite/SKILL.md",
    "bootstrap/common/.agents/skills/experiment-runner/SKILL.md",
    "bootstrap/common/.agents/skills/literature-scan/SKILL.md",
]

REQUIRED_PROFILES = ["base", "research-python", "python-library", "llm-research"]

REQUIRED_TOOLS = [
    "tools/init_project.py",
    "tools/validate_template.py",
    "tools/render_templates.py",
]

REQUIRED_GITHUB = [
    ".github/workflows/validate-template.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
]

REQUIRED_EXAMPLES = [
    "examples/workspace-layout.md",
    "examples/initialized-project-tree.md",
]


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def find_template_root() -> Path:
    return Path(__file__).resolve().parent.parent


def check_files_exist(root: Path, paths: list[str], label: str) -> list[str]:
    errors = []
    for p in paths:
        if not (root / p).exists():
            errors.append(f"[{label}] Missing: {p}")
    return errors


def check_profiles(root: Path) -> list[str]:
    errors = []
    for profile in REQUIRED_PROFILES:
        pdir = root / "bootstrap" / "profiles" / profile
        if not pdir.is_dir():
            errors.append(f"[profiles] Missing profile directory: {profile}")
            continue
        readme = pdir / "README.md"
        if not readme.exists():
            errors.append(f"[profiles] Missing README.md in profile: {profile}")
    return errors


def check_no_empty_files(root: Path) -> list[str]:
    """Check that bootstrap common files are not empty stubs."""
    errors = []
    common = root / "bootstrap" / "common"
    if not common.is_dir():
        return ["[content] bootstrap/common/ directory not found"]

    for path in common.rglob("*"):
        if path.is_file() and path.stat().st_size == 0:
            rel = path.relative_to(root)
            errors.append(f"[content] Empty file: {rel}")
    return errors


def check_placeholder_consistency(root: Path) -> list[str]:
    """Check that bootstrap files only use known placeholders."""
    warnings = []
    common = root / "bootstrap" / "common"
    profiles = root / "bootstrap" / "profiles"

    for base_dir in [common, profiles]:
        if not base_dir.is_dir():
            continue
        for path in base_dir.rglob("*"):
            if not path.is_file():
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            found = set(PLACEHOLDER_RE.findall(content))
            unknown = found - KNOWN_PLACEHOLDERS
            if unknown:
                rel = path.relative_to(root)
                warnings.append(
                    f"[placeholders] Unknown placeholder(s) in {rel}: {', '.join(sorted(unknown))}"
                )
    return warnings


def check_scripts_executable(root: Path) -> list[str]:
    """Check that .sh scripts have the executable bit set."""
    import os

    errors = []
    scripts_dir = root / "bootstrap" / "common" / "scripts"
    if not scripts_dir.is_dir():
        return []
    for sh_file in scripts_dir.glob("*.sh"):
        if not os.access(sh_file, os.X_OK):
            rel = sh_file.relative_to(root)
            errors.append(f"[scripts] Not executable: {rel}")
    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    root = find_template_root()
    print(f"Validating template at: {root}")
    print()

    all_issues: list[str] = []

    checks = [
        ("Root files", lambda: check_files_exist(root, REQUIRED_ROOT_FILES, "root")),
        ("Documentation", lambda: check_files_exist(root, REQUIRED_DOCS, "docs")),
        ("Templates", lambda: check_files_exist(root, REQUIRED_TEMPLATES, "templates")),
        ("Common bootstrap", lambda: check_files_exist(root, REQUIRED_COMMON, "common")),
        ("Claude skills", lambda: check_files_exist(root, REQUIRED_SKILLS_CLAUDE, "claude-skills")),
        ("Agent skills", lambda: check_files_exist(root, REQUIRED_SKILLS_AGENTS, "agent-skills")),
        ("Profiles", lambda: check_profiles(root)),
        ("Tools", lambda: check_files_exist(root, REQUIRED_TOOLS, "tools")),
        ("GitHub", lambda: check_files_exist(root, REQUIRED_GITHUB, "github")),
        ("Examples", lambda: check_files_exist(root, REQUIRED_EXAMPLES, "examples")),
        ("Non-empty files", lambda: check_no_empty_files(root)),
        ("Placeholder consistency", lambda: check_placeholder_consistency(root)),
        ("Script permissions", lambda: check_scripts_executable(root)),
    ]

    for name, check_fn in checks:
        issues = check_fn()
        if issues:
            print(f"  FAIL  {name} ({len(issues)} issue(s))")
            all_issues.extend(issues)
        else:
            print(f"  OK    {name}")

    print()

    if all_issues:
        print(f"Found {len(all_issues)} issue(s):")
        for issue in all_issues:
            print(f"  - {issue}")
        print()
        print("VALIDATION FAILED")
        return 1
    else:
        print("ALL CHECKS PASSED")
        return 0


if __name__ == "__main__":
    sys.exit(main())
