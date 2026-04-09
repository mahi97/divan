# Custom Skills

Place custom Claude Code skill files here as `.md` files with YAML frontmatter.

## Format

```markdown
---
name: my-skill
description: Brief description of what this skill does (used for matching)
---

Skill instructions go here. Claude will follow these when the skill is invoked.
```

## Tips

- The `description` field is critical - it determines when the skill gets triggered
- Keep skills focused on a single task or workflow
- Use clear, imperative instructions
- Reference specific file paths or patterns when relevant
