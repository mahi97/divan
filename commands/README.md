# Custom Commands

Place custom slash commands here as `.md` files.

## Format

```markdown
---
name: my-command
description: What this command does
arguments:
  - name: target
    description: The target to operate on
    required: false
---

Command instructions here. Use $ARGUMENTS to reference passed arguments.
```

## Usage

Once installed, invoke with `/my-command` in Claude Code.
