---
name: monitoring-setup
description: Set up experiment monitoring with W&B, TensorBoard, or custom logging
---

# Monitoring Setup

## When to Use

- Setting up experiment tracking for a new project
- Adding monitoring to existing training code
- The operator asks to "track experiments" or "set up W&B"

## Inputs

- Monitoring tool preference: wandb, tensorboard, or both
- Metrics to track (loss, accuracy, learning rate, GPU utilization)
- Project name and entity (for W&B)

## Steps

1. **Choose monitoring tool:**

   | Tool         | Best for                     | Setup complexity |
   |--------------|------------------------------|-----------------|
   | W&B          | Full experiment tracking      | pip install + API key |
   | TensorBoard  | Quick local visualization     | pip install only |
   | Both         | W&B for tracking + TB for live | Both setups |

2. **Install dependencies:**
   ```bash
   pip install wandb tensorboard
   ```

3. **Configure W&B (if selected):**
   ```bash
   wandb login  # Prompts for API key
   ```
   Add to `.env` (gitignored):
   ```
   WANDB_PROJECT={{PROJECT_NAME}}
   WANDB_ENTITY={{OWNER}}
   ```

4. **Add logging code:**

   W&B integration:
   ```python
   import wandb

   wandb.init(project="{{PROJECT_NAME}}", config=config)

   # In training loop:
   wandb.log({"loss": loss, "lr": lr, "epoch": epoch})

   # At end:
   wandb.finish()
   ```

   TensorBoard integration:
   ```python
   from torch.utils.tensorboard import SummaryWriter

   writer = SummaryWriter("runs/experiment_NNNN")

   # In training loop:
   writer.add_scalar("loss/train", loss, step)
   writer.add_scalar("lr", lr, step)

   writer.close()
   ```

5. **Add GPU monitoring:**
   ```python
   import subprocess

   def log_gpu_stats():
       result = subprocess.run(
           ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used,temperature.gpu",
            "--format=csv,noheader,nounits"],
           capture_output=True, text=True
       )
       gpu_util, mem_used, temp = result.stdout.strip().split(", ")
       return {"gpu_util": float(gpu_util), "gpu_mem": float(mem_used), "gpu_temp": float(temp)}
   ```

6. **Verify monitoring works:**
   Run a short training loop and check the dashboard.

## Output

```
## Monitoring Setup Report
- Tool: wandb + tensorboard
- W&B project: {{PROJECT_NAME}}
- TensorBoard logdir: runs/
- Metrics tracked: loss, lr, accuracy, gpu_util, gpu_mem
- Dashboard: [W&B URL if applicable]
```

## Safety

- Never commit W&B API keys or tokens
- Add `wandb/` to `.gitignore`
- Use `.env` for API keys, loaded with `python-dotenv` or shell export
- TensorBoard `runs/` directory should be gitignored if large
