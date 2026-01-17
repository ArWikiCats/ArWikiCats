"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

test_data_skip = {
    "Assamese-language remakes of Hindi films": "",
    "Assamese-language remakes of Malayalam films": "",
}

test_data_0 = {
    "Persian-language singers of Tajikistan": "مغنون باللغة الفارسية في طاجيكستان",
    "Yiddish-language singers of Austria": "مغنون باللغة اليديشية في النمسا",
    "Yiddish-language singers of Russia": "مغنون باللغة اليديشية في روسيا",
    "Tajik-language singers of Russia": "مغنون باللغة الطاجيكية في روسيا",
    "Persian-language singers of Russia": "مغنون باللغة الفارسية في روسيا",
    "Hebrew-language singers of Russia": "مغنون باللغة العبرية في روسيا",
    "German-language singers of Russia": "مغنون باللغة الألمانية في روسيا",
    "Azerbaijani-language singers of Russia": "مغنون باللغة الأذربيجانية في روسيا",
    "Urdu-language films by decade": "أفلام باللغة الأردية حسب العقد",
    "Czech-language films by genre": "أفلام باللغة التشيكية حسب النوع الفني",
    "Arabic-language action films": "أفلام حركة باللغة العربية",
}


to_test = [
    ("test_language_films_main_1", test_data_0),
]


@pytest.mark.parametrize("category, expected", test_data_0.items(), ids=test_data_0.keys())
@pytest.mark.fast
def test_language_films_main_1(category: str, expected: str) -> None:
    label2 = resolve_label_ar(category)
    assert label2 == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
