#
import json
from pathlib import Path
from typing import Callable


diff_data_path = Path(__file__).parent / "diff_data"
diff_data_path.mkdir(exist_ok=True, parents=True)


def dump_one(data: dict, file_name: str, folder: Path = diff_data_path) -> None:
    file_path = folder / f"{file_name}.json"

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing diff data: {e}")


def dump_diff(data: dict, file_name: str, _sort: bool = True) -> None:
    if not data:
        return

    if _sort:
        data_sorted = {x: v for x, v in data.items() if v}
        data_sorted.update({y: z for y, z in data.items() if not z})
    else:
        data_sorted = data

    dump_one(data_sorted, file_name)


def dump_diff_text(expected: dict, diff_result: dict, file_name: str) -> None:
    """
    Dump diff data as text file for easy copy-paste to wiki.

    #  dump_diff_text(expected, diff_result, name)
    """
    if not expected or not diff_result:
        return

    save3 = [
        f"# {{{{وب:طنت/سطر|{v}|{diff_result[x]}|سبب النقل=تصحيح ArWikiCats}}}}"
        for x, v in expected.items()
        if v and diff_result.get(x)
    ]

    if not save3:
        return

    diff_data_path = Path(__file__).parent / "diff_data"
    diff_data_path.mkdir(exist_ok=True, parents=True)
    file_path = diff_data_path / f"{file_name}_wiki.json"

    text = "\n".join(save3)
    text = text.replace("تصنيف:", "")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error writing diff data: {e}")


def one_dump_test(dataset: dict, callback: Callable[[str], str], do_strip=False) -> tuple[dict, dict]:
    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = dict(dataset.items())  # if v
    for cat, ar in data.items():
        result = callback(cat)
        # ---
        if do_strip:
            result = result.strip() if isinstance(result, str) else result
            ar = ar.strip() if isinstance(ar, str) else ar
        # ---
        if result != ar:
            org[cat] = ar
            diff[cat] = result

    return org, diff


def one_dump_test_no_labels(dataset: dict, callback: Callable[[str], str], do_strip=False) -> tuple[dict, dict]:
    print(f"len of dataset: {len(dataset)}, callback: {callback.__name__}")
    org = {}
    diff = {}
    data = dict(dataset.items())  # if v
    no_labels = []
    for cat, ar in data.items():
        result = callback(cat)
        # ---
        if do_strip:
            result = result.strip() if isinstance(result, str) else result
            ar = ar.strip() if isinstance(ar, str) else ar
        # ---
        if not result:
            no_labels.append(cat)
        elif result != ar:
            org[cat] = ar
            diff[cat] = result
    return org, diff, no_labels


def dump_one_new(data: dict, folder_name: str, file_name: str) -> None:
    if not data:
        return

    folder_path = diff_data_path / folder_name
    folder_path.mkdir(exist_ok=True, parents=True)
    file_path = folder_path / f"{file_name}.json"

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing diff data: {e}")


def dump_same_and_not_same(data: dict, diff_result: dict, name: str, just_dump: bool = False) -> None:
    """
    Dump same data as JSON file for easy copy-paste to wiki.

    dump_same_add(data, diff_result, name)
    """
    if not data or not diff_result:
        return

    same_data = {x: v for x, v in data.items() if x not in diff_result}
    if len(same_data) != len(data) or just_dump:
        dump_one_new(same_data, name, "same")

    add_data = {x: v for x, v in data.items() if x in diff_result}
    if len(add_data) != len(data) or just_dump:
        dump_one_new(add_data, name, "not_same")
