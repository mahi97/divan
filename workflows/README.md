# Workflows

Multi-step workflow definitions that combine skills, commands, and agents.

## Format

```yaml
# workflows/deploy-review.yaml
name: deploy-review
description: Full deploy review workflow
steps:
  - skill: code-review
  - skill: verification-before-completion
  - command: commit-push-pr
  - skill: deploy
```

## Tips

- Workflows orchestrate existing skills and commands
- Each step runs sequentially unless marked as parallel
- Use workflows for repeatable multi-step processes
