import pytest

from ArWikiCats.translations_resolvers.nats_sports import (
    normalize_both,
    normalize_nat_label,
    normalize_other_label,
)

data = {
    "100 metres in the african championships in athletics": "100 metres in the {nat_en} championships in {sport_en}",
    "1330 in south american football": "1330 in {nat_en} {sport_en}",
    "1789 in south american football": "1789 in {nat_en} {sport_en}",
    "1789 in south american women's football": "1789 in {nat_en} women's {sport_en}",
    "1880 european competition for women's football": "1880 {nat_en} competition for women's {sport_en}",
    "1880 european men's handball championship": "1880 {nat_en} men's {sport_en} championship",
    "1880 european women's handball championship": "1880 {nat_en} women's {sport_en} championship",
    "1880 south american women's football championship": "1880 {nat_en} women's {sport_en} championship",
    "1970 european competition for women's football": "1970 {nat_en} competition for women's {sport_en}",
    "1970 european men's handball championship": "1970 {nat_en} men's {sport_en} championship",
    "1970 european women's handball championship": "1970 {nat_en} women's {sport_en} championship",
    "1970 south american women's football championship": "1970 {nat_en} women's {sport_en} championship",
    "1994–95 in european rugby union": "1994–95 in {nat_en} {sport_en}",
    "afghan competitors by sports event": "{nat_en} competitors by {sport_en} event",
    "american basketball coaches by state": "{nat_en} {sport_en} coaches by state",
    "american basketball players by ethnic or national origin": "{nat_en} {sport_en} players by ethnic or national origin",
    "american wheelchair sports competitors": "{nat_en} {sport_en} competitors",
    "american wheelchair track and field athletes": "{nat_en} wheelchair {sport_en} athletes",
    "asian football by country": "{nat_en} {sport_en} by country",
    "australian rules football awards": "{nat_en} rules {sport_en} awards",
    "british figure skating championships": "{nat_en} {sport_en} championships",
    "british wheelchair sports competitors": "{nat_en} {sport_en} competitors",
    "british wheelchair track and field athletes": "{nat_en} wheelchair {sport_en} athletes",
    "canadian ice hockey by league": "{nat_en} {sport_en} by league",
    "canadian ice hockey by team": "{nat_en} {sport_en} by team",
    "canadian wheelchair sports competitors": "{nat_en} {sport_en} competitors",
    "defunct american football venues": "defunct {nat_en} {sport_en} venues",
    "dominican republic national sports teams ": "{nat_en} national {sport_en} teams",
    "dutch basketball league by club": "{nat_en} {sport_en} league by club",
    "emirati football in 2017": "{nat_en} {sport_en} in 2017",
    "european rugby union by country": "{nat_en} {sport_en} by country",
    "european wheelchair handball nations’ tournament": "{nat_en} {sport_en} nations’ tournament",
    "metres in the african championships in athletics": "metres in the {nat_en} championships in {sport_en}",
    "moroccan competitors by sports event": "{nat_en} competitors by {sport_en} event",
    "pan american wheelchair handball championship": "pan {nat_en} {sport_en} championship",
    "parapan american games medalists in wheelchair basketball": "parapan {nat_en} games medalists in {sport_en}",
    "parapan american games medalists in wheelchair tennis": "parapan {nat_en} games medalists in {sport_en}",
    "players of american football from massachusetts": "players of {nat_en} {sport_en} from massachusetts",
    "puerto rican wheelchair sports competitors": "{nat_en} {sport_en} competitors",
    "puerto rican wheelchair track and field athletes": "{nat_en} wheelchair {sport_en} athletes",
    "seasons in omani football": "seasons in {nat_en} {sport_en}",
    "south american football by country": "{nat_en} {sport_en} by country",
    "the african championships in athletics": "the {nat_en} championships in {sport_en}",
    "wheelchair basketball in 2020 parapan american games": "{sport_en} in 2020 parapan {nat_en} games",
    "wheelchair basketball in the asian para games": "{sport_en} in the {nat_en} para games",
    "wheelchair basketball in the parapan american games": "{sport_en} in the parapan {nat_en} games",
    "wheelchair basketball playerss in 2020 parapan american games": "{sport_en} playerss in 2020 parapan {nat_en} games",
    "wheelchair rugby in 2020 parapan american games": "{sport_en} in 2020 parapan {nat_en} games",
    "wheelchair rugby in the parapan american games": "{sport_en} in the parapan {nat_en} games",
    "wheelchair rugby playerss in 2020 parapan american games": "{sport_en} playerss in 2020 parapan {nat_en} games",
    "wheelchair tennis in 2020 parapan american games": "{sport_en} in 2020 parapan {nat_en} games",
    "wheelchair tennis in the asian para games": "{sport_en} in the {nat_en} para games",
    "wheelchair tennis in the parapan american games": "{sport_en} in the parapan {nat_en} games",
    "wheelchair tennis playerss in 2020 asian para games": "{sport_en} playerss in 2020 {nat_en} para games",
    "wheelchair tennis playerss in 2020 parapan american games": "{sport_en} playerss in 2020 parapan {nat_en} games",
    "Yemeni football championships": "{nat_en} {sport_en} championships",
    "Yemeni national football teams": "{nat_en} national {sport_en} teams",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_normalize_both(key: str, expected: str) -> None:
    template_label = normalize_both(key)
    assert template_label != ""
    assert template_label == expected


data2 = {
    "Yemeni national football teams": "{nat_en} national football teams",
    "1970 european women's handball championship": "1970 {nat_en} women's handball championship",
    "1970 south american women's football championship": "1970 {nat_en} women's football championship",
    "american basketball players by ethnic or national origin": "{nat_en} basketball players by ethnic or national origin",
}


@pytest.mark.parametrize("key,expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_normalize_nat_label(key: str, expected: str) -> None:
    template_label = normalize_nat_label(key)
    assert template_label != ""
    assert template_label == expected


data3 = {
    "Yemeni national football teams": "Yemeni national {sport_en} teams",
    "1970 european women's handball championship": "1970 european women's {sport_en} championship",
    "1970 south american women's football championship": "1970 south american women's {sport_en} championship",
    "american basketball players by ethnic or national origin": "american {sport_en} players by ethnic or national origin",
}


@pytest.mark.parametrize("key,expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_normalize_sport_label(key: str, expected: str) -> None:
    template_label = normalize_other_label(key)
    assert template_label != ""
    assert template_label == expected
