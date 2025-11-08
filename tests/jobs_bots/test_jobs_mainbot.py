from __future__ import annotations

import pytest

from src.make2_bots.jobs_bots import jobs_mainbot, priffix_bot


@pytest.fixture(autouse=True)
def reset_caches() -> None:
    jobs_mainbot.JOBS_CACHE.clear()
    priffix_bot.PRIFFIX_MEN_CACHE.clear()
    priffix_bot.PRIFFIX_WOMEN_CACHE.clear()
    yield
    jobs_mainbot.JOBS_CACHE.clear()
    priffix_bot.PRIFFIX_MEN_CACHE.clear()
    priffix_bot.PRIFFIX_WOMEN_CACHE.clear()


@pytest.fixture(autouse=True)
def silence_logs(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(jobs_mainbot, "log_debug", lambda *args, **kwargs: None)
    monkeypatch.setattr(priffix_bot, "log_debug", lambda *args, **kwargs: None)


def test_jobs_secondary_returns_expected_label() -> None:
    label = jobs_mainbot.jobs_secondary("category", "zanzibari", "bahá'ís christians")
    assert label == "مسيحيون بهائيون زنجباريون"


def test_jobs_returns_primary_mens_label() -> None:
    label = jobs_mainbot.jobs("category", "zanzibari", "bahá'ís christians")
    assert label == "مسيحيون بهائيون زنجباريون"


def test_jobs_returns_womens_label_when_needed() -> None:
    label = jobs_mainbot.jobs("category", "zanzibari", "actresses")
    assert label == "ممثلات زنجباريات"


def test_jobs_respects_gender_overrides() -> None:
    label = jobs_mainbot.jobs(
        "category",
        "unknown",
        "actresses",
        overrides={"womens": "مخصصات"},
    )
    assert label == "ممثلات مخصصات"


def test_jobs_uses_mens_override() -> None:
    label = jobs_mainbot.jobs(
        "category",
        "zanzibari",
        "bahá'ís christians",
        overrides={"mens": "مخصص"},
    )
    assert label == "مسيحيون بهائيون مخصص"


def test_jobs_caches_results(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[tuple[str, ...], dict[str, object]]] = []

    def fake_resolve(*args: object, **kwargs: object) -> str:
        calls.append((args, kwargs))
        return "label"

    monkeypatch.setattr(jobs_mainbot, "_resolve_job_label", fake_resolve)

    first = jobs_mainbot.jobs("category", "country", "key")
    second = jobs_mainbot.jobs("category", "country", "key")

    assert first == "label"
    assert second == "label"
    assert len(calls) == 1
