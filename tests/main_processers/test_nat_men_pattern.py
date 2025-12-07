"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.main_processers.nat_men_pattern import get_label

test_data = {
    # standard
    "welsh people": "أعلام ويلزيون",
    "yemeni people": "أعلام يمنيون",
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

    "libyan political people": "ساسة ليبيون",
    "south african political people": "ساسة جنوب إفريقيون",
    "albanian lgbtq people": "أعلام إل جي بي تي كيو ألبان",
    "bangladeshi lgbtq people": "أعلام إل جي بي تي كيو بنغلاديشيون",
    "german lgbtq people": "أعلام إل جي بي تي كيو ألمان",
    "jamaican lgbtq people": "أعلام إل جي بي تي كيو جامايكيون",
    "norwegian lgbtq people": "أعلام إل جي بي تي كيو نرويجيون",
    "sierra leonean lgbtq people": "أعلام إل جي بي تي كيو سيراليونيون",
    "south african lgbtq people": "أعلام إل جي بي تي كيو جنوب إفريقيون",
    "thai lgbtq people": "أعلام إل جي بي تي كيو تايلنديون",
    "tunisian lgbtq people": "أعلام إل جي بي تي كيو تونسيون",
    "native american people": "أعلام أمريكيون أصليون",

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
