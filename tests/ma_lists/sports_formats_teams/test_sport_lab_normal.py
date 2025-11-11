#!/usr/bin/python3
"""


"""
import pytest
from src.ma_lists.sports_formats_teams.sport_lab import Get_New_team_xo_normal, match_sport_key
from load_one_data import ye_test_one_dataset, dump_diff


def wrap(team):
    sport_key = match_sport_key(team)
    # ---
    if not sport_key:
        return ""
    # ---
    return Get_New_team_xo_normal(team, sport_key)


data = {
    "Category:World Wheelchair Rugby Championships": "",
    "Category:World Wheelchair Curling Championship": "",
    "Category:National wheelchair rugby league teams": "",
    "Category:Wheelchair rugby league templates": "",
    "Category:Wheelchair rugby league players": "",
    "Category:Wheelchair Rugby League finals": "",
    "Category:Wheelchair rugby league": "",
    "Category:2020 Wheelchair Basketball World Championships": "",
    "Category:2020 Women's World Wheelchair Basketball Championship": "",
    "Category:National men's wheelchair basketball teams": "",
    "Category:National wheelchair basketball teams": "",
    "Category:National wheelchair handball teams": "",
    "Category:National wheelchair rugby teams": "",
    "Category:National women's wheelchair basketball teams": "",
    "Category:Wheelchair Handball World Championship": "",
    "Category:Wheelchair Rugby League World Cup": "",
    "Category:Wheelchair rugby league competitions": "",
    "Category:Wheelchair rugby league teams": "",
    "Category:Women's national youth association football teams": "",
    "Category:Coaches of national cricket teams": "",
    "Category:International women's basketball competitions hosted by Cuba": "",
}


def test_normal():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, wrap)

    dump_diff(diff_result, "test_normal")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.fast
def test_Get_New_team_xo_normal() -> None:
    data = {
        "national youth women's under-14 xoxo leagues umpires": "حكام دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 xoxo teams trainers": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 xoxo leagues trainers": "مدربو دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 xoxo teams scouts": "كشافة منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 xoxo leagues scouts": "كشافة دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national xoxo teams coaches": "مدربو منتخبات كرة لينة وطنية",
    }
    for x, v in data.items():
        label = Get_New_team_xo_normal(x, "softball")
        assert label.strip() == v
