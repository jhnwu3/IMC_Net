#!/bin/bash
#SBATCH --time=0-50:10:00 
#SBATCH --job-name=DataLoad
#SBATCH --partition=general
#SBATCH --nodes=1
#SBATCH --output=data%j.txt
#SBATCH --cpus-per-task=30
# load all modules, build terminal code, move all outputs into output folders.

matlab -nodisplay -nosplash -nodesktop -r "run('convertData.m');exit;"
