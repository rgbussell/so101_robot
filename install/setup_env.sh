#!/bin/bash
set -e

REPO_DIR=~/repos

cd REPO_DIR
git clone https://github.com/huggingface/lerobot.git
cd lerobot

conda create -y -n lerobot python=3.10
conda activate lerobot

conda install ffmpeg=7.1.1 -c conda-forge # this part was not straighforward on mac osx

pip install -e .

# install sim environment 
pip install -e ".[aloha]"

# install motors
pip install -e ".[feetech]"

# set up weights and biases tracking
wand login
