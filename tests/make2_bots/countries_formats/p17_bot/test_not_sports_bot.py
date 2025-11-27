"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from src.make2_bots.countries_formats.not_sports_bot import (
    resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT,
)

main_data = {
    "england war and conflict": "حروب ونزاعات إنجلترا",
    "england war": "حرب إنجلترا",
    "georgia governorate": "حكومة جورجيا",
    "israel war and conflict": "حروب ونزاعات إسرائيل",
    "israel war": "حرب إسرائيل",
    "oceania cup": "كأس أوقيانوسيا",
    "spain war and conflict": "حروب ونزاعات إسبانيا",
    "spain war": "حرب إسبانيا",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=list(main_data.keys()))
@pytest.mark.fast
def test_resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT(category, expected) -> None:
    label = resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT", main_data, resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
