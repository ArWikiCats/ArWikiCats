"""
Tests
"""

import pytest

from src.make2_bots.ma_bots.ar_lab import find_ar_label

data_list = [
    {"tito": " in ", "category": "1450s disestablishments in arizona territory", "output": "انحلالات عقد 1450 في إقليم أريزونا"},
]


@pytest.mark.parametrize("tab", data_list, ids=lambda x: x["category"])
@pytest.mark.slow
def test_big_data(tab) -> None:
    label_no_event2 = find_ar_label(tab["category"], tab["tito"], use_event2=False)
    label_with_event2 = find_ar_label(tab["category"], tab["tito"], use_event2=True)
    # ---
    assert label_no_event2 != tab["output"]
    assert label_with_event2 == tab["output"]
