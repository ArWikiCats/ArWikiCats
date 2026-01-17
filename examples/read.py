import json
from pathlib import Path

from tqdm import tqdm

dir = Path(__file__).parent

f_path = dir / "endings.json"

f_data = {}

json_files = list((dir / "big_data").glob("*.json"))
# json_files.extend(list((dir / "data").glob("*.json")))

for file in tqdm(json_files, desc="Processing JSON files"):
    with open(file, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    json_data_original = json_data.copy()
    for key, value in json_data.copy().items():
        if "endings" in key:
            f_data[key] = value
            del json_data[key]
    if json_data_original != json_data:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

if f_data:
    with open(f_path, "w", encoding="utf-8") as f:
        json.dump(f_data, f, ensure_ascii=False, indent=4)
