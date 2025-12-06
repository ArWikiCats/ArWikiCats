"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.main_processers.nat_men_pattern import get_label

test_data = {
    # standard
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "yemeni men": "رجال يمنيون",
    "libyan political people": "أعلام سياسية ليبية",
    "south african political people": "أعلام سياسية جنوبية إفريقية",

    "albanian lgbtq people": "أعلام إل جي بي تي كيو ألبانية",
    "bangladeshi lgbtq people": "أعلام إل جي بي تي كيو بنغلاديشية",
    "german lgbtq people": "أعلام إل جي بي تي كيو ألمانية",
    "jamaican lgbtq people": "أعلام إل جي بي تي كيو جامايكية",
    "norwegian lgbtq people": "أعلام إل جي بي تي كيو نرويجية",
    "sierra leonean lgbtq people": "أعلام إل جي بي تي كيو سيراليونية",
    "south african lgbtq people": "أعلام إل جي بي تي كيو جنوبية إفريقية",
    "thai lgbtq people": "أعلام إل جي بي تي كيو تايلندية",
    "tunisian lgbtq people": "أعلام إل جي بي تي كيو تونسية",

    "native american people": "أعلام أمريكيون أصليون",

    "africanamerican people": "أعلام أمريكيون أفارقة",
    "american people": "أعلام أمريكيون",
    "argentine people": "أعلام أرجنتينيون",
    "australian people": "أعلام أستراليون",
    "austrian people": "أعلام نمساويون",
    "barbadian people": "أعلام بربادوسيون",
    "bhutanese people": "أعلام بوتانيون",
    "bolivian people": "أعلام بوليفيون",
    "botswana people": "أعلام بوتسوانيون",
    "cameroonian people": "أعلام كاميرونيون",
    "cape verdean people": "أعلام أخضريون",
    "central american people": "أعلام أمريكيون أوسطيون",
    "dutch people": "أعلام هولنديون",
    "english people": "أعلام إنجليز",
    "gambian people": "أعلام غامبيون",
    "german people": "أعلام ألمان",
    "indian people": "أعلام هنود",
    "iraqi people": "أعلام عراقيون",
    "italian people": "أعلام إيطاليون",
    "latvian people": "أعلام لاتفيون",
    "malagasy people": "أعلام مدغشقريون",
    "malaysian people": "أعلام ماليزيون",
    "mexican people": "أعلام مكسيكيون",
    "moldovan people": "أعلام مولدوفيون",
    "mongolian people": "أعلام منغوليون",
    "polish people": "أعلام بولنديون",
    "rhodesian people": "أعلام رودوسيون",
    "romanian people": "أعلام رومانيون",
    "salvadoran people": "أعلام سلفادوريون",
    "scottish people": "أعلام إسكتلنديون",
    "serbian people": "أعلام صرب",
    "somalian people": "أعلام صوماليون",
    "south african people": "أعلام جنوب إفريقيون",
    "sri lankan people": "أعلام سريلانكيون",
    "sudanese people": "أعلام سودانيون",
    "swedish people": "أعلام سويديون",
    "tajikistani people": "أعلام طاجيك",
    "togolese people": "أعلام توغويون",
    "turkish cypriot people": "أعلام قبرصيون شماليون",
    "turkish people": "أعلام أتراك",
    "ukrainian people": "أعلام أوكرانيون",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_nat_pattern(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected


to_test = [
    ("test_nat_pattern", test_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, get_label)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
