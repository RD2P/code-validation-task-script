#!/bin/bash

# This script automates the process of generating Java files from the dataset.

# Exit immediately if a command exits with a non-zero status.
set -e

# 1. Generate the "buggy" versions of the Java files
echo "--- Generating buggy code files ---"
python3 main.py buggy_code

# 2. Stage all the generated files in Git
echo "--- Staging files with git add . ---"
git add .

# 3. Generate the "fixed" versions of the Java files
# This will overwrite the buggy files with the fixed versions.
echo "--- Generating fixed code files ---"
python3 main.py fixed_code

echo "--- Automation complete ---"