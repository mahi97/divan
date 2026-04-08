---
name: hpc-submit
description: Submit and manage jobs on an HPC cluster using PBS/Torque
---

# HPC Submit

## When to Use

- Submitting training or evaluation jobs to the HPC cluster
- Managing queued or running jobs on the supercomputer
- Creating PBS job scripts for batch processing

## Inputs

- Server connection details (read from `divan/docs/servers/hpc-pbs.md`)
- Experiment config (from `configs/`)
- Resource requirements (GPUs, CPUs, memory, walltime)

## Steps

1. **Read server config:**
   Read `divan/docs/servers/hpc-pbs.md` for login node, queue names, module
   system, and file paths.

2. **Create job script:**
   Write a PBS job script in `scripts/jobs/`:

   ```bash
   #!/bin/bash
   #PBS -N {{PROJECT_NAME}}_{{EXPERIMENT}}
   #PBS -l select=1:ncpus=8:ngpus=1:mem=32gb
   #PBS -l walltime=24:00:00
   #PBS -q {{QUEUE_NAME}}
   #PBS -o logs/{{EXPERIMENT}}.out
   #PBS -e logs/{{EXPERIMENT}}.err

   cd $PBS_O_WORKDIR
   module load python/3.12 cuda/12.x

   source .venv/bin/activate
   python src/train.py --config configs/{{CONFIG}}
   ```

3. **Sync code to cluster:**
   ```bash
   rsync -avz --exclude='.venv' --exclude='data/' --exclude='results/' \
     --exclude='wandb/' --exclude='.git' --exclude='divan/' \
     ./ {{LOGIN_NODE}}:~/projects/{{PROJECT_NAME}}/
   ```

4. **Submit job:**
   ```bash
   ssh {{LOGIN_NODE}} "cd ~/projects/{{PROJECT_NAME}} && qsub scripts/jobs/{{SCRIPT}}"
   ```

5. **Check status:**
   ```bash
   ssh {{LOGIN_NODE}} "qstat -u $USER"
   ```

6. **Monitor output:**
   ```bash
   ssh {{LOGIN_NODE}} "tail -f ~/projects/{{PROJECT_NAME}}/logs/{{EXPERIMENT}}.out"
   ```

## Job Management Commands

| Command                    | Purpose                              |
|----------------------------|--------------------------------------|
| `qsub script.pbs`         | Submit a job                         |
| `qstat -u $USER`          | List your jobs                       |
| `qstat -f JOB_ID`         | Job details                          |
| `qdel JOB_ID`             | Cancel a job                         |
| `qstat -Q`                | List available queues                |
| `pbsnodes -a`             | List all nodes and their status      |

## Output

```
## HPC Submit Report
- Cluster: {{CLUSTER_NAME}}
- Job ID: [from qsub output]
- Job script: scripts/jobs/{{SCRIPT}}
- Queue: {{QUEUE_NAME}}
- Resources: 1 GPU, 8 CPUs, 32GB RAM, 24h walltime
- Config: configs/{{CONFIG}}
- Status: queued
- Check: ssh {{LOGIN_NODE}} "qstat -f JOB_ID"
```

## Safety

- NEVER run compute on the login node — always use qsub
- Check queue status before submitting large batches
- Set reasonable walltime limits
- Ensure log directories exist before submitting
- Record job ID in the experiment log
- Clean up completed job logs periodically
- Respect fair-share policies — check current cluster load
