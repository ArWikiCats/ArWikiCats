import pytest
from src.make2_bots.countries_formats.p17_bot import Get_P17


get_p17_data = {
    # "yemen international footballers": "لاعبو كرة قدم دوليون من اليمن",
    "yemen international footballers": "لاعبو منتخب اليمن لكرة القدم",
    "yemen international soccer players": "لاعبو منتخب اليمن لكرة القدم",

    "democratic-republic-of-the-congo amateur international soccer players": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للهواة",

    "yemen under-13 international footballers": "لاعبو منتخب اليمن تحت 13 سنة لكرة القدم ",
    "yemen under-14 international footballers": "لاعبو منتخب اليمن تحت 14 سنة لكرة القدم ",

    # ---------------------------------------------------------
    # en_is_P17_ar_is_P17
    # ---------------------------------------------------------

    "yemen board members": "أعضاء مجلس اليمن",
    "yemen government": "حكومة اليمن",
    "yemen elections": "انتخابات اليمن",
    "yemen war": "حرب اليمن",
    "yemen responses": "استجابات اليمن",
    "yemen executive cabinet": "مجلس وزراء اليمن التنفيذي",
    "yemen presidents": "رؤساء اليمن",
    "yemen afc asian cup squad": "تشكيلات اليمن في كأس آسيا",
    "yemen afc women's asian cup squad": "تشكيلات اليمن في كأس آسيا للسيدات",
    "yemen conflict": "نزاع اليمن",
    "yemen cup": "كأس اليمن",

    "victoria-australia elections": "انتخابات فيكتوريا (أستراليا)",
    "victoria-australia executive cabinet": "مجلس وزراء فيكتوريا (أستراليا) التنفيذي",
    "victoria-australia fifa futsal world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم لكرة الصالات",
    "victoria-australia fifa world cup squad": "تشكيلات فيكتوريا (أستراليا) في كأس العالم",
    "victoria-australia government": "حكومة فيكتوريا (أستراليا)",

    "west india government personnel": "موظفي حكومة الهند الغربية",
    "west india olympics squad": "تشكيلات الهند الغربية في الألعاب الأولمبية",
    "west india political leader": "قادة الهند الغربية السياسيون",
    "west india presidents": "رؤساء الهند الغربية",
    "west india responses": "استجابات الهند الغربية",
    "west india summer olympics": " الهند الغربية في الألعاب الأولمبية الصيفية",

    "democratic-republic-of-the-congo summer olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الصيفية",
    "democratic-republic-of-the-congo territorial judges": "قضاة أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-the-congo territorial officials": "مسؤولو أقاليم جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-the-congo war": "حرب جمهورية الكونغو الديمقراطية",
    "democratic-republic-of-the-congo winter olympics": " جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    "democratic-republic-of-the-congo winter olympics squad": "تشكيلات جمهورية الكونغو الديمقراطية في الألعاب الأولمبية الشتوية",
    # ---------------------------------------------------------
    # SPORT_FORMTS_EN_AR_IS_P17
    # ---------------------------------------------------------
    "yemen rally championship": "بطولة اليمن للراليات",
    "yemen sports templates": "قوالب اليمن الرياضية",

    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",
    "tunisia national team": "منتخبات تونس الوطنية",
    "tunisia national teams": "منتخبات تونس الوطنية",
    "tunisia presidents": "رؤساء تونس",
    "tunisia governorate": "حكومة تونس",
    "tunisia rally championship": "بطولة تونس للراليات",
    "tunisia sports templates": "قوالب تونس الرياضية",
    "tunisia territorial judges": "قضاة أقاليم تونس",
    "tunisia territorial officials": "مسؤولو أقاليم تونس",
}

pop_format_test_data = {
    # ---------------------------------------------------------
    # pop_format  (category end with "of X")
    # ---------------------------------------------------------

    "yemen prehistory of": "اليمن ما قبل التاريخ",
    "yemen politics of": "سياسة اليمن",
    "yemen diplomatic missions of": "بعثات اليمن الدبلوماسية",
    "yemen umayyad governors of": "ولاة اليمن الأمويون",
    "yemen military installations of": "منشآت اليمن العسكرية",
    "yemen political history of": "تاريخ اليمن السياسي",
    "yemen economic history of": "تاريخ اليمن الاقتصادي",
    "yemen military history of": "تاريخ اليمن العسكري",
    "yemen natural history of": "تاريخ اليمن الطبيعي",
    "yemen foreign relations of": "علاقات اليمن الخارجية",
    "yemen national symbols of": "رموز اليمن الوطنية",
    "yemen grand prix": "جائزة اليمن الكبرى",

    # ---------------------------------------------------------
    # university of / history of / relations / etc.
    # ---------------------------------------------------------

    "yemen university of": "جامعة اليمن",
    "yemen university of the arts": "جامعة اليمن للفنون",
    "yemen early-modern history of": "تاريخ اليمن الحديث المبكر",
    "yemen modern history of": "تاريخ اليمن الحديث",
    "yemen contemporary history of": "تاريخ اليمن المعاصر",

    # ---------------------------------------------------------
    # cases for different countries (not only yemen)
    # ---------------------------------------------------------

    "venezuela politics of": "سياسة فنزويلا",
    "venezuela military history of": "تاريخ فنزويلا العسكري",
    "venezuela international footballers": "لاعبو منتخب فنزويلا لكرة القدم ",
    "venezuela rally championship": "بطولة فنزويلا للراليات",

    "zambia politics of": "سياسة زامبيا",
    "zambia military history of": "تاريخ زامبيا العسكري",
    "zambia international footballers": "لاعبو منتخب زامبيا لكرة القدم ",
    "zambia rally championship": "بطولة زامبيا للراليات",

    "zimbabwe politics of": "سياسة زيمبابوي",
    "zimbabwe military history of": "تاريخ زيمبابوي العسكري",
    "zimbabwe international footballers": "لاعبو منتخب زيمبابوي لكرة القدم ",
    "zimbabwe rally championship": "بطولة زيمبابوي للراليات",
}


# =====================================================================
# test with parametrized
# =====================================================================


@pytest.mark.parametrize("category, expected", get_p17_data.items(), ids=list(get_p17_data.keys()))
@pytest.mark.fast
def test_get_p17(category, expected):
    result = Get_P17(category)
    assert result.strip() == expected.strip()


# =====================================================================
# test with parametrized
# =====================================================================

@pytest.mark.parametrize(
    "category, expected",
    pop_format_test_data.items(),
    ids=list(pop_format_test_data.keys())
)
@pytest.mark.fast
def test_get_p17_new(category, expected):
    result = Get_P17(category)
    assert result.strip() == expected.strip()
