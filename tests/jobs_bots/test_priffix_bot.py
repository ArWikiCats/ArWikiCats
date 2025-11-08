from __future__ import annotations

import pytest

from src.make2_bots.jobs_bots import priffix_bot


@pytest.fixture(autouse=True)
def clear_caches() -> None:
    priffix_bot.PRIFFIX_MEN_CACHE.clear()
    priffix_bot.PRIFFIX_WOMEN_CACHE.clear()
    yield
    priffix_bot.PRIFFIX_MEN_CACHE.clear()
    priffix_bot.PRIFFIX_WOMEN_CACHE.clear()


@pytest.fixture(autouse=True)
def silence_logs(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(priffix_bot, "log_debug", lambda *args, **kwargs: None)


def test_strip_people_suffix_preserves_known_nationality() -> None:
    assert priffix_bot._strip_people_suffix("zanzibari people") == "zanzibari"


def test_strip_people_suffix_returns_trimmed_value() -> None:
    assert priffix_bot._strip_people_suffix("mystery people") == "mystery people"


def test_match_prefix_with_table_formats_label() -> None:
    label = priffix_bot._match_prefix_with_table("amputee bahá'ís christians")
    assert label == "مسيحيون بهائيون مبتورو أحد الأطراف"


def test_match_suffix_formats_label() -> None:
    label = priffix_bot._match_suffix("bahá'ís male deaf")
    assert label == "بهائيون صم ذكور"


def test_resolve_mens_prefix_uses_direct_match() -> None:
    assert priffix_bot._resolve_mens_prefix("bahá'ís christians") == "مسيحيون بهائيون"


def test_resolve_womens_prefix_uses_direct_match() -> None:
    assert priffix_bot._resolve_womens_prefix("actresses") == "ممثلات"


def test_priffix_mens_work_caches_results(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def fake_resolve(value: str) -> str:
        calls.append(value)
        return "label"

    monkeypatch.setattr(priffix_bot, "_resolve_mens_prefix", fake_resolve)

    first = priffix_bot.priffix_Mens_work("example")
    second = priffix_bot.priffix_Mens_work("example")

    assert first == "label"
    assert second == "label"
    assert calls == ["example"]


def test_priffix_womens_work_caches_results(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def fake_resolve(value: str) -> str:
        calls.append(value)
        return "label"

    monkeypatch.setattr(priffix_bot, "_resolve_womens_prefix", fake_resolve)

    first = priffix_bot.Women_s_priffix_work("example")
    second = priffix_bot.Women_s_priffix_work("example")

    assert first == "label"
    assert second == "label"
    assert calls == ["example"]
