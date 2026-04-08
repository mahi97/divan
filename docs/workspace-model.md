# Workspace Model

How divan lives inside your projects and what it touches.

---

## Layout

Divan is cloned **inside** each project as a subdirectory:

```
my_ml_project/                 ← your research project (git repo)
  divan/                       ← cloned inside (git repo or submodule)
    skills/                    ← AI agents read these
    bootstrap/                 ← files copied to parent on init
    docs/                      ← standards, server guides
    tools/                     ← scripts
  src/                         ← your code
  tests/                       ← your tests
  configs/                     ← experiment configs
  docs/                        ← project-specific docs
  scripts/                     ← check, test, lint, deploy
  AGENTS.md                    ← created by init, points to divan/
  CLAUDE.md                    ← created by init, points to divan/
  .gitignore                   ← created by init
```

## Relationship

```
my_project/
  divan/
    ├── bootstrap/common/     ──copy──►  ../   (parent project root)
    ├── bootstrap/profiles/X/ ──overlay──►  ../ (parent project root)
    ├── skills/               ──read by──►  AI agents
    ├── docs/standards/       ──referenced by──►  AGENTS.md, CLAUDE.md
    └── docs/servers/         ──read by──►  deploy skills
```

- **Copy** = files are physically copied from `bootstrap/` to the parent directory
- **Overlay** = profile files are copied on top of common files
- **Read** = agents access skills and standards directly from `divan/`

## After Initialization

The parent project owns the copied files (AGENTS.md, scripts, etc.), but
divan remains inside as a **living reference**. Unlike a one-time template:

- Skills in `divan/skills/` are read on demand by agents
- Standards in `divan/docs/` remain the source of truth
- You can `git pull` inside `divan/` to get updated skills and workflows
- Re-running `init.sh --force` updates copied files

## Git Handling

Two options for tracking divan:

### Option A: Gitignore (recommended for personal use)

Add `divan/` to your project's `.gitignore`. Each collaborator clones divan
themselves. Simpler, but each person must set up divan independently.

### Option B: Git submodule

```bash
git submodule add https://github.com/YOUR_USER/divan.git divan
```

Tracked in the parent repo. Collaborators get divan automatically on clone.
Better for teams sharing the same toolkit.

The init script adds `divan/` to `.gitignore` by default. Remove it if using
submodules.

## Multiple Projects

Each project gets its own divan clone, but they all point to the same repo:

```
~/research/
  attention_paper/
    divan/           ← clone of your divan repo
    src/
  scaling_laws/
    divan/           ← same repo, independent clone
    src/
  benchmark_suite/
    divan/           ← same repo, independent clone
    src/
```

Update all at once:
```bash
for dir in ~/research/*/divan; do (cd "$dir" && git pull); done
```

## Server Configuration

Divan carries server profiles for two compute environments:

| Environment    | Documented in             | Access pattern              |
|----------------|---------------------------|-----------------------------|
| Bare GPU       | `docs/servers/bare-gpu.md` | SSH → run directly          |
| HPC Cluster    | `docs/servers/hpc-pbs.md`  | SSH → login node → qsub    |

Skills like `gpu-deploy` and `hpc-submit` read these docs to know how to
interact with each server type.
