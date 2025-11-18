#!/usr/bin/python3
"""


"""
import pytest
from src.translations.sports_formats_teams.sport_lab import Get_New_team_xo, Get_Sport_Format_xo_en_ar_is_P17


@pytest.mark.fast
def test_Get_New_team_xo() -> None:

    label = Get_New_team_xo("national softball teams")
    assert label == 'منتخبات كرة لينة وطنية'


data = {
    "national youth women's under-14 softball leagues umpires": "حكام دوريات كرة لينة وطنية تحت 14 سنة للشابات",
    "national youth women's under-14 softball teams trainers": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
    "national youth women's under-14 softball leagues trainers": "مدربو دوريات كرة لينة وطنية تحت 14 سنة للشابات",
    "national youth women's under-14 softball teams scouts": "كشافة منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
    "national youth women's under-14 softball leagues scouts": "كشافة دوريات كرة لينة وطنية تحت 14 سنة للشابات",
    "national youth women's under-14 softball teams coaches": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",

    "football seventh tier leagues": "دوريات كرة قدم من الدرجة السابعة",
    "football chairmen and investors": "رؤساء ومسيرو كرة قدم",
    "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "domestic football cup": "كؤوس كرة قدم محلية",
    "current football seasons": "مواسم كرة قدم حالية",
    "football cups": "كؤوس كرة قدم",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "domestic football": "كرة قدم محلية",
    "indoor football": "كرة قدم داخل الصالات",
    "defunct football clubs": "أندية كرة قدم سابقة",

    "national women's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للسيدات",
    "national men's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للرجال",
    "national equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية",
    "under-13 equestrian": "فروسية تحت 13 سنة",
    "national under-13 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 13 سنة",
    "under-13 equestrian manager history": "تاريخ مدربو فرق فروسية تحت 13 سنة",
    "under-14 equestrian": "فروسية تحت 14 سنة",
    "national under-14 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 14 سنة",
    "under-14 equestrian manager history": "تاريخ مدربو فرق فروسية تحت 14 سنة",
    "outdoor equestrian": "فروسية في الهواء الطلق",

    "under-13 baseball leagues finals": "نهائيات دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams positions": "مراكز فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues positions": "مراكز دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams tournaments": "بطولات فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues tournaments": "بطولات دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams films": "أفلام فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues films": "أفلام دوريات كرة قاعدة تحت 13 سنة",
}


@pytest.mark.fast
@pytest.mark.parametrize("category, expected_key", data.items(), ids=list(data.keys()))
def test_all(category, expected_key):
    result = Get_New_team_xo(category)
    assert result.strip() == expected_key, f"Mismatch for {category}"


data2 = {
    "national women's soccer team": "منتخب {} لكرة القدم للسيدات",
    "winter olympics softball": "كرة لينة {} في الألعاب الأولمبية الشتوية",
}


@pytest.mark.parametrize("category, expected_key", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_Get_Sport_Format_xo_en_ar_is_P17(category, expected_key) -> None:

    label = Get_Sport_Format_xo_en_ar_is_P17(category)
    assert label.strip() == expected_key


def test_get_teams_new_mens_softball_world_cup_regression() -> None:
    """The resolver should correctly translate the softball world cup query."""

    result = Get_New_team_xo("men's softball world cup")
    assert result == "كأس العالم للكرة اللينة للرجال"


def test_get_teams_new_returns_default_for_unknown_category() -> None:
    """Unmapped categories should return the provided default value."""

    assert Get_New_team_xo("mystery sport") == ""
