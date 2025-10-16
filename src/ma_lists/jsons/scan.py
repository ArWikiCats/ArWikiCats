# -*- coding: utf-8 -*-
"""

python3 core8/pwb.py make/jsons/scan

write python code to do:
# scan all json files in correct folder
# output error message when found bad json format or an error
"""

import os
import json
from pathlib import Path
from colorama import Fore, Style


Dir = Path(__file__).parent


def scan_json_files(folder_path):
    """Scans all JSON files in a folder and reports errors.

    Args:
      folder_path: The path to the folder containing JSON files.

    Returns:
      None
    """
    errors = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Open the file and load JSON data
                with open(file_path, "r") as f:
                    json.load(f)
                print(f"Successfully parsed {filename}")
            except (json.JSONDecodeError, FileNotFoundError) as e:
                # Handle different error types with specific messages
                if isinstance(e, json.JSONDecodeError):
                    error_msg = f"Error parsing JSON in {filename}: {str(e)}"
                else:
                    error_msg = f"File not found: {filename}"
                print(error_msg)
                errors.append(file_path)

            except Exception as e:
                error_msg = f"Unexpected error in {filename}: {str(e)}"
                errors.append(file_path)
    # ---
    for file in errors:
        # print error message
        # print(f"Error: {file}")
        print(f"{Fore.RED}Error: {file}{Style.RESET_ALL}")


scan_json_files(Dir)
