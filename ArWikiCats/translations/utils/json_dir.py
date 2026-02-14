#!/usr/bin/python3
"""JSON file loading utilities for translation data.

This module provides cached JSON file loading functions for the translation
dictionaries used throughout ArWikiCats.
"""

import functools
import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

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

    Args:
        file_path: Relative path to the JSON file (with or without .json extension).

    Returns:
        The parsed JSON data, or empty dict if the file cannot be loaded.
    """
    if not file_path:
        return {}
    file_path_path = _build_json_path(file_path)
    if not file_path_path.exists():
        logger.warning(f"JSON file not found: {file_path_path}")
        return {}
    try:
        with open(file_path_path, "r", encoding="utf-8") as f:
            return json.load(f)  # type: ignore[no-any-return]
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Failed to load JSON from {file_path_path}: {e}")
        return {}
