"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.o_bots.bys_new import resolve_by_labels

from ArWikiCats.translations.by_type import (
    by_of_fields,
    by_table_year,
    by_and_fields,
    by_or_fields,
    by_by_fields,
    by_musics,
    Music_By_table,
)
data1 = {
    "by city": "حسب المدينة",
    "by country": "حسب البلد",
    "by year": "حسب السنة",
}

to_test = [
    ("test_bys_new_1", data1),
    ("test_by_table_year", by_table_year),
    ("test_by_of_fields", by_of_fields),
    ("test_by_and_fields", by_and_fields),
    ("test_by_or_fields", by_or_fields),
    ("test_by_by_fields", by_by_fields),
    ("test_by_musics", by_musics),
    ("test_music_by_table", Music_By_table),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_bys_new_1(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", by_table_year.items(), ids=by_table_year.keys())
@pytest.mark.fast
def test_by_table_year(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", by_of_fields.items(), ids=by_of_fields.keys())
@pytest.mark.fast
def test_by_of_fields(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
