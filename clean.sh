#!/bin/bash

# This script removes all generated files from the output/ directory.

echo "--- Cleaning output directory ---"

# The -f flag prevents an error if the directory is empty
rm -f output/*

echo "--- Cleanup complete ---"