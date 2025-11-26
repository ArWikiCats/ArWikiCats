#
import pytest
from load_one_data import dump_diff, one_dump_test
from src.make2_bots.countries_formats.p17_bot import get_con_3_lab, get_con_3_lab_pop_format, from_category_relation_mapping


test_data_get_con_3_lab = {
    "afc asian cup squad": "تشكيلات {} في كأس آسيا",
    "afc women's asian cup squad": "تشكيلات {} في كأس آسيا للسيدات",
    "board members": "أعضاء مجلس {}",
    "conflict": "نزاع {}",
    "elections": "انتخابات {}",
    "executive cabinet": "مجلس وزراء {} التنفيذي",
    "fifa futsal world cup squad": "تشكيلات {} في كأس العالم لكرة الصالات",
    "fifa world cup squad": "تشكيلات {} في كأس العالم",
    "government personnel": "موظفي حكومة {}",
    "government": "حكومة {}",
    "olympics squad": "تشكيلات {} في الألعاب الأولمبية",
    "political leader": "قادة {} السياسيون",
    "responses": "استجابات {}",
    "summer olympics squad": "تشكيلات {} في الألعاب الأولمبية الصيفية",
    "summer olympics": " {} في الألعاب الأولمبية الصيفية",
    "winter olympics squad": "تشكيلات {} في الألعاب الأولمبية الشتوية",
    "winter olympics": " {} في الألعاب الأولمبية الشتوية",

    "governorate": ("حكومة {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "presidents": ("رؤساء {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "territorial judges": ("قضاة أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "territorial officials": ("مسؤولو أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "war and conflict": ("حروب ونزاعات {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "war": ("حرب {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
    "cup": ("كأس {}", "SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT"),
}

test_data_with_pop_format = {
    "contemporary history of": "تاريخ {} المعاصر",
    "diplomatic missions of": "بعثات {} الدبلوماسية",
    "early-modern history of": "تاريخ {} الحديث المبكر",
    "economic history of": "تاريخ {} الاقتصادي",
    "foreign relations of": "علاقات {} الخارجية",
    "grand prix": "جائزة {} الكبرى",
    "military history of": "تاريخ {} العسكري",
    "military installations of": "منشآت {} العسكرية",
    "modern history of": "تاريخ {} الحديث",
    "national symbols of": "رموز {} الوطنية",
    "natural history of": "تاريخ {} الطبيعي",
    "political history of": "تاريخ {} السياسي",
    "politics of": "سياسة {}",
    "prehistory of": "{} ما قبل التاريخ",
    "umayyad governors of": "ولاة {} الأمويون",
    "university of the arts": "جامعة {} للفنون",
    "university of": "جامعة {}",
}

test_data_relation_mapping = {

}


@pytest.mark.parametrize("category, expected", test_data_get_con_3_lab.items(), ids=list(test_data_get_con_3_lab.keys()))
@pytest.mark.fast
def test_get_con_3_lab(category, expected):
    result = get_con_3_lab(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", test_data_with_pop_format.items(), ids=list(test_data_with_pop_format.keys()))
@pytest.mark.fast
def test_with_pop_format(category, expected):
    result = get_con_3_lab_pop_format(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", test_data_relation_mapping.items(), ids=list(test_data_relation_mapping.keys()))
@pytest.mark.fast
def test_from_category_relation_mapping(category, expected):
    result = from_category_relation_mapping(category)
    assert result == expected


TEMPORAL_CASES = [
    ("test_get_con_3_lab", test_data_get_con_3_lab, get_con_3_lab),
    ("test_with_pop_format", test_data_with_pop_format, get_con_3_lab_pop_format),
    ("test_from_category_relation_mapping", test_data_relation_mapping, from_category_relation_mapping),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
