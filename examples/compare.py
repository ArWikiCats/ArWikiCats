""" """

import json
import sys
import time
from pathlib import Path

from tqdm import tqdm

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(Path(__file__).parent))
    sys.path.append(str(_Dir))

from ArWikiCats import batch_resolve_labels, print_memory


def compare_and_export_labels(data, name, remove_ar_prefix=False):
    time_start = time.perf_counter()

    result = batch_resolve_labels(tqdm(list(data.keys())))
    labels = result.labels

    no_labels = {x: data.get(x) for x in result.no_labels}

    print(f"total: {len(data)}")
    print(f"labels: {len(labels)}")
    print(f"no_labels: {len(no_labels)}")

    time_diff = time.perf_counter() - time_start
    print(f"total time: {time_diff} seconds")
    print_memory()

    same = {}
    diff = {
        "old": {},
        "new": {},
    }
    for key, value in labels.items():
        value = value.replace("تصنيف:", "") if remove_ar_prefix else value
        data_value = data.get(key, "").replace("تصنيف:", "") if remove_ar_prefix else data.get(key, "")

        if value == data_value:
            same[key] = value
        else:
            diff["new"][key] = value
            diff["old"][key] = data_value

    print(f"same: {len(same)}, diff: {len(diff['old'])}")

    output_dir = Path(__file__).parent
    if diff["new"]:
        with open(output_dir / f"{name}_diff.json", "w", encoding="utf-8") as f:
            json.dump(diff, f, ensure_ascii=False, indent=4)

    if no_labels:
        with open(output_dir / f"{name}_no_labels.json", "w", encoding="utf-8") as f:
            json.dump(no_labels, f, ensure_ascii=False, indent=4)

    if diff["new"] or no_labels:
        with open(output_dir / f"{name}_same.json", "w", encoding="utf-8") as f:
            json.dump(same, f, ensure_ascii=False, indent=4)
