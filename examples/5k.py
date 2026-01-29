import json
import sys
from pathlib import Path

if _Dir := Path(__file__).parent:
    sys.path.append(str(_Dir))

from compare import compare_and_export_labels

DATA_DIR = Path(__file__).parent / "data"

FILE_PATHS = sorted(DATA_DIR.glob("*.json"))

all_data = {}
for file_path in FILE_PATHS:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_data.update(data)

if len(all_data) > 5000:
    data_5k = {k: v for i, (k, v) in enumerate(all_data.items()) if i < 5000}
else:
    data_5k = all_data

compare_and_export_labels(data_5k, "5k")
