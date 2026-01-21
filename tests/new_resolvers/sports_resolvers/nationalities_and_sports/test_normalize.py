import pytest

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import _load_bot

data = {
    "100 metres in the african championships in athletics": "100 metres in {en} championships in {en_sport}",
    "1330 in south american football": "1330 in {en} {en_sport}",
    "1789 in south american football": "1789 in {en} {en_sport}",
    "1789 in south american women's football": "1789 in {en} women's {en_sport}",
    "1880 european competition for women's football": "1880 {en} competition for women's {en_sport}",
    "1880 european men's handball championship": "1880 {en} men's {en_sport} championship",
    "1880 european women's handball championship": "1880 {en} women's {en_sport} championship",
    "1880 south american women's football championship": "1880 {en} women's {en_sport} championship",
    "the african championships in athletics": "{en} championships in {en_sport}",
    "wheelchair basketball in 2020 parapan american games": "{en_sport} in 2020 parapan {en} games",
    "wheelchair basketball in the asian para games": "{en_sport} in {en} para games",
    "wheelchair basketball in the parapan american games": "{en_sport} in the parapan {en} games",
    "wheelchair basketball players in 2020 parapan american games": "{en_sport} players in 2020 parapan {en} games",
    "Yemeni football championships": "{en} {en_sport} championships",
    "Yemeni national football teams": "{en} national {en_sport} teams",
}

both_bot_v2 = _load_bot()


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_normalize_both(key: str, expected: str) -> None:
    template_label2 = both_bot_v2.normalize_both(key)
    assert template_label2 == expected


data2 = {
    "Yemeni national football teams": "{en} national football teams",
    "1970 european women's handball championship": "1970 {en} women's handball championship",
    "1970 south american women's football championship": "1970 {en} women's football championship",
    "american basketball players by ethnic or national origin": "{en} basketball players by ethnic or national origin",
}


@pytest.mark.parametrize("key,expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_normalize_nat_label(key: str, expected: str) -> None:
    template_label = both_bot_v2.normalize_nat_label(key)
    assert template_label != ""
    assert template_label == expected


data3 = {
    "Yemeni national football teams": "Yemeni national {en_sport} teams",
    "1970 european women's handball championship": "1970 european women's {en_sport} championship",
    "1970 south american women's football championship": "1970 south american women's {en_sport} championship",
    "american basketball players by ethnic or national origin": "american {en_sport} players by ethnic or national origin",
}


@pytest.mark.parametrize("key,expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_normalize_sport_label(key: str, expected: str) -> None:
    template_label = both_bot_v2.normalize_other_label(key)
    assert template_label != ""
    assert template_label == expected
