#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.translations.sports_formats_oioioi.bot import (
    both_bot,
    get_start_p17,
)

data = {
    "swiss wheelchair curling championship": ("{nat} wheelchair curling championship", "swiss"),
    "canadian open tennis": ("{nat} open tennis", "canadian"),
    "caribbean handball championship": ("{nat} handball championship", "caribbean"),
    "european motocross championship": ("{nat} motocross championship", "european"),
    "central american women's handball championship": ("{nat} women's handball championship", "central american"),
    "european athletics u23 championships": ("{nat} athletics u23 championships", "european"),
    "european cricket championship": ("{nat} cricket championship", "european"),
    "central american beach handball championship": ("{nat} beach handball championship", "central american"),
    "european handball championship": ("{nat} handball championship", "european"),
    "african youth athletics championships": ("{nat} youth athletics championships", "african"),
    "german darts championship": ("{nat} darts championship", "german"),
    "dutch open tennis": ("{nat} open tennis", "dutch"),
    "south american cricket championship": ("{nat} cricket championship", "south american"),
    "french open (badminton)": ("{nat} open (badminton)", "french"),
    "australian open (badminton)": ("{nat} open (badminton)", "australian"),
    "european athletics indoor championships": ("{nat} athletics indoor championships", "european"),
    "asian beach volleyball championship": ("{nat} beach volleyball championship", "asian"),
    "british rally championship": ("{nat} rally championship", "british"),
    "hungarian open (table tennis)": ("{nat} open (table tennis)", "hungarian"),
    "german ice hockey championship": ("{nat} ice hockey championship", "german"),
    "belgian open tennis": ("{nat} open tennis", "belgian"),
    "czech women's curling championship": ("{nat} women's curling championship", "czech"),
    "asian men's volleyball championship": ("{nat} men's volleyball championship", "asian"),
    "european volleyball championship": ("{nat} volleyball championship", "european"),
    "european beach volleyball championship": ("{nat} beach volleyball championship", "european"),
    "african volleyball championship": ("{nat} volleyball championship", "african"),
    "asian amateur boxing championships": ("{nat} amateur boxing championships", "asian"),
    "asian open tennis": ("{nat} open tennis", "asian"),
    "british rowing junior championships": ("{nat} rowing junior championships", "british"),
    "swedish men's curling championship": ("{nat} men's curling championship", "swedish"),
    "european women's handball championship": ("{nat} women's handball championship", "european"),
    "swedish ice hockey championship": ("{nat} ice hockey championship", "swedish"),
    "australasian championships tennis": ("{nat} championships tennis", "australasian"),
    "kazakhstani futsal championship": ("{nat} futsal championship", "kazakhstani"),
    "greenlandic men's handball championship": ("{nat} men's handball championship", "greenlandic"),
    "asian baseball championship": ("{nat} baseball championship", "asian"),
    "greenlandic men's football championship": ("{nat} men's football championship", "greenlandic"),
    "asian sailing championship": ("{nat} sailing championship", "asian"),
    "czech open tennis": ("{nat} open tennis", "czech"),
    "african rally championship": ("{nat} rally championship", "african"),
    "italian football championship": ("{nat} football championship", "italian"),
    "russian women's football championship": ("{nat} women's football championship", "russian"),
    "swedish women's curling championship": ("{nat} women's curling championship", "swedish"),
    "central asian men's volleyball championship": ("{nat} men's volleyball championship", "central asian"),
    "cape verdean football championship": ("{nat} football championship", "cape verdean"),
    "asian netball championship": ("{nat} netball championship", "asian"),
    "european baseball championship": ("{nat} baseball championship", "european"),
    "estonian football championship": ("{nat} football championship", "estonian"),
    "lithuanian men's curling championship": ("{nat} men's curling championship", "lithuanian"),
    "canadian open (golf)": ("{nat} open (golf)", "canadian"),
    "chinese boxing cups": ("{nat} boxing cups", "chinese"),
    "chinese boxing leagues": ("{nat} boxing leagues", "chinese"),
    "chinese boxing chairmen and investors": ("{nat} boxing chairmen and investors", "chinese"),
    "chinese boxing clubs": ("{nat} boxing clubs", "chinese"),
    "chinese boxing coaches": ("{nat} boxing coaches", "chinese"),
    "chinese boxing competitions": ("{nat} boxing competitions", "chinese"),
    "chinese boxing cup competitions": ("{nat} boxing cup competitions", "chinese"),
    "chinese outdoor boxing": ("{nat} outdoor boxing", "chinese"),
    "chinese women's boxing": ("{nat} women's boxing", "chinese"),
    "chinese amateur boxing championship": ("{nat} amateur boxing championship", "chinese"),
    "chinese amateur boxing championships": ("{nat} amateur boxing championships", "chinese"),
    "chinese championships (boxing)": ("{nat} championships (boxing)", "chinese"),
    "chinese championships boxing": ("{nat} championships boxing", "chinese"),
    "chinese current boxing seasons": ("{nat} current boxing seasons", "chinese"),
    "chinese defunct indoor boxing clubs": ("{nat} defunct indoor boxing clubs", "chinese"),
    "chinese defunct indoor boxing coaches": ("{nat} defunct indoor boxing coaches", "chinese"),
    "chinese defunct indoor boxing competitions": ("{nat} defunct indoor boxing competitions", "chinese"),
    "chinese defunct indoor boxing cups": ("{nat} defunct indoor boxing cups", "chinese"),
    "chinese defunct indoor boxing leagues": ("{nat} defunct indoor boxing leagues", "chinese"),
    "chinese defunct boxing clubs": ("{nat} defunct boxing clubs", "chinese"),
    "chinese defunct boxing coaches": ("{nat} defunct boxing coaches", "chinese"),
    "chinese defunct boxing competitions": ("{nat} defunct boxing competitions", "chinese"),
    "chinese defunct boxing cup competitions": ("{nat} defunct boxing cup competitions", "chinese"),
    "chinese defunct boxing cups": ("{nat} defunct boxing cups", "chinese"),
    "chinese defunct boxing leagues": ("{nat} defunct boxing leagues", "chinese"),
    "chinese defunct outdoor boxing clubs": ("{nat} defunct outdoor boxing clubs", "chinese"),
    "chinese defunct outdoor boxing coaches": ("{nat} defunct outdoor boxing coaches", "chinese"),
    "chinese defunct outdoor boxing competitions": ("{nat} defunct outdoor boxing competitions", "chinese"),
    "chinese defunct outdoor boxing cups": ("{nat} defunct outdoor boxing cups", "chinese"),
    "chinese defunct outdoor boxing leagues": ("{nat} defunct outdoor boxing leagues", "chinese"),
    "chinese domestic boxing": ("{nat} domestic boxing", "chinese"),
    "chinese domestic boxing clubs": ("{nat} domestic boxing clubs", "chinese"),
    "chinese domestic boxing coaches": ("{nat} domestic boxing coaches", "chinese"),
    "chinese domestic boxing competitions": ("{nat} domestic boxing competitions", "chinese"),
    "chinese domestic boxing cup": ("{nat} domestic boxing cup", "chinese"),
    "chinese domestic boxing cups": ("{nat} domestic boxing cups", "chinese"),
    "chinese domestic boxing leagues": ("{nat} domestic boxing leagues", "chinese"),
    "chinese domestic women's boxing clubs": ("{nat} domestic women's boxing clubs", "chinese"),
    "chinese domestic women's boxing coaches": ("{nat} domestic women's boxing coaches", "chinese"),
    "chinese domestic women's boxing competitions": ("{nat} domestic women's boxing competitions", "chinese"),
    "chinese domestic women's boxing cups": ("{nat} domestic women's boxing cups", "chinese"),
    "chinese domestic women's boxing leagues": ("{nat} domestic women's boxing leagues", "chinese"),
    "chinese indoor boxing": ("{nat} indoor boxing", "chinese"),
    "chinese indoor boxing clubs": ("{nat} indoor boxing clubs", "chinese"),
    "chinese indoor boxing coaches": ("{nat} indoor boxing coaches", "chinese"),
    "chinese indoor boxing competitions": ("{nat} indoor boxing competitions", "chinese"),
    "chinese indoor boxing cups": ("{nat} indoor boxing cups", "chinese"),
    "chinese indoor boxing leagues": ("{nat} indoor boxing leagues", "chinese"),
    "chinese youth boxing championships": ("{nat} youth boxing championships", "chinese"),
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_get_start_p17(category, expected) -> None:
    key1, start1 = get_start_p17(category)
    expected_1, expected_2 = expected

    start2, key2 = both_bot.country_bot.normalize_category_with_key(category)

    assert key2 == expected_1
    assert start2 == expected_2

    assert key1 == expected_1
    assert start1 == expected_2
