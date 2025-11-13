from __future__ import annotations

import pytest
import src.main as main_module


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
