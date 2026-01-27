""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

fast_data = {
    "Remakes of American films": "أفلام أمريكية معاد إنتاجها",
    "Remakes of Argentine films": "أفلام أرجنتينية معاد إنتاجها",
    "Remakes of Australian films": "أفلام أسترالية معاد إنتاجها",
    "Remakes of Austrian films": "أفلام نمساوية معاد إنتاجها",
    "Remakes of Belgian films": "أفلام بلجيكية معاد إنتاجها",
    "Remakes of Brazilian films": "أفلام برازيلية معاد إنتاجها",
    "Remakes of British films": "أفلام بريطانية معاد إنتاجها",
    "Remakes of Burmese films": "أفلام بورمية معاد إنتاجها",
    "Remakes of Canadian films": "أفلام كندية معاد إنتاجها",
    "Remakes of Chilean films": "أفلام تشيلية معاد إنتاجها",
    "Remakes of Chinese films": "أفلام صينية معاد إنتاجها",
    "Remakes of Danish films": "أفلام دنماركية معاد إنتاجها",
    "Remakes of Dutch films": "أفلام هولندية معاد إنتاجها",
    "Remakes of Finnish films": "أفلام فنلندية معاد إنتاجها",
    "Remakes of French films": "أفلام فرنسية معاد إنتاجها",
    "Remakes of German films": "أفلام ألمانية معاد إنتاجها",
    "Remakes of Hong Kong films": "أفلام هونغ كونغية معاد إنتاجها",
    "Remakes of Hungarian films": "أفلام مجرية معاد إنتاجها",
    "Remakes of Icelandic films": "أفلام آيسلندية معاد إنتاجها",
    "Remakes of Indian films": "أفلام هندية معاد إنتاجها",
    "Remakes of Indian television series": "مسلسلات تلفزيونية هندية معاد إنتاجها",
    "Remakes of Indonesian films": "أفلام إندونيسية معاد إنتاجها",
    "Remakes of Irish films": "أفلام أيرلندية معاد إنتاجها",
    "Remakes of Italian films": "أفلام إيطالية معاد إنتاجها",
    "Remakes of Japanese films": "أفلام يابانية معاد إنتاجها",
    "Remakes of Malaysian films": "أفلام ماليزية معاد إنتاجها",
    "Remakes of Mexican films": "أفلام مكسيكية معاد إنتاجها",
    "Remakes of Norwegian films": "أفلام نرويجية معاد إنتاجها",
    "Remakes of Pakistani films": "أفلام باكستانية معاد إنتاجها",
    "Remakes of Philippine films": "أفلام فلبينية معاد إنتاجها",
    "Remakes of Russian films": "أفلام روسية معاد إنتاجها",
    "Remakes of South Korean films": "أفلام كورية جنوبية معاد إنتاجها",
    "Remakes of Spanish films": "أفلام إسبانية معاد إنتاجها",
    "Remakes of Sri Lankan films": "أفلام سريلانكية معاد إنتاجها",
    "Remakes of Swedish films": "أفلام سويدية معاد إنتاجها",
    "Remakes of Taiwanese films": "أفلام تايوانية معاد إنتاجها",
    "Remakes of Thai films": "أفلام تايلندية معاد إنتاجها",
    "Remakes of Turkish films": "أفلام تركية معاد إنتاجها",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
def test_Keep_it_last_extended(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_Keep_it_last_extended", fast_data),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_Keep_it_last_dump(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
