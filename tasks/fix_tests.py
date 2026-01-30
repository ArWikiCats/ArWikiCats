"""
search for any test file with: `from ArWikiCats import resolve_arabic_category_label`
replace it with `from ArWikiCats import resolve_label_ar`

and search for any item like this:
    "Category:20th century members of maine legislature": "تصنيف:أعضاء هيئة مين التشريعية في القرن 20",
replace it with:
    "20th century members of maine legislature": "أعضاء هيئة مين التشريعية في القرن 20",
"""

import re
from pathlib import Path

TASKS_DIR = Path(__file__).resolve().parent


def find_test_files(root_dir: Path) -> list[Path]:
    """Find all test files in the directory tree."""
    test_files = []
    for path in root_dir.rglob("*.py"):
        if path.name.startswith("test_") or path.stem.endswith("_test"):
            test_files.append(path)
    return test_files


def fix_imports(content: str) -> tuple[str, int]:
    """Replace old import and function name with new ones."""
    old_import = "from ArWikiCats import resolve_arabic_category_label"
    new_import = "from ArWikiCats import resolve_label_ar"

    new_content = content.replace(old_import, new_import)
    new_content = new_content.replace("resolve_arabic_category_label", "resolve_label_ar")

    count = (
        content.count(old_import)
        + content.count("resolve_arabic_category_label")
        - new_content.count("resolve_arabic_category_label")
    )
    return new_content, count


def fix_category_items(content: str) -> tuple[str, int]:
    """Replace Category: prefixed keys and تصنيف: prefixed values with non-prefixed versions."""
    pattern = r'"Category:([^"]+)":\s*"تصنيف:([^"]+)"'
    replacement = r'"\1": "\2"'

    new_content = re.sub(pattern, replacement, content, flags=re.I)
    count = len(re.findall(pattern, content, flags=re.I))
    return new_content, count


def process_file(file_path: Path) -> dict:
    """Process a single file and return statistics."""
    result = {"imports_fixed": 0, "categories_fixed": 0, "modified": False}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "from ArWikiCats import resolve_arabic_category_label" not in content:
            return result  # No changes needed

        # Fix imports
        content, imports_count = fix_imports(content)
        result["imports_fixed"] = imports_count

        # Fix category items
        content, categories_count = fix_category_items(content)
        result["categories_fixed"] = categories_count

        # Write back if modifications were made
        if imports_count > 0 and categories_count > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            result["modified"] = True

    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    """Main entry point."""
    root_dir = TASKS_DIR.parent
    test_files = find_test_files(root_dir)

    if not test_files:
        print("No test files found.")
        return

    print(f"Found {len(test_files)} test file(s):\n")

    total_imports = 0
    total_categories = 0
    modified_count = 0

    for file_path in test_files:
        rel_path = file_path.relative_to(root_dir)
        result = process_file(file_path)

        if "error" in result:
            print(f"  {rel_path}: ERROR - {result['error']}")
            continue

        if result["modified"]:
            modified_count += 1
            total_imports += result["imports_fixed"]
            total_categories += result["categories_fixed"]

            parts = []
            if result["imports_fixed"]:
                parts.append(f"{result['imports_fixed']} import(s)")
            if result["categories_fixed"]:
                parts.append(f"{result['categories_fixed']} categor(y/ies)")

            print(f"  {rel_path}: FIXED - {', '.join(parts)}")

    print("\nSummary:")
    print(f"  Files modified: {modified_count}/{len(test_files)}")
    print(f"  Total imports fixed: {total_imports}")
    print(f"  Total categories fixed: {total_categories}")


if __name__ == "__main__":
    main()
