"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from src.make2_bots.countries_formats.p17_bot import (
    Get_P17_main,
)

main_data = {
    "australia political leader": "قادة أستراليا السياسيون",
    "china university of": "جامعة الصين",
    "japan political leader": "قادة اليابان السياسيون",
    "mauritius political leader": "قادة موريشيوس السياسيون",
    "morocco political leader": "قادة المغرب السياسيون",
    "rwanda political leader": "قادة رواندا السياسيون",
    "syria political leader": "قادة سوريا السياسيون",
    "tunisia political leader": "قادة تونس السياسيون",
    "united states elections": "انتخابات الولايات المتحدة",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=list(main_data.keys()))
@pytest.mark.fast
def test_Get_P17_main(category, expected) -> None:
    label = Get_P17_main(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_Get_P17_main", main_data, Get_P17_main),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
