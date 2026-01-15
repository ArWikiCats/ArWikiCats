import pytest

from ArWikiCats.ma_bots2.year_or_typeo.bot_lab import label_for_startwith_year_or_typeo

fast_data = {
    "1650s crimes": "جرائم عقد 1650",
    "1650s disasters": "كوارث عقد 1650",
    "1650s disestablishments": "انحلالات عقد 1650",
    "1650s establishments": "تأسيسات عقد 1650",
    "1650s films": "أفلام إنتاج عقد 1650",
    "1650s floods": "فيضانات عقد 1650",
    "1650s mass shootings": "إطلاق نار عشوائي عقد 1650",
    "1650s murders": "جرائم قتل عقد 1650",
    "1650s television series": "مسلسلات تلفزيونية عقد 1650",
    "1st millennium bc establishments": "تأسيسات الألفية 1 ق م",
    "1st millennium disestablishments": "انحلالات الألفية 1",
    "20th century attacks": "هجمات القرن 20",
    "20th century bc kings of": "ملوك القرن 20 ق م",
    "20th century bce kings of": "ملوك القرن 20 ق م",
    "20th century clergy": "رجال دين في القرن 20",
    "20th century heads of": "قادة القرن 20",
    "20th century kings of": "ملوك القرن 20",
    "20th century lawyers": "محامون في القرن 20",
    "20th century mathematicians": "رياضياتيون في القرن 20",
    "20th century mayors of": "عمدات القرن 20",
    "20th century members of": "أعضاء القرن 20",
    "20th century military history of": "التاريخ العسكري في القرن 20",
    "20th century north american people": "أمريكيون شماليون في القرن 20",
    "20th century norwegian people": "نرويجيون في القرن 20",
    "20th century people": "أشخاص في القرن 20",
    "20th century philosophers": "فلاسفة في القرن 20",
    "20th century photographers": "مصورون في القرن 20",
    "20th century presidents of": "رؤساء القرن 20",
    "20th century prime ministers of": "رؤساء وزراء القرن 20",
    "20th century princesses of": "أميرات القرن 20",
    "20th century religious buildings": "مبان دينية القرن 20",
    "20th century roman catholic bishops": "أساقفة كاثوليك رومان في القرن 20",
    "20th century roman catholic church buildings": "مبان كنائس رومانية كاثوليكية القرن 20",
    "20th century romanian people": "رومان في القرن 20",
    "20th century sultans of": "سلاطين القرن 20",
    "20th century women": "المرأة في القرن 20",
    "march 1650 crimes": "جرائم مارس 1650",
    "october 1650 sports-events": "أحداث أكتوبر 1650 الرياضية",
    "september 1650 crimes": "جرائم سبتمبر 1650",
    "september 1650 sports-events": "أحداث سبتمبر 1650 الرياضية",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.skipmk3
def test_event2_fast(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected


def test_unknown_country() -> None:
    res = label_for_startwith_year_or_typeo("something 2020 Unknownland")
    assert res == ""  # no country_label → fallback fail


def test_return_empty_if_nolab() -> None:
    assert label_for_startwith_year_or_typeo("random") == ""
