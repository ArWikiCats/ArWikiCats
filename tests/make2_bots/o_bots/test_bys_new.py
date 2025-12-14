"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.o_bots.bys_new import resolve_by_labels

data1 = {
    "by city": "حسب المدينة",
    "by country": "حسب البلد",
    "by year": "حسب السنة",
}

file_path = Path(__file__).parent.parent.parent.parent.parent / "len_data/by_table.py/by_table.json"

data2 = {}

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        data2 = json.load(f)

to_test = [
    ("test_bys_new_1", data1),
    ("test_bys_new_2", data2),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_bys_new_1(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_bys_new_2(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
