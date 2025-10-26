#!/bin/bash

set -euo pipefail

VERBOSE=false
TEST_MODE=false
CLEAN=false
EXECUTE=false

# Valid short options: t (tests), v (verbose), c (clean)
while getopts "tvcx" opt; do
  case $opt in
    v)
      VERBOSE=true
      echo "Verbose mode enabled"
      ;;
    t)
      TEST_MODE=true
      if [ "$VERBOSE" = true ]; then
          echo "Test mode enabled"
      fi
      ;;
    c)
      CLEAN=true
      if [ "$VERBOSE" = true ]; then
          echo "Clean mode enabled"
      fi
      ;;
    x)
      EXECUTE=true
      if [ "$VERBOSE" = true ]; then
          echo "Execute mode enabled"
      fi
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

if [ "$TEST_MODE" = true ]; then
    if [ "$VERBOSE" = true ]; then
        echo "Executing tests"
        echo "python3 -m unittest discover -v -s tests"
    fi
    # Run the tests using python -m unittest
    python3 -m unittest discover -v -s tests
fi

if [ "$EXECUTE" = true ]; then
    if [ "$VERBOSE" = true ]; then
        echo "Executing main python file"
        echo "python3 src/2_norm.py $@"
    fi
    # Run the main python script
    python3 src/2_norm.py $@
fi


if [ "$CLEAN" = true ]; then
    if [ "$VERBOSE" = true ]; then
        echo "Clearing generated files: logs, tests, output"
    fi
    # Remove logs if present, ignore errors if not
    rm -f logs/*.log || true
    rm -rf tests/__pycache__ || true
    rm -rf src/__pycache__ || true
    rm -rf data/output/* || true
fi



