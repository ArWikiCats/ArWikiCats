"""
pytest tests/test_big_data.py -m skip2
"""

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

ENTERTAINMENT_CASES = []

for i in range(1, 11):
    file = Path(__file__).parent / "data" / f"{i}.json"
    if file.exists():
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        ENTERTAINMENT_CASES.append((f"test_big_{i}", data))


@pytest.mark.parametrize("name,data", ENTERTAINMENT_CASES)
@pytest.mark.skip2
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
