#!/usr/bin/env python3
"""
Script to replace logging functions across the codebase.
Replaces:
- print_put -> logger.info
- print_def_head -> logger.info
"""

import os
import re
from pathlib import Path


def replace_logging_functions(file_path):
    """Replace logging functions in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace import statements
    content = re.sub(
        r'from (\.+)helps\.print_bot import print_put',
        r'from \1helps.log import logger',
        content
    )
    content = re.sub(
        r'from (\.+)helps\.print_bot import print_def_head',
        r'from \1helps.log import logger',
        content
    )
    # Replace function calls
    content = re.sub(r'\bprint_put\(', 'logger.info(', content)
    content = re.sub(r'\bprint_def_head\(', 'logger.info(', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    """Main function to process all Python files."""
    base_path = Path(r'd:\categories_bot\make2_new\src\make2_bots')

    modified_files = []

    for py_file in base_path.rglob('*.py'):
        try:
            if replace_logging_functions(py_file):
                modified_files.append(str(py_file))
                print(f"Modified: {py_file}")
        except Exception as e:
            print(f"Error processing {py_file}: {e}")

    print(f"\n\nTotal files modified: {len(modified_files)}")
    for f in modified_files:
        print(f"  - {f}")


if __name__ == '__main__':
    main()
