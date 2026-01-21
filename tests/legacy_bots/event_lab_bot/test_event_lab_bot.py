"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.event_lab_bot import event_Lab

data = {
    "category:air force navigational boxes": "تصنيف:صناديق تصفح قوات جوية",
    "category:action films by genre": "تصنيف:أفلام حركة حسب النوع الفني",
    "category:africanamerican history by state": "تصنيف:تاريخ أمريكي إفريقي حسب الولاية",
    "category:airlines by dependent territory": "تصنيف:شركات طيران حسب الأقاليم التابعة",
    "category:ambassadors by mission country": "تصنيف:سفراء حسب بلد البعثة",
    "category:american culture by state": "تصنيف:ثقافة أمريكية حسب الولاية",
    "category:animals by year of formal description": "تصنيف:حيوانات حسب سنة الوصف",
    "category:athletics in the summer universiade navigational boxes": "تصنيف:صناديق تصفح ألعاب القوى في الألعاب الجامعية الصيفية",
    "category:bridges in wales by type": "تصنيف:جسور في ويلز حسب الفئة",
    "category:celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
    "category:comics set in 1st century bc": "تصنيف:قصص مصورة تقع أحداثها في القرن 1 ق م",
    "category:decades in oklahoma": "تصنيف:عقود في أوكلاهوما",
    "category:destroyed churches by country": "تصنيف:كنائس مدمرة حسب البلد",
    "category:dinosaurs in video games": "تصنيف:ديناصورات في ألعاب فيديو",
    "category:editorial cartoonists from northern ireland": "تصنيف:محررون كارتونيون من أيرلندا الشمالية",
    "category:environment of united states by state or territory": "تصنيف:بيئة الولايات المتحدة حسب الولاية أو الإقليم",
    "category:fantasy films by genre": "تصنيف:أفلام فانتازيا حسب النوع الفني",
    "category:figure skaters in 2002 winter olympics": "تصنيف:متزلجون فنيون في الألعاب الأولمبية الشتوية 2002",
    "category:films by movement": "تصنيف:أفلام حسب الحركة",
    "category:golfers from massachusetts": "تصنيف:لاعبو غولف من ماساتشوستس",
    "category:historic trails and roads in the united states by state": "تصنيف:طرق وممرات تاريخية في الولايات المتحدة حسب الولاية",
    "category:international women's basketball competitions hosted by cuba": "تصنيف:منافسات كرة سلة دولية للسيدات استضافتها كوبا",
    "category:languages of cayman islands": "تصنيف:لغات جزر كايمان",
    "category:multi-sport events in yemen": "تصنيف:أحداث رياضية متعددة في اليمن",
    "category:parks in the roman empire": "تصنيف:متنزهات في الإمبراطورية الرومانية",
}


@pytest.mark.parametrize("text, expected", data.items(), ids=data.keys())
def test_basic_cases(text: str, expected: str) -> None:
    result = event_Lab(text)
    assert result == expected


@pytest.mark.fast
def test_event_lab() -> None:
    # Test with a basic input
    result = event_Lab("test event")
    assert isinstance(result, str)

    # Test with different input
    result_various = event_Lab("sports event")
    assert isinstance(result_various, str)

    # Test with empty string
    result_empty = event_Lab("")
    assert isinstance(result_empty, str)


# ---------------------------------------------------------------------------
# 1) Direct label via resolve_squads_labels_and_templates
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_direct_lab2() -> None:
    result = event_Lab("Category:German footballers")
    assert result == "تصنيف:لاعبو كرة قدم ألمان"


# ---------------------------------------------------------------------------
# 2) Episodes branch + SEO fallback (list_of_cat used, no other labels)
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_episodes_branch_with_seo_fallback() -> None:
    result = event_Lab("Category:Game_of_Thrones_(season_1)_episodes")
    assert result == "تصنيف:حلقات صراع العروش الموسم 1"


# ---------------------------------------------------------------------------
# 3) Templates branch + SEO fallback
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_templates_branch_with_seo_fallback() -> None:
    result = event_Lab("Category:Association_football_templates")

    assert result == "تصنيف:قوالب كرة القدم"


# ---------------------------------------------------------------------------
# 4) get_list_of_and_cat3 footballers + Get_country2 special branch
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_footballers_country_special_case() -> None:
    result = event_Lab("Category:Ethiopian_basketball_players")

    assert result == "تصنيف:لاعبو كرة سلة إثيوبيون"


# ---------------------------------------------------------------------------
# 5) General translation fallback via general_resolver.translate_general_category
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_general_translate_category_fallback() -> None:
    result = event_Lab("Unknown Category For Testing")

    assert result == ""


# ---------------------------------------------------------------------------
# 6) Cricketers / cricket captains branch
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_event_lab_cricketers_country_mapping() -> None:
    result = event_Lab("Category:Indian cricketers")

    # Expected: "لاعبو كريكت من الهند" with تصنيف: prefix
    assert result == "تصنيف:لاعبو كريكت هنود"
