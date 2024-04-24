#!/bin/bash

# Update package lists
sudo apt update

# Install necessary packages
sudo apt install -y python3 python3-pip git

# Check installed Python version
python3 --version

# Install additional Python packages if needed
pip3 install click

# Clone the Git repository to a specific location
git clone <repository_url> /Documents

# Enter the directory of the cloned repository
cd /path/to/destination

# Install CLI application
python3 -m pip install -e .

# Check todo installation
todo --version

