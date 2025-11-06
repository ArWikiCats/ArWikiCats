#
import json
from typing import Callable
from pathlib import Path


def _dump_diff(diff, file_name):
    try:
        with open(Path(__file__).parent / "diff_data" / f"{file_name}.json", "w") as f:
            f.write(json.dumps(diff, ensure_ascii=False, indent=4))
    except Exception as e:
        print(f"Error writing diff data: {e}")


def ye_test_one_dataset(dataset: dict, callback : Callable[[str], str], file_name=""):
    diff_data_path = Path(__file__).parent / "diff_data"
    diff_data_path.mkdir(exist_ok=True, parents=True)

    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = callback(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    if file_name:
        _dump_diff(diff, file_name)

    return org, diff
