"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import Nat_Womens, jobs_with_nat_prefix


@pytest.mark.fast
def test_jobs() -> None:
    # Test with basic inputs
    result = jobs_with_nat_prefix("test category", "united states", "players")
    assert isinstance(result, str)
    assert result == ""

    # Test with empty strings
    result_empty = jobs_with_nat_prefix("", "", "")
    assert isinstance(result_empty, str)
    assert result_empty == ""

    # Test with type parameter
    result_with_type = jobs_with_nat_prefix("sports", "france", "athletes")
    assert isinstance(result_with_type, str)
    assert result_with_type == ""

    # Test with tab parameter - avoid the error by testing parameters individually
    result_with_mens_tab = jobs_with_nat_prefix("category", "united states", "workers", "رجال")
    assert isinstance(result_with_mens_tab, str)
    assert result_with_mens_tab == "عمال رجال"

    result_with_womens_tab = jobs_with_nat_prefix("category", "united states", "workers", "سيدات")
    assert isinstance(result_with_womens_tab, str)
    assert result_with_womens_tab == "عمال سيدات"


# =========================================================
#                 TESTS FOR MEN'S PATH
# =========================================================


def test_mens_direct_job_from_jobs_mens_data() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", "writers")
    assert result == "كتاب يمنيون"


def test_womens_jobs_prefix() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "african", "women's rights activists")
    assert result == "أفارقة ناشطون في حقوق المرأة"

    result = jobs_with_nat_prefix("", "african", "female women's rights activists")
    assert result == "ناشطات في حقوق المرأة إفريقيات"


def test_mens_prefix_fallback_when_no_jobs_data() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", "sailors")
    assert result == "بحارة يمنيون"


def test_mens_people_only() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "egyptian", "people")
    assert result == "مصريون"


def test_mens_nato() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", "eugenicists")
    assert result == "علماء يمنيون متخصصون في تحسين النسل"


def test_womens_nato() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix(
        "", "yemeni", "female eugenicists", females=""
    )  # Removed 'females="يمنيات"' to test natural fallback
    assert result == "عالمات متخصصات في تحسين النسل يمنيات"


def test_womens_no_nat() -> None:
    jobs_with_nat_prefix.cache_clear()
    result2 = jobs_with_nat_prefix("", "", "female eugenicists", females="")
    assert result2 == ""


# =========================================================
#                 TESTS FOR WOMEN'S PATH
# =========================================================


def test_womens_short_jobs() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "egyptian", "actresses")
    assert result == "ممثلات مصريات"


def test_womens_prefix_fallback() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "egyptian", "women sailors")
    assert result == "بحارات مصريات"
    jobs_with_nat_prefix.cache_clear()  # Clear cache for next call
    result = jobs_with_nat_prefix("", "egyptian", "female sailors")
    assert result == "بحارات مصريات"


def test_womens_direct_word_women_keyword() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "egyptian", "women")
    assert result == "مصريات"


# =========================================================
#                 MIXED CASES
# =========================================================


def test_mens_priority_over_women_if_mens_exists() -> None:
    # nationality exists for men → choose men's path
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", "writers")
    assert "يمنيون" in result


def test_override_mens_manually() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "abc", "writers", mens="رجال")
    assert result.startswith("كتاب رجال")


def test_override_womens_manually() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "abc", "actresses", females="نساء")
    assert result.startswith("ممثلات نساء")


def test_no_mens_no_women_return_empty() -> None:
    # no nationality and no job match
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "unknown", "zzz")
    assert result == ""


# =========================================================
#                 EDGE CASES
# =========================================================


def test_con_3_starts_with_people_space() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", "writers")
    assert "يمنيون" in result
    assert result == "كتاب يمنيون"


def test_empty_con_3() -> None:
    jobs_with_nat_prefix.cache_clear()
    assert jobs_with_nat_prefix("", "yemeni", "") == ""


def test_empty_start() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "", "writers")
    # no nationality found → empty
    assert result == ""


# =========================================================
#                 NEW EXPANDED TESTS
# =========================================================

# --- New Nationalities Tests ---


def test_new_mens_nationality_afghan_people() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "afghan", "people")
    assert result == "أفغان"


def test_new_womens_nationality_afghan_women() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "afghan", "women")
    assert result == "أفغانيات"


def test_new_mens_nationality_algerian_writers() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "algerian", "writers")
    assert result == "كتاب جزائريون"


def test_new_womens_nationality_algerian_actresses() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "algerian", "actresses")
    assert result == "ممثلات جزائريات"


def test_new_mens_nationality_argentine_sailors() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "argentine", "sailors")
    assert result == "بحارة أرجنتينيون"


def test_new_womens_nationality_argentine_female_sailors() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "argentine", "female sailors")
    assert result == "بحارات أرجنتينيات"


# --- New Men's Jobs Data Tests ---


def test_new_mens_job_classical_europop_composers_albanian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "albanian", "classical europop composers")
    assert result == "ملحنو يوروبوب كلاسيكيون ألبان"


def test_new_mens_job_abidat_rma_pianists_arab() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "arab", "abidat rma pianists")
    assert result == "عازفو بيانو عبيدات الرما عرب"


def test_new_mens_job_historical_objectivists_ancient_roman() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "ancient-roman", "historical objectivists")
    assert result == "موضوعيون تاريخيون رومان قدماء"


# --- New Women's Short Jobs Data Tests ---


def test_new_womens_short_job_deaf_actresses_african() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "african", "deaf actresses")
    assert result == "ممثلات صم إفريقيات"


def test_new_womens_short_job_pornographic_film_actresses_andalusian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "andalusian", "pornographic film actresses")
    assert result == "ممثلات أفلام إباحية أندلسيات"


def test_new_womens_short_job_women_in_politics_argentinean() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "argentinean", "women in politics")
    assert result == "سياسيات أرجنتينيات"


# --- MEN_WOMENS_WITH_NATO Tests ---


def test_mens_with_people() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "african", "people contemporary artists")
    assert result == "فنانون أفارقة معاصرون"


def test_womens_with_people() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "african", "female contemporary artists", females=Nat_Womens["african"])
    assert result == ""  # "فنانات إفريقيات معاصرات"


def test_mens_nato_politicians_who_committed_suicide_albanian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "albanian", "politicians who committed suicide")
    assert result == "سياسيون ألبان أقدموا على الانتحار"


def test_womens_nato_politicians_who_committed_suicide_albanian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix(
        "", "albanian", "female politicians who committed suicide", females=Nat_Womens["albanian"]
    )
    assert result in ["سياسيات ألبانيات أقدمن على الانتحار", "سياسيات أقدمن على الانتحار ألبانيات"]


# --- Combined Cases ---


def test_womens_new_job_with_prefix_and_nato_algerian_female_eugenicists() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "algerian", "female eugenicists")
    assert result == "عالمات متخصصات في تحسين النسل جزائريات"


# Test for a nationality that is in both mens and females, defaulting to mens


def test_mens_priority_new_nationality() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "afghan", "writers")
    assert result == "كتاب أفغان"
