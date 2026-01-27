"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.event_lab_bot import event_label_work
from utils.dump_runner import make_dump_test_name_data

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
    "1830 alabama": "1830 في ألاباما",
    "1830 arkansas": "1830 في أركنساس",
    "1830 connecticut": "1830 في كونيتيكت",
    "1830 delaware": "1830 في ديلاوير",
    "1830 georgia (u.s. state)": "1830 في ولاية جورجيا",
    "1830 illinois": "1830 في إلينوي",
    "1830 indiana": "1830 في إنديانا",
    "1830 kentucky": "1830 في كنتاكي",
    "1830 louisiana": "1830 في لويزيانا",
    "1830 maine": "1830 في مين",
    "1830 maryland": "1830 في ماريلند",
    "1830 massachusetts": "1830 في ماساتشوستس",
    "1830 michigan": "1830 في ميشيغان",
    "1830 mississippi": "1830 في مسيسيبي",
    "1830 missouri": "1830 في ميزوري",
    "1830 new hampshire": "1830 في نيوهامشير",
    "1830 new jersey": "1830 في نيوجيرسي",
    "1830 new york (state)": "1830 في ولاية نيويورك",
    "1830 north carolina": "1830 في كارولاينا الشمالية",
    "1830 ohio": "1830 في أوهايو",
    "1830 pennsylvania": "1830 في بنسلفانيا",
    "1830 rhode island": "1830 في رود آيلاند",
    "1830 south carolina": "1830 في كارولاينا الجنوبية",
    "1830 tennessee": "1830 في تينيسي",
    "1830 vermont": "1830 في فيرمونت",
    "1830 virginia": "1830 في فرجينيا",
    "1830 florida territory": "إقليم فلوريدا 1830",
    "1830 indiana territory": "إقليم إنديانا 1830",
    "1830 iowa territory": "إقليم آيوا 1830",
    "1830 michigan territory": "إقليم ميشيغان 1830",
    "1830 mississippi territory": "إقليم مسيسيبي 1830",
    "1830 trabzon": "طرابزون 1830",
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

test_dump_all = make_dump_test_name_data(to_test, event_label_work, run_same=True)
