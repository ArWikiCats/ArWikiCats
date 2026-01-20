"""
pytest tests/big_data/test_big.py -m dumpbig
"""

import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_arabic_category_label


@pytest.fixture
def load_json_data(request: pytest.FixtureRequest):
    file_path = request.param
    file_path = Path(file_path)

    if not file_path.exists():
        pytest.skip(f"File {file_path} not found")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_dump_logic(name, data):
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


def JSON_FILES():
    base_path = Path(__file__).parent.parent.parent / "examples/religions_data"
    return sorted(base_path.glob("*.json"))


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES(), indirect=True, ids=lambda p: f"test_big_{p.name}")
def test_religions_big_data(load_json_data: dict, request: pytest.FixtureRequest) -> None:
    name = request.node.callspec.id
    run_dump_logic(name, load_json_data)
