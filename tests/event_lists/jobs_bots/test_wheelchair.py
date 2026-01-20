"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

wheelchair_racers_by_nat = {
    "American men wheelchair racers": "متسابقو كراسي متحركة أمريكيون",
    "Australian men wheelchair racers": "متسابقو كراسي متحركة أستراليون",
    "Austrian men wheelchair racers": "متسابقو كراسي متحركة نمساويون",
    "Belgian men wheelchair racers": "متسابقو كراسي متحركة بلجيكيون",
    "Brazilian men wheelchair racers": "متسابقو كراسي متحركة برازيليون",
    "British men wheelchair racers": "متسابقو كراسي متحركة بريطانيون",
    "Canadian men wheelchair racers": "متسابقو كراسي متحركة كنديون",
    "Chinese men wheelchair racers": "متسابقو كراسي متحركة صينيون",
    "Dutch men wheelchair racers": "متسابقو كراسي متحركة هولنديون",
    "English men wheelchair racers": "متسابقو كراسي متحركة إنجليز",
    "Finnish men wheelchair racers": "متسابقو كراسي متحركة فنلنديون",
    "French men wheelchair racers": "متسابقو كراسي متحركة فرنسيون",
    "Gabonese men wheelchair racers": "متسابقو كراسي متحركة غابونيون",
    "German men wheelchair racers": "متسابقو كراسي متحركة ألمان",
    "Irish men wheelchair racers": "متسابقو كراسي متحركة أيرلنديون",
    "Israeli men wheelchair racers": "متسابقو كراسي متحركة إسرائيليون",
    "Japanese men wheelchair racers": "متسابقو كراسي متحركة يابانيون",
    "Mexican men wheelchair racers": "متسابقو كراسي متحركة مكسيكيون",
    "Swiss men wheelchair racers": "متسابقو كراسي متحركة سويسريون",
    "Welsh men wheelchair racers": "متسابقو كراسي متحركة ويلزيون",
    "American wheelchair racers": "متسابقو كراسي متحركة أمريكيون",
    "American women wheelchair racers": "متسابقات كراسي متحركة أمريكيات",
    "Australian wheelchair racers": "متسابقو كراسي متحركة أستراليون",
    "Australian women wheelchair racers": "متسابقات كراسي متحركة أستراليات",
    "Austrian wheelchair racers": "متسابقو كراسي متحركة نمساويون",
    "Belgian wheelchair racers": "متسابقو كراسي متحركة بلجيكيون",
    "Belgian women wheelchair racers": "متسابقات كراسي متحركة بلجيكيات",
    "Brazilian wheelchair racers": "متسابقو كراسي متحركة برازيليون",
    "Brazilian women wheelchair racers": "متسابقات كراسي متحركة برازيليات",
    "British wheelchair racers": "متسابقو كراسي متحركة بريطانيون",
    "British women wheelchair racers": "متسابقات كراسي متحركة بريطانيات",
    "Canadian wheelchair racers": "متسابقو كراسي متحركة كنديون",
    "Canadian women wheelchair racers": "متسابقات كراسي متحركة كنديات",
    "Chinese wheelchair racers": "متسابقو كراسي متحركة صينيون",
    "Chinese women wheelchair racers": "متسابقات كراسي متحركة صينيات",
    "Czech wheelchair racers": "متسابقو كراسي متحركة تشيكيون",
    "Danish wheelchair racers": "متسابقو كراسي متحركة دنماركيون",
    "Dutch wheelchair racers": "متسابقو كراسي متحركة هولنديون",
    "Dutch women wheelchair racers": "متسابقات كراسي متحركة هولنديات",
    "Emirati wheelchair racers": "متسابقو كراسي متحركة إماراتيون",
    "English wheelchair racers": "متسابقو كراسي متحركة إنجليز",
    "English women wheelchair racers": "متسابقات كراسي متحركة إنجليزيات",
    "Finnish wheelchair racers": "متسابقو كراسي متحركة فنلنديون",
    "Finnish women wheelchair racers": "متسابقات كراسي متحركة فنلنديات",
    "French wheelchair racers": "متسابقو كراسي متحركة فرنسيون",
    "Gabonese wheelchair racers": "متسابقو كراسي متحركة غابونيون",
    "German wheelchair racers": "متسابقو كراسي متحركة ألمان",
    "Irish wheelchair racers": "متسابقو كراسي متحركة أيرلنديون",
    "Irish women wheelchair racers": "متسابقات كراسي متحركة أيرلنديات",
    "Israeli wheelchair racers": "متسابقو كراسي متحركة إسرائيليون",
    "Italian wheelchair racers": "متسابقو كراسي متحركة إيطاليون",
    "Japanese wheelchair racers": "متسابقو كراسي متحركة يابانيون",
    "Japanese women wheelchair racers": "متسابقات كراسي متحركة يابانيات",
    "Kuwaiti wheelchair racers": "متسابقو كراسي متحركة كويتيون",
    "Lithuanian wheelchair racers": "متسابقو كراسي متحركة ليتوانيون",
    "Macedonian wheelchair racers": "متسابقو كراسي متحركة مقدونيون",
    "Men wheelchair racers": "متسابقو كراسي متحركة",
    "Mexican wheelchair racers": "متسابقو كراسي متحركة مكسيكيون",
    "Mexican women wheelchair racers": "متسابقات كراسي متحركة مكسيكيات",
    "Norwegian wheelchair racers": "متسابقو كراسي متحركة نرويجيون",
    "Russian wheelchair racers": "متسابقو كراسي متحركة روس",
    "Paralympic wheelchair racers": "متسابقو كراسي متحركة في الألعاب البارالمبية",
    "Polish wheelchair racers": "متسابقو كراسي متحركة بولنديون",
    "Sammarinese wheelchair racers": "متسابقو كراسي متحركة سان مارينيون",
    "Scottish wheelchair racers": "متسابقو كراسي متحركة إسكتلنديون",
    "Scottish women wheelchair racers": "متسابقات كراسي متحركة إسكتلنديات",
    "South Korean wheelchair racers": "متسابقو كراسي متحركة كوريون جنوبيون",
    "Spanish wheelchair racers": "متسابقو كراسي متحركة إسبان",
    "Swedish wheelchair racers": "متسابقو كراسي متحركة سويديون",
    "Swiss wheelchair racers": "متسابقو كراسي متحركة سويسريون",
    "Swiss women wheelchair racers": "متسابقات كراسي متحركة سويسريات",
    "Thai wheelchair racers": "متسابقو كراسي متحركة تايلنديون",
    "Tunisian wheelchair racers": "متسابقو كراسي متحركة تونسيون",
    "Turkish wheelchair racers": "متسابقو كراسي متحركة أتراك",
    "Turkish women wheelchair racers": "متسابقات كراسي متحركة تركيات",
    "Welsh wheelchair racers": "متسابقو كراسي متحركة ويلزيون",
    "Welsh women wheelchair racers": "متسابقات كراسي متحركة ويلزيات",
    "Wheelchair racers at the 2020 Summer Olympics": "متسابقو كراسي متحركة في الألعاب الأولمبية الصيفية 2020",
    "Wheelchair racers by nationality": "متسابقو كراسي متحركة حسب الجنسية",
    "Wheelchair racers": "متسابقو كراسي متحركة",
    "Women wheelchair racers": "متسابقات كراسي متحركة",
    "Zambian wheelchair racers": "متسابقو كراسي متحركة زامبيون",
    "Australia women's national wheelchair basketball team": "منتخب أستراليا لكرة السلة على الكراسي المتحركة للسيدات",
    "Women's National Wheelchair Basketball League": "الدوري الوطني لكرة السلة على الكراسي المتحركة للسيدات",
    "New Zealand wheelchair racers": "متسابقو كراسي متحركة نيوزيلنديون",
    "New Zealand wheelchair rugby players": "لاعبو رجبي على كراسي متحركة نيوزيلنديون",
    "Olympic men wheelchair racers": "متسابقو كراسي متحركة في الألعاب الأولمبية",
    "Olympic women wheelchair racers": "متسابقات كراسي متحركة في الألعاب الأولمبية",
}


data2 = {
    "Category:European Wheelchair Handball Nations’ Tournament": "",
    "Category:French Open by year – Wheelchair events": "",
    "Category:College men's wheelchair basketball teams in the United States": "",
    "Category:College women's wheelchair basketball teams in the United States": "",
    "Category:Canadian wheelchair sports competitors": "",
    "Category:British wheelchair shot putters": "",
    "Category:British wheelchair sports competitors": "",
    "Category:British wheelchair track and field athletes": "",
    "Category:American wheelchair javelin throwers": "",
    "Category:American wheelchair shot putters": "",
    "Category:American wheelchair sports competitors": "",
    "Category:American wheelchair track and field athletes": "",
    "Category:Australian Open by year – Wheelchair events": "",
    "Category:IWBF U23 World Wheelchair Basketball Championship": "",
    "Category:Pan American Wheelchair Handball Championship": "",
    "Category:Paralympic wheelchair basketball squads": "",
    "Category:Puerto Rican wheelchair sports competitors": "",
    "Category:Puerto Rican wheelchair track and field athletes": "",
    "Category:RFL Wheelchair Super League": "",
    "Category:Women's U25 Wheelchair Basketball World Championship": "",
    "Category:World Wheelchair Mixed Doubles Curling Championship": "",
    "Category:Wheelchair rugby Paralympic champions navigational boxes": "",
    "Category:Wheelchair Tennis Masters": "",
    "Category:Wheelchair basketball at the 2020 ASEAN Para Games": "",
    "Category:Wheelchair basketball at the ASEAN Para Games": "",
    "Category:Wheelchair fencing at the 2020 ASEAN Para Games": "",
    "Category:Wheelchair fencing at the ASEAN Para Games": "",
    "Category:Wheelchair javelin throwers": "",
    "Category:Wheelchair manufacturers": "",
    "Category:Wheelchair marathons": "",
    "Category:Wheelchair organizations": "",
    "Category:Wheelchair rugby biography stubs": "",
    "Category:Wheelchair shot putters": "",
    "Category:Wheelchair sports classifications": "",
    "Category:Wheelchair sports competitors by nationality": "",
    "Category:Wheelchair sports competitors": "",
    "Category:Wheelchair tennis at the 2020 ASEAN Para Games": "",
    "Category:Wheelchair tennis at the ASEAN Para Games": "",
    "Category:Wheelchair track and field athletes by nationality": "",
    "Category:Wheelchair track and field athletes": "",
    "Category:Wheelchair users by nationality": "",
    "Category:Wheelchair users from Georgia (country)": "",
    "Category:Wheelchair-category Paralympic competitors": "",
    "Category:Wheelchairs": "",
    "Category:Wimbledon Championship by year – Wheelchair events": "",
    "Category:Wimbledon Championship by year – Wheelchair men's doubles": "",
    "Category:Wimbledon Championship by year – Wheelchair men's singles": "",
    "Category:Wimbledon Championship by year – Wheelchair quad doubles": "",
    "Category:Wimbledon Championship by year – Wheelchair quad singles": "",
    "Category:Wimbledon Championship by year – Wheelchair women's doubles": "",
    "Category:Wimbledon Championship by year – Wheelchair women's singles": "",
}

test_data = [
    ("test_wheelchair_racers_by_nat", wheelchair_racers_by_nat),
    ("test_wheelchair_3", data2),
]


@pytest.mark.parametrize(
    "category, expected", wheelchair_racers_by_nat.items(), ids=list(wheelchair_racers_by_nat.keys())
)
@pytest.mark.fast
def test_wheelchair_racers_by_nat(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_wheelchair_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: str) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
