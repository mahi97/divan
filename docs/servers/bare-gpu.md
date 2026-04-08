# Bare GPU Server Guide

Direct SSH access to a dedicated GPU machine.

---

## Connection

```bash
# Add to ~/.ssh/config for convenience:
Host gpu
  HostName {{GPU_SERVER_HOST}}
  User {{GPU_SERVER_USER}}
  IdentityFile ~/.ssh/id_rsa
  ServerAliveInterval 60

# Then connect with:
ssh gpu
```

Fill in:
- `{{GPU_SERVER_HOST}}` — e.g., `192.168.1.100` or `gpu.mylab.org`
- `{{GPU_SERVER_USER}}` — your username on the server

## Hardware

```
GPUs:     {{GPU_TYPE}} x {{GPU_COUNT}}  (e.g., NVIDIA A100 x 2)
VRAM:     {{GPU_VRAM}} each
CPU:      {{CPU_INFO}}
RAM:      {{SERVER_RAM}}
Storage:  {{STORAGE_INFO}}
```

## Paths

```bash
HOME:      /home/{{GPU_SERVER_USER}}/
PROJECTS:  /home/{{GPU_SERVER_USER}}/projects/
DATA:      {{DATA_PATH}}          # e.g., /data/shared/ or /scratch/
SCRATCH:   {{SCRATCH_PATH}}       # Fast local storage for runs
```

## Software Environment

```bash
# Python
{{PYTHON_SETUP}}    # e.g., conda or pyenv

# CUDA
CUDA version: {{CUDA_VERSION}}
cuDNN:        {{CUDNN_VERSION}}

# Load environment:
{{ENV_ACTIVATE}}    # e.g., source ~/miniconda3/etc/profile.d/conda.sh && conda activate base
```

## Checking GPU Availability

```bash
# Quick check
ssh gpu "nvidia-smi"

# Detailed — memory, utilization, processes
ssh gpu "nvidia-smi --query-gpu=index,name,memory.free,memory.total,utilization.gpu,temperature.gpu --format=csv"

# Watch live
ssh gpu "watch -n 2 nvidia-smi"
```

## Deploying and Running Jobs

### 1. Sync code

```bash
rsync -avz \
  --exclude='.venv' --exclude='data/' --exclude='results/' \
  --exclude='wandb/' --exclude='.git' --exclude='divan/' \
  ./ gpu:~/projects/{{PROJECT_NAME}}/
```

### 2. Set up environment (first time)

```bash
ssh gpu "
  cd ~/projects/{{PROJECT_NAME}} &&
  python3 -m venv .venv &&
  source .venv/bin/activate &&
  pip install -e '.[dev]'
"
```

### 3. Run in tmux (survives disconnect)

```bash
# Start a new session
ssh gpu "tmux new-session -d -s {{SESSION_NAME}} \
  'cd ~/projects/{{PROJECT_NAME}} && source .venv/bin/activate && \
   python src/train.py --config configs/{{CONFIG}}'"

# Attach to watch
ssh gpu "tmux attach -t {{SESSION_NAME}}"

# Detach: Ctrl+B then D

# List sessions
ssh gpu "tmux ls"

# Kill session
ssh gpu "tmux kill-session -t {{SESSION_NAME}}"
```

## Environment Variables on Server

Set project-specific variables in `~/.bashrc` or a per-project `.env`:

```bash
export WANDB_API_KEY="..."
export HF_TOKEN="..."
export DATA_ROOT="{{DATA_PATH}}"
```

Load in Python:
```python
from dotenv import load_dotenv
load_dotenv()  # reads .env file
```

## Common Issues

| Problem              | Fix                                          |
|----------------------|----------------------------------------------|
| SSH timeout          | Add `ServerAliveInterval 60` to ssh config   |
| OOM on GPU           | Reduce batch size, use gradient checkpointing|
| Process stuck        | `ssh gpu "kill -9 PID"` or `nvidia-smi` PID |
| Permission denied    | Check file ownership: `ls -la`               |
| CUDA not found       | Run the environment load command again       |

## Monitoring a Running Job

```bash
# GPU utilization
ssh gpu "watch -n 2 nvidia-smi"

# Training logs (if piped to file)
ssh gpu "tail -f ~/projects/{{PROJECT_NAME}}/logs/train.log"

# tmux output
ssh gpu "tmux attach -t {{SESSION_NAME}}"
```
