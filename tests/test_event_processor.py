from __future__ import annotations

import pytest
import src.main as main_module


def test_event_with_return_no_labs(monkeypatch, tmp_path):
    # monkeypatch.setattr(main_module, "Dir_ma", tmp_path)

    category = "Category:Totally Nonexistent Category"
    labels, missing = main_module.event([category], return_no_labs=True)

    assert category not in labels
    assert category in missing
