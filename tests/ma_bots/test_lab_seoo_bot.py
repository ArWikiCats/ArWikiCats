"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.legacy_bots.ma_bots.lab_seoo_bot import event_label_work

event_Lab_seoo_data = {
    "100th united states congress": "الكونغرس الأمريكي المئة",
    "101st united states congress": "الكونغرس الأمريكي الأول بعد المئة",
    "102nd united states congress": "الكونغرس الأمريكي الثاني بعد المئة",
    "103rd united states congress": "الكونغرس الأمريكي الثالث بعد المئة",
    "104th united states congress": "الكونغرس الأمريكي الرابع بعد المئة",
    "105th united states congress": "الكونغرس الأمريكي الخامس بعد المئة",
    "106th united states congress": "الكونغرس الأمريكي السادس بعد المئة",
    "107th united states congress": "الكونغرس الأمريكي السابع بعد المئة",
    "108th united states congress": "الكونغرس الأمريكي الثامن بعد المئة",
    "109th united states congress": "الكونغرس الأمريكي التاسع بعد المئة",
    "10th united states congress": "الكونغرس الأمريكي العاشر",
    "110th united states congress": "الكونغرس الأمريكي العاشر بعد المئة",
    "111th united states congress": "الكونغرس الأمريكي الحادي عشر بعد المئة",
    "112th united states congress": "الكونغرس الأمريكي الثاني عشر بعد المئة",
    "113th united states congress": "الكونغرس الأمريكي الثالث عشر بعد المئة",
    "114th united states congress": "الكونغرس الأمريكي الرابع عشر بعد المئة",
    "115th united states congress": "الكونغرس الأمريكي الخامس عشر بعد المئة",
    "116th united states congress": "الكونغرس الأمريكي السادس عشر بعد المئة",
    "117th united states congress": "الكونغرس الأمريكي السابع عشر بعد المئة",
    "118th united states congress": "الكونغرس الأمريكي الثامن عشر بعد المئة",
    "119th united states congress": "الكونغرس الأمريكي التاسع عشر بعد المئة",
    "11th united states congress": "الكونغرس الأمريكي الحادي عشر",
    "12th united states congress": "الكونغرس الأمريكي الثاني عشر",
    "13th united states congress": "الكونغرس الأمريكي الثالث عشر",
    "14th united states congress": "الكونغرس الأمريكي الرابع عشر",
    "15th united states congress": "الكونغرس الأمريكي الخامس عشر",
    "16th united states congress": "الكونغرس الأمريكي السادس عشر",
    "1830 alabama": "ألاباما 1830",
    "1830 arkansas": "أركنساس 1830",
    "1830 connecticut": "كونيتيكت 1830",
    "1830 delaware": "ديلاوير 1830",
    "1830 florida territory": "إقليم فلوريدا 1830",
    "1830 georgia (u.s. state)": "ولاية جورجيا 1830",
    "1830 illinois": "إلينوي 1830",
    "1830 indiana territory": "إقليم إنديانا 1830",
    "1830 indiana": "إنديانا 1830",
    "1830 iowa territory": "إقليم آيوا 1830",
    "1830 kentucky": "كنتاكي 1830",
    "1830 louisiana": "لويزيانا 1830",
    "1830 maine": "مين 1830",
    "1830 maryland": "ماريلند 1830",
    "1830 massachusetts": "ماساتشوستس 1830",
    "1830 michigan territory": "إقليم ميشيغان 1830",
    "1830 michigan": "ميشيغان 1830",
    "1830 mississippi territory": "إقليم مسيسيبي 1830",
    "1830 mississippi": "مسيسيبي 1830",
    "1830 missouri": "ميزوري 1830",
    "1830 new hampshire": "نيوهامشير 1830",
    "1830 new jersey": "نيوجيرسي 1830",
    "1830 new york (state)": "ولاية نيويورك 1830",
    "1830 north carolina": "كارولاينا الشمالية 1830",
    "1830 ohio": "أوهايو 1830",
    "1830 pennsylvania": "بنسلفانيا 1830",
    "1830 rhode island": "رود آيلاند 1830",
    "1830 south carolina": "كارولاينا الجنوبية 1830",
    "1830 tennessee": "تينيسي 1830",
    "1830 trabzon": "طرابزون 1830",
    "1830 vermont": "فيرمونت 1830",
    "1830 virginia": "فرجينيا 1830",
    "1830 wisconsin territory": "إقليم ويسكونسن 1830",
}


@pytest.mark.parametrize("category, expected_key", event_Lab_seoo_data.items(), ids=event_Lab_seoo_data.keys())
@pytest.mark.fast
def test_event_Lab_seoo_data(category: str, expected_key: str) -> None:
    label = event_label_work(category)
    assert label == expected_key


to_test = [
    ("test_lab_seoo_bot_1", event_Lab_seoo_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, event_label_work)
    dump_same_and_not_same(data, diff_result, name)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
