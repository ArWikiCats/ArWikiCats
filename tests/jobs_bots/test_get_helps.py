from __future__ import annotations

import pytest

from src.make2_bots.jobs_bots import get_helps


@pytest.fixture(autouse=True)
def clear_country_cache() -> None:
    get_helps.GET_COUNTRY_CACHE.clear()
    yield
    get_helps.GET_COUNTRY_CACHE.clear()


@pytest.fixture(autouse=True)
def silence_logs(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(get_helps, "log_debug", lambda *args, **kwargs: None)


def test_match_prefix_matches_basic_prefix() -> None:
    suffix, key = get_helps._match_prefix("American poets", "American", category_type="nat")
    assert suffix == "poets"
    assert key == "American"


def test_match_prefix_handles_articles() -> None:
    suffix, key = get_helps._match_prefix("Bahamas explorers", "the Bahamas", category_type="")
    assert suffix == "explorers"
    assert key == "the Bahamas"


def test_match_prefix_returns_empty_on_mismatch() -> None:
    suffix, key = get_helps._match_prefix("Unknown", "American", category_type="")
    assert suffix == ""
    assert key == ""


def test_get_con_3_uses_cache(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def fake_match(category: str, key: str, *, category_type: str) -> tuple[str, str]:
        calls.append(key)
        if key == "beta":
            return "suffix", key
        return "", ""

    monkeypatch.setattr(get_helps, "_match_prefix", fake_match)

    first = get_helps.get_con_3("category", ["alpha", "beta"], "type")
    second = get_helps.get_con_3("category", ["alpha", "beta"], "type")

    assert first == ("suffix", "beta")
    assert second == ("suffix", "beta")
    assert calls == ["alpha", "beta"]
