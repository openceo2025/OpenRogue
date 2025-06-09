#!/usr/bin/env bash
set -e

# Install runtime dependencies
if [ -f "requirements.txt" ]; then
    python -m pip install -r requirements.txt
fi

# Install pytest so tests can be executed
python -m pip install pytest

