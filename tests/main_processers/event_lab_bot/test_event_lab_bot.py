"""
Tests
"""
import pytest

from src.main_processers.event_lab_bot import event_Lab


def test_event_lab():
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
# 1) Direct label via get_list_of_and_cat3_with_lab2
# ---------------------------------------------------------------------------


def test_event_lab_direct_lab2():

    result = event_Lab("Category:German footballers")
    assert result == "تصنيف:لاعبو كرة قدم ألمان"


# ---------------------------------------------------------------------------
# 2) Episodes branch + SEO fallback (list_of_cat used, no other labels)
# ---------------------------------------------------------------------------

def test_event_lab_episodes_branch_with_seo_fallback():

    result = event_Lab("Category:Game_of_Thrones_(season_1)_episodes")
    assert result == "تصنيف:حلقات صراع العروش الموسم 1"


# ---------------------------------------------------------------------------
# 3) Templates branch + SEO fallback
# ---------------------------------------------------------------------------

def test_event_lab_templates_branch_with_seo_fallback():

    result = event_Lab("Category:Association_football_templates")

    assert result == "تصنيف:قوالب كرة القدم"


# ---------------------------------------------------------------------------
# 4) get_list_of_and_cat3 footballers + Get_country2 special branch
# ---------------------------------------------------------------------------

def test_event_lab_footballers_country_special_case():

    result = event_Lab("Category:Ethiopian_basketball_players")

    assert result == "تصنيف:لاعبو كرة سلة إثيوبيون"


# ---------------------------------------------------------------------------
# 5) General translation fallback via ye_ts_bot.translate_general_category
# ---------------------------------------------------------------------------

def test_event_lab_general_translate_category_fallback():

    result = event_Lab("Unknown Category For Testing")

    assert result == ""


# ---------------------------------------------------------------------------
# 6) Cricketers / cricket captains branch with New_P17_Finall
# ---------------------------------------------------------------------------

def test_event_lab_cricketers_country_mapping():

    result = event_Lab("Category:Indian cricketers")

    # Expected: "لاعبو كريكت من الهند" with تصنيف: prefix
    assert result == "تصنيف:لاعبو كريكت هنود"
