""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.relations_resolver.remakes_of_resolver import resolve_remakes_of_resolver

fast_data_empty = {
    "American remakes of Argentine films": "x",
    "American remakes of Belgian films": "x",
    "American remakes of Brazilian films": "x",
    "American remakes of British films": "x",
    "American remakes of Canadian films": "x",
    "American remakes of Danish films": "x",
    "American remakes of Dutch films": "x",
    "American remakes of French films": "x",
    "American remakes of German films": "x",
    "American remakes of Hong Kong films": "x",
    "American remakes of Indian films": "x",
    "American remakes of Israeli films": "x",
    "American remakes of Italian films": "x",
    "American remakes of Japanese films": "x",
    "American remakes of Mexican films": "x",
    "American remakes of Norwegian films": "x",
    "American remakes of South Korean films": "x",
    "American remakes of Spanish films": "x",
    "American remakes of Swedish films": "x",
    "American remakes of Thai films": "x",
    "Bangladeshi remakes of American films": "x",
    "Bangladeshi remakes of Indian films": "x",
    "Bangladeshi remakes of Tamil films": "x",
    "British remakes of American films": "x",
    "British remakes of French films": "x",
    "British remakes of German films": "x",
    "Bangladeshi remakes of Telugu films": "x",
    "Bengali remakes of English films": "x",
    "Bengali remakes of Hindi films": "x",
    "Bengali remakes of Kannada films": "x",
    "Bengali remakes of Malayalam films": "x",
    "Bengali remakes of Marathi films": "x",
    "Bengali remakes of Punjabi films": "x",
    "Bengali remakes of Tamil films": "x",
    "Bengali remakes of Telugu films": "x",
    "Bhojpuri remakes of Tamil films": "x",
    "Bhojpuri remakes of Telugu films": "x",
    "Chinese remakes of American films": "x",
    "Chinese remakes of Japanese films": "x",
    "Chinese remakes of South Korean films": "x",
    "Dutch remakes of British films": "x",
    "French remakes of American films": "x",
    "Gujarati remakes of Marathi films": "x",
    "Gujarati remakes of Tamil films": "x",
    "Hindi remakes of Bengali films": "x",
    "Hindi remakes of English films": "x",
    "Hindi remakes of Gujarati films": "x",
    "Hindi remakes of Kannada films": "x",
    "Hindi remakes of Malayalam films": "x",
    "Hindi remakes of Marathi films": "x",
    "Hindi remakes of Odia films": "x",
    "Hindi remakes of Punjabi films": "x",
    "Hindi remakes of Rajasthani films": "x",
    "Hindi remakes of silent films": "x",
    "Hindi remakes of Tamil films": "x",
    "Hindi remakes of Telugu films": "x",
    "Hong Kong remakes of American films": "x",
    "Indian remakes of American films": "x",
    "Indian remakes of British films": "x",
    "Indian remakes of French films": "x",
    "Indian remakes of Hong Kong films": "x",
    "Indian remakes of Italian films": "x",
    "Indian remakes of Japanese films": "x",
    "Indian remakes of Pakistani films": "x",
    "Indian remakes of South Korean films": "x",
    "Indian remakes of Spanish films": "x",
    "Indian remakes of Thai films": "x",
    "Iranian remakes of American films": "x",
    "Italian remakes of French films": "x",
    "Japanese remakes of American films": "x",
    "Japanese remakes of South Korean films": "x",
    "Kannada remakes of Bengali films": "x",
    "Kannada remakes of Hindi films": "x",
    "Kannada remakes of Malayalam films": "x",
    "Kannada remakes of Marathi films": "x",
    "Kannada remakes of Rajasthani films": "x",
    "Kannada remakes of Tamil films": "x",
    "Kannada remakes of Telugu films": "x",
    "Malayalam remakes of Bengali films": "x",
    "Malayalam remakes of Hindi films": "x",
    "Malayalam remakes of Kannada films": "x",
    "Malayalam remakes of Marathi films": "x",
    "Malayalam remakes of Tamil films": "x",
    "Malayalam remakes of Telugu films": "x",
    "Maldivian remakes of Indian films": "x",
    "Marathi remakes of Bengali films": "x",
    "Marathi remakes of Hindi films": "x",
    "Marathi remakes of Kannada films": "x",
    "Marathi remakes of Malayalam films": "x",
    "Marathi remakes of Rajasthani films": "x",
    "Marathi remakes of Tamil films": "x",
    "Marathi remakes of Telugu films": "x",
    "Meitei remakes of Telugu films": "x",
    "Odia remakes of Bengali films": "x",
    "Odia remakes of Hindi films": "x",
    "Odia remakes of Kannada films": "x",
    "Odia remakes of Malayalam films": "x",
    "Odia remakes of Marathi films": "x",
    "Odia remakes of Punjabi films": "x",
    "Odia remakes of Tamil films": "x",
    "Odia remakes of Telugu films": "x",
    "Pakistani remakes of American films": "x",
    "Pakistani remakes of Indian films": "x",
    "Philippine remakes of South Korean films": "x",
    "Punjabi remakes of Hindi films": "x",
    "Punjabi remakes of Malayalam films": "x",
    "Punjabi remakes of Marathi films": "x",
    "Punjabi remakes of Tamil films": "x",
    "Punjabi remakes of Telugu films": "x",
    "South Korean remakes of Brazilian films": "x",
    "South Korean remakes of Japanese films": "x",
    "South Korean remakes of Spanish films": "x",
    "South Korean remakes of Taiwanese films": "x",
    "Spanish remakes of Argentine films": "x",
    "Spanish remakes of French films": "x",
    "Spanish remakes of Italian films": "x",
    "Sri Lankan remakes of Indian films": "x",
    "Taiwanese remakes of South Korean films": "x",
    "Tamil remakes of Bengali films": "x",
    "Tamil remakes of Hindi films": "x",
    "Tamil remakes of Kannada films": "x",
    "Tamil remakes of Malayalam films": "x",
    "Tamil remakes of Marathi films": "x",
    "Tamil remakes of Telugu films": "x",
    "Television remakes of films": "x",
    "Telugu remakes of Bengali films": "x",
    "Telugu remakes of Gujarati films": "x",
    "Telugu remakes of Hindi films": "x",
    "Telugu remakes of Kannada films": "x",
    "Telugu remakes of Malayalam films": "x",
    "Telugu remakes of Marathi films": "x",
    "Telugu remakes of Punjabi films": "x",
    "Telugu remakes of Tamil films": "x",
    "Thai remakes of Taiwanese films": "",
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


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_remakes_of(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_remakes_of_resolver)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
