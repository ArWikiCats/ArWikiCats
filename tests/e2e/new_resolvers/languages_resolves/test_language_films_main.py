"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

test_data_skip = {
    "Assamese-language remakes of Hindi films": "",
    "Assamese-language remakes of Malayalam films": "",
}

test_data_0 = {
    "fijian language": "اللغة الفيجية",
    "japanese language": "اللغة اليابانية",
    "Chinese language templates": "قوالب اللغة الصينية",
    "1960s Dutch-language films": "أفلام باللغة الهولندية في عقد 1960",
    "2010s French-language films": "أفلام باللغة الفرنسية في عقد 2010",
    "1960s in Dutch-language films": "أفلام باللغة الهولندية في عقد 1960",
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


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
