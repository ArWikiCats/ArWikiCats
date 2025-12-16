"""Comprehensive pytest suite for move_years module."""

import pytest
from ArWikiCats.fix.mv_years import move_by_in, move_years_first
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

move_years_first_data = {
    "عقد 1910 في بابوا غينيا الجديدة": "بابوا غينيا الجديدة في عقد 1910",
    "2016 في بابوا غينيا الجديدة حسب الشهر": "بابوا غينيا الجديدة في 2016 حسب الشهر",
    "1330 في كرة قدم دولية للرجال": "كرة قدم دولية للرجال في 1330",
    "2023 في أقاليم ما وراء البحار البريطانية": "أقاليم ما وراء البحار البريطانية في 2023",
    "عقد 1880 في الأفلام حسب البلد": "الأفلام في عقد 1880 حسب البلد",
    "عقد 1880 في أفلام حسب البلد": "أفلام في عقد 1880 حسب البلد",
    "1994–95 في اتحاد الرجبي الأوروبي": "اتحاد الرجبي الأوروبي في 1994–95",
    "1994–95 في اتحاد الرجبي الأوروبي حسب البلد": "اتحاد الرجبي الأوروبي في 1994–95 حسب البلد",
    "عقد 2000 في السينما الأمريكية": "السينما الأمريكية في عقد 2000",
    "2006 في رياضة أيرلندية شمالية": "رياضة أيرلندية شمالية في 2006",
    "2006 في رياضة كورية شمالية": "رياضة كورية شمالية في 2006",
    "2017 في كرة القدم الإماراتية": "كرة القدم الإماراتية في 2017",
    "الألفية 10 في الخيال": "الخيال في الألفية 10",
    "عقد 1270 في الإمبراطورية الرومانية المقدسة": "الإمبراطورية الرومانية المقدسة في عقد 1270",
    "عقد 2000 في الولايات المتحدة حسب الولاية": "الولايات المتحدة في عقد 2000 حسب الولاية",
    "القرن 21 في التشيك": "التشيك في القرن 21",
    "القرن 21 في قطر": "قطر في القرن 21",


}
move_by_in_data = {
    "أمريكيون حسب المهنة في القرن 20": "أمريكيون في القرن 20 حسب المهنة",
    "ملكيون حسب البلد في القرن 20": "ملكيون في القرن 20 حسب البلد",
    "ممثلون حسب الدين في القرن 19": "ممثلون في القرن 19 حسب الدين",
    "أشخاص حسب الدين في القرن 19": "أشخاص في القرن 19 حسب الدين",
    "كتاب غير روائيين حسب الجنسية في القرن 20": "كتاب غير روائيين في القرن 20 حسب الجنسية",
    "موسيقيون حسب الآلة من أيرلندا الشمالية في القرن 20": "موسيقيون في القرن 20 حسب الآلة من أيرلندا الشمالية",

}

to_test = [
    ("test_move_years_first", move_years_first_data),
    ("test_move_by_in", move_by_in_data),
]


@pytest.mark.parametrize("category, expected", move_years_first_data.items(), ids=move_years_first_data.keys())
@pytest.mark.fast
def test_move_years_first(category: str, expected: str) -> None:
    label = move_years_first(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", move_by_in_data.items(), ids=move_by_in_data.keys())
@pytest.mark.fast
def test_move_by_in(category: str, expected: str) -> None:
    label = move_by_in(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
