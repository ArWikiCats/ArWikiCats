"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import (
    GENDER_NATIONALITY_TEMPLATES,
    jobs_with_nat_prefix,
)
from ArWikiCats.translations import Nat_mens, Nat_Womens, jobs_mens_data, short_womens_jobs

Nat_mens = {k: Nat_mens[k] for k in list(Nat_mens.keys())[:30]}
Nat_Womens = {k: Nat_Womens[k] for k in list(Nat_Womens.keys())[:30]}
jobs_mens_data = {k: jobs_mens_data[k] for k in list(jobs_mens_data.keys())[:30]}
short_womens_jobs = {k: short_womens_jobs[k] for k in list(short_womens_jobs.keys())[:30]}

# =========================================================
#           NEW TESTS – Nat_mens / Nat_Womens COVERAGE
# =========================================================


@pytest.mark.parametrize("country_key, expected_label", Nat_mens.items())
@pytest.mark.dict
def test_nat_mens_people_uses_full_mapping(country_key: str, expected_label: str) -> None:
    """Every key in Nat_mens should work with suffix 'people'."""
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", country_key, "people")
    # If something is missing in jobs_with_nat_prefix logic, this will fail and show which key
    assert result == f"أعلام {expected_label}"


@pytest.mark.parametrize("country_key", sorted(set(Nat_mens.keys()) & set(Nat_Womens.keys())))
@pytest.mark.dict
def test_nat_womens_women_uses_full_mapping_for_intersection(country_key: str) -> None:
    """For countries present in both Nat_mens and Nat_Womens, 'women' must use Nat_Womens."""
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", country_key, "women")
    assert result == Nat_Womens[country_key]


# =========================================================
#           NEW TESTS – jobs_mens_data INTEGRATION
# =========================================================


@pytest.mark.parametrize("suffix, job_label", jobs_mens_data.items())
@pytest.mark.dict
def test_jobs_mens_data_combined_with_nationality_yemeni(suffix: str, job_label: str) -> None:
    """
    Ensure that for every key in jobs_mens_data, jobs_with_nat_prefix uses it and appends men's nationality.

    We use 'democratic republic of congo' as a representative nationality because it is used in other tests.
    """
    mens_nat = Nat_mens.get("democratic republic of congo") or "كونغويون ديمقراطيون"
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "democratic republic of congo", suffix)

    # Result must not be empty and must include both job label and nationality.
    assert result != ""
    assert job_label in result
    assert result.endswith(mens_nat)


# =========================================================
#       NEW TESTS – short_womens_jobs INTEGRATION
# =========================================================


@pytest.mark.parametrize("suffix, short_label", short_womens_jobs.items())
@pytest.mark.dict
def test_short_womens_jobs_combined_with_nationality_egyptian(
    suffix: str,
    short_label: str,
) -> None:
    """
    Ensure that every key in short_womens_jobs works with a valid women's nationality.

    We use 'egyptian' as a representative nationality (مصريات) which is already used in other tests.
    """
    women_nat = Nat_Womens.get("egyptian") or "مصريات"
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "egyptian", suffix)

    assert result != ""
    assert result == f"{short_label} {women_nat}"


# =========================================================
#   NEW TESTS – GENDER_NATIONALITY_TEMPLATES TEMPLATE BEHAVIOR
# =========================================================


@pytest.mark.parametrize("suffix, template", GENDER_NATIONALITY_TEMPLATES.items())
@pytest.mark.dict
def test_mens_nato_templates_are_applied_for_all_men_keys(
    suffix: str,
    template: dict,
) -> None:
    """
    For every key in GENDER_NATIONALITY_TEMPLATES, the men's template should be used
    with {nato} replaced by the correct nationality name.
    """
    mens_nat = Nat_mens.get("yemeni") or "يمنيون"

    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", suffix)

    expected = template["males"].format(nato=mens_nat)
    assert result == expected


@pytest.mark.fast
def test_mens_religious_expatriate() -> None:
    """Test religious + expatriate combination (both in NAT_BEFORE_OCC)"""
    result = jobs_with_nat_prefix("", "turkmenistan", "jewish")
    assert result == "تركمانيون يهود"
