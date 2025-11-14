#!/usr/bin/python3
"""


"""
import pytest
from src.ma_lists.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025_for_tests
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "National men's wheelchair basketball teams": "منتخبات كرة سلة على كراسي متحركة وطنية للرجال",
    "National women's wheelchair basketball teams": "منتخبات كرة سلة على كراسي متحركة وطنية للسيدات",
    "National wheelchair basketball teams": "منتخبات كرة سلة على كراسي متحركة وطنية",
    "National wheelchair handball teams": "منتخبات كرة يد على كراسي متحركة وطنية",
    "National wheelchair rugby teams": "منتخبات رجبي على كراسي متحركة وطنية",

    "World Wheelchair Rugby Championships": "بطولة العالم الرجبي على الكراسي المتحركة",
    "World Wheelchair Curling Championship": "بطولة العالم الكيرلنغ على الكراسي المتحركة",
    "Wheelchair Rugby League finals": "نهائيات دوري الرجبي على الكراسي المتحركة",
    "Wheelchair rugby league": "دوري الرجبي على الكراسي المتحركة",
    "Wheelchair Handball World Championship": "بطولة العالم كرة اليد على الكراسي المتحركة",
    "Wheelchair Rugby League World Cup": "كأس العالم لدوري الرجبي على الكراسي المتحركة",
    "Wheelchair rugby league competitions": "منافسات دوري رجبي على كراسي متحركة",
    "Wheelchair rugby league teams": "فرق دوري رجبي على كراسي متحركة",
}


def test_normal():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, wrap_team_xo_normal_2025_for_tests)

    dump_diff(diff_result, "test_normal")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.fast
def test_wrap_team_xo_normal_2025() -> None:
    data = {
        "national youth women's under-14 softball leagues umpires": "حكام دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball teams trainers": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball leagues trainers": "مدربو دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball teams scouts": "كشافة منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball leagues scouts": "كشافة دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national softball teams coaches": "مدربو منتخبات كرة لينة وطنية",
    }
    for x, v in data.items():
        label = wrap_team_xo_normal_2025_for_tests(x)
        assert label.strip() == v
