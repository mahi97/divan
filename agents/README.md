# Custom Agents

Place custom agent definitions here as `.md` files with YAML frontmatter.

## Format

```markdown
---
name: my-agent
description: When to use this agent (used for matching)
model: sonnet  # or opus, haiku
tools: [Read, Grep, Glob, Bash]
---

Agent system prompt and instructions here.
```

## Tips

- The `description` determines when Claude dispatches to this agent
- Limit tools to what the agent actually needs
- Use `haiku` for fast, simple tasks; `opus` for complex reasoning
- Agents run in isolation - they don't see conversation history
