""" """

import json
from pathlib import Path
from typing import Callable

import pytest

from ArWikiCats import resolve_arabic_category_label
from utils.resolver_runner import make_resolver_test


diff_data_path = Path(__file__).parent / "diff_data"


def dump_one_new(data: dict, file_path: Path) -> None:
    if not data:
        return

    file_path.parent.mkdir(exist_ok=True, parents=True)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing diff data: {e}")


def dump_same_and_not_same(data: dict, diff_result: dict, name: str, folder_name: str) -> None:
    """
    Dump same data as JSON file for easy copy-paste to wiki.

    dump_same_add(data, diff_result, name)
    """
    folder_path = diff_data_path / folder_name / name
    folder_path_same = diff_data_path / folder_name / "same"

    dump_one_new(diff_result, folder_path / "new.json")

    if not data or not diff_result:
        return

    same_data = {x: v for x, v in data.items() if x not in diff_result}
    if len(same_data) != len(data):
        dump_one_new(same_data, folder_path_same / f"{name}.json")

    add_data = {x: v for x, v in data.items() if x in diff_result}
    if len(add_data) != len(data):
        dump_one_new(add_data, folder_path / "not_same.json")


def one_dump_test(dataset: dict, callback: Callable[[str], str], do_strip=False) -> tuple[dict, dict]:
    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = dict(dataset.items())  # if v
    for cat, ar in data.items():
        result = callback(cat)
        # ---
        if do_strip:
            result = result.strip() if isinstance(result, str) else result
            ar = ar.strip() if isinstance(ar, str) else ar
        # ---
        if result != ar:
            org[cat] = ar
            diff[cat] = result

    return org, diff


def JSON_FILES(dir_path) -> list:
    DATA_DIR = Path(__file__).parent / dir_path
    FILE_PATHS = sorted(DATA_DIR.glob("*.json"))
    return FILE_PATHS


def _test_data_helper(load_json_data: tuple[dict[str, str], str], folder_name: str) -> None:
    data, name = load_json_data

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_same_and_not_same(data, diff_result, name, folder_name)

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES("religions_data"), indirect=True, ids=lambda p: p.name)
def test_religions_data(load_json_data: tuple[dict[str, str], str]) -> None:
    _test_data_helper(load_json_data, "religions_data")


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES("big_data"), indirect=True, ids=lambda p: p.name)
def test_big_data(load_json_data: tuple[dict[str, str], str]) -> None:
    _test_data_helper(load_json_data, "big_data")


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES("data"), indirect=True, ids=lambda p: p.name)
def test_big_data_examples(load_json_data: tuple[dict[str, str], str]) -> None:
    _test_data_helper(load_json_data, "data")


def create_resolver_big_tests(dir_paths: list):
    for dir_path in dir_paths:
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


create_resolver_big_tests(
    [
        "religions_data",
        "big_data",
        "data",
    ]
)
