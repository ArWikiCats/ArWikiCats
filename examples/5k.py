"""

"""
import sys
import json
import time
from tqdm import tqdm
from pathlib import Path


if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from src import print_memory, batch_resolve_labels

file_path = Path(Path(__file__).parent, "5k.json")

time_start = time.time()

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

result = batch_resolve_labels(tqdm(data))
labels = result.labels
no_labels = result.no_labels

print(f"total: {len(data)}")
print(f"labels: {len(labels)}")
print(f"no_labels: {len(no_labels)}")

time_diff = time.time() - time_start
print(f"total time: {time_diff} seconds")
print_memory()
