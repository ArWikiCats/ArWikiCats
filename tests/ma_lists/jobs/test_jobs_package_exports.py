"""Ensure the package-level exports remain stable for downstream imports."""

from __future__ import annotations

from src.ma_lists.jobs import (
    Female_Jobs,
    Jobs_key,
    Jobs_key_mens,
    Jobs_key_womens,
    Jobs_new,
    Men_Womens_Jobs,
    Men_Womens_with_nato,
    Nat_Before_Occ,
    jobs_defs,
    jobs_players_list,
    jobs_singers,
)
from src.ma_lists.jobs.Jobs import (
    Female_Jobs as module_Female_Jobs,
    Jobs_key as module_Jobs_key,
    Jobs_key_mens as module_Jobs_key_mens,
    Jobs_key_womens as module_Jobs_key_womens,
    Jobs_new as module_Jobs_new,
    Men_Womens_Jobs as module_Men_Womens_Jobs,
    Men_Womens_with_nato as module_Men_Womens_with_nato,
    Nat_Before_Occ as module_Nat_Before_Occ,
)


def test_package_exports_reference_underlying_modules() -> None:
    """Objects re-exported at the package level should match module contents."""

    assert Men_Womens_Jobs is module_Men_Womens_Jobs
    assert Female_Jobs is module_Female_Jobs
    assert Jobs_key is module_Jobs_key
    assert Jobs_key_mens is module_Jobs_key_mens
    assert Jobs_key_womens is module_Jobs_key_womens
    assert Jobs_new is module_Jobs_new
    assert Men_Womens_with_nato is module_Men_Womens_with_nato
    assert Nat_Before_Occ is module_Nat_Before_Occ


def test_jobs_submodules_are_accessible() -> None:
    """Consumers should still be able to reach refactored submodules."""

    assert hasattr(jobs_defs, "gendered_label")
    assert hasattr(jobs_players_list, "PLAYERS_TO_MEN_WOMENS_JOBS")
    assert hasattr(jobs_singers, "MEN_WOMENS_SINGERS")
