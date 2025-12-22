"""

"""
import sys
import json
import time
from tqdm import tqdm
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(Path(__file__).parent))
    sys.path.append(str(_Dir))

from ArWikiCats import print_memory, batch_resolve_labels


def compare_and_export_labels(data, name):
    time_start = time.time()

    result = batch_resolve_labels(tqdm(list(data.keys())))
    labels = result.labels

    no_labels = {x: data.get(x) for x in result.no_labels}

    print(f"total: {len(data)}")
    print(f"labels: {len(labels)}")
    print(f"no_labels: {len(no_labels)}")

    time_diff = time.time() - time_start
    print(f"total time: {time_diff} seconds")
    print_memory()

    same = {}
    diff = {
        "old": {},
        "new": {},
    }
    for key, value in labels.items():
        if value == data.get(key):
            same[key] = value
        else:
            diff["new"][key] = value
            diff["old"][key] = data.get(key)

    print(f"{len(same)=}, {len(diff['old'])=}")

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
