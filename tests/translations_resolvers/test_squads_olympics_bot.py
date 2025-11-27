"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from src.translations_resolvers.squads_olympics_bot import resolve_en_is_P17_ar_is_P17_SPORTS

data = {
    "uzbekistan afc asian cup squad": "تشكيلات أوزبكستان في كأس آسيا",
    "china afc women's asian cup squad": "تشكيلات الصين في كأس آسيا للسيدات",
    "democratic-republic-of-the-congo winter olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "democratic-republic-of-the-congo summer olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الصيفية",
    "west india olympics squad": "تشكيلات الهند الغربية في الألعاب الأولمبية",
    "victoria-australia fifa futsal world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم لكرة الصالات",
    "victoria-australia fifa world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم",
    "yemen afc asian cup squad": "تشكيلات اليمن في كأس آسيا",
    "yemen afc women's asian cup squad": "تشكيلات اليمن في كأس آسيا للسيدات",
    "democratic-republic-of-the-congo winter olympics": "جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "west india summer olympics": "الهند الغربية في الألعاب الأولمبية الصيفية",
}


@pytest.mark.parametrize("category, expected_key", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_resolve_en_is_P17_ar_is_P17_SPORTS(category, expected_key) -> None:
    label1 = resolve_en_is_P17_ar_is_P17_SPORTS(category)

    assert label1.strip() == expected_key


TEMPORAL_CASES = [
    ("test_resolve_en_is_P17_ar_is_P17_SPORTS", data, resolve_en_is_P17_ar_is_P17_SPORTS),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=True)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
