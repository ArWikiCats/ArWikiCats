import pytest
from ArWikiCats.make_bots.countries_formats.p17_bot import Get_P17_main


pop_format_test_data = {
    # ---------------------------------------------------------
    # pop_format  (category end with "of X")
    # ---------------------------------------------------------

    "china university of": "جامعة الصين",
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

    "zambia politics of": "سياسة زامبيا",
    "zambia military history of": "تاريخ زامبيا العسكري",

    "zimbabwe politics of": "سياسة زيمبابوي",
    "zimbabwe military history of": "تاريخ زيمبابوي العسكري",
}


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
    result = Get_P17_main(category)
    assert result.strip() == expected.strip()
