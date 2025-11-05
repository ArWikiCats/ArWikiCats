from __future__ import annotations

import sys
from pathlib import Path
import pytest

from src import event, new_func_lab

from tests_lists import (
    OIUHNM2,
    Yell,
    indianalist,
    c21st_list,
    shar_list,
    impooor_list,
    manga_list,
    States_list,
    States2_list,
    States3_list,
)


def new_func_lab_wrap(cat):
    result = new_func_lab(cat)

    if result and not result.startswith("تصنيف:"):
        result = f"تصنيف:{result}"

    return result


def test_ye():
    datasets = [
        ("2x", OIUHNM2),
        ("ye", Yell),
        ("indiana", indianalist),
        ("21", c21st_list),
        ("sh", shar_list),
        ("imp", impooor_list),
        ("manga", manga_list),
        ("States", States_list),
        ("States2", States2_list),
        ("States3", States3_list),
    ]
    org = {}
    diff = {}
    for name, dataset in datasets:
        print(f"{name=}")
        data = {x: v for x, v in dataset.items() if v}
        for cat, ar in data.items():
            result = new_func_lab_wrap(cat)
            if result == ar:
                print(f"{cat=}")
                assert result == ar
            else:
                org[cat] = ar
                diff[cat] = result

    assert org == diff
