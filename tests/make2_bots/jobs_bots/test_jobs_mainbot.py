"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import Jobs


@pytest.mark.fast
def test_jobs():
    # Test with basic inputs
    result = Jobs("test category", "united states", "players")
    assert isinstance(result, str)
    assert result == ""

    # Test with empty strings
    result_empty = Jobs("", "", "")
    assert isinstance(result_empty, str)
    assert result_empty == ""

    # Test with type parameter
    result_with_type = Jobs("sports", "france", "athletes")
    assert isinstance(result_with_type, str)
    assert result_with_type == ""

    # Test with tab parameter - avoid the error by testing parameters individually
    result_with_mens_tab = Jobs("category", "united states", "workers", "رجال")
    assert isinstance(result_with_mens_tab, str)
    assert result_with_mens_tab == "عمال رجال"

    result_with_womens_tab = Jobs("category", "united states", "workers", "سيدات")
    assert isinstance(result_with_womens_tab, str)
    assert result_with_womens_tab == "عمال سيدات"


# =========================================================
#                 TESTS FOR MEN'S PATH
# =========================================================

def test_mens_direct_job_from_jobs_mens_data():
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "writers")
    assert result == "كتاب يمنيون"


def test_womens_jobs_prefix():
    Jobs.cache_clear()
    result = Jobs("", "african", "women's rights activists")
    assert result == "أفارقة ناشطون في حقوق المرأة"

    result = Jobs("", "african", "female women's rights activists")
    assert result == "ناشطات في حقوق المرأة إفريقيات"


def test_mens_prefix_fallback_when_no_jobs_data():
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "sailors")
    assert result == "بحارة يمنيون"


def test_mens_people_only():
    Jobs.cache_clear()
    result = Jobs("", "egyptian", "people")
    assert result == "مصريون"


def test_mens_nat_before_occ():
    Jobs.cache_clear()
    # expatriates in NAT_BEFORE_OCC → nationality BEFORE occupation
    result = Jobs("", "yemeni", "expatriates")
    assert result == "يمنيون مغتربون"


def test_mens_nato():
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "eugenicists")
    assert result == "علماء يمنيون متخصصون في تحسين النسل"


def test_womens_nato():
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "female eugenicists", womens="")  # Removed 'womens="يمنيات"' to test natural fallback
    assert result == "عالمات متخصصات في تحسين النسل يمنيات"


def test_womens_no_nat():
    Jobs.cache_clear()
    result2 = Jobs("", "", "female eugenicists", womens="")
    assert result2 == ""


def test_mens_with_pkjn_suffix():
    Jobs.cache_clear()
    # prefix returns مغتربون => pkjn modifies it
    result = Jobs("", "yemeni", "expatriates")
    assert "يمنيون مغتربون" in result

# =========================================================
#                 TESTS FOR WOMEN'S PATH
# =========================================================


def test_womens_short_jobs():
    Jobs.cache_clear()
    result = Jobs("", "egyptian", "actresses")
    assert result == "ممثلات مصريات"


def test_womens_prefix_fallback():
    Jobs.cache_clear()
    result = Jobs("", "egyptian", "women sailors")
    assert result == "بحارات مصريات"
    Jobs.cache_clear()  # Clear cache for next call
    result = Jobs("", "egyptian", "female sailors")
    assert result == "بحارات مصريات"


def test_womens_direct_word_women_keyword():
    Jobs.cache_clear()
    result = Jobs("", "egyptian", "women")
    assert result == "مصريات"

# =========================================================
#                 MIXED CASES
# =========================================================


def test_mens_priority_over_women_if_mens_exists():
    # nationality exists for men → choose men's path
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "writers")
    assert "يمنيون" in result


def test_override_mens_manually():
    Jobs.cache_clear()
    result = Jobs("", "abc", "writers", mens="رجال")
    assert result.startswith("كتاب رجال")


def test_override_womens_manually():
    Jobs.cache_clear()
    result = Jobs("", "abc", "actresses", womens="نساء")
    assert result.startswith("ممثلات نساء")


def test_no_mens_no_women_return_empty():
    # no nationality and no job match
    Jobs.cache_clear()
    result = Jobs("", "unknown", "zzz")
    assert result == ""


# =========================================================
#                 EDGE CASES
# =========================================================

def test_con_3_starts_with_people_space():
    Jobs.cache_clear()
    result = Jobs("", "yemeni", "writers")
    assert "يمنيون" in result
    assert result == "كتاب يمنيون"


def test_empty_con_3():
    Jobs.cache_clear()
    assert Jobs("", "yemeni", "") == ""


def test_empty_start():
    Jobs.cache_clear()
    result = Jobs("", "", "writers")
    # no nationality found → empty
    assert result == ""
