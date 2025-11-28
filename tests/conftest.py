"""Test configuration for the test-suite."""

import sys
from pathlib import Path

# Add the ArWikiCats directory to the python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
