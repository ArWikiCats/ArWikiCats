"""Ensure the package-level exports remain stable for downstream imports."""

from __future__ import annotations

from src.ma_lists.jobs import (
    Jobs_key_mens,
    Jobs_new,
    Men_Womens_Jobs,
    jobs_players_list,
    jobs_singers,
)
from src.ma_lists.jobs.Jobs import (
    Jobs_key_mens as module_Jobs_key_mens,
    Jobs_new as module_Jobs_new,
    Men_Womens_Jobs as module_Men_Womens_Jobs,
)


def test_package_exports_reference_underlying_modules() -> None:
    """Objects re-exported at the package level should match module contents."""

    assert Men_Womens_Jobs is module_Men_Womens_Jobs
    assert Jobs_key_mens is module_Jobs_key_mens
    assert Jobs_new is module_Jobs_new


def test_jobs_submodules_are_accessible() -> None:
    """Consumers should still be able to reach refactored submodules."""

    assert hasattr(jobs_players_list, "PLAYERS_TO_MEN_WOMENS_JOBS")
    assert hasattr(jobs_singers, "MEN_WOMENS_SINGERS")
