#!/bin/bash

# This script removes all generated files from the output/ directory
# and unstages them from Git.

echo "--- Cleaning output directory and Git index ---"

# Use git rm to remove files from both the working directory and the staging area.
# The --ignore-unmatch flag prevents an error if there are no files to remove.
# The -f flag forces removal of modified files.
# The -q flag suppresses output for each file removed.
git rm -fq --ignore-unmatch output/*

echo "--- Cleanup complete ---"