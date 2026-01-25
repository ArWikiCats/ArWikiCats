#!/usr/bin/python3
"""
!
"""

import functools
import json
from pathlib import Path
from typing import Any, Dict, List

Dir2 = Path(__file__).parent.parent.parent


def _build_json_path(relative_path: str) -> Path:
    """Return the full path to a JSON file under ``jsons``.

    The helper accepts either bare filenames (``"example"``) or paths that
    include nested folders (``"geography/us_counties"``). When the provided
    path does not include an extension, ``.json`` is appended automatically.
    """
    path = Path(relative_path)
    if path.suffix != ".json":
        path = path.with_suffix(".json")
    return Dir2 / "jsons" / path


@functools.lru_cache(maxsize=128)
def open_json_file(file_path: str = "") -> Dict[str, Any] | List[Any]:
    """Open a JSON resource from the bundled ``jsons`` directory by name.

    Results are cached to avoid repeated file I/O for the same file.
    """
    if not file_path:
        return {}
    file_path_path = _build_json_path(file_path)
    if not file_path_path.exists():
        print(f"file {file_path_path} not found")
        return {}
    try:
        with open(file_path_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file_path_path.name}")
    return {}
