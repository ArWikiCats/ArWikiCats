"""

"""

import pytest

from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import add_in_tab, find_ar_label

fast_data = {
    "togolese expatriates in israel": "توغويون مغتربون في إسرائيل",
    "togolese expatriates in turkey": "توغويون مغتربون في تركيا",
    "tourism in united kingdom": "سياحة في المملكة المتحدة",
    "tourist attractions in almaty": "مواقع جذب سياحي في ألماتي",
    "tourist attractions in amman": "مواقع جذب سياحي في عمان",
    "tourist attractions in dâmbovița county": "مواقع جذب سياحي في مقاطعة دامبوفيتا",
    "tourist attractions in marinduque": "مواقع جذب سياحي في ماريندوك",
    "transport in kirov oblast": "نقل في أوبلاست كيروف",
    "transport in newfoundland and labrador": "نقل في نيوفاوندلاند واللابرادور",
    "transport in oxford": "نقل في أكسفورد",
    "transport in ternopil oblast": "نقل في تيرنوبل أوبلاست",
    "transport museums in zambia": "متاحف نقل في زامبيا",
    "tunisian expatriate sports-people in libya": "رياضيون تونسيون مغتربون في ليبيا",
    "universities and colleges in isabela (province)": "جامعات وكليات في ايزابلا (محافظة)",
    "universities and colleges in montpellier": "جامعات وكليات في مونبلييه",
    "vietnamese diaspora in canada": "شتات فيتنامي في كندا",
    "villages in datia district": "قرى في مقاطعة داتيا",
    "villages in north macedonia": "قرى في مقدونيا الشمالية",
    "villages in poltava oblast": "قرى في بولتافا أوبلاست",
    "villages in ramanagara district": "قرى في مقاطعة رامانجارا",
    "vocational education in uganda": "تعليم مهني في أوغندا",
    "waste management in brazil": "إدارة المخلفات في البرازيل",
    "1550 in belgian motorsport": "1550 في رياضة المحركات البلجيكية",
    "1550 in chinese motorsport": "1550 في رياضة المحركات الصينية",
    "1550 in english cricket": "1550 في الكريكت الإنجليزية",
    "1550 establishments in uruguay": "تأسيسات سنة 1550 في أوروغواي",
    "1550 establishments in virginia": "تأسيسات سنة 1550 في فرجينيا",
    "1550 establishments in wales": "تأسيسات سنة 1550 في ويلز",
    "1550 establishments in wyoming": "تأسيسات سنة 1550 في وايومنغ",
    "1550 establishments in yugoslavia": "تأسيسات سنة 1550 في يوغسلافيا",
    "1550 crimes in madagascar": "جرائم 1550 في مدغشقر",
    "1550 crimes in oceania": "جرائم 1550 في أوقيانوسيا",
    "1550 disasters in australia": "كوارث 1550 في أستراليا",
    "1550 disestablishments in indiana": "انحلالات سنة 1550 في إنديانا",
    "1550 disestablishments in new york (state)": "انحلالات سنة 1550 في ولاية نيويورك",
    "1550 disestablishments in north america": "انحلالات سنة 1550 في أمريكا الشمالية",
    "1550 disestablishments in philippines": "انحلالات سنة 1550 في الفلبين",
    "1550 disasters in kenya": "كوارث 1550 في كينيا",
    "00s establishments in the Roman Empire": "تأسيسات عقد 00 في الإمبراطورية الرومانية",
    "1000s disestablishments in Asia": "انحلالات عقد 1000 في آسيا",
    "1990s BC disestablishments in Asia": "انحلالات عقد 1990 ق م في آسيا",
    "1990s disestablishments in Europe": "انحلالات عقد 1990 في أوروبا",
    "April 1983 events in Europe": "أحداث أبريل 1983 في أوروبا",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_find_ar_label_fast(category: str, expected: str) -> None:
    label = find_ar_label(category, "in")
    assert label == expected


def test_add_in_tab() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


def test_add_in_tab_2() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


@pytest.mark.fast
def test_find_ar_label() -> None:
    # Test with basic inputs
    result = find_ar_label("test category", "from")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = find_ar_label("sports category", "in")
    assert isinstance(result_various, str)

    # Test with another valid combination instead of empty strings
    result_safe = find_ar_label("music from france", "from")
    assert isinstance(result_safe, str)
