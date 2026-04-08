# HPC Cluster Guide (PBS/Torque)

Access to a supercomputer via SSH to a login node, with job submission via PBS.

---

## Connection

```bash
# Add to ~/.ssh/config:
Host hpc
  HostName {{HPC_LOGIN_NODE}}
  User {{HPC_USER}}
  IdentityFile ~/.ssh/id_rsa
  ServerAliveInterval 60

# Connect:
ssh hpc
```

Fill in:
- `{{HPC_LOGIN_NODE}}` — e.g., `login.cluster.uni.edu`
- `{{HPC_USER}}` — your cluster username

## Hardware Overview

```
Login nodes:    {{LOGIN_NODE_COUNT}} nodes (NO COMPUTE HERE)
GPU queues:     {{GPU_QUEUE_INFO}}   (e.g., gpu_a100: 8x A100 per node)
CPU queues:     {{CPU_QUEUE_INFO}}
Max walltime:   {{MAX_WALLTIME}}     (e.g., 48:00:00)
Max GPUs/job:   {{MAX_GPUS}}
```

## Storage

```bash
HOME:     /home/{{HPC_USER}}/          # Limited quota, for code and configs
SCRATCH:  {{SCRATCH_PATH}}             # Large fast storage, use for data/results
SHARED:   {{SHARED_DATA_PATH}}         # Shared datasets (read-only typically)
```

> **Important:** Run large jobs from SCRATCH, not HOME. Check quotas: `quota -s`

## Module System

```bash
# List available modules
module avail

# Load Python and CUDA
module load {{PYTHON_MODULE}}     # e.g., python/3.12
module load {{CUDA_MODULE}}       # e.g., cuda/12.1
module load {{CUDNN_MODULE}}      # e.g., cudnn/8.9

# Check loaded modules
module list

# Add to job scripts to ensure consistent environment
```

## PBS Job Script Template

Save as `scripts/jobs/train.pbs`:

```bash
#!/bin/bash
#PBS -N {{PROJECT_NAME}}_train
#PBS -l select=1:ncpus={{NCPUS}}:ngpus={{NGPUS}}:mem={{MEM}}gb
#PBS -l walltime={{WALLTIME}}
#PBS -q {{QUEUE_NAME}}
#PBS -o {{SCRATCH_PATH}}/{{PROJECT_NAME}}/logs/${PBS_JOBID}.out
#PBS -e {{SCRATCH_PATH}}/{{PROJECT_NAME}}/logs/${PBS_JOBID}.err
#PBS -j oe                          # Merge stdout and stderr (optional)

# Print job info
echo "Job ID: $PBS_JOBID"
echo "Node: $(hostname)"
echo "Start: $(date)"

# Load modules
module load {{PYTHON_MODULE}}
module load {{CUDA_MODULE}}

# Set working directory
cd $PBS_O_WORKDIR

# Activate environment
source .venv/bin/activate

# Run experiment
python src/train.py --config configs/${CONFIG:-base.yaml}

echo "End: $(date)"
```

## Key PBS Commands

| Command                            | Purpose                            |
|------------------------------------|------------------------------------|
| `qsub script.pbs`                  | Submit a job                       |
| `qsub -v CONFIG=exp_0001.yaml script.pbs` | Submit with variable     |
| `qstat`                            | All jobs in queue                  |
| `qstat -u $USER`                   | Your jobs only                     |
| `qstat -f JOB_ID`                  | Full job details                   |
| `qdel JOB_ID`                      | Cancel a job                       |
| `qstat -Q`                         | List queues                        |
| `pbsnodes -a`                      | Node status (available/busy)       |
| `checkjob JOB_ID`                  | Why is job waiting? (Moab/Torque)  |

## Typical Workflow

```bash
# 1. Sync code to cluster
rsync -avz \
  --exclude='.venv' --exclude='data/' --exclude='results/' \
  --exclude='wandb/' --exclude='.git' --exclude='divan/' \
  ./ hpc:~/projects/{{PROJECT_NAME}}/

# 2. SSH to login node for setup
ssh hpc "
  cd ~/projects/{{PROJECT_NAME}} &&
  module load {{PYTHON_MODULE}} &&
  uv sync --extra dev
"

# 3. Create log directory on scratch
ssh hpc "mkdir -p {{SCRATCH_PATH}}/{{PROJECT_NAME}}/logs"

# 4. Submit job
ssh hpc "cd ~/projects/{{PROJECT_NAME}} && qsub scripts/jobs/train.pbs"
# → Output: 12345.cluster (your Job ID)

# 5. Monitor
ssh hpc "qstat -u $USER"
ssh hpc "tail -f {{SCRATCH_PATH}}/{{PROJECT_NAME}}/logs/12345.cluster.out"

# 6. Retrieve results when done
rsync -avz hpc:{{SCRATCH_PATH}}/{{PROJECT_NAME}}/results/ ./results/
```

## Array Jobs (Multiple Experiments)

Run the same script with different configs:

```bash
#!/bin/bash
#PBS -J 1-5                    # Array: indices 1 through 5
#PBS -l select=1:ngpus=1:mem=32gb
#PBS -l walltime=12:00:00
#PBS -q {{QUEUE_NAME}}
#PBS -o logs/${PBS_JOBID}.out

# Map array index to config
CONFIGS=(exp_0001.yaml exp_0002.yaml exp_0003.yaml exp_0004.yaml exp_0005.yaml)
CONFIG=${CONFIGS[$PBS_ARRAY_INDEX-1]}

module load {{PYTHON_MODULE}} {{CUDA_MODULE}}
source .venv/bin/activate
python src/train.py --config configs/$CONFIG
```

Submit: `qsub array_job.pbs`
Check: `qstat -t` (shows each sub-job)

## Common Issues

| Problem                     | Fix                                              |
|-----------------------------|--------------------------------------------------|
| Job stays queued            | `checkjob JOB_ID` to see why                    |
| Ran on login node by mistake| Always use `qsub`. Kill immediately.             |
| Job killed: walltime        | Increase `#PBS -l walltime` or add checkpointing |
| Job killed: OOM             | Increase `mem=` in select statement              |
| CUDA not found              | Add `module load {{CUDA_MODULE}}` to job script  |
| Can't find data             | Use full SCRATCH path, not relative paths        |
| Module conflict             | `module purge` before loading                    |

## Environment Variables in Jobs

Set in job script or via `-v`:

```bash
qsub -v "WANDB_API_KEY=${WANDB_API_KEY},EXPERIMENT=0001" train.pbs
```

Or export from `.env` before submitting:
```bash
export $(cat .env | xargs) && qsub train.pbs
```

## Monitoring Running Jobs

```bash
# Watch your jobs
ssh hpc "watch -n 10 'qstat -u $USER'"

# Live log output
ssh hpc "tail -f {{SCRATCH_PATH}}/{{PROJECT_NAME}}/logs/JOB_ID.out"

# GPU utilization (if allowed on compute nodes)
ssh hpc "ssh NODE_NAME 'nvidia-smi'"
```
