import pytest

from src.translations.sports_formats_nats.new import (
    normalize_both,
)

data = {
    "100 metres in the african championships in athletics": "100 metres in the natar championships in xoxo",
    "1330 in south american football": "1330 in natar xoxo",
    "1789 in south american football": "1789 in natar xoxo",
    "1789 in south american women's football": "1789 in natar women's xoxo",
    "1880 european competition for women's football": "1880 natar competition for women's xoxo",
    "1880 european men's handball championship": "1880 natar men's xoxo championship",
    "1880 european women's handball championship": "1880 natar women's xoxo championship",
    "1880 south american women's football championship": "1880 natar women's xoxo championship",
    "1970 european competition for women's football": "1970 natar competition for women's xoxo",
    "1970 european men's handball championship": "1970 natar men's xoxo championship",
    "1970 european women's handball championship": "1970 natar women's xoxo championship",
    "1970 south american women's football championship": "1970 natar women's xoxo championship",
    "1994–95 in european rugby union": "1994–95 in natar xoxo",
    "afghan competitors by sports event": "natar competitors by xoxo event",
    "american basketball coaches by state": "natar xoxo coaches by state",
    "american basketball players by ethnic or national origin": "natar xoxo players by ethnic or national origin",
    "american wheelchair sports competitors": "natar xoxo competitors",
    "american wheelchair track and field athletes": "natar wheelchair xoxo athletes",
    "asian football by country": "natar xoxo by country",
    "australian rules football awards": "natar rules xoxo awards",
    "british figure skating championships": "natar xoxo championships",
    "british wheelchair sports competitors": "natar xoxo competitors",
    "british wheelchair track and field athletes": "natar wheelchair xoxo athletes",
    "canadian ice hockey by league": "natar xoxo by league",
    "canadian ice hockey by team": "natar xoxo by team",
    "canadian wheelchair sports competitors": "natar xoxo competitors",
    "defunct american football venues": "defunct natar xoxo venues",
    "dominican republic national sports teams ": "natar national xoxo teams",
    "dutch basketball league by club": "natar xoxo league by club",
    "emirati football in 2017": "natar xoxo in 2017",
    "european rugby union by country": "natar xoxo by country",
    "european wheelchair handball nations’ tournament": "natar xoxo nations’ tournament",
    "metres in the african championships in athletics": "metres in the natar championships in xoxo",
    "moroccan competitors by sports event": "natar competitors by xoxo event",
    "pan american wheelchair handball championship": "pan natar xoxo championship",
    "parapan american games medalists in wheelchair basketball": "parapan natar games medalists in xoxo",
    "parapan american games medalists in wheelchair tennis": "parapan natar games medalists in xoxo",
    "players of american football from massachusetts": "players of natar xoxo from massachusetts",
    "puerto rican wheelchair sports competitors": "natar xoxo competitors",
    "puerto rican wheelchair track and field athletes": "natar wheelchair xoxo athletes",
    "seasons in omani football": "seasons in natar xoxo",
    "south american football by country": "natar xoxo by country",
    "the african championships in athletics": "the natar championships in xoxo",
    "wheelchair basketball in 2020 parapan american games": "xoxo in 2020 parapan natar games",
    "wheelchair basketball in the asian para games": "xoxo in the natar para games",
    "wheelchair basketball in the parapan american games": "xoxo in the parapan natar games",
    "wheelchair basketball playerss in 2020 parapan american games": "xoxo playerss in 2020 parapan natar games",
    "wheelchair rugby in 2020 parapan american games": "xoxo in 2020 parapan natar games",
    "wheelchair rugby in the parapan american games": "xoxo in the parapan natar games",
    "wheelchair rugby playerss in 2020 parapan american games": "xoxo playerss in 2020 parapan natar games",
    "wheelchair tennis in 2020 parapan american games": "xoxo in 2020 parapan natar games",
    "wheelchair tennis in the asian para games": "xoxo in the natar para games",
    "wheelchair tennis in the parapan american games": "xoxo in the parapan natar games",
    "wheelchair tennis playerss in 2020 asian para games": "xoxo playerss in 2020 natar para games",
    "wheelchair tennis playerss in 2020 parapan american games": "xoxo playerss in 2020 parapan natar games",
    "Yemeni football championships": "natar xoxo championships",
    "Yemeni national football teams": "natar national xoxo teams",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_normalize_both(key, expected) -> None:
    template_label = normalize_both(key)
    assert template_label != ""
    assert template_label == expected
