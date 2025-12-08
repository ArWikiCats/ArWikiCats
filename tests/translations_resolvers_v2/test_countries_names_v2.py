"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations_resolvers_v2.countries_names_v2 import (
    resolve_by_countries_names_v2,
)

main_data = {
    # ar
    "Olympic gold medalists for the United States in alpine skiing": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "uzbekistan afc asian cup squad": "تشكيلات أوزبكستان في كأس آسيا",
    "china afc women's asian cup squad": "تشكيلات الصين في كأس آسيا للسيدات",
    "democratic-republic-of-congo winter olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "democratic-republic-of-congo summer olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الصيفية",
    "west india olympics squad": "تشكيلات الهند الغربية في الألعاب الأولمبية",
    "victoria-australia fifa futsal world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم لكرة الصالات",
    "victoria-australia fifa world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم",
    "yemen afc asian cup squad": "تشكيلات اليمن في كأس آسيا",
    "yemen afc women's asian cup squad": "تشكيلات اليمن في كأس آسيا للسيدات",
    "democratic-republic-of-congo winter olympics": "جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "west india summer olympics": "الهند الغربية في الألعاب الأولمبية الصيفية",
    "tunisia presidents": "رؤساء تونس",
    "tunisia government": "حكومة تونس",
    "tunisia territorial judges": "قضاة أقاليم تونس",
    "tunisia territorial officials": "مسؤولو أقاليم تونس",

    "yemen board members": "أعضاء مجلس اليمن",
    "yemen government": "حكومة اليمن",
    "yemen elections": "انتخابات اليمن",
    "yemen war": "حرب اليمن",
    "yemen responses": "استجابات اليمن",
    "yemen executive cabinet": "مجلس وزراء اليمن التنفيذي",
    "yemen presidents": "رؤساء اليمن",
    "yemen conflict": "نزاع اليمن",
    "yemen cup": "كأس اليمن",

    "victoria-australia elections": "انتخابات فيكتوريا (أستراليا)",
    "victoria-australia executive cabinet": "مجلس وزراء فيكتوريا (أستراليا) التنفيذي",
    "victoria-australia government": "حكومة فيكتوريا (أستراليا)",

    "west india government personnel": "موظفي حكومة الهند الغربية",
    "west india political leader": "قادة الهند الغربية السياسيون",
    "west india presidents": "رؤساء الهند الغربية",
    "west india responses": "استجابات الهند الغربية",

    "democratic-republic-of-congo territorial judges": "قضاة أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-congo territorial officials": "مسؤولو أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-congo war": "حرب جمهورية الكونغو الديمقراطية",

    "australia political leader": "قادة أستراليا السياسيون",
    "japan political leader": "قادة اليابان السياسيون",
    "mauritius political leader": "قادة موريشيوس السياسيون",
    "morocco political leader": "قادة المغرب السياسيون",
    "rwanda political leader": "قادة رواندا السياسيون",
    "syria political leader": "قادة سوريا السياسيون",
    "tunisia political leader": "قادة تونس السياسيون",
    "united states elections": "انتخابات الولايات المتحدة",
    "england war and conflict": "حروب ونزاعات إنجلترا",
    "england war": "حرب إنجلترا",
    "georgia government": "حكومة جورجيا",
    "israel war and conflict": "حروب ونزاعات إسرائيل",
    "israel war": "حرب إسرائيل",
    "oceania cup": "كأس أوقيانوسيا",
    "spain war and conflict": "حروب ونزاعات إسبانيا",
    "spain war": "حرب إسبانيا",

    # the_female
    "yemen royal air force": "القوات الجوية الملكية اليمنية",

    # males
    "yemen government officials": "مسؤولون حكوميون يمنيون",

    # the_male
    "yemen premier division": "الدوري اليمني الممتاز",
    "yemen coast guard": "خفر السواحل اليمني",
    "Bangladesh Federation Cup": "كأس الاتحاد البنغلاديشي",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=list(main_data.keys()))
@pytest.mark.fast
def test_resolve_by_countries_names_v2(category: str, expected: str) -> None:
    label = resolve_by_countries_names_v2(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_by_countries_names_v2", main_data, resolve_by_countries_names_v2),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
