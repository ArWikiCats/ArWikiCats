#
import pytest
from load_one_data import dump_diff, one_dump_test
from src.make2_bots.countries_formats.p17_bot import get_con_3_lab, get_con_3_lab_pop_format, from_category_relation_mapping


test_data_get_con_3_lab = {
    "afc asian cup squad": ("تشكيلات {} في كأس آسيا", "en_is_P17_ar_is_P17"),
    "afc women's asian cup squad": ("تشكيلات {} في كأس آسيا للسيدات", "en_is_P17_ar_is_P17"),
    "amateur international footballers": ("لاعبو منتخب {} لكرة القدم للهواة", "SPORT_FORMTS_EN_AR_IS_P17"),
    "amateur international soccer players": ("لاعبو منتخب {} لكرة القدم للهواة", "SPORT_FORMTS_EN_AR_IS_P17"),
    "board members": ("أعضاء مجلس {}", "en_is_P17_ar_is_P17"),
    "conflict": ("نزاع {}", "en_is_P17_ar_is_P17"),
    "cup": ("كأس {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "elections": ("انتخابات {}", "en_is_P17_ar_is_P17"),
    "executive cabinet": ("مجلس وزراء {} التنفيذي", "en_is_P17_ar_is_P17"),
    "fifa futsal world cup squad": ("تشكيلات {} في كأس العالم لكرة الصالات", "en_is_P17_ar_is_P17"),
    "fifa world cup squad": ("تشكيلات {} في كأس العالم", "en_is_P17_ar_is_P17"),
    "government personnel": ("موظفي حكومة {}", "en_is_P17_ar_is_P17"),
    "government": ("حكومة {}", "en_is_P17_ar_is_P17"),
    "governorate": ("حكومة {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "international footballers": ("لاعبو منتخب {} لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "international soccer players": ("لاعبو منتخب {} لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's a' international footballers": ("لاعبو منتخب {} لكرة القدم للرجال للمحليين", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's international footballers": ("لاعبو منتخب {} لكرة القدم للرجال", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's international soccer players": ("لاعبو منتخب {} لكرة القدم للرجال", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's under-20 international footballers": ("لاعبو منتخب {} تحت 20 سنة لكرة القدم للرجال", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's under-21 international footballers": ("لاعبو منتخب {} تحت 21 سنة لكرة القدم للرجال", "SPORT_FORMTS_EN_AR_IS_P17"),
    "men's youth international footballers": ("لاعبو منتخب {} لكرة القدم للشباب", "SPORT_FORMTS_EN_AR_IS_P17"),
    "national football team managers": ("مدربو منتخب {} لكرة القدم", "SPORT_FORMTS_EN_AR_IS_P17"),
    "national team": ("منتخبات {} الوطنية", "SPORT_FORMTS_EN_AR_IS_P17"),
    "national teams": ("منتخبات {} الوطنية", "SPORT_FORMTS_EN_AR_IS_P17"),
    "olympics squad": ("تشكيلات {} في الألعاب الأولمبية", "en_is_P17_ar_is_P17"),
    "political leader": ("قادة {} السياسيون", "en_is_P17_ar_is_P17"),
    "presidents": ("رؤساء {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "rally championship": ("بطولة {} للراليات", "SPORT_FORMTS_EN_AR_IS_P17"),
    "responses": ("استجابات {}", "en_is_P17_ar_is_P17"),
    "sports templates": ("قوالب {} الرياضية", "SPORT_FORMTS_EN_AR_IS_P17"),
    "summer olympics squad": ("تشكيلات {} في الألعاب الأولمبية الصيفية", "en_is_P17_ar_is_P17"),
    "summer olympics": (" {} في الألعاب الأولمبية الصيفية", "en_is_P17_ar_is_P17"),
    "territorial judges": ("قضاة أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "territorial officials": ("مسؤولو أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "under-13 international footballers": ("لاعبو منتخب {} تحت 13 سنة لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "under-14 international footballers": ("لاعبو منتخب {} تحت 14 سنة لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "war and conflict": ("حروب ونزاعات {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "war": ("حرب {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "winter olympics squad": ("تشكيلات {} في الألعاب الأولمبية الشتوية", "en_is_P17_ar_is_P17"),
    "winter olympics": (" {} في الألعاب الأولمبية الشتوية", "en_is_P17_ar_is_P17"),
    "women's international footballers": ("لاعبات منتخب {} لكرة القدم للسيدات", "SPORT_FORMTS_EN_AR_IS_P17"),
    "women's youth international footballers": ("لاعبات منتخب {} لكرة القدم للشابات", "SPORT_FORMTS_EN_AR_IS_P17"),
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
