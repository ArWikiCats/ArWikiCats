"""Integration tests for the refactored jobs datasets."""

from __future__ import annotations

from src.ma_lists.jobs.jobs_data import NAT_BEFORE_OCC
from src.ma_lists.jobs.Jobs import (
    Female_Jobs,
    Jobs_key,
    Jobs_key_mens,
    Jobs_key_womens,
    Jobs_new,
    Men_Womens_Jobs,
    Men_Womens_with_nato,
    womens_Jobs_2017,
)
from src.ma_lists.jobs.Jobs2 import JOBS_2, JOBS_3333


def test_jobs_key_mens_syncs_with_gendered_dataset() -> None:
    """Every entry in ``Jobs_key_mens`` should exist in ``Men_Womens_Jobs``."""

    assert Jobs_key_mens  # sanity check that data is populated
    for key, mens_label in Jobs_key_mens.items():
        if key in Men_Womens_Jobs:
            assert Men_Womens_Jobs[key]["mens"] == mens_label
            continue
        # Legacy dataset exposes "men's footballers" via the generic football entry.
        assert key == "men's footballers"
        football_label = Men_Womens_Jobs["footballers"]["mens"]
        assert mens_label.startswith(football_label)


def test_womens_jobs_only_contains_entries_with_feminine_label() -> None:
    """``womens_Jobs_2017`` should mirror feminine labels from the master map."""

    assert womens_Jobs_2017
    for key, womens_label in womens_Jobs_2017.items():
        assert womens_label
        assert key in Men_Womens_Jobs
        assert Men_Womens_Jobs[key]["womens"] == womens_label


def test_female_jobs_include_film_and_sport_variants() -> None:
    """Female-specific roles should include derived movie and sport categories."""

    assert "sportswomen" in Female_Jobs
    assert "film actresses" in Female_Jobs
    assert Female_Jobs["sportswomen"] == "رياضيات"
    assert Female_Jobs["film actresses"].startswith("ممثلات")


def test_jobs_new_contains_female_and_general_entries() -> None:
    """Flattened mapping should expose lowercase keys for combined datasets."""

    assert "footballers" in Jobs_new
    assert "film actresses" in Jobs_new
    assert "footballers" in Jobs_key
    assert Jobs_new["footballers"] == Men_Womens_Jobs["footballers"]["mens"]
    assert Jobs_new["film actresses"] == Female_Jobs["film actresses"]


def test_jobs_key_womens_mirrors_female_jobs() -> None:
    """Female job lookups should align with the lower-case key mapping."""

    assert Jobs_key_womens
    for key, label in Jobs_key_womens.items():
        assert key in Female_Jobs
        assert Female_Jobs[key] == label


def test_men_womens_with_nato_matches_source_template() -> None:
    """NATO-labelled entries should retain the placeholder for substitution."""

    assert Men_Womens_with_nato
    for labels in Men_Womens_with_nato.values():
        assert "{nato}" in labels["mens"]
        assert "{nato}" in labels["womens"]


def test_nat_before_occ_includes_religious_expansions() -> None:
    """The nationality-before-occupation list should include religion keys."""

    assert "anglican" in NAT_BEFORE_OCC
    assert "anglicans" in NAT_BEFORE_OCC


def test_jobs2_contains_men_womens_jobs_entries() -> None:
    """``JOBS_2`` should extend the shared MEN_WOMENS_JOBS_2 configuration."""

    sample_keys = [
        "aerospace engineers",
        "archaeologists",
        "biblical scholars",
        "botanists",
        "chemists",
    ]
    for key in sample_keys:
        assert key in JOBS_2
        assert JOBS_2[key]["mens"]


def test_jobs2_aliases_are_consistent() -> None:
    """The two exported job datasets should expose distinct objects with data."""

    assert JOBS_2 is not JOBS_3333
    assert JOBS_2
    assert JOBS_3333
