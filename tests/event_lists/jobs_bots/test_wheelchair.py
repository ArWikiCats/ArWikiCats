"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

wheelchair_racers_by_nat = {
    "Category:American men wheelchair racers": "تصنيف:متسابقو كراسي متحركة أمريكيون",
    "Category:Australian men wheelchair racers": "تصنيف:متسابقو كراسي متحركة أستراليون",
    "Category:Austrian men wheelchair racers": "تصنيف:متسابقو كراسي متحركة نمساويون",
    "Category:Belgian men wheelchair racers": "تصنيف:متسابقو كراسي متحركة بلجيكيون",
    "Category:Brazilian men wheelchair racers": "تصنيف:متسابقو كراسي متحركة برازيليون",
    "Category:British men wheelchair racers": "تصنيف:متسابقو كراسي متحركة بريطانيون",
    "Category:Canadian men wheelchair racers": "تصنيف:متسابقو كراسي متحركة كنديون",
    "Category:Chinese men wheelchair racers": "تصنيف:متسابقو كراسي متحركة صينيون",
    "Category:Dutch men wheelchair racers": "تصنيف:متسابقو كراسي متحركة هولنديون",
    "Category:English men wheelchair racers": "تصنيف:متسابقو كراسي متحركة إنجليز",
    "Category:Finnish men wheelchair racers": "تصنيف:متسابقو كراسي متحركة فنلنديون",
    "Category:French men wheelchair racers": "تصنيف:متسابقو كراسي متحركة فرنسيون",
    "Category:Gabonese men wheelchair racers": "تصنيف:متسابقو كراسي متحركة غابونيون",
    "Category:German men wheelchair racers": "تصنيف:متسابقو كراسي متحركة ألمان",
    "Category:Irish men wheelchair racers": "تصنيف:متسابقو كراسي متحركة أيرلنديون",
    "Category:Israeli men wheelchair racers": "تصنيف:متسابقو كراسي متحركة إسرائيليون",
    "Category:Japanese men wheelchair racers": "تصنيف:متسابقو كراسي متحركة يابانيون",
    "Category:Mexican men wheelchair racers": "تصنيف:متسابقو كراسي متحركة مكسيكيون",
    "Category:Swiss men wheelchair racers": "تصنيف:متسابقو كراسي متحركة سويسريون",
    "Category:Welsh men wheelchair racers": "تصنيف:متسابقو كراسي متحركة ويلزيون",
    "Category:American wheelchair racers": "تصنيف:متسابقو كراسي متحركة أمريكيون",
    "Category:American women wheelchair racers": "تصنيف:متسابقات كراسي متحركة أمريكيات",
    "Category:Australian wheelchair racers": "تصنيف:متسابقو كراسي متحركة أستراليون",
    "Category:Australian women wheelchair racers": "تصنيف:متسابقات كراسي متحركة أستراليات",
    "Category:Austrian wheelchair racers": "تصنيف:متسابقو كراسي متحركة نمساويون",
    "Category:Belgian wheelchair racers": "تصنيف:متسابقو كراسي متحركة بلجيكيون",
    "Category:Belgian women wheelchair racers": "تصنيف:متسابقات كراسي متحركة بلجيكيات",
    "Category:Brazilian wheelchair racers": "تصنيف:متسابقو كراسي متحركة برازيليون",
    "Category:Brazilian women wheelchair racers": "تصنيف:متسابقات كراسي متحركة برازيليات",
    "Category:British wheelchair racers": "تصنيف:متسابقو كراسي متحركة بريطانيون",
    "Category:British women wheelchair racers": "تصنيف:متسابقات كراسي متحركة بريطانيات",
    "Category:Canadian wheelchair racers": "تصنيف:متسابقو كراسي متحركة كنديون",
    "Category:Canadian women wheelchair racers": "تصنيف:متسابقات كراسي متحركة كنديات",
    "Category:Chinese wheelchair racers": "تصنيف:متسابقو كراسي متحركة صينيون",
    "Category:Chinese women wheelchair racers": "تصنيف:متسابقات كراسي متحركة صينيات",
    "Category:Czech wheelchair racers": "تصنيف:متسابقو كراسي متحركة تشيكيون",
    "Category:Danish wheelchair racers": "تصنيف:متسابقو كراسي متحركة دنماركيون",
    "Category:Dutch wheelchair racers": "تصنيف:متسابقو كراسي متحركة هولنديون",
    "Category:Dutch women wheelchair racers": "تصنيف:متسابقات كراسي متحركة هولنديات",
    "Category:Emirati wheelchair racers": "تصنيف:متسابقو كراسي متحركة إماراتيون",
    "Category:English wheelchair racers": "تصنيف:متسابقو كراسي متحركة إنجليز",
    "Category:English women wheelchair racers": "تصنيف:متسابقات كراسي متحركة إنجليزيات",
    "Category:Finnish wheelchair racers": "تصنيف:متسابقو كراسي متحركة فنلنديون",
    "Category:Finnish women wheelchair racers": "تصنيف:متسابقات كراسي متحركة فنلنديات",
    "Category:French wheelchair racers": "تصنيف:متسابقو كراسي متحركة فرنسيون",
    "Category:Gabonese wheelchair racers": "تصنيف:متسابقو كراسي متحركة غابونيون",
    "Category:German wheelchair racers": "تصنيف:متسابقو كراسي متحركة ألمان",
    "Category:Irish wheelchair racers": "تصنيف:متسابقو كراسي متحركة أيرلنديون",
    "Category:Irish women wheelchair racers": "تصنيف:متسابقات كراسي متحركة أيرلنديات",
    "Category:Israeli wheelchair racers": "تصنيف:متسابقو كراسي متحركة إسرائيليون",
    "Category:Italian wheelchair racers": "تصنيف:متسابقو كراسي متحركة إيطاليون",
    "Category:Japanese wheelchair racers": "تصنيف:متسابقو كراسي متحركة يابانيون",
    "Category:Japanese women wheelchair racers": "تصنيف:متسابقات كراسي متحركة يابانيات",
    "Category:Kuwaiti wheelchair racers": "تصنيف:متسابقو كراسي متحركة كويتيون",
    "Category:Lithuanian wheelchair racers": "تصنيف:متسابقو كراسي متحركة ليتوانيون",
    "Category:Macedonian wheelchair racers": "تصنيف:متسابقو كراسي متحركة مقدونيون",
    "Category:Men wheelchair racers": "تصنيف:متسابقو كراسي متحركة",
    "Category:Mexican wheelchair racers": "تصنيف:متسابقو كراسي متحركة مكسيكيون",
    "Category:Mexican women wheelchair racers": "تصنيف:متسابقات كراسي متحركة مكسيكيات",
    "Category:Norwegian wheelchair racers": "تصنيف:متسابقو كراسي متحركة نرويجيون",
    "Category:Russian wheelchair racers": "تصنيف:متسابقو كراسي متحركة روس",
    "Category:Paralympic wheelchair racers": "تصنيف:متسابقو كراسي متحركة في الألعاب البارالمبية",
    "Category:Polish wheelchair racers": "تصنيف:متسابقو كراسي متحركة بولنديون",
    "Category:Sammarinese wheelchair racers": "تصنيف:متسابقو كراسي متحركة سان مارينيون",
    "Category:Scottish wheelchair racers": "تصنيف:متسابقو كراسي متحركة إسكتلنديون",
    "Category:Scottish women wheelchair racers": "تصنيف:متسابقات كراسي متحركة إسكتلنديات",
    "Category:South Korean wheelchair racers": "تصنيف:متسابقو كراسي متحركة كوريون جنوبيون",
    "Category:Spanish wheelchair racers": "تصنيف:متسابقو كراسي متحركة إسبان",
    "Category:Swedish wheelchair racers": "تصنيف:متسابقو كراسي متحركة سويديون",
    "Category:Swiss wheelchair racers": "تصنيف:متسابقو كراسي متحركة سويسريون",
    "Category:Swiss women wheelchair racers": "تصنيف:متسابقات كراسي متحركة سويسريات",
    "Category:Thai wheelchair racers": "تصنيف:متسابقو كراسي متحركة تايلنديون",
    "Category:Tunisian wheelchair racers": "تصنيف:متسابقو كراسي متحركة تونسيون",
    "Category:Turkish wheelchair racers": "تصنيف:متسابقو كراسي متحركة أتراك",
    "Category:Turkish women wheelchair racers": "تصنيف:متسابقات كراسي متحركة تركيات",
    "Category:Welsh wheelchair racers": "تصنيف:متسابقو كراسي متحركة ويلزيون",
    "Category:Welsh women wheelchair racers": "تصنيف:متسابقات كراسي متحركة ويلزيات",
    "Category:Wheelchair racers at the 2020 Summer Olympics": "تصنيف:متسابقو كراسي متحركة في الألعاب الأولمبية الصيفية 2020",
    "Category:Wheelchair racers by nationality": "تصنيف:متسابقو كراسي متحركة حسب الجنسية",
    "Category:Wheelchair racers": "تصنيف:متسابقو كراسي متحركة",
    "Category:Women wheelchair racers": "تصنيف:متسابقات كراسي متحركة",
    "Category:Zambian wheelchair racers": "تصنيف:متسابقو كراسي متحركة زامبيون",
    "Category:Australia women's national wheelchair basketball team": "تصنيف:منتخب أستراليا لكرة السلة على الكراسي المتحركة للسيدات",
    "Category:Women's National Wheelchair Basketball League": "تصنيف:الدوري الوطني لكرة السلة على الكراسي المتحركة للسيدات",
    "Category:New Zealand wheelchair racers": "تصنيف:متسابقو كراسي متحركة نيوزيلنديون",
    "Category:New Zealand wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة نيوزيلنديون",
    "Category:Olympic men wheelchair racers": "تصنيف:متسابقو كراسي متحركة في الألعاب الأولمبية",
    "Category:Olympic women wheelchair racers": "تصنيف:متسابقات كراسي متحركة في الألعاب الأولمبية",
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
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_wheelchair_3(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: str) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
