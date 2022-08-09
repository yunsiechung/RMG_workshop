#!/bin/bash
#SBATCH -J rmg_methane
#SBATCH -n 1
#SBATCH --time=5-0:00:00

conda activate rmg_env_bin

rmg.py input.py

conda deactivate


