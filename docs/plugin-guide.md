# Plugin Guide

Detailed descriptions of every plugin in the Divan stack.

## Core Workflow

### superpowers (required)
The backbone of the stack. Provides structured workflows for:
- **Brainstorming** - Explore intent and requirements before implementation
- **Writing plans** - Multi-step implementation planning
- **Executing plans** - Plan execution with review checkpoints
- **TDD** - Test-driven development workflow
- **Systematic debugging** - Root cause analysis before fixing
- **Parallel agents** - Dispatch independent tasks concurrently
- **Code review** - Request and receive structured reviews
- **Git worktrees** - Isolated feature branches

### commit-commands (required)
Git workflow commands:
- `/commit` - Create a well-formatted git commit
- `/commit-push-pr` - Commit, push, and open a PR in one step
- `/clean_gone` - Clean up branches deleted on remote

### feature-dev
Guided feature development with three specialized agents:
- `code-architect` - Designs feature architecture
- `code-explorer` - Traces execution paths and maps dependencies
- `code-reviewer` - Reviews for bugs, security, and quality

### hookify
Create hooks from conversation analysis or explicit instructions:
- `/hookify` - Analyze conversation for behaviors to prevent
- `/hookify:list` - List configured rules
- `/hookify:configure` - Enable/disable rules

## Git & Code Quality

### github (required)
Full GitHub integration via Copilot MCP server. Issues, PRs, code search, repos, branches, releases, and more.

### code-review
PR review workflows. Use `/code-review` to review a pull request.

### code-simplifier
Post-implementation cleanup. Use `/simplify` to review changed code for reuse opportunities and quality improvements.

### qodo-skills
Loads coding rules from Qodo relevant to your current task. Integrates with PR review feedback across GitHub, GitLab, Bitbucket, Azure DevOps, and Gerrit.

## AI/ML Platforms

### vercel
Complete Vercel platform integration:
- Deployment (`/vercel:deploy`)
- Environment variables (`/vercel:env`)
- AI SDK guidance (`/vercel:ai-sdk`)
- Functions, storage, caching, middleware
- 20+ specialized skills for Next.js, Turbopack, auth, etc.

### huggingface-skills
ML operations on Hugging Face:
- Model training (LLM, vision, segmentation)
- Dataset operations
- Gradio app building
- Hub CLI operations
- Paper search and publishing
- Transformers.js for browser ML

### supabase
Database, auth, and storage via Supabase MCP server.

## Code Intelligence

### context7 (required)
Live documentation lookup for any library, framework, or SDK. Always fetches current docs instead of relying on training data.

### greptile
Semantic codebase search and analysis. Understands code structure beyond text matching.

## Frontend

### frontend-design
Creates distinctive, production-grade frontend interfaces. Avoids generic AI aesthetics. Use `/frontend-design` for component, page, or application generation.

## Development Tools

### plugin-dev
Toolkit for building Claude Code extensions:
- Plugin structure and scaffolding
- Skill, hook, agent, and command development
- MCP integration
- Plugin settings and validation

### skill-creator
Create, modify, evaluate, and benchmark skills. Includes performance variance analysis.

### agent-sdk-dev
Scaffold and verify Claude Agent SDK applications (TypeScript and Python).

### claude-code-setup
Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).

### claude-md-management
Audit and improve CLAUDE.md files in repositories.

## Communication

### telegram
Telegram bot integration. Send/receive messages, react, edit, and handle attachments.

## Language Servers

### clangd-lsp
C/C++ language server for code intelligence, diagnostics, and completions.

### pyright-lsp
Python type checking and language intelligence.

## Session Management

### remember
Persistent session state. Saves conversation context for clean continuation in the next session.

### ralph-loop (required)
Prevents self-referential loops where Claude gets stuck repeating actions.
