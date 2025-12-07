"""

"""

import pytest

from ArWikiCats.main_processers.event2bot import event2, event2_d2, stubs_label

fast_data = {
    "1650s films": "أفلام إنتاج عقد 1650",
    "1650 central american": "أمريكيون أوسطيون في 1650",
    "1650s soviet": "سوفيت في عقد 1650",
    "20th century canadian violinists": "عازفو كمان كنديون في القرن 20",
    "20th century chinese dramatists": "دراميون صينيون في القرن 20",
    "20th century dramatists": "دراميون في القرن 20",
    "20th century english dramatists": "دراميون إنجليز في القرن 20",
    "20th century israeli dramatists": "دراميون إسرائيليون في القرن 20",
    "20th century polish dramatists": "دراميون بولنديون في القرن 20",
    "20th century religious buildings": "مبان دينية القرن 20",
    "20th century russian dramatists": "دراميون روس في القرن 20",
    "1650s establishments": "تأسيسات عقد 1650",
    "1650s disestablishments": "انحلالات عقد 1650",
    "1650s television series": "مسلسلات تلفزيونية عقد 1650",
    "1650s disasters": "كوارث عقد 1650",
    "1650s crimes": "جرائم عقد 1650",
    "20th century north american people": "أمريكيون شماليون في القرن 20",
    "20th century norwegian people": "نرويجيون في القرن 20",
    "20th century people": "أشخاص في القرن 20",
    "20th century philosophers": "فلاسفة في القرن 20",
    "20th century roman catholic bishops": "أساقفة كاثوليك رومان في القرن 20",
    "20th century roman catholic church buildings": "مبان كنائس رومانية كاثوليكية القرن 20",
    "20th century romanian people": "رومانيون في القرن 20",
    "20th century women": "المرأة في القرن 20",
    "march 1650 crimes": "جرائم مارس 1650",
    "20th century clergy": "رجال دين في القرن 20",
    "20th century lawyers": "محامون في القرن 20",
    "20th century mathematicians": "رياضياتيون في القرن 20",
    "20th century philosophers": "فلاسفة في القرن 20",
    "20th century photographers": "مصورون في القرن 20",
    "20th century women musicians": "موسيقيات في القرن 20",
    "1650s establishments": "تأسيسات عقد 1650",
    "1650s disestablishments": "انحلالات عقد 1650",
    "1650s murders": "جرائم قتل عقد 1650",
    "1650s controversies": "خلافات عقد 1650",
    "1650s disasters": "كوارث عقد 1650",
    "1650s floods": "فيضانات عقد 1650",
    "1650s mass shootings": "إطلاق نار عشوائي عقد 1650",
    "1650s murders": "جرائم قتل عقد 1650",
    "1st millennium bc establishments": "تأسيسات الألفية 1 ق م",
    "1st millennium disestablishments": "انحلالات الألفية 1",
    "1650s crimes": "جرائم عقد 1650",
    "october 1650 sports-events": "أحداث أكتوبر 1650 الرياضية",
    "september 1650 crimes": "جرائم سبتمبر 1650",
    "september 1650 sports-events": "أحداث سبتمبر 1650 الرياضية",
    "20th century bc kings of": "ملوك القرن 20 ق م",
    "20th century bce kings of": "ملوك القرن 20 ق م",
    "20th century heads of": "قادة القرن 20",
    "20th century kings of": "ملوك القرن 20",
    "20th century mayors of": "عمدات القرن 20",
    "20th century members of": "أعضاء القرن 20",
    "20th century military history of": "التاريخ العسكري في القرن 20",
    "20th century presidents of": "رؤساء القرن 20",
    "20th century prime ministers of": "رؤساء وزراء القرن 20",
    "20th century princesses of": "أميرات القرن 20",
    "20th century sultans of": "سلاطين القرن 20",
    "20th century attacks": "هجمات القرن 20",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_event2_fast(category: str, expected: str) -> None:
    label = event2(category)
    assert label == expected


def test_event2_d2() -> None:
    # Test with a basic input
    result = event2_d2("test category")
    assert isinstance(result, str)

    # Test with century format
    result_century = event2_d2("21st century")
    assert isinstance(result_century, str)

    # Test with empty string
    result_empty = event2_d2("")
    assert isinstance(result_empty, str)


def test_stubs_label() -> None:
    # Test with a basic input
    result = stubs_label("test category")
    assert isinstance(result, str)

    # Test with stubs format
    result_stubs = stubs_label("test stubs")
    assert isinstance(result_stubs, str)

    # Test with empty string
    result_empty = stubs_label("")
    assert isinstance(result_empty, str)


def test_event2() -> None:
    # Test with a basic input
    result = event2("test category")
    assert isinstance(result, str)

    # Test with different input
    result_various = event2("sports event")
    assert isinstance(result_various, str)

    # Test with empty string
    result_empty = event2("")
    assert isinstance(result_empty, str)
