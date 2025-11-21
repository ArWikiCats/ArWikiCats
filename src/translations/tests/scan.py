# -*- coding: utf-8 -*-
"""

python3 core8/pwb.py make/jsons/scan

write python code to do:
# scan all json files in correct folder
# output error message when found bad json format or an error
"""

import os
from pathlib import Path

from colorama import Fore, Style

from ..utils.json_dir import open_json_file

Dir = Path(__file__).parent / "jsons"


def scan_json_files(folder_path: os.PathLike[str] | str) -> None:
    """Scans all JSON files in a folder and reports errors.

    Args:
      folder_path: The path to the folder containing JSON files.

    Returns:
      None
    """
    errors = []
    folder = Path(folder_path)
    for filename in os.listdir(folder):
        if not filename.endswith(".json"):
            continue
        file_path = folder / filename
        if file_path.is_dir():
            continue
        try:
            result = open_json_file(file_path.stem)
            if result is False:
                print(f"Failed to parse {filename}")
                errors.append(str(file_path))
            else:
                print(f"Successfully parsed {filename}")
        except Exception as e:
            print(f"Unexpected error in {filename}: {str(e)}")
            errors.append(str(file_path))
    for file in errors:
        # print error message
        # print(f"Error: {file}")
        print(f"{Fore.RED}Error: {file}{Style.RESET_ALL}")


scan_json_files(Dir)
