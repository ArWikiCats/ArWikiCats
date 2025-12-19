"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.o_bots.bys_new import resolve_by_labels

from ArWikiCats.translations.by_type import (
    by_and_fields,
    by_or_fields,
    by_by_fields,
    by_musics,
    Music_By_table,
)

to_test = [
    ("test_by_and_fields", by_and_fields),
    ("test_by_or_fields", by_or_fields),
    ("test_by_by_fields", by_by_fields),
    ("test_by_musics", by_musics),
    ("test_music_by_table", Music_By_table),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
