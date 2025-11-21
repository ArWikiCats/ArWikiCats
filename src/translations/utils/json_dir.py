#!/usr/bin/python3
"""
!
"""

import json
from pathlib import Path
from typing import Any

Dir2 = Path(__file__).parent.parent


def _build_json_path(relative_path: str) -> Path:
    """Return the full path to a JSON file under ``jsons``.

    The helper accepts either bare filenames (``"example"``) or paths that
    include nested folders (``"geography/us_counties"``).  When the provided
    path does not include an extension, ``.json`` is appended automatically.
    """

    path = Path(relative_path)
    if path.suffix != ".json":
        path = path.with_suffix(".json")
    return Dir2 / "jsons" / path


def open_json_file(file: str = "") -> dict[str, Any] | list[Any]:
    """Open a JSON resource from the bundled ``jsons`` directory by name."""
    if not file:
        return {}
    file_path = _build_json_path(file)
    if not file_path.exists():
        print(f"file {file_path} not found")
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file_path.name}")
    return {}


def open_json(file_path: str = "") -> dict[str, Any] | list[Any]:
    """Open a JSON file given a relative path under the ``jsons`` directory."""
    if not file_path:
        return {}
    file_path = _build_json_path(file_path)
    if not file_path.exists():
        print(f"file {file_path} not found")
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file_path.name}")
    return {}
