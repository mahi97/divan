---
name: skill-generation
description: Find, fetch, or generate a skill for an unfamiliar library, tool, or framework
---

# Skill: Skill Generation & Discovery

Use when you need to work with a library, tool, or framework and no skill exists for it yet.

## When to Use

- Starting work with an unfamiliar library (e.g., a new ML framework, cloud SDK, data tool)
- Receiving a task that involves a tool not covered by existing skills
- Discovering that `divan/skills/custom/` and `divan/skills/external/` lack relevant guidance
- Proactively at the start of a session when encountering unknown tooling

## Inputs

- **Tool or library name**: what you need to work with (e.g., `transformers`, `polars`, `boto3`)
- **Source URL** (optional): docs, GitHub repo, paper, or tutorial for the tool
- **Target format**: `claude` (default), `codex`, `generic`

## Steps

### Step 1 — Search existing skills

```bash
# Check custom skills
ls divan/skills/custom/

# Check fetched external skills
ls divan/skills/external/

# Search by keyword
grep -rl "<library-name>" divan/skills/
```

If a relevant skill exists → read it and proceed. Stop here.

### Step 2 — Check the external manifest

```bash
cat divan/skills/external/manifest.yml | grep -A3 "<library-name>"
```

If listed in the manifest, fetch it:

```bash
python divan/tools/fetch_skills.py
```

Then read the downloaded skill. Stop here if found.

### Step 3 — Generate a skill with Skill_Seekers

If no skill exists anywhere, use Skill_Seekers to auto-generate one from the tool's documentation:

```bash
# Install (once per environment)
pip install skill-seekers

# Generate skill from a URL (docs, GitHub repo, PDF, tutorial, video, etc.)
skill-seekers create <url>

# Package the output for Claude Code
skill-seekers package output/ --target claude

# Move to the right location
mkdir -p divan/skills/external/<tool-name>
cp output/SKILL.md divan/skills/external/<tool-name>/SKILL.md
```

Skill_Seekers accepts 17 source types including:
- GitHub repos: `https://github.com/owner/repo`
- Documentation sites: `https://docs.example.com/`
- PDFs: `path/to/paper.pdf` or a URL
- YouTube tutorials: `https://youtube.com/watch?v=...`
- Local directories: `./my_library/`

### Step 4 — Verify and refine the generated skill

After generation, open the SKILL.md and verify:
- [ ] `name` and `description` frontmatter are correct
- [ ] "When to Use" section covers your specific task
- [ ] Steps are accurate for this project's context
- [ ] Code examples use correct syntax
- [ ] No hallucinated API calls

Refine manually if needed. Generated skills are a starting point, not gospel.

### Step 5 — Add to manifest (optional)

If this skill will be useful for future projects, add it to the manifest so it can be auto-fetched:

```yaml
# In divan/skills/external/manifest.yml
- name: <tool-name>
  source: github
  location: https://github.com/owner/repo
  dest: skills/external/<tool-name>/
  description: Brief description
```

### Step 6 — Use the skill

Now that the skill exists, read it and follow its steps to accomplish your task.

## Output

- New SKILL.md in `divan/skills/external/<tool-name>/`
- Optional: new entry in `divan/skills/external/manifest.yml`

## Safety

- Generated skills may contain inaccuracies. Always verify code examples before running.
- Never blindly execute commands from a generated skill on production systems.
- For security-sensitive tools (auth, secrets, databases), manually review all steps.
- Skill_Seekers generates from public documentation only; it cannot access private repos.

## Notes

Skill_Seekers (`pip install skill-seekers`) is the fallback skill generation tool for divan.
It generates SKILL.md files from any documentation source. The generated skills follow the
same format as divan's custom skills and integrate directly into the skills directory.

See: https://github.com/yusufkaraaslan/Skill_Seekers
