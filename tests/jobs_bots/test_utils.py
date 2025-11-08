from __future__ import annotations

import pytest

from src.make2_bots.jobs_bots import utils


def test_normalize_cache_key_strips_and_lowercases() -> None:
    result = utils.normalize_cache_key("  Hello  ", None, "WORLD", 42)
    assert result == "hello, world, 42"


def test_cached_lookup_invokes_factory_once() -> None:
    cache: dict[str, str] = {}
    calls: list[None] = []

    def factory() -> str:
        calls.append(None)
        return "value"

    first = utils.cached_lookup(cache, ("foo",), factory)
    second = utils.cached_lookup(cache, ("foo",), factory)

    assert first == "value"
    assert second == "value"
    assert len(calls) == 1


def test_log_debug_emits_logging_and_output(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, tuple[object, ...]]] = []

    class DummyLogger:
        def debug(self, message: str, *args: object) -> None:
            calls.append((message, args))

    captured: list[str] = []

    monkeypatch.setattr(utils, "LOGGER", DummyLogger())
    monkeypatch.setattr(utils, "output_test4", captured.append)

    utils.log_debug("message %s", "value")

    assert calls == [("message %s", ("value",))]
    assert captured == ["message value"]


def test_log_debug_handles_output_errors(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    class DummyLogger:
        def debug(self, message: str, *args: object) -> None:
            calls.append(message % args if args else message)

    def failing_output(_: str) -> None:
        raise RuntimeError("boom")

    monkeypatch.setattr(utils, "LOGGER", DummyLogger())
    monkeypatch.setattr(utils, "output_test4", failing_output)

    utils.log_debug("fail %s", "case")

    assert calls[0] == "fail case"
    assert "output_test4 failed" in calls[1]
