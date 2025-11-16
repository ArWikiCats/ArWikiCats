"""Integration tests for the refactored jobs datasets."""

from __future__ import annotations

from src.translations.jobs.jobs_data import NAT_BEFORE_OCC, MEN_WOMENS_WITH_NATO
from src.translations.jobs.Jobs import (
    jobs_mens_data,
    Jobs_new,
)
from src.translations.jobs.Jobs2 import JOBS_2, JOBS_3333

def test_jobs_new_contains_female_and_general_entries() -> None:
    """Flattened mapping should expose lowercase keys for combined datasets."""

    assert "film actresses" in Jobs_new
    assert "footballers" in jobs_mens_data


def test_men_womens_with_nato_matches_source_template() -> None:
    """NATO-labelled entries should retain the placeholder for substitution."""

    assert MEN_WOMENS_WITH_NATO
    for labels in MEN_WOMENS_WITH_NATO.values():
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
