#!/usr/bin/env bash
set -euo pipefail

# Load .env if present
if [ -f .env ]; then
  # shellcheck disable=SC2046
  export $(grep -v '^#' .env | xargs)
fi

# Run uvicorn from this directory
exec uvicorn main:app --reload --host 0.0.0.0 --port 8000