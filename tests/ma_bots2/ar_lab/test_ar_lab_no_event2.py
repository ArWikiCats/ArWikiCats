"""
Tests
"""

import pytest
from load_one_data import dump_diff

from ArWikiCats.ma_bots2.ar_lab.ar_lab_bot import find_ar_label
from ArWikiCats.ma_bots.ye_ts_bot import translate_general_category


fast_data_list = [
    {
        "separator": " in ",
        "category": "1450s disestablishments in arizona territory",
        "output": "انحلالات عقد 1450 في إقليم أريزونا",
    },
    {
        "separator": " in ",
        "category": "1450s disestablishments in the papal states",
        "output": "انحلالات عقد 1450 في الدولة البابوية",
    },
    {
        "separator": " in ",
        "category": "january 1450 sports-events in north america",
        "output": "أحداث يناير 1450 الرياضية في أمريكا الشمالية",
    },
    {
        "separator": " in ",
        "category": "july 1450 sports-events in china",
        "output": "أحداث يوليو 1450 الرياضية في الصين",
    },
    {"separator": " in ", "category": "1450s crimes in california", "output": "جرائم عقد 1450 في كاليفورنيا"},
    {"separator": " in ", "category": "1450s crimes in asia", "output": "جرائم عقد 1450 في آسيا"},
    {
        "separator": " in ",
        "category": "november 1450 sports-events in germany",
        "output": "أحداث نوفمبر 1450 الرياضية في ألمانيا",
    },
    {"separator": " in ", "category": "1450s establishments in england", "output": "تأسيسات عقد 1450 في إنجلترا"},
    {"separator": " in ", "category": "may 1450 crimes in asia", "output": "جرائم مايو 1450 في آسيا"},
    {
        "separator": " in ",
        "category": "november 1450 sports-events in the united states",
        "output": "أحداث نوفمبر 1450 الرياضية في الولايات المتحدة",
    },
]


@pytest.mark.parametrize("tab", fast_data_list, ids=lambda x: x["category"])
@pytest.mark.fast
def test_translate_general_category_event2_fast(tab) -> None:
    label = translate_general_category(tab["category"])
    # ---
    assert label == tab["output"]


data_list_bad = [
    ("september 1550 sports-events in germany", " in ", "أحداث سبتمبر 1550 الرياضية في ألمانيا"),
    ("1550s disestablishments in yugoslavia", " in ", "انحلالات عقد 1550 في يوغسلافيا"),
    ("20th century disestablishments in the united kingdom", " in ", "انحلالات القرن 20 في المملكة المتحدة"),
    ("november 1550 sports-events in north america", " in ", "أحداث نوفمبر 1550 الرياضية في أمريكا الشمالية"),
    ("1550s establishments in wisconsin", " in ", "تأسيسات عقد 1550 في ويسكونسن"),
    ("20th century disestablishments in sri lanka", " in ", "انحلالات القرن 20 في سريلانكا"),
    ("3rd millennium disestablishments in england", " in ", "انحلالات الألفية 3 في إنجلترا"),
    ("may 1550 sports-events in the united states", " in ", "أحداث مايو 1550 الرياضية في الولايات المتحدة"),
    ("december 1550 sports-events in the united states", " in ", "أحداث ديسمبر 1550 الرياضية في الولايات المتحدة"),
    ("1550s crimes in pakistan", " in ", "جرائم عقد 1550 في باكستان"),
    ("2nd millennium establishments in rhode island", " in ", "تأسيسات الألفية 2 في رود آيلاند"),
    ("1550s establishments in chile", " in ", "تأسيسات عقد 1550 في تشيلي"),
    ("1550s disestablishments in southeast asia", " in ", "انحلالات عقد 1550 في جنوب شرق آسيا"),
    ("december 1550 sports-events in the united kingdom", " in ", "أحداث ديسمبر 1550 الرياضية في المملكة المتحدة"),
    ("1550s establishments in jamaica", " in ", "تأسيسات عقد 1550 في جامايكا"),
    ("march 1550 sports-events in belgium", " in ", "أحداث مارس 1550 الرياضية في بلجيكا"),
    ("20th century disasters in afghanistan", " in ", "كوارث القرن 20 في أفغانستان"),
    ("april 1550 sports-events in the united kingdom", " in ", "أحداث أبريل 1550 الرياضية في المملكة المتحدة"),
    ("1550s disestablishments in mississippi", " in ", "انحلالات عقد 1550 في مسيسيبي"),
    ("1550s establishments in maine", " in ", "تأسيسات عقد 1550 في مين"),
    ("1550s establishments in sweden", " in ", "تأسيسات عقد 1550 في السويد"),
    (
        "20th century disestablishments in newfoundland and labrador",
        " in ",
        "انحلالات القرن 20 في نيوفاوندلاند واللابرادور",
    ),
    (
        "20th century disestablishments in the danish colonial empire",
        " in ",
        "انحلالات القرن 20 في الإمبراطورية الاستعمارية الدنماركية",
    ),
    ("20th century establishments in french guiana", " in ", "تأسيسات القرن 20 في غويانا الفرنسية"),
    ("20th century establishments in ireland", " in ", "تأسيسات القرن 20 في أيرلندا"),
    ("20th century monarchs by country", " by ", "ملكيون في القرن 20 حسب البلد"),
    ("august 1550 sports-events in france", " in ", "أحداث أغسطس 1550 الرياضية في فرنسا"),
    ("february 1550 sports-events in germany", " in ", "أحداث فبراير 1550 الرياضية في ألمانيا"),
    ("july 1550 crimes by continent", " by ", "جرائم يوليو 1550 حسب القارة"),
    ("july 1550 sports-events in north america", " in ", "أحداث يوليو 1550 الرياضية في أمريكا الشمالية"),
    ("june 1550 sports-events in malaysia", " in ", "أحداث يونيو 1550 الرياضية في ماليزيا"),
    ("march 1550 sports-events in thailand", " in ", "أحداث مارس 1550 الرياضية في تايلاند"),
    ("november 1550 sports-events in europe", " in ", "أحداث نوفمبر 1550 الرياضية في أوروبا"),
    ("november 1550 sports-events in the united kingdom", " in ", "أحداث نوفمبر 1550 الرياضية في المملكة المتحدة"),
    ("october 1550 sports-events in oceania", " in ", "أحداث أكتوبر 1550 الرياضية في أوقيانوسيا"),
]


def test_result_only_with_event2() -> None:
    expected_result = {}
    diff_result = {}
    for tab in data_list_bad:
        category, separator, expected = tab
        result = find_ar_label(category, separator, use_event2=True)
        result2 = find_ar_label(category, separator, use_event2=False)
        if result != expected and result2 != expected:
            expected_result[category] = expected
            diff_result[category] = result

    dump_diff(diff_result, "test_result_only_with_event2")
    assert diff_result == expected_result, f"Differences found: {len(diff_result)}"
