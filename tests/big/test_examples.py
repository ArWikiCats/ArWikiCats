"""
"""
import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test
from ArWikiCats import resolve_arabic_category_label
from utils.resolver_runner import make_resolver_test


def JSON_FILES(dir_path):
    DATA_DIR = Path(__file__).parent.parent.parent / dir_path
    FILE_PATHS = sorted(DATA_DIR.glob("*.json"))
    return FILE_PATHS


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES("examples/data"), indirect=True, ids=lambda p: p.name)
def test_big_data(load_json_data: tuple[dict[str, str], str]) -> None:
    data, name = load_json_data
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


def create_resolver_big_tests(dir_path):
    for file_path in JSON_FILES(dir_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data1 = json.load(f)

        test_func = make_resolver_test(
            resolver=resolve_arabic_category_label,
            data=data1,
            test_name=f"test_{file_path}",
            marks=[pytest.mark.big],
        )

        globals()[test_func.__name__] = test_func


create_resolver_big_tests("examples/data")
