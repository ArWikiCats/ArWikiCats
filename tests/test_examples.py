"""
pytest tests/test_examples.py -m examples
"""

import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats import resolve_arabic_category_label

_CASES = {}

json_files = [x for x in (Path(__file__).parent.parent / "examples/data").glob("*.json")]

for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    _CASES[f"file_{file.name}_{len(data)}_item"] = data


@pytest.mark.parametrize("name,data", _CASES.items())
@pytest.mark.examples
def test_examples_data(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
