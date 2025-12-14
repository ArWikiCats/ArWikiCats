"""

"""
import sys
import json
import time
from tqdm import tqdm
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats import print_memory, batch_resolve_labels

file_path = Path(__file__).parent / "2025-11-28.json"

time_start = time.time()

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

result = batch_resolve_labels(tqdm(list(data.keys())))
labels = result.labels

no_labels = {x: data.get(x) for x in result.no_labels}

print(f"total: {len(data)}")
print(f"labels: {len(labels)}")
print(f"no_labels: {len(no_labels)}")

time_diff = time.time() - time_start
print(f"total time: {time_diff} seconds")
print_memory()

same = 0
diff = {}

for key, value in labels.items():
    if value == data.get(key):
        same += 1
    else:
        diff[key] = {
            "old": data.get(key),
            "new": value
        }

print(f"{same=}, {len(diff)=}")

output_dir = Path(__file__).parent

with open(output_dir / "compare_diff.json", "w", encoding="utf-8") as f:
    json.dump(diff, f, ensure_ascii=False, indent=4)

with open(output_dir / "compare_no_labels.json", "w", encoding="utf-8") as f:
    json.dump(no_labels, f, ensure_ascii=False, indent=4)
