"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from src import resolve_arabic_category_label

data = {
    "Category:2020 in wheelchair basketball": "تصنيف:كرة السلة على الكراسي المتحركة في 2020",
    "Category:2020 in wheelchair rugby": "تصنيف:الرجبي على الكراسي المتحركة في 2020",
    "Category:2020 Wheelchair Basketball World Championship": "تصنيف:بطولة العالم لكرة السلة على الكراسي المتحركة 2020",
    "Category:2020 Wheelchair Basketball World Championships": "تصنيف:بطولة العالم لكرة السلة على الكراسي المتحركة 2020",
    "Category:American wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة أمريكيون",
    "Category:American wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة أمريكيون",
    "Category:American wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة أمريكيون",
    "Category:American wheelchair discus throwers": "تصنيف:رماة قرص على الكراسي المتحركة أمريكيون",
    "Category:American wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة أمريكيون",
    "Category:American wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة أمريكيون",
    "Category:Australian wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة أستراليون",
    "Category:Australian wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة أستراليون",
    "Category:Australian wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة أستراليون",
    "Category:British wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة بريطانيون",
    "Category:British wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة بريطانيون",
    "Category:British wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة بريطانيون",
    "Category:British wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة بريطانيون",
    "Category:Cameroonian wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة كاميرونيون",
    "Category:Canadian male wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة ذكور كنديون",
    "Category:Canadian wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة كنديون",
    "Category:Canadian wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة كنديون",
    "Category:Canadian wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة كنديون",
    "Category:Canadian Wheelchair Curling Championships": "تصنيف:بطولات كيرلنغ على كراسي متحركة كندية",
    "Category:Canadian wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة كنديون",
    "Category:Chinese wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة صينيون",
    "Category:Danish wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة دنماركيون",
    "Category:Dutch wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة هولنديون",
    "Category:Dutch wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة هولنديون",
    "Category:English wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة إنجليز",
    "Category:Finnish wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة فنلنديون",
    "Category:Finnish wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة فنلنديون",
    "Category:French wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة فرنسيون",
    "Category:French wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة فرنسيون",
    "Category:German wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة ألمان",
    "Category:German wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة ألمان",
    "Category:German wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة ألمان",
    "Category:Israeli wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة إسرائيليون",
    "Category:Israeli wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة إسرائيليون",
    "Category:Italian wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة إيطاليون",
    "Category:Japanese wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة يابانيون",
    "Category:Japanese wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة يابانيون",
    "Category:Japanese wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة يابانيون",
    "Category:Japanese wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة يابانيون",
    "Category:Kuwaiti wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة كويتيون",
    "Category:Latvian wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة لاتفيون",
    "Category:National wheelchair rugby league teams": "تصنيف:منتخبات دوري رجبي على كراسي متحركة وطنية",
    "Category:Norwegian wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة نرويجيون",
}

wheelchair_racers = {
    "Category:Olympic wheelchair racers by country": "تصنيف:متسابقو كراسي متحركة أولمبيون حسب البلد",
    "Category:Olympic wheelchair racers by year": "تصنيف:متسابقو كراسي متحركة أولمبيون حسب السنة",
    "Category:Olympic wheelchair racers for Australia": "تصنيف:متسابقو كراسي متحركة أولمبيون في أستراليا",
    "Category:Olympic wheelchair racers for Canada": "تصنيف:متسابقو كراسي متحركة أولمبيون في كندا",
    "Category:Olympic wheelchair racers for France": "تصنيف:متسابقو كراسي متحركة أولمبيون في فرنسا",
    "Category:Olympic wheelchair racers for Germany": "تصنيف:متسابقو كراسي متحركة أولمبيون في ألمانيا",
    "Category:Olympic wheelchair racers for Great Britain": "تصنيف:متسابقو كراسي متحركة أولمبيون في بريطانيا العظمى",
    "Category:Olympic wheelchair racers for Japan": "تصنيف:متسابقو كراسي متحركة أولمبيون في اليابان",
    "Category:Olympic wheelchair racers for Mexico": "تصنيف:متسابقو كراسي متحركة أولمبيون في المكسيك",
    "Category:Olympic wheelchair racers for Switzerland": "تصنيف:متسابقو كراسي متحركة أولمبيون في سويسرا",
    "Category:Olympic wheelchair racers for the United States": "تصنيف:متسابقو كراسي متحركة أولمبيون في الولايات المتحدة",
    "Category:Olympic wheelchair racers": "تصنيف:متسابقو كراسي متحركة أولمبيون",
}


mens_womens = {
    "Category:Israeli women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية إسرائيليات",
    "Category:Japanese men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية يابانيون",
    "Category:German women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية ألمانيات",
    "Category:Israeli men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية إسرائيليون",
    "Category:French women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية فرنسيات",
    "Category:German men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية ألمان",
    "Category:French men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية فرنسيون",
    "Category:Dutch women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية هولنديات",
    "Category:Dutch men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية هولنديون",
    "Category:Canadian women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية كنديات",
    "Category:Canadian men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية كنديون",
    "Category:British women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية بريطانيات",
    "Category:Cameroonian men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية كاميرونيون",
    "Category:Australian women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية أستراليات",
    "Category:British men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية بريطانيون",
    "Category:2020 Women's World Wheelchair Basketball Championship": "تصنيف:بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات 2020",
    "Category:American men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية أمريكيون",
    "Category:American women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة نسائية أمريكيات",
    "Category:Australian men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية أستراليون",
    "Category:Kuwaiti men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية كويتيون",
    "Category:Men's wheelchair basketball players by nationality": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية حسب الجنسية",
    "Category:Men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة رجالية",
}


TEMPORAL_CASES = [
    ("test_wheelchair_1", data),
    ("test_wheelchair_racers", wheelchair_racers),
    ("test_wheelchair_mens_womens", mens_womens),
]


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_wheelchair_1(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", wheelchair_racers.items(), ids=list(wheelchair_racers.keys()))
@pytest.mark.fast
def test_wheelchair_racers(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", mens_womens.items(), ids=list(mens_womens.keys()))
@pytest.mark.fast
def test_wheelchair_mens_womens(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.slow
def test_all(name, data):
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
