---
name: gpu-deploy
description: Deploy and run code on a bare GPU server via SSH
---

# GPU Deploy

## When to Use

- Deploying code to a bare GPU server for training or inference
- Setting up a remote environment on a GPU machine
- Launching a training run on a directly-accessible GPU server

## Inputs

- Server connection details (read from `divan/docs/servers/bare-gpu.md`)
- Code to deploy (current project, or specific files)
- Experiment config (from `configs/`)
- GPU requirements (number of GPUs, memory)

## Steps

1. **Read server config:**
   Read `divan/docs/servers/bare-gpu.md` for connection details, paths, and
   environment setup instructions.

2. **Check GPU availability:**
   ```bash
   ssh {{SERVER}} "nvidia-smi --query-gpu=index,memory.free,utilization.gpu --format=csv"
   ```

3. **Sync code to server:**
   ```bash
   rsync -avz --exclude='.venv' --exclude='data/' --exclude='results/' \
     --exclude='wandb/' --exclude='.git' --exclude='divan/' \
     ./ {{SERVER}}:~/projects/{{PROJECT_NAME}}/
   ```

4. **Set up remote environment (first time):**
   ```bash
   ssh {{SERVER}} "cd ~/projects/{{PROJECT_NAME}} && python -m venv .venv && \
     source .venv/bin/activate && pip install -e '.[dev]'"
   ```

5. **Launch training in tmux:**
   ```bash
   ssh {{SERVER}} "tmux new-session -d -s train 'cd ~/projects/{{PROJECT_NAME}} && \
     source .venv/bin/activate && python src/train.py --config configs/{{CONFIG}}'"
   ```

6. **Verify job started:**
   ```bash
   ssh {{SERVER}} "tmux ls && nvidia-smi"
   ```

## Output

```
## GPU Deploy Report
- Server: {{SERVER}}
- GPU(s): [indices used]
- Config: configs/{{CONFIG}}
- tmux session: train
- Status: running
- Monitor: ssh {{SERVER}} "tmux attach -t train"
```

## Safety

- Always check GPU availability before launching
- Use tmux/screen so jobs survive SSH disconnects
- Do not deploy secrets (check .gitignore before rsync)
- Do not overwrite running experiments without confirmation
- Record the server and session name in the experiment log
