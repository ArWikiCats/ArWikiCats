import pytest

from ArWikiCats.translations_resolvers_v2.nats_sport_multi_v2 import _load_bot

data = {
    "100 metres in the african championships in athletics": "100 metres in {en_nat} championships in {en_sport}",
    "1330 in south american football": "1330 in {en_nat} {en_sport}",
    "1789 in south american football": "1789 in {en_nat} {en_sport}",
    "1789 in south american women's football": "1789 in {en_nat} women's {en_sport}",
    "1880 european competition for women's football": "1880 {en_nat} competition for women's {en_sport}",
    "1880 european men's handball championship": "1880 {en_nat} men's {en_sport} championship",
    "1880 european women's handball championship": "1880 {en_nat} women's {en_sport} championship",
    "1880 south american women's football championship": "1880 {en_nat} women's {en_sport} championship",
    "the african championships in athletics": "{en_nat} championships in {en_sport}",
    "wheelchair basketball in 2020 parapan american games": "{en_sport} in 2020 parapan {en_nat} games",
    "wheelchair basketball in the asian para games": "{en_sport} in {en_nat} para games",
    "wheelchair basketball in the parapan american games": "{en_sport} in the parapan {en_nat} games",
    "wheelchair basketball playerss in 2020 parapan american games": "{en_sport} playerss in 2020 parapan {en_nat} games",
    "Yemeni football championships": "{en_nat} {en_sport} championships",
    "Yemeni national football teams": "{en_nat} national {en_sport} teams",
}

both_bot_v2 = _load_bot()


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_normalize_both(key: str, expected: str) -> None:
    template_label2 = both_bot_v2.normalize_both(key)
    assert template_label2 == expected


data2 = {
    "Yemeni national football teams": "{en_nat} national football teams",
    "1970 european women's handball championship": "1970 {en_nat} women's handball championship",
    "1970 south american women's football championship": "1970 {en_nat} women's football championship",
    "american basketball players by ethnic or national origin": "{en_nat} basketball players by ethnic or national origin",
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
