"""
Integration tests for countries names resolvers
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names import resolve_by_countries_names

political_data_v1 = {
    "Spies for China": "جواسيس لصالح الصين",
    "Spies for Germany": "جواسيس لصالح ألمانيا",
    "Spies for Israel": "جواسيس لصالح إسرائيل",
    "Spies for Russia": "جواسيس لصالح روسيا",
    "Spies for Taiwan": "جواسيس لصالح تايوان",
    "Spies for Soviet Union": "جواسيس لصالح الاتحاد السوفيتي",
    "Spies for United Kingdom": "جواسيس لصالح المملكة المتحدة",
    "Spies for United States": "جواسيس لصالح الولايات المتحدة",
    "World War I spies for France": "جواسيس الحرب العالمية الأولى لصالح فرنسا",
    "World War I spies for Germany": "جواسيس الحرب العالمية الأولى لصالح ألمانيا",
    "World War I spies for United Kingdom": "جواسيس الحرب العالمية الأولى لصالح المملكة المتحدة",
    "World War I spies for United States": "جواسيس الحرب العالمية الأولى لصالح الولايات المتحدة",
    "World War II spies for France": "جواسيس الحرب العالمية الثانية لصالح فرنسا",
    "World War II spies for Germany": "جواسيس الحرب العالمية الثانية لصالح ألمانيا",
    "World War II spies for Italy": "جواسيس الحرب العالمية الثانية لصالح إيطاليا",
    "World War II spies for Japan": "جواسيس الحرب العالمية الثانية لصالح اليابان",
    "World War II spies for Poland": "جواسيس الحرب العالمية الثانية لصالح بولندا",
    "World War II spies for Sweden": "جواسيس الحرب العالمية الثانية لصالح السويد",
    "World War II spies for Soviet Union": "جواسيس الحرب العالمية الثانية لصالح الاتحاد السوفيتي",
    "World War II spies for United Kingdom": "جواسيس الحرب العالمية الثانية لصالح المملكة المتحدة",
    "World War II spies for United States": "جواسيس الحرب العالمية الثانية لصالح الولايات المتحدة",
    "west india political leader": "قادة الهند الغربية السياسيون",
    "australia political leader": "قادة أستراليا السياسيون",
    "japan political leader": "قادة اليابان السياسيون",
    "mauritius political leader": "قادة موريشيوس السياسيون",
    "morocco political leader": "قادة المغرب السياسيون",
    "rwanda political leader": "قادة رواندا السياسيون",
    "syria political leader": "قادة سوريا السياسيون",
    "tunisia political leader": "قادة تونس السياسيون",
}

test_data_1 = {
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
    "west india presidents": "رؤساء الهند الغربية",
    "west india responses": "استجابات الهند الغربية",
    "democratic-republic-of-congo territorial judges": "قضاة أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-congo territorial officials": "مسؤولو أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-congo war": "حرب جمهورية الكونغو الديمقراطية",
    "united states elections": "انتخابات الولايات المتحدة",
    "england war and conflict": "حروب ونزاعات إنجلترا",
    "england war": "حرب إنجلترا",
    "georgia government": "حكومة جورجيا",
    "israel war and conflict": "حروب ونزاعات إسرائيل",
    "israel war": "حرب إسرائيل",
    "oceania cup": "كأس أوقيانوسيا",
    "spain war and conflict": "حروب ونزاعات إسبانيا",
    "spain war": "حرب إسبانيا",
}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_resolve_by_countries_names(category: str, expected: str) -> None:
    label = resolve_by_countries_names(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", political_data_v1.items(), ids=political_data_v1.keys())
@pytest.mark.fast
def test_political_data_v1(category: str, expected: str) -> None:
    label = resolve_by_countries_names(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_by_countries_names", test_data_1, resolve_by_countries_names),
    ("test_political_data_v1", political_data_v1, resolve_by_countries_names),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
