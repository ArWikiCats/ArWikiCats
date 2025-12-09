"""
pytest tests/big_data/test_big.py -m skip2
"""

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

_CASES = []

json_files = [x for x in (Path(__file__).parent).glob("*.json")]

for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    _CASES.append((f"test_big_{file.name}_{len(data)}_item", data))


@pytest.mark.parametrize("name,data", _CASES)
@pytest.mark.skip2
def test_relegins_big_data(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
