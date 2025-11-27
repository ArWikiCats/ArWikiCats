"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from src.make2_bots.countries_formats.not_sports_bot import (
    resolve_en_is_P17_ar_is_P17,
)

main_data = {
    "tunisia presidents": "رؤساء تونس",
    "tunisia governorate": "حكومة تونس",
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

    "democratic-republic-of-the-congo territorial judges": "قضاة أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-the-congo territorial officials": "مسؤولو أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-the-congo war": "حرب جمهورية الكونغو الديمقراطية",

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
    "georgia governorate": "حكومة جورجيا",
    "israel war and conflict": "حروب ونزاعات إسرائيل",
    "israel war": "حرب إسرائيل",
    "oceania cup": "كأس أوقيانوسيا",
    "spain war and conflict": "حروب ونزاعات إسبانيا",
    "spain war": "حرب إسبانيا",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=list(main_data.keys()))
@pytest.mark.fast
def test_resolve_en_is_P17_ar_is_P17(category, expected) -> None:
    label = resolve_en_is_P17_ar_is_P17(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_en_is_P17_ar_is_P17", main_data, resolve_en_is_P17_ar_is_P17),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
