""" """

import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_arabic_category_label


@pytest.fixture
def example_data(request: pytest.FixtureRequest):
    file_path = request.param
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f), file_path.stem


DATA_DIR = Path(__file__).parent.parent.parent / "examples/big_data"
FILE_PATHS = sorted(DATA_DIR.glob("*.json"))


@pytest.mark.dumpbig
@pytest.mark.parametrize("example_data", FILE_PATHS, indirect=True, ids=lambda p: p.name)
def test_big_data(example_data: tuple[dict[str, str], str]) -> None:
    data, name = example_data
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
