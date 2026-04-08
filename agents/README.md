# Agents

Agent definitions for automating multi-step research tasks.

These are higher-level than skills — an agent may invoke multiple skills in
sequence, make decisions based on results, and operate more autonomously.

## Available Agents

| Agent               | Purpose                                           |
|---------------------|---------------------------------------------------|
| `experiment-agent`  | Fully autonomous experiment run + log cycle       |
| `paper-agent`       | Drafts a paper section from experiment results    |

## How to Use

Agents are invoked by name. Claude Code and Codex will read the agent definition
file and follow the instructions.

Example: "Use the experiment-agent to run experiment 0003."

## Creating New Agents

Add a new markdown file to this directory with:
1. **Purpose** — what the agent does autonomously
2. **Inputs** — what it needs to start
3. **Decision points** — where it makes choices
4. **Steps** — ordered procedure
5. **Safety stops** — conditions under which it must pause and ask
6. **Output** — what it produces
