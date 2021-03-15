#!/bin/bash
set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Changing dir to location of heimdall.py (or where it should be...)"
cd $script_dir

# Start up the bot!
pipenv run ./heimdall.py
