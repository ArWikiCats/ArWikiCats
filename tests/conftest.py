"""Test configuration for the test-suite."""

import sys
from pathlib import Path

# Ensure the parent directory (one level above this folder) is on sys.path,
# mirroring testmain2.py's behavior, so that `make2` can be imported.
REPO_ROOT = Path(__file__).resolve().parent.parent

candidate_str = str(REPO_ROOT)
if candidate_str not in sys.path:
    sys.path.append(candidate_str)
