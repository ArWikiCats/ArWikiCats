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
def test_religions_big_data(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


data_2 = {}
with open(Path(__file__).parent / "religions2.json", "r", encoding="utf-8") as f:
    data_2 = json.load(f)


@pytest.mark.parametrize("name,data", [(f"test_big_data_2_{len(data_2)}_item", data_2)])
@pytest.mark.skip2
def test_religions_big_data_2(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
