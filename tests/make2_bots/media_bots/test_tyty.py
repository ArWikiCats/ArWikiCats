"""
Tests
"""

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import search_multi


def fast_data1():
    file_path = Path("D:/categories_bot/len_data/films_mslslat.py/tyty_data.json")
    data = json.loads(file_path.read_text(encoding="utf-8"))

    return data  # dict(list(data.items())[:10000])


test_data = {}

test_data = fast_data1()


@pytest.mark.parametrize("category, expected", test_data.items(), ids=list(test_data.keys()))
@pytest.mark.skip2
def test_search_multi(category: str, expected: str) -> None:
    label = search_multi(category)
    assert label == expected


to_test = [
    ("test_search_multi", test_data, search_multi),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result)}"
