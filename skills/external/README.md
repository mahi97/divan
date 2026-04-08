# External Skills

Skills fetched from external sources (GitHub repos, URLs, etc.).

## Fetching Skills

```bash
python tools/fetch_skills.py
```

This reads `manifest.yml` and downloads skills to subdirectories here.

## Adding a New External Skill

Edit `manifest.yml` and add an entry:

```yaml
- name: my-skill
  source: github
  location: https://github.com/org/repo/tree/main/skills/my-skill
  dest: skills/external/my-skill/
  description: What this skill does
```

Then run `python tools/fetch_skills.py`.

## Currently Listed

See `manifest.yml` for the full list. Installed skills will appear as
subdirectories here with their own `SKILL.md`.

## Note

External skills are not committed to this repo by default (they are in
`.gitignore`). Only the manifest is committed. Run `fetch_skills.py` after
cloning to install them.
