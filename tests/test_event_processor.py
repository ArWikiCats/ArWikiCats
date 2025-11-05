from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECT_PARENT = REPO_ROOT.parent
for candidate in (PROJECT_PARENT, REPO_ROOT):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.append(candidate_str)

import make2_new.src.main as main_module
from src.src.event_processing import get_shared_event_cache


@pytest.fixture(autouse=True)
def clear_event_cache():
    cache = get_shared_event_cache()
    cache.clear()
    yield
    cache.clear()


def test_event_with_maketab(monkeypatch, tmp_path):
    monkeypatch.setattr(main_module, "Dir_ma", tmp_path)

    categories = ["Category:Japan Golf Tour golfers"]
    result = main_module.event(categories, maketab=True)

    key = "Category:Japan Golf Tour golfers"
    assert key in result

    table_entry = result[key]
    assert table_entry["title"] == key
    assert table_entry["ar"]


def test_event_with_return_no_labs(monkeypatch, tmp_path):
    monkeypatch.setattr(main_module, "Dir_ma", tmp_path)

    category = "Category:Totally Nonexistent Category"
    labels, missing = main_module.event([category], return_no_labs=True)

    assert category not in labels
    assert category in missing


def test_event_with_printfirst_logs(monkeypatch, tmp_path):
    monkeypatch.setattr(main_module, "Dir_ma", tmp_path)

    categories = ["Category:Japan Golf Tour golfers"]
    main_module.event(categories, printfirst=True)

    logfile = tmp_path / "textfiles" / "make2-err.txt"
    assert logfile.exists()
    assert "Category:Japan Golf Tour golfers" in logfile.read_text(encoding="utf-8")
