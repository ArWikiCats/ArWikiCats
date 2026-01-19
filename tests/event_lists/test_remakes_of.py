""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.relations_resolver.remakes_of_resolver import resolve_remakes_of_resolver

fast_data_empty = {
    "American remakes of Argentine films": "أفلام أمريكية مأخوذة من أفلام أرجنتينية",
    "American remakes of Belgian films": "أفلام أمريكية مأخوذة من أفلام بلجيكية",
    "American remakes of Brazilian films": "أفلام أمريكية مأخوذة من أفلام برازيلية",
    "American remakes of British films": "أفلام أمريكية مأخوذة من أفلام بريطانية",
    "American remakes of Canadian films": "أفلام أمريكية مأخوذة من أفلام كندية",
    "American remakes of Danish films": "أفلام أمريكية مأخوذة من أفلام دنماركية",
    "American remakes of Dutch films": "أفلام أمريكية مأخوذة من أفلام هولندية",
    "American remakes of French films": "أفلام أمريكية مأخوذة من أفلام فرنسية",
    "American remakes of German films": "أفلام أمريكية مأخوذة من أفلام ألمانية",
    "American remakes of Hong Kong films": "أفلام أمريكية مأخوذة من أفلام هونغ كونغية",
    "American remakes of Indian films": "أفلام أمريكية مأخوذة من أفلام هندية",
    "American remakes of Israeli films": "أفلام أمريكية مأخوذة من أفلام إسرائيلية",
    "American remakes of Italian films": "أفلام أمريكية مأخوذة من أفلام إيطالية",
    "American remakes of Japanese films": "أفلام أمريكية مأخوذة من أفلام يابانية",
    "American remakes of Mexican films": "أفلام أمريكية مأخوذة من أفلام مكسيكية",
    "American remakes of Norwegian films": "أفلام أمريكية مأخوذة من أفلام نرويجية",
    "American remakes of South Korean films": "أفلام أمريكية مأخوذة من أفلام كورية جنوبية",
    "American remakes of Spanish films": "أفلام أمريكية مأخوذة من أفلام إسبانية",
    "American remakes of Swedish films": "أفلام أمريكية مأخوذة من أفلام سويدية",
    "American remakes of Thai films": "أفلام أمريكية مأخوذة من أفلام تايلندية",
    "Bangladeshi remakes of American films": "أفلام بنغلاديشية مأخوذة من أفلام أمريكية",
    "Bangladeshi remakes of Indian films": "أفلام بنغلاديشية مأخوذة من أفلام هندية",
    "Bangladeshi remakes of Tamil films": "أفلام بنغلاديشية مأخوذة من أفلام تاميلية",
    "British remakes of American films": "أفلام بريطانية مأخوذة من أفلام أمريكية",
    "British remakes of French films": "أفلام بريطانية مأخوذة من أفلام فرنسية",
    "British remakes of German films": "أفلام بريطانية مأخوذة من أفلام ألمانية",
    "Bangladeshi remakes of Telugu films": "أفلام بنغلاديشية مأخوذة من أفلام تيلوغوية",
    "Bengali remakes of English films": "أفلام بنغالية مأخوذة من أفلام إنجليزية",
    "Bengali remakes of Tamil films": "أفلام بنغالية مأخوذة من أفلام تاميلية",
    "Bengali remakes of Telugu films": "أفلام بنغالية مأخوذة من أفلام تيلوغوية",
    "Chinese remakes of American films": "أفلام صينية مأخوذة من أفلام أمريكية",
    "Chinese remakes of Japanese films": "أفلام صينية مأخوذة من أفلام يابانية",
    "Chinese remakes of South Korean films": "أفلام صينية مأخوذة من أفلام كورية جنوبية",
    "Dutch remakes of British films": "أفلام هولندية مأخوذة من أفلام بريطانية",
    "French remakes of American films": "أفلام فرنسية مأخوذة من أفلام أمريكية",
    "Gujarati remakes of Tamil films": "أفلام غجراتية مأخوذة من أفلام تاميلية",
    "Hong Kong remakes of American films": "أفلام هونغ كونغية مأخوذة من أفلام أمريكية",
    "Indian remakes of American films": "أفلام هندية مأخوذة من أفلام أمريكية",
    "Indian remakes of British films": "أفلام هندية مأخوذة من أفلام بريطانية",
    "Indian remakes of French films": "أفلام هندية مأخوذة من أفلام فرنسية",
    "Indian remakes of Hong Kong films": "أفلام هندية مأخوذة من أفلام هونغ كونغية",
    "Indian remakes of Italian films": "أفلام هندية مأخوذة من أفلام إيطالية",
    "Indian remakes of Japanese films": "أفلام هندية مأخوذة من أفلام يابانية",
    "Indian remakes of Pakistani films": "أفلام هندية مأخوذة من أفلام باكستانية",
    "Indian remakes of South Korean films": "أفلام هندية مأخوذة من أفلام كورية جنوبية",
    "Indian remakes of Spanish films": "أفلام هندية مأخوذة من أفلام إسبانية",
    "Indian remakes of Thai films": "أفلام هندية مأخوذة من أفلام تايلندية",
    "Iranian remakes of American films": "أفلام إيرانية مأخوذة من أفلام أمريكية",
    "Italian remakes of French films": "أفلام إيطالية مأخوذة من أفلام فرنسية",
    "Japanese remakes of American films": "أفلام يابانية مأخوذة من أفلام أمريكية",
    "Japanese remakes of South Korean films": "أفلام يابانية مأخوذة من أفلام كورية جنوبية",
    "Maldivian remakes of Indian films": "أفلام مالديفية مأخوذة من أفلام هندية",
    "Pakistani remakes of American films": "أفلام باكستانية مأخوذة من أفلام أمريكية",
    "Pakistani remakes of Indian films": "أفلام باكستانية مأخوذة من أفلام هندية",
    "Philippine remakes of South Korean films": "أفلام فلبينية مأخوذة من أفلام كورية جنوبية",
    "South Korean remakes of Brazilian films": "أفلام كورية جنوبية مأخوذة من أفلام برازيلية",
    "South Korean remakes of Japanese films": "أفلام كورية جنوبية مأخوذة من أفلام يابانية",
    "South Korean remakes of Spanish films": "أفلام كورية جنوبية مأخوذة من أفلام إسبانية",
    "South Korean remakes of Taiwanese films": "أفلام كورية جنوبية مأخوذة من أفلام تايوانية",
    "Spanish remakes of Argentine films": "أفلام إسبانية مأخوذة من أفلام أرجنتينية",
    "Spanish remakes of French films": "أفلام إسبانية مأخوذة من أفلام فرنسية",
    "Spanish remakes of Italian films": "أفلام إسبانية مأخوذة من أفلام إيطالية",
    "Sri Lankan remakes of Indian films": "أفلام سريلانكية مأخوذة من أفلام هندية",
    "Taiwanese remakes of South Korean films": "أفلام تايوانية مأخوذة من أفلام كورية جنوبية",
    "Tamil remakes of Bengali films": "أفلام تاميلية مأخوذة من أفلام بنغالية",
    "Tamil remakes of Telugu films": "أفلام تاميلية مأخوذة من أفلام تيلوغوية",
    "Television remakes of films": "مسلسلات تلفزيونية مأخوذة من أفلام",
    "Telugu remakes of Bengali films": "أفلام تيلوغوية مأخوذة من أفلام بنغالية",
    "Telugu remakes of Gujarati films": "أفلام تيلوغوية مأخوذة من أفلام غجراتية",
    "Telugu remakes of Tamil films": "أفلام تيلوغوية مأخوذة من أفلام تاميلية",
    "Thai remakes of Taiwanese films": "أفلام تايلندية مأخوذة من أفلام تايوانية",
}

fast_data = {
    "American remakes of Argentine films": "أفلام أمريكية مأخوذة من أفلام أرجنتينية",
}

TEMPORAL_CASES = [
    ("test_remakes_of", resolve_label_ar),
]


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_politics_and_history(category: str, expected: str) -> None:
    label = resolve_remakes_of_resolver(category)
    assert label == expected

@pytest.mark.parametrize("category, expected", fast_data_empty.items(), ids=fast_data_empty.keys())
@pytest.mark.fast
def test_politics_and_history2(category: str, expected: str) -> None:
    label = resolve_remakes_of_resolver(category)
    assert label == expected


@pytest.mark.parametrize("name", ["test_remakes_of"])
@pytest.mark.dump
def test_remakes_of(name: str) -> None:
    data = fast_data_empty
    expected, diff_result = one_dump_test(data, resolve_remakes_of_resolver)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
