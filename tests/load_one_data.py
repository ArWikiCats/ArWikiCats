#
import json
from pathlib import Path
from typing import Callable


def dump_diff(data, file_name, _sort=True):
    if not data:
        return

    diff_data_path = Path(__file__).parent / "diff_data"
    diff_data_path.mkdir(exist_ok=True, parents=True)
    file_path = diff_data_path / f"{file_name}.json"

    if _sort:
        data_sorted = {x: v for x, v in data.items() if v}
        data_sorted.update({y: z for y, z in data.items() if not z})
    else:
        data_sorted = data

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_sorted, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing diff data: {e}")


def one_dump_test(dataset: dict, callback: Callable[[str], str]):
    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items()}  # if v
    for cat, ar in data.items():
        result = callback(cat)
        if result != ar:
            org[cat] = ar
            diff[cat] = result

    return org, diff
