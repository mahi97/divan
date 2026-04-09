# Custom Hooks

Place custom hook configurations here. Scripts go in `scripts/`.

## Hook Events

- `PreToolUse` - Before a tool is executed
- `PostToolUse` - After a tool completes
- `SessionStart` - When a session begins
- `SessionEnd` - When a session ends
- `UserPromptSubmit` - When user sends a message
- `Stop` - When Claude stops generating

## Format

Define hooks in YAML and reference scripts in `scripts/`:

```yaml
# hooks/example-hook.yaml
event: PreToolUse
matcher: Bash
script: hooks/scripts/validate-command.sh
description: Validates bash commands before execution
```

## Script Convention

Scripts in `scripts/` receive context via environment variables and stdin.
Exit code 0 = allow, non-zero = block.
