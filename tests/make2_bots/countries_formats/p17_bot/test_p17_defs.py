import pytest
from src.make2_bots.countries_formats.p17_bot import get_con_3_lab


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
    "governorate": ("حكومة {nat}", "SPORT_FORMTS_EN_AR_IS_P17"),
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
    "rally championship": ("بطولة {nat} للراليات", "SPORT_FORMTS_EN_AR_IS_P17"),
    "responses": ("استجابات {}", "en_is_P17_ar_is_P17"),
    "sports templates": ("قوالب {} الرياضية", "SPORT_FORMTS_EN_AR_IS_P17"),
    "summer olympics squad": ("تشكيلات {} في الألعاب الأولمبية الصيفية", "en_is_P17_ar_is_P17"),
    "summer olympics": (" {} في الألعاب الأولمبية الصيفية", "en_is_P17_ar_is_P17"),
    "territorial judges": ("قضاة أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "territorial officials": ("مسؤولو أقاليم {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "under-13 international footballers": ("لاعبو منتخب {} تحت 13 سنة لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "under-14 international footballers": ("لاعبو منتخب {} تحت 14 سنة لكرة القدم ", "SPORT_FORMTS_EN_AR_IS_P17"),
    "war and conflict": ("حروب ونزاعات {nat}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "war": ("حرب {}", "SPORT_FORMTS_EN_AR_IS_P17"),
    "winter olympics squad": ("تشكيلات {} في الألعاب الأولمبية الشتوية", "en_is_P17_ar_is_P17"),
    "winter olympics": (" {} في الألعاب الأولمبية الشتوية", "en_is_P17_ar_is_P17"),
    "women's international footballers": ("لاعبات منتخب {} لكرة القدم للسيدات", "SPORT_FORMTS_EN_AR_IS_P17"),
    "women's youth international footballers": ("لاعبات منتخب {} لكرة القدم للشابات", "SPORT_FORMTS_EN_AR_IS_P17"),
}

test_data_2 = {
}


@pytest.mark.parametrize("category, expected", test_data_get_con_3_lab.items(), ids=list(test_data_get_con_3_lab.keys()))
@pytest.mark.fast
def test_get_con_3_lab(category, expected):
    result = get_con_3_lab(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", test_data_2.items(), ids=list(test_data_2.keys()))
@pytest.mark.fast
def test_get_p17_new(category, expected):
    result = get_con_3_lab(category)
    assert result == expected
