# This script runs pytest from inside Python so Scalene can profile it.
# python -m scalene run_pytest.py

import pytest

pytest.main(["-q"])
