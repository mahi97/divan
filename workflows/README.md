# Workflows

Multi-step research pipeline definitions. Workflows chain together skills to
automate common research sequences.

## Available Workflows

| Workflow              | Description                                     |
|-----------------------|-------------------------------------------------|
| `train-evaluate`      | Full train → evaluate → log cycle               |
| `sweep-and-select`    | Sweep → pick best → final train run             |
| `experiment-to-paper` | Experiment → results → figure → paper section  |
| `new-project-setup`   | Clone → init → environment → first run          |

## How Agents Use Workflows

An agent reads a workflow file and follows the numbered steps. Workflows
reference skills by name — the agent should read the corresponding skill file
for detailed instructions.

## Example

"Run a hyperparameter sweep and produce a comparison figure":
→ Follow `workflows/sweep-and-select.md`
