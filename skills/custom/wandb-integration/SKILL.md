---
name: wandb-integration
description: Integrate Weights & Biases (W&B) as the single system of record for research runs, configs, sweeps, code snapshots, artifacts, checkpoints, and paper-ready analysis. Use when setting up or refactoring experiment tracking, sweep execution, result export, checkpoint resume/eval, or LLM evaluation workflows around W&B.
---

# WandB Integration

## When to Use

- Setting up W&B in a new ML or LLM research project
- Replacing ad hoc logging with one consistent experiment system
- Standardizing run names, config hashes, seed-grouping, and sweep tracking
- Adding artifact-based checkpoint storage, reload, resume, or re-evaluation flows
- Building scripts that pull runs from W&B and generate paper-quality matplotlib figures

## Inputs

- Project root and entrypoints for train, eval, sweep, and resume
- Main config structure and which fields define the readable run identity
- Seed field name and any fields that should be ignored for grouping
- W&B project/entity/job_type conventions
- Checkpoint policy: latest, best, periodic, final
- Whether the project has LLM-specific evals that should use W&B Weave

## Core Rule

Treat W&B as the experiment source of truth.

- Send configs to `wandb.config`
- Send metrics and logs to `wandb.log`
- Send sweeps through W&B sweeps
- Send code provenance and git metadata to W&B
- Send checkpoints and other reusable outputs as W&B artifacts

Do not build a parallel logging system unless the project already requires local logs as a cache or failure fallback.

If working from inside `divan/`, move to the parent project before editing runtime code. Keep the skill in `divan/`, but put training code, scripts, configs, and tests in the parent project.

## Recommended Tracking Contract

Add a small tracking block or equivalent computed fields to every run config.

```yaml
tracking:
  project: my-project
  entity: my-team
  job_type: train
  seed: 7
  run_stem: cifar10-resnet18-adamw-cosine-bs128
  run_hash: 7c9a31d2
  run_name: cifar10-resnet18-adamw-cosine-bs128-7c9a31d2
  config_hash: 1d8840d7
  group_hash: a42d9f16
  git_commit: 2f4c1ab
  git_dirty: false
  sweep_id: null
```

Use three identifiers, not one:

1. `run_hash`
   Unique per launched run. Use it to guarantee the final run name is always unique, even when the readable config stem repeats.
2. `config_hash`
   Deterministic hash of the fully resolved config, including seed. Use it to identify an exact reproducible config.
3. `group_hash`
   Deterministic hash of the resolved config with seed and other volatile fields removed. Use it to group runs that share the same experimental setup but vary by seed.

## Naming and Hashing Rules

### 1. Build an informative run stem

Construct `run_stem` from the main config choices that matter in tables and paper captions:

- task or dataset
- model
- optimizer or scheduler if important
- key batch or sequence setting if it changes interpretation
- ablation tag if applicable

Keep it short enough to scan in the W&B UI.

Example:

```text
cifar10-resnet18-adamw-cosine-bs128
```

### 2. Make the displayed run name unique

Always append a short `run_hash`:

```text
{run_stem}-{run_hash}
```

Do not rely on `run_stem` alone. Two launches with the same readable config must still get distinct names.

### 3. Canonicalize before hashing

Before computing hashes:

- resolve defaults
- sort keys recursively
- convert paths to stable relative strings when possible
- drop fields that are runtime-only for `group_hash`
- use a deterministic serializer such as sorted JSON

Suggested rule:

```python
full_config_for_hash = resolved_config
group_config_for_hash = resolved_config without ["seed", "tracking.run_hash", "tracking.run_name", "tracking.git_commit", "tracking.git_dirty", "output_dir", "timestamp"]
```

Use short hashes for names and tags, but keep the full canonical payload in the config for debugging if useful.

## W&B Initialization Rules

Initialize every run with explicit metadata.

```python
wandb.init(
    project=tracking.project,
    entity=tracking.entity,
    name=tracking.run_name,
    job_type=tracking.job_type,
    group=tracking.group_hash,
    config=resolved_config,
    tags=[tracking.job_type, tracking.config_hash],
    save_code=True,
)
```

Also record:

- git commit
- git dirty state
- branch if helpful
- hostname, cluster job id, or machine label if relevant
- sweep id for sweep-launched runs

If the repo is dirty, record that fact in config and in the run summary. Do not hide it.

## Logging Rules

### Metric names

Do not use `/` in metric names.

Use flat snake case so all plots stay in one consistent namespace:

- `train_loss`
- `train_lr`
- `val_accuracy`
- `eval_bleu`
- `system_gpu_mem_gb`

Avoid:

- `train/loss`
- `eval/accuracy`
- `gpu/memory`

### Round synchronization

If the code issues multiple `wandb.log` calls for one logical round, include the same `round` value in all of them.

```python
wandb.log({"round": round_idx, "train_loss": loss}, step=global_step, commit=False)
wandb.log({"round": round_idx, "train_grad_norm": grad_norm}, step=global_step, commit=False)
wandb.log({"round": round_idx, "train_lr": lr}, step=global_step)
```

Use:

- `round` for the logical training/eval round
- `step` for the monotonically increasing global step

Keep them explicit. Do not depend on implicit UI grouping.

### Summary values

At run end, write stable summary values for later tables and figure scripts:

- `best_val_loss`
- `best_val_accuracy`
- `final_train_loss`
- `best_checkpoint_artifact`
- `config_hash`
- `group_hash`

## Sweep Rules

Route sweeps through W&B.

- Define sweep search spaces in W&B-compatible config
- Record the base config and the resolved trial config
- Preserve `config_hash` and `group_hash` for each trial
- Tag sweep trials with a clear `job_type` and sweep identifier

For seed replicates inside a sweep:

- keep the trial-specific `run_hash` unique
- keep `group_hash` shared across seed variants of the same non-seed config
- use `group_hash` later to compute mean and standard deviation across seeds

## Code and Git Provenance

Every run should expose enough provenance to reproduce it.

- enable `save_code=True` or equivalent code capture
- log the git commit hash
- log whether the worktree was dirty
- log the config file path or resolved config artifact
- attach important launch files as artifacts when that improves reproducibility

When the project has generated config files, upload the final resolved config as an artifact or store it directly in W&B config in addition to the source file path.

## Artifact and Checkpoint Rules

Store reusable outputs in W&B artifacts.

At minimum, consider artifacts for:

- model checkpoints
- tokenizer or processor files
- resolved configs
- prediction dumps
- evaluation tables
- paper-ready derived datasets

Use consistent aliases such as:

- `latest`
- `best`
- `final`
- `epoch-0005`
- `step-010000`

When adding checkpoint support, also add project scripts for:

- pulling an artifact by name or alias
- resuming training from an artifact checkpoint
- re-evaluating a checkpoint artifact
- exporting predictions or metrics from a checkpoint

Prefer a small dedicated script surface such as:

```text
scripts/wandb_pull_artifact.py
scripts/wandb_resume.py
scripts/wandb_eval_checkpoint.py
scripts/wandb_export_runs.py
scripts/wandb_plot_runs.py
```

Adapt names to the repo's existing style.

## Paper Figure Workflow

Add scripts that read runs from the W&B SDK or API, then build publication-ready matplotlib figures.

The default workflow should be:

1. select runs from W&B by project, tags, run ids, config filters, or `group_hash`
2. pull summary metrics, histories, and artifacts
3. aggregate across seeds with mean and standard deviation using `group_hash`
4. render figures with matplotlib
5. save vector outputs such as PDF for paper use

Target outputs such as:

- `paper/figures/*.pdf`
- `results/figures/*.pdf`
- `results/tables/*.csv`

Keep these scripts editable and style-oriented. They should be easy to adjust for:

- color palette
- fonts
- legend placement
- smoothing choices
- metric selection
- run filtering logic
- seed aggregation

## LLM-Specific Rules

If the project works with LLMs:

- upload checkpoints, adapters, tokenizers, prompts, and eval outputs as artifacts
- prefer W&B Weave for trace-heavy LLM evaluation if the project already uses that stack
- otherwise store eval inputs, outputs, and scores in standard W&B tables and artifacts
- keep enough metadata to reload a checkpoint and rerun evaluation later

For LLM evaluation, store identifiers for:

- model artifact version
- prompt version
- dataset version
- judge or scorer version
- decoding settings

## Implementation Checklist

When applying this skill to a project:

1. add a small tracking utility that resolves config, builds hashes, and creates the W&B init payload
2. update train and eval entrypoints to call that utility
3. flatten metric names to snake case without `/`
4. add `round` to every logical logging round
5. upload checkpoints and reusable outputs as artifacts
6. add resume, reload, and re-eval scripts for artifacts
7. add W&B-backed export and plotting scripts for paper figures
8. test one normal run, one repeated run, and one same-config-different-seed pair

## Validation Checks

Before closing the task, verify:

- two launches with the same readable config get different `run_name` values
- two launches with the same full config get the same `config_hash`
- two launches with the same config except seed share the same `group_hash`
- W&B shows code provenance and git metadata
- no logged metric names contain `/`
- multi-log rounds share the same `round`
- checkpoint artifacts can be pulled and reused
- figure scripts can select runs and emit PDF output

## Output

```
## WandB Integration Report
- Tracking: W&B is the source of truth for configs, logs, sweeps, code, and artifacts
- Naming: informative stem + unique run_hash suffix
- Hashes: config_hash for exact config, group_hash for cross-seed grouping
- Logging: flat metric names, explicit round field
- Artifacts: checkpoints and reusable outputs uploaded to W&B
- Analysis: export/plot scripts generate paper-ready PDFs
```

## Safety

- Never commit W&B API keys or secrets
- Never upload private credentials inside artifacts
- Do not assume artifact storage is cheap; set a checkpoint retention policy
- Record dirty worktrees honestly
- Validate resume and re-eval flows with a short smoke test before large jobs
