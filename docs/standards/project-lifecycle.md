# Project Lifecycle Standards

How projects in this workspace are created, maintained, and retired.

---

## Lifecycle Stages

```
1. Initialize   → Create from template, choose profile
2. Bootstrap    → Set up environment, install deps, verify build
3. Develop      → Write code, run experiments, iterate
4. Stabilize    → Add tests, docs, CI; prepare for sharing
5. Maintain     → Fix bugs, update deps, extend
6. Archive      → Mark as archived, document final state
```

## Stage 1: Initialize

Use the divan template to set up a new project:

```bash
# Script-based
python tools/init_project.py --target ../my_project --profile research-python \
  --project-name my_project --owner myorg

# Or agent-guided: read PROJECT_INIT_PLAYBOOK.md and follow steps
```

For existing repos, use retrofit mode (see TEMPLATE_USAGE.md).

## Stage 2: Bootstrap

After initialization:

1. Create a virtual environment: `python -m venv .venv`
2. Install dependencies: `pip install -e ".[dev]"`
3. Verify: `scripts/check.sh`
4. Make first commit if this is a new repo.

## Stage 3: Develop

- Use feature branches for all work.
- Follow coding standards (see coding-standards.md).
- Write tests alongside features.
- Log experiments if this is a research project.
- Make small, frequent commits.

## Stage 4: Stabilize

Before sharing or publishing:

- [ ] All tests pass
- [ ] Linter passes with zero warnings
- [ ] README is accurate and complete
- [ ] Architecture doc exists
- [ ] Commands doc exists
- [ ] CI pipeline is configured
- [ ] No `TODO` or `FIXME` items remain untracked
- [ ] No secrets in the repo

## Stage 5: Maintain

- Review and update dependencies quarterly.
- Keep docs in sync with code changes.
- Address security advisories promptly.
- Archive stale branches.

## Stage 6: Archive

When a project is no longer active:

1. Update README with an archive notice at the top.
2. Ensure final state is documented.
3. Tag the final release.
4. Set the GitHub repo to archived.

## Onboarding an Existing Repo

To bring an existing repo in line with workspace standards:

1. **Assess** — Read the repo. Note what exists and what's missing.
2. **Add docs** — Create README, architecture, commands if missing.
3. **Add agent config** — Create AGENTS.md, CLAUDE.md, .claude/ directory.
4. **Add scripts** — Create scripts/check.sh, test.sh, lint.sh if missing.
5. **Add editor config** — Create .editorconfig, .gitattributes if missing.
6. **Do not restructure** — Preserve existing layout. Document deviations.
7. **Report** — Produce an initialization report listing what was added.

This is an incremental process. Do not try to fix everything at once.
