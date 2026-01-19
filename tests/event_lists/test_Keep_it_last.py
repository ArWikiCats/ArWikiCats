""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_arabic_category_label

fast_data = {
    "Category:Remakes of American films": "تصنيف:أفلام أمريكية معاد إنتاجها",
    "Category:Remakes of Argentine films": "تصنيف:أفلام أرجنتينية معاد إنتاجها",
    "Category:Remakes of Australian films": "تصنيف:أفلام أسترالية معاد إنتاجها",
    "Category:Remakes of Austrian films": "تصنيف:أفلام نمساوية معاد إنتاجها",
    "Category:Remakes of Belgian films": "تصنيف:أفلام بلجيكية معاد إنتاجها",
    "Category:Remakes of Brazilian films": "تصنيف:أفلام برازيلية معاد إنتاجها",
    "Category:Remakes of British films": "تصنيف:أفلام بريطانية معاد إنتاجها",
    "Category:Remakes of Burmese films": "تصنيف:أفلام بورمية معاد إنتاجها",
    "Category:Remakes of Canadian films": "تصنيف:أفلام كندية معاد إنتاجها",
    "Category:Remakes of Chilean films": "تصنيف:أفلام تشيلية معاد إنتاجها",
    "Category:Remakes of Chinese films": "تصنيف:أفلام صينية معاد إنتاجها",
    "Category:Remakes of Danish films": "تصنيف:أفلام دنماركية معاد إنتاجها",
    "Category:Remakes of Dutch films": "تصنيف:أفلام هولندية معاد إنتاجها",
    "Category:Remakes of Finnish films": "تصنيف:أفلام فنلندية معاد إنتاجها",
    "Category:Remakes of French films": "تصنيف:أفلام فرنسية معاد إنتاجها",
    "Category:Remakes of German films": "تصنيف:أفلام ألمانية معاد إنتاجها",
    "Category:Remakes of Hong Kong films": "تصنيف:أفلام هونغ كونغية معاد إنتاجها",
    "Category:Remakes of Hungarian films": "تصنيف:أفلام مجرية معاد إنتاجها",
    "Category:Remakes of Icelandic films": "تصنيف:أفلام آيسلندية معاد إنتاجها",
    "Category:Remakes of Indian films": "تصنيف:أفلام هندية معاد إنتاجها",
    "Category:Remakes of Indian television series": "تصنيف:مسلسلات تلفزيونية هندية معاد إنتاجها",
    "Category:Remakes of Indonesian films": "تصنيف:أفلام إندونيسية معاد إنتاجها",
    "Category:Remakes of Irish films": "تصنيف:أفلام أيرلندية معاد إنتاجها",
    "Category:Remakes of Italian films": "تصنيف:أفلام إيطالية معاد إنتاجها",
    "Category:Remakes of Japanese films": "تصنيف:أفلام يابانية معاد إنتاجها",
    "Category:Remakes of Malaysian films": "تصنيف:أفلام ماليزية معاد إنتاجها",
    "Category:Remakes of Mexican films": "تصنيف:أفلام مكسيكية معاد إنتاجها",
    "Category:Remakes of Norwegian films": "تصنيف:أفلام نرويجية معاد إنتاجها",
    "Category:Remakes of Pakistani films": "تصنيف:أفلام باكستانية معاد إنتاجها",
    "Category:Remakes of Philippine films": "تصنيف:أفلام فلبينية معاد إنتاجها",
    "Category:Remakes of Russian films": "تصنيف:أفلام روسية معاد إنتاجها",
    "Category:Remakes of South Korean films": "تصنيف:أفلام كورية جنوبية معاد إنتاجها",
    "Category:Remakes of Spanish films": "تصنيف:أفلام إسبانية معاد إنتاجها",
    "Category:Remakes of Sri Lankan films": "تصنيف:أفلام سريلانكية معاد إنتاجها",
    "Category:Remakes of Swedish films": "تصنيف:أفلام سويدية معاد إنتاجها",
    "Category:Remakes of Taiwanese films": "تصنيف:أفلام تايوانية معاد إنتاجها",
    "Category:Remakes of Thai films": "تصنيف:أفلام تايلندية معاد إنتاجها",
    "Category:Remakes of Turkish films": "تصنيف:أفلام تركية معاد إنتاجها",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
def test_Keep_it_last_extended(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_Keep_it_last_extended", fast_data),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_Keep_it_last_dump(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
