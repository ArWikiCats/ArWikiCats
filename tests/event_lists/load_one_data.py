#
from typing import Callable


def ye_test_one_dataset(dataset: dict, callback : Callable[[str], str]):
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

    return org, diff
