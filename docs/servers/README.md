# Server Access Guides

This directory documents how to access and use the two GPU compute environments.

| Server Type   | Guide             | Access Method      | Job Management           |
|---------------|-------------------|--------------------|--------------------------|
| Bare GPU      | `bare-gpu.md`     | SSH direct         | tmux, manual             |
| HPC Cluster   | `hpc-pbs.md`      | SSH to login node  | qsub / qstat / qdel      |

## Quick Decision Guide

- **Small experiments, fast iteration:** bare GPU
- **Large jobs, long walltime, multiple GPUs:** HPC cluster
- **Interactive debugging:** bare GPU
- **Reproducible batch runs:** HPC cluster

## Filling in Your Details

Both guide files contain `{{PLACEHOLDER}}` values that you should replace
with your actual server details. Do this once after cloning divan:

1. Edit `docs/servers/bare-gpu.md` — fill in your server hostname, username,
   paths, and GPU types.
2. Edit `docs/servers/hpc-pbs.md` — fill in your login node, queue names,
   module system details, and storage paths.

These files are personal configuration. Do not commit real hostnames or
usernames if this repo is public.
