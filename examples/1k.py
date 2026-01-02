import json
import sys
from pathlib import Path

if _Dir := Path(__file__).parent:
    sys.path.append(str(_Dir))

from compare import compare_and_export_labels

file_path = Path(__file__).parent / "data/1k.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

compare_and_export_labels(data, "1k")
