"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_callback

data_0 = {
    "1520 in men's football": "كرة قدم رجالية في 1520",
    "1550s in cycle racing": "سباق الدراجات في عقد 1550",
    "1550 in motorsport": "رياضة المحركات في 1550",
    "1520 in youth football": "كرة قدم شبابية في 1520",
    "Coaches of American football from West Virginia": "مدربو كرة القدم الأمريكية من فرجينيا الغربية",
}

data_1 = {
    "Soccer clubs in Papua New Guinea": "أندية كرة قدم في بابوا غينيا الجديدة",
    "Table tennis clubs": "أندية كرة طاولة",
    "volleyball clubs in italy": "أندية كرة طائرة في إيطاليا",
    "Wheelchair basketball leagues in Australia": "دوريات كرة سلة على كراسي متحركة في أستراليا",
    "Wheelchair basketball leagues in Europe": "دوريات كرة سلة على كراسي متحركة في أوروبا",
    "Wheelchair tennis tournaments": "بطولات كرة المضرب على الكراسي المتحركة",
    "Papua New Guinea in international cricket": "بابوا غينيا الجديدة في كريكت دولية",
    "Women's basketball in Papua New Guinea": "كرة سلة نسائية في بابوا غينيا الجديدة",
    "Women's soccer in Papua New Guinea": "كرة قدم نسائية في بابوا غينيا الجديدة",
    "Women's cricket in Papua New Guinea": "كريكت نسائية في بابوا غينيا الجديدة",
    "Tennis tournaments in Antigua and Barbuda": "بطولات كرة المضرب في أنتيغوا وباربودا",
    "Women's cricket in Antigua and Barbuda": "كريكت نسائية في أنتيغوا وباربودا",
    "Youth athletics": "ألعاب قوى شبابية",
    "Women's sports seasons by continent": "مواسم رياضات نسائية حسب القارة",
    "Documentary films about women's sports": "أفلام وثائقية عن رياضات نسائية",
    "History of women's sports": "تاريخ رياضات نسائية",
    "Women's sports in the United States by state": "رياضات نسائية في الولايات المتحدة حسب الولاية",
    "Works about women's sports": "أعمال عن رياضات نسائية",
    "women's sports leagues in uzbekistan": "دوريات رياضية نسائية في أوزبكستان",
    "Women's sports organizations in the United States": "منظمات رياضية نسائية في الولايات المتحدة",
    "Women's sports teams in Cuba": "فرق رياضية نسائية في كوبا",
    "Women's sports in United States by state": "رياضات نسائية في الولايات المتحدة حسب الولاية",
    "motorsport venues in massachusetts": "ملاعب رياضة المحركات في ماساتشوستس",
    "motorsport venues in scotland": "ملاعب رياضة المحركات في إسكتلندا",
    "women's cricket teams in india": "فرق كريكت نسائية في الهند",
    "women's football in slovakia": "كرة قدم نسائية في سلوفاكيا",
    "women's futsal in bolivia": "كرة صالات نسائية في بوليفيا",
    "tennis tournaments in serbia-and-montenegro": "بطولات كرة المضرب في صربيا والجبل الأسود",
    "men's football leagues in algeria": "دوريات كرة قدم رجالية في الجزائر",
    "basketball leagues in oceania": "دوريات كرة سلة في أوقيانوسيا",
}


@pytest.mark.parametrize("category, expected_key", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_new_data(category: str, expected_key: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected_key


to_test = [
    ("test_sports_new_1", data_0, resolve_label_ar),
    ("test_sports_new_2", data_1, resolve_label_ar),
]
test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
