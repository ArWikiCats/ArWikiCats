#
from typing import Dict
import json
from typing import Callable
from pathlib import Path

from src import new_func_lab_final_label


def dump_diff(data, file_name):
    diff_data_path = Path(__file__).parent / "diff_data"
    diff_data_path.mkdir(exist_ok=True, parents=True)
    file_path = diff_data_path / f"{file_name}.json"

    if data or file_path.exists():
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error writing diff data: {e}")


def ye_test_one_dataset(dataset: dict, callback : Callable[[str], str]):

    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = callback(cat)
        if result != ar:
            org[cat] = ar
            diff[cat] = result

    return org, diff


def ye_test_one_dataset_new(dataset: Dict):

    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab_final_label(cat)
        if result != ar:
            org[cat] = ar
            diff[cat] = result

    return org, diff
