#!/usr/bin/python3
"""

from .json_dir import open_json_file# open_json_file(file="")

"""

from pathlib import Path
from typing import Any

import json

Dir2 = Path(__file__).parent.parent


def open_json_file(file: str="") -> dict[str, Any] | list[Any]:
    # ---
    if not file:
        return {}
    # ---
    file_path = Dir2 / f"jsons/{file}.json"
    # ---
    if not file_path.exists():
        print(f"file {file_path} not found")
        return {}
    # ---
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file_path.name}")
    # ---
    return {}


def open_json(file_path: str="") -> dict[str, Any] | list[Any]:
    # ---
    if not file_path:
        return {}
    # ---
    file_path = Dir2 / "jsons" / file_path
    # ---
    if not file_path.exists():
        print(f"file {file_path} not found")
        return {}
    # ---
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file_path.name}")
    # ---
    return {}
