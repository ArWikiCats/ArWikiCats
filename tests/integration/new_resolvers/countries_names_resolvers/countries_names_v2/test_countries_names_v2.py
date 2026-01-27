"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_v2 import resolve_by_countries_names_v2

political_data = {
    "tunisia political leader": "قادة سياسيون تونسيون",
    "australia political leader": "قادة سياسيون أستراليون",
    "japan political leader": "قادة سياسيون يابانيون",
    "mauritius political leader": "قادة سياسيون موريشيوسيون",
    "morocco political leader": "قادة سياسيون مغاربة",
    "rwanda political leader": "قادة سياسيون روانديون",
    "syria political leader": "قادة سياسيون سوريون",
    "west india political leader": "قادة سياسيون هنود غربيون",
}

main_data = {
    # ar patterns
    "national university of yemen": "جامعة اليمن الوطنية",
    "yemen board members": "أعضاء مجلس اليمن",
    "accidental deaths from falls in tunisia": "وفيات عرضية نتيجة السقوط في تونس",
    "yemen conflict": "نزاع اليمن",
    "yemen cup": "كأس اليمن",
    "oceania cup": "كأس أوقيانوسيا",
    "yemen elections": "انتخابات اليمن",
    "united states elections": "انتخابات الولايات المتحدة",
    "yemen executive cabinet": "مجلس وزراء اليمن التنفيذي",
    "victoria-australia executive cabinet": "مجلس وزراء فيكتوريا (أستراليا) التنفيذي",
    "west india government personnel": "موظفي حكومة الهند الغربية",
    "yemen government": "حكومة اليمن",
    "tunisia government": "حكومة تونس",
    "victoria-australia government": "حكومة فيكتوريا (أستراليا)",
    "georgia government": "حكومة جورجيا",
    "yemen governorate": "محافظة اليمن",
    "yemen presidents": "رؤساء اليمن",
    "tunisia presidents": "رؤساء تونس",
    "west india presidents": "رؤساء الهند الغربية",
    "yemen responses": "استجابات اليمن",
    "west india responses": "استجابات الهند الغربية",
    "tunisia territorial judges": "قضاة أقاليم تونس",
    "democratic-republic-of-congo territorial judges": "قضاة أقاليم جمهورية الكونغو الديمقراطية",
    "tunisia territorial officials": "مسؤولو أقاليم تونس",
    "democratic-republic-of-congo territorial officials": "مسؤولو أقاليم جمهورية الكونغو الديمقراطية",
    "england war and conflict": "حروب ونزاعات إنجلترا",
    "spain war and conflict": "حروب ونزاعات إسبانيا",
    "israel war and conflict": "حروب ونزاعات إسرائيل",
    "yemen war": "حرب اليمن",
    "england war": "حرب إنجلترا",
    "spain war": "حرب إسبانيا",
    "israel war": "حرب إسرائيل",
    "democratic-republic-of-congo war": "حرب جمهورية الكونغو الديمقراطية",
    # squad patterns
    "yemen afc women's asian cup squad": "تشكيلات اليمن في كأس آسيا للسيدات",
    "china afc women's asian cup squad": "تشكيلات الصين في كأس آسيا للسيدات",
    "yemen afc asian cup squad": "تشكيلات اليمن في كأس آسيا",
    "uzbekistan afc asian cup squad": "تشكيلات أوزبكستان في كأس آسيا",
    "victoria-australia fifa world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم",
    "victoria-australia fifa futsal world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم لكرة الصالات",
    "democratic-republic-of-congo summer olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الصيفية",
    "democratic-republic-of-congo winter olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "west india olympics squad": "تشكيلات الهند الغربية في الألعاب الأولمبية",
    # olympics patterns
    "west india summer olympics": "الهند الغربية في الألعاب الأولمبية الصيفية",
    "democratic-republic-of-congo winter olympics": "جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    # the_female patterns
    "yemen royal air force": "القوات الجوية الملكية اليمنية",
    "tunisia civil war": "الحرب الأهلية التونسية",
    "yemen air force": "القوات الجوية اليمنية",
    "morocco royal defence force": "قوات الدفاع الملكية المغربية",
    "tunisia navy": "البحرية التونسية",
    "morocco royal navy": "البحرية الملكية المغربية",
    "syria naval force": "البحرية السورية",
    "egypt naval forces": "البحرية المصرية",
    # males patterns
    "yemen government officials": "مسؤولون حكوميون يمنيون",
    # the_male patterns
    "yemen premier division": "الدوري اليمني الممتاز",
    "yemen coast guard": "خفر السواحل اليمني",
    "united states congressional delegation": "وفود الكونغرس الأمريكي",
    "united states congressional delegations": "وفود الكونغرس الأمريكي",
    "yemen parliament": "البرلمان اليمني",
    "united states congress": "الكونغرس الأمريكي",
    "england house of commons": "مجلس العموم الإنجليزي",
    "england house-of-commons": "مجلس العموم الإنجليزي",
    "united states senate election": "انتخابات مجلس الشيوخ الأمريكي",
    "united states senate elections": "انتخابات مجلس الشيوخ الأمريكي",
    "iraq fa cup": "كأس الاتحاد العراقي",
    "Bangladesh Federation Cup": "كأس الاتحاد البنغلاديشي",
    "united states marine corps personnel": "أفراد سلاح مشاة البحرية الأمريكي",
    "yemen army personnel": "أفراد الجيش اليمني",
    "united states coast guard aviation": "طيران خفر السواحل الأمريكي",
    "united states abortion law": "قانون الإجهاض الأمريكي",
    "france labour law": "قانون العمل الفرنسي",
    "yemen professional league": "دوري المحترفين اليمني",
    "yemen first division league": "الدوري اليمني الدرجة الأولى",
    "yemen second division": "الدوري اليمني الدرجة الثانية",
    "yemen second division league": "الدوري اليمني الدرجة الثانية",
    "yemen third division league": "الدوري اليمني الدرجة الثالثة",
    "yemen forth division league": "الدوري اليمني الدرجة الرابعة",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=main_data.keys())
@pytest.mark.fast
def test_resolve_by_countries_names_v2(category: str, expected: str) -> None:
    label = resolve_by_countries_names_v2(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", political_data.items(), ids=political_data.keys())
@pytest.mark.fast
def test_political_data_v2(category: str, expected: str) -> None:
    label = resolve_by_countries_names_v2(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_by_countries_names_v2", main_data, resolve_by_countries_names_v2),
    ("test_political_data_v2", political_data, resolve_by_countries_names_v2),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
