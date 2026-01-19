"""
Tests
"""

import pytest

# from ArWikiCats.new_resolvers.sports_resolvers import main_sports_resolvers
from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.sports_resolvers import _not_main_sports_resolvers

data_0 = {
    "1520 in men's football": "1520 في كرة القدم للرجال",
    "1550s in cycle racing": "عقد 1550 في سباق دراجات",
    "1550 in motorsport": "1550 في رياضة محركات",
    "1520 in youth football": "1520 في كرة القدم للشباب",
    "Coaches of American football from West Virginia": "مدربو كرة قدم أمريكية من فرجينيا الغربية",
}

data_1 = {
    "Wheelchair basketball leagues in Australia": "دوريات كرة السلة على الكراسي المتحركة في أستراليا",
    "Wheelchair basketball leagues in Europe": "دوريات كرة السلة على الكراسي المتحركة في أوروبا",
    "Wheelchair tennis tournaments": "بطولات كرة مضرب على كراسي متحركة",
    "Papua New Guinea in international cricket": "بابوا غينيا الجديدة في كريكت دولي",
    "Soccer clubs in Papua New Guinea": "أندية كرة قدم في بابوا غينيا الجديدة",
    "Women's basketball in Papua New Guinea": "كرة السلة للسيدات في بابوا غينيا الجديدة",
    "Women's soccer in Papua New Guinea": "كرة القدم للسيدات في بابوا غينيا الجديدة",
    "Women's cricket in Papua New Guinea": "الكريكت للسيدات في بابوا غينيا الجديدة",
    "Tennis tournaments in Antigua and Barbuda": "بطولات كرة مضرب في أنتيغوا وباربودا",
    "Women's cricket in Antigua and Barbuda": "الكريكت للسيدات في أنتيغوا وباربودا",
    "Youth athletics": "ألعاب القوى للشباب",
    "Table tennis clubs": "أندية كرة طاولة",
    "Women's sports seasons by continent": "مواسم رياضات نسائية حسب القارة",
    "Documentary films about women's sports": "أفلام وثائقية عن رياضات نسائية",
    "History of women's sports": "تاريخ رياضات نسائية",
    "Women's sports in the United States by state": "رياضات نسائية في الولايات المتحدة حسب الولاية",
    "Works about women's sports": "أعمال عن رياضات نسائية",
    "women's sports leagues in uzbekistan": "دوريات رياضات نسائية في أوزبكستان",
    "Women's sports organizations in the United States": "منظمات رياضات نسائية في الولايات المتحدة",
    "Women's sports teams in Cuba": "فرق رياضات نسائية في كوبا",
    "Women's sports in United States by state": "رياضات نسائية في الولايات المتحدة حسب الولاية",
    "motorsport venues in massachusetts": "ملاعب رياضة محركات في ماساتشوستس",
    "motorsport venues in scotland": "ملاعب رياضة محركات في إسكتلندا",
    "volleyball clubs in italy": "أندية كرة طائرة في إيطاليا",
    "women's cricket teams in india": "فرق الكريكت للسيدات في الهند",
    "women's football in slovakia": "كرة القدم للسيدات في سلوفاكيا",
    "women's futsal in bolivia": "كرة صالات للسيدات في بوليفيا",
    "tennis tournaments in serbia-and-montenegro": "بطولات كرة مضرب في صربيا والجبل الأسود",
    "men's football leagues in algeria": "دوريات كرة القدم للرجال في الجزائر",
    "basketball leagues in oceania": "دوريات كرة السلة في أوقيانوسيا",
}


@pytest.mark.parametrize("category, expected_key", data_1.items(), ids=data_1.keys())
@pytest.mark.skip2
def test_new_data(monkeypatch: pytest.MonkeyPatch, category: str, expected_key: str) -> None:
    """
    pytest tests/new_resolvers/sports_resolvers/test_sports_new.py -m skip2 --maxfail=1000
    """

    # monkeypatch.setattr(
    #     "ArWikiCats.new_resolvers.sports_resolvers.sub_main_sports_resolvers",
    #     _not_main_sports_resolvers,
    #     raising=True,
    # )
    label = resolve_label_ar(category)
    assert label == expected_key
