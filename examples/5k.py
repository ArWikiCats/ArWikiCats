"""

"""
import sys
import json
import time
from tqdm import tqdm
from pathlib import Path


if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from src import print_memory, event_result

file_path = Path(Path(__file__).parent, "5k.json")

time_start = time.time()

data = json.load(open(file_path, "r", encoding="utf-8"))

result = event_result(tqdm(data))
labels = result.labels
no_labels = result.no_labels

print(f"total: {len(data)}")
print(f"labels: {len(labels)}")
print(f"no_labels: {len(no_labels)}")

time_diff = time.time() - time_start
print(f"total time: {time_diff} seconds")
print_memory()
