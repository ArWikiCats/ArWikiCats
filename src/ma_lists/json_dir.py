#!/usr/bin/python3
"""

from .json_dir import open_json_file# open_json_file(file="")

"""

from pathlib import Path
import json

Dir2 = Path(__file__).parent


def open_json_file(file=""):
    # ---
    if not file:
        return False
    # ---
    file_path = Dir2 / f"jsons/{file}.json"
    # ---
    if not file_path.exists():
        print(f"file {file_path} not found")
        return False
    # ---
    try:
        with open(f"{Dir2}/jsons/{file}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except BaseException:
        print(f"cant open {file}.json")
    # ---
    return False
