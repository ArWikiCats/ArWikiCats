#
import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar


@pytest.fixture
def load_json_data(request):
    file_path = request.param
    if not file_path.exists():
        return {}  # أو pytest.skip(f"File {file_path} not found")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_dump_logic(name, data):
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    # dump_diff(expected2, f"{name}_expected")
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


FILES_PATHS = [
    Path("D:/categories_bot/len_data/films_mslslat.py/films_mslslat_tab_base_org.json"),
    # Path("D:/categories_bot/len_data/films_mslslat.py/films_key_for_nat_extended_org.json"),
]


@pytest.mark.skip2
# @pytest.mark.dump
@pytest.mark.parametrize("load_json_data", FILES_PATHS, indirect=True, ids=lambda p: f"test_big_{p.name}")
def test_religions_big_data(load_json_data, request) -> None:
    name = request.node.callspec.id
    run_dump_logic(name, load_json_data)
