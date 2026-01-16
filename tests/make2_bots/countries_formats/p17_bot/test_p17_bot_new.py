import pytest

from ArWikiCats.make_bots.countries_formats.p17_bot import get_p17_main

pop_format_test_data = {
    # ---------------------------------------------------------
    # pop_format  (category end with "of X")
    # ---------------------------------------------------------
    "china university of": "جامعة الصين",
    "yemen politics of": "سياسة اليمن",
    "yemen diplomatic missions of": "بعثات اليمن الدبلوماسية",
    "yemen umayyad governors of": "ولاة اليمن الأمويون",
    "yemen military installations of": "منشآت اليمن العسكرية",
    "yemen foreign relations of": "علاقات اليمن الخارجية",
    "yemen national symbols of": "رموز اليمن الوطنية",
    "yemen grand prix": "جائزة اليمن الكبرى",
    # ---------------------------------------------------------
    # university of / history of / relations / etc.
    # ---------------------------------------------------------
    "yemen university of": "جامعة اليمن",
    "yemen university of arts": "جامعة اليمن للفنون",
    # ---------------------------------------------------------
    # cases for different countries (not only yemen)
    # ---------------------------------------------------------
    "venezuela politics of": "سياسة فنزويلا",
    "zambia politics of": "سياسة زامبيا",
    "zimbabwe politics of": "سياسة زيمبابوي",
}


# =====================================================================
# test with parametrized
# =====================================================================


@pytest.mark.parametrize("category, expected", pop_format_test_data.items(), ids=list(pop_format_test_data.keys()))
@pytest.mark.fast
def test_get_p17_new(category: str, expected: str) -> None:
    result = get_p17_main(category)
    assert result == expected
