#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data_1 = {
    "Shooting sports events": "أحداث الرماية",
    "International sports events": "أحداث رياضية دولية",
    "April 2020 sports events France": "",
    "ASEAN sports events": "",
    "Cancelled sports events": "",
    "Cancelled sports events by sport": "",
    "Charity sports events": "",
    "Current sports events": "",
    "LGBTQ sports events": "",
    "Qualification for sports events": "",
    "Red Bull sports events": "",
    "Sports events affected by the COVID-19 pandemic": "",
    "Sports events affected by the Russian invasion of Ukraine": "",
    "Sports events affected by the September 11 attacks": "",
    "Sports events at Caesars Palace": "",
    "Sports events at MGM Grand Garden Arena": "",
    "Sports events at Wembley Stadium": "",
    "Sports events by venue": "",
    "Sports events external link templates": "",
    "Sports events founded by Sri Chinmoy": "",
    "Sports events music": "",
    "Sports events official songs and anthems": "",
}

fast_data_2 = {
    "2010 rugby union tournaments for national teams": "بطولات اتحاد الرجبي للمنتخبات الوطنية 2010",
    "Equestrian events at 2010 Asian Games": "أحداث الفروسية في الألعاب الآسيوية 2010",
    "Football events in England": "أحداث كرة القدم في إنجلترا",
    "Football events in Paraguay": "أحداث كرة القدم في باراغواي",
    "Football events in Russia": "أحداث كرة القدم في روسيا",
    "Football events in Scotland": "أحداث كرة القدم في إسكتلندا",
    "Tennis tournaments in Dominican Republic": "بطولات كرة المضرب في جمهورية الدومينيكان",
    "Tennis tournaments in North America": "بطولات كرة المضرب في أمريكا الشمالية",
    "Tennis tournaments in Wales": "بطولات كرة المضرب في ويلز",
    "Athletics events at Islamic Solidarity Games": "أحداث ألعاب القوى في ألعاب التضامن الإسلامي",
}

fast_data_3 = {
    "Lists of sports events": "قوائم أحداث رياضية",
    "Sports events navigational boxes": "صناديق تصفح أحداث رياضية",
    "Sports events templates": "قوالب أحداث رياضية",
    "Lists of sports events in Australia": "قوائم أحداث رياضية في أستراليا",
    "Lists of American sports events": "قوائم أحداث رياضية أمريكية",
    "Lists of announcers of American sports events": "قوائم مذيعون من أحداث رياضية أمريكية",
    "Lists of Taiwanese sports events": "قوائم أحداث رياضية تايوانية",
    "Men's sports events by continent": "أحداث رياضية رجالية حسب القارة",
    "Men's sports events in Africa": "أحداث رياضية رجالية في إفريقيا",
    "Men's sports events in Asia": "أحداث رياضية رجالية في آسيا",
    "Men's sports events in Europe": "أحداث رياضية رجالية في أوروبا",
    "Men's sports events in North America": "أحداث رياضية رجالية في أمريكا الشمالية",
    "Men's sports events in Oceania": "أحداث رياضية رجالية في أوقيانوسيا",
    "Men's sports events": "أحداث رياضية رجالية",
    "Sports events by continent": "أحداث رياضية حسب القارة",
    "Sports events by sport": "أحداث رياضية حسب الرياضة",
    "Sports events": "أحداث رياضية",
    "Women's sports events by continent": "أحداث رياضية نسائية حسب القارة",
    "Women's sports events in Africa": "أحداث رياضية نسائية في إفريقيا",
    "Women's sports events in Asia": "أحداث رياضية نسائية في آسيا",
    "Women's sports events in Europe": "أحداث رياضية نسائية في أوروبا",
    "Women's sports events in North America": "أحداث رياضية نسائية في أمريكا الشمالية",
    "Women's sports events in Oceania": "أحداث رياضية نسائية في أوقيانوسيا",
    "Women's sports events in South America": "أحداث رياضية نسائية في أمريكا الجنوبية",
    "Women's sports events": "أحداث رياضية نسائية",
}

to_test = [
    ("test_sports_events_2", fast_data_2),
    ("test_sports_events_3", fast_data_3),
]


@pytest.mark.parametrize("category, expected", fast_data_1.items(), ids=fast_data_1.keys())
@pytest.mark.fast
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data_2.items(), ids=fast_data_2.keys())
@pytest.mark.fast
def test_fast_data_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data_3.items(), ids=fast_data_3.keys())
@pytest.mark.fast
def test_fast_data_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
