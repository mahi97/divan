#!/usr/bin/env python3
"""Validate the divan template repository structure.

Run from divan root:
    python tools/validate_template.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Required files
# ---------------------------------------------------------------------------

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")
KNOWN_PLACEHOLDERS = {
    "{{PROJECT_NAME}}", "{{OWNER}}", "{{DESCRIPTION}}",
    "{{PRIMARY_LANGUAGE}}", "{{PYTHON_VERSION}}", "{{LICENSE}}", "{{YEAR}}",
    # Server-specific — OK to leave as-is
    "{{GPU_SERVER_HOST}}", "{{GPU_SERVER_USER}}", "{{GPU_TYPE}}", "{{GPU_COUNT}}",
    "{{GPU_VRAM}}", "{{CPU_INFO}}", "{{SERVER_RAM}}", "{{STORAGE_INFO}}",
    "{{DATA_PATH}}", "{{SCRATCH_PATH}}", "{{PYTHON_SETUP}}", "{{CUDA_VERSION}}",
    "{{CUDNN_VERSION}}", "{{ENV_ACTIVATE}}", "{{SESSION_NAME}}", "{{CONFIG}}",
    "{{PROJECT_NAME}}", "{{HPC_LOGIN_NODE}}", "{{HPC_USER}}", "{{LOGIN_NODE_COUNT}}",
    "{{GPU_QUEUE_INFO}}", "{{CPU_QUEUE_INFO}}", "{{MAX_WALLTIME}}", "{{MAX_GPUS}}",
    "{{SHARED_DATA_PATH}}", "{{PYTHON_MODULE}}", "{{CUDA_MODULE}}", "{{CUDNN_MODULE}}",
    "{{QUEUE_NAME}}", "{{NCPUS}}", "{{NGPUS}}", "{{MEM}}", "{{WALLTIME}}",
    "{{SCRIPT}}", "{{CLUSTER_NAME}}", "{{EXPERIMENT}}", "{{SERVER}}",
    "{{LOGIN_NODE}}", "{{PAPER_TITLE}}", "{{AUTHOR}}", "{{OWNER}}",
}

REQUIRED_ROOT_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "PROJECT_INIT_PLAYBOOK.md",
    "init.sh",
    "init.ps1",
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
    "docs/servers/README.md",
    "docs/servers/bare-gpu.md",
    "docs/servers/hpc-pbs.md",
]

REQUIRED_SKILLS = [
    "skills/README.md",
    "skills/custom/gpu-deploy/SKILL.md",
    "skills/custom/hpc-submit/SKILL.md",
    "skills/custom/experiment-runner/SKILL.md",
    "skills/custom/sweep-runner/SKILL.md",
    "skills/custom/monitoring-setup/SKILL.md",
    "skills/custom/results-viz/SKILL.md",
    "skills/custom/latex-paper/SKILL.md",
    "skills/custom/project-setup/SKILL.md",
    "skills/custom/repo-onboarding/SKILL.md",
    "skills/custom/legacy-rewrite/SKILL.md",
    "skills/custom/skill-generation/SKILL.md",
    "skills/custom/graphify/SKILL.md",
    "skills/external/manifest.yml",
    "skills/external/README.md",
]

REQUIRED_AGENTS = [
    "agents/README.md",
    "agents/experiment-agent.md",
    "agents/paper-agent.md",
]

REQUIRED_WORKFLOWS = [
    "workflows/README.md",
    "workflows/train-evaluate.md",
    "workflows/sweep-and-select.md",
    "workflows/experiment-to-paper.md",
    "workflows/new-project-setup.md",
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

REQUIRED_PROFILES = ["base", "ml-research", "llm-research", "general-python"]

REQUIRED_TOOLS = [
    "tools/init_project.py",
    "tools/validate_template.py",
    "tools/render_templates.py",
    "tools/fetch_skills.py",
]

REQUIRED_GITHUB = [
    ".github/workflows/validate-template.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
]


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def find_divan_root() -> Path:
    return Path(__file__).resolve().parent.parent


def check_files_exist(root: Path, paths: list[str], label: str) -> list[str]:
    return [
        f"[{label}] Missing: {p}"
        for p in paths
        if not (root / p).exists()
    ]


def check_profiles(root: Path) -> list[str]:
    errors = []
    for profile in REQUIRED_PROFILES:
        pdir = root / "bootstrap" / "profiles" / profile
        if not pdir.is_dir():
            errors.append(f"[profiles] Missing profile directory: {profile}")
            continue
        if not (pdir / "README.md").exists():
            errors.append(f"[profiles] Missing README.md in profile: {profile}")
    return errors


def check_no_empty_files(root: Path) -> list[str]:
    errors = []
    for check_dir in ["bootstrap/common", "skills/custom", "workflows", "agents"]:
        d = root / check_dir
        if not d.is_dir():
            continue
        for path in d.rglob("*"):
            if path.is_file() and path.stat().st_size == 0:
                errors.append(f"[content] Empty file: {path.relative_to(root)}")
    return errors


def check_placeholder_consistency(root: Path) -> list[str]:
    """Check bootstrap files only use known placeholders."""
    warnings = []
    for base_dir in ["bootstrap/common", "bootstrap/profiles"]:
        d = root / base_dir
        if not d.is_dir():
            continue
        for path in d.rglob("*"):
            if not path.is_file():
                continue
            # Skip server docs — they intentionally have unfilled server-specific placeholders
            if "servers" in str(path):
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
                    f"[placeholders] Unknown in {rel}: {', '.join(sorted(unknown))}"
                )
    return warnings


def check_scripts_executable(root: Path) -> list[str]:
    import os
    errors = []
    for sh_file in (root / "bootstrap" / "common" / "scripts").glob("*.sh"):
        if not os.access(sh_file, os.X_OK):
            errors.append(f"[scripts] Not executable: {sh_file.relative_to(root)}")
    if (root / "init.sh").exists() and not os.access(root / "init.sh", os.X_OK):
        errors.append("[scripts] init.sh is not executable")
    return errors


def check_skill_format(root: Path) -> list[str]:
    """Check that each custom skill has a name frontmatter."""
    errors = []
    for skill_dir in (root / "skills" / "custom").iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"[skills] Missing SKILL.md in: {skill_dir.name}")
            continue
        content = skill_md.read_text(encoding="utf-8")
        if "name:" not in content:
            errors.append(f"[skills] Missing 'name:' frontmatter in: {skill_dir.name}/SKILL.md")
    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    root = find_divan_root()
    print(f"Validating divan at: {root}")
    print()

    all_issues: list[str] = []

    checks = [
        ("Root files",          lambda: check_files_exist(root, REQUIRED_ROOT_FILES, "root")),
        ("Documentation",       lambda: check_files_exist(root, REQUIRED_DOCS, "docs")),
        ("Skills",              lambda: check_files_exist(root, REQUIRED_SKILLS, "skills")),
        ("Agents",              lambda: check_files_exist(root, REQUIRED_AGENTS, "agents")),
        ("Workflows",           lambda: check_files_exist(root, REQUIRED_WORKFLOWS, "workflows")),
        ("Bootstrap common",    lambda: check_files_exist(root, REQUIRED_COMMON, "common")),
        ("Profiles",            lambda: check_profiles(root)),
        ("Tools",               lambda: check_files_exist(root, REQUIRED_TOOLS, "tools")),
        ("GitHub",              lambda: check_files_exist(root, REQUIRED_GITHUB, "github")),
        ("Non-empty files",     lambda: check_no_empty_files(root)),
        ("Placeholder syntax",  lambda: check_placeholder_consistency(root)),
        ("Script permissions",  lambda: check_scripts_executable(root)),
        ("Skill format",        lambda: check_skill_format(root)),
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
