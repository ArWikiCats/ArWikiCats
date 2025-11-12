"""Ensure the package-level exports remain stable for downstream imports."""

from __future__ import annotations

from src.ma_lists.jobs import (
    jobs_mens_data,
    Jobs_new,
    jobs_players_list,
    jobs_singers,
)
from src.ma_lists.jobs.Jobs import (
    jobs_mens_data as module_jobs_mens_data,
    Jobs_new as module_Jobs_new,
)


def test_package_exports_reference_underlying_modules() -> None:
    """Objects re-exported at the package level should match module contents."""

    assert jobs_mens_data is module_jobs_mens_data
    assert Jobs_new is module_Jobs_new


def test_jobs_submodules_are_accessible() -> None:
    """Consumers should still be able to reach refactored submodules."""

    assert hasattr(jobs_players_list, "PLAYERS_TO_MEN_WOMENS_JOBS")
    assert hasattr(jobs_singers, "MEN_WOMENS_SINGERS")
