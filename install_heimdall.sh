#!/bin/bash
set -e

# Thanks stack overflow! https://stackoverflow.com/questions/59895/how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itsel
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Moving to script dir, just in case we're not already there..."
cd $script_dir
# Install python dependencies first
echo "Installing Python dependencies..."
python3 -m pip install pipenv
pipenv install

# TODO: Other checks/install dependencies?
