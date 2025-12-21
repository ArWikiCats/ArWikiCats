"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.o_bots.bys_new import resolve_by_labels

from ArWikiCats.translations.by_type import (
    _by_and_fields,
    _by_or_fields,
    _by_by_fields,
    _by_music_labels,
    _by_music_table_base,
    _by_map_table,
)

to_test = [
    ("test_by_and_fields", _by_and_fields),
    ("test_by_or_fields", _by_or_fields),
    ("test_by_by_fields", _by_by_fields),
    ("test_by_musics", _by_music_labels),
    ("test_music_by_table", _by_music_table_base),
    ("_by_map_table", _by_map_table),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
