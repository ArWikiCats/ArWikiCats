"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data = {
    "2020 in wheelchair basketball": "كرة السلة على الكراسي المتحركة في 2020",
    "2020 in wheelchair rugby": "الرجبي على الكراسي المتحركة في 2020",
    "2020 Wheelchair Basketball World Championship": "بطولة العالم لكرة السلة على الكراسي المتحركة 2020",
    "2020 Wheelchair Basketball World Championships": "بطولة العالم لكرة السلة على الكراسي المتحركة 2020",
    "American wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أمريكيون",
    "American wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة أمريكيون",
    "American wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة أمريكيون",
    "American wheelchair discus throwers": "رماة قرص على الكراسي المتحركة أمريكيون",
    "American wheelchair rugby players": "لاعبو رجبي على كراسي متحركة أمريكيون",
    "American wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أمريكيون",
    "Australian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أستراليون",
    "Australian wheelchair rugby players": "لاعبو رجبي على كراسي متحركة أستراليون",
    "Australian wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أستراليون",
    "British wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة بريطانيون",
    "British wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة بريطانيون",
    "British wheelchair rugby players": "لاعبو رجبي على كراسي متحركة بريطانيون",
    "British wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة بريطانيون",
    "Cameroonian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كاميرونيون",
    "Canadian male wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ذكور كنديون",
    "Canadian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كنديون",
    "Canadian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة كنديون",
    "Canadian wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة كنديون",
    "Canadian wheelchair rugby players": "لاعبو رجبي على كراسي متحركة كنديون",
    "Chinese wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة صينيون",
    "Danish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة دنماركيون",
    "Dutch wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة هولنديون",
    "Dutch wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة هولنديون",
    "English wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إنجليز",
    "Finnish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة فنلنديون",
    "Finnish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة فنلنديون",
    "French wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة فرنسيون",
    "French wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة فرنسيون",
    "German wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ألمان",
    "German wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة ألمان",
    "German wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة ألمان",
    "Israeli wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسرائيليون",
    "Israeli wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة إسرائيليون",
    "Italian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إيطاليون",
    "Japanese wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة يابانيون",
    "Japanese wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة يابانيون",
    "Japanese wheelchair rugby players": "لاعبو رجبي على كراسي متحركة يابانيون",
    "Japanese wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة يابانيون",
    "Kuwaiti wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كويتيون",
    "Latvian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة لاتفيون",
    "National wheelchair rugby league teams": "منتخبات دوري رجبي على كراسي متحركة وطنية",
    "Norwegian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة نرويجيون",
}

wheelchair_racers = {
    "Olympic wheelchair racers by country": "متسابقو كراسي متحركة أولمبيون حسب البلد",
    "Olympic wheelchair racers by year": "متسابقو كراسي متحركة أولمبيون حسب السنة",
    "Olympic wheelchair racers for Australia": "متسابقو كراسي متحركة أولمبيون في أستراليا",
    "Olympic wheelchair racers for Canada": "متسابقو كراسي متحركة أولمبيون في كندا",
    "Olympic wheelchair racers for France": "متسابقو كراسي متحركة أولمبيون في فرنسا",
    "Olympic wheelchair racers for Germany": "متسابقو كراسي متحركة أولمبيون في ألمانيا",
    "Olympic wheelchair racers for Great Britain": "متسابقو كراسي متحركة أولمبيون في بريطانيا العظمى",
    "Olympic wheelchair racers for Japan": "متسابقو كراسي متحركة أولمبيون في اليابان",
    "Olympic wheelchair racers for Mexico": "متسابقو كراسي متحركة أولمبيون في المكسيك",
    "Olympic wheelchair racers for Switzerland": "متسابقو كراسي متحركة أولمبيون في سويسرا",
    "Olympic wheelchair racers for the United States": "متسابقو كراسي متحركة أولمبيون في الولايات المتحدة",
    "Olympic wheelchair racers": "متسابقو كراسي متحركة أولمبيون",
}


mens_womens = {
    "Men's wheelchair basketball players by nationality": "لاعبو كرة سلة على كراسي متحركة حسب الجنسية",
    "Men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة",
    "2020 Women's World Wheelchair Basketball Championship": "بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات 2020",
    "American men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أمريكيون",
    "American women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة أمريكيات",
    "Australian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أستراليون",
    "Australian women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة أستراليات",
    "British men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة بريطانيون",
    "British women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة بريطانيات",
    "Cameroonian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كاميرونيون",
    "Canadian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كنديون",
    "Canadian women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة كنديات",
    "Dutch men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة هولنديون",
    "Dutch women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة هولنديات",
    "French men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة فرنسيون",
    "French women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة فرنسيات",
    "German men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ألمان",
    "German women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة ألمانيات",
    "Israeli men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسرائيليون",
    "Israeli women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة إسرائيليات",
    "Japanese men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة يابانيون",
    "Kuwaiti men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كويتيون",
}


TEMPORAL_CASES = [
    ("test_wheelchair_1", data),
    ("test_wheelchair_racers", wheelchair_racers),
    ("test_wheelchair_mens_womens", mens_womens),
]


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_wheelchair_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_racers.items(), ids=wheelchair_racers.keys())
@pytest.mark.fast
def test_wheelchair_racers(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", mens_womens.items(), ids=mens_womens.keys())
@pytest.mark.fast
def test_wheelchair_mens_womens(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
