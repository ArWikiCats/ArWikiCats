import json
from pathlib import Path

from tqdm import tqdm

Dir = Path(__file__).parent


json_files = list((Dir / "religions_data").glob("*.json"))
# read all json_files, make big data dict, split them between all files
all_data = {}

for json_file in tqdm(json_files, desc="Processing JSON files"):
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        all_data.update(json_data)

all_data = dict(sorted(all_data.items()))

# data_per_file = 1000
data_per_file = len(all_data) // len(json_files) + 1

print(f"data_per_file: {data_per_file}, total data: {len(all_data)}")

json_files.sort()

for i, json_file in enumerate(tqdm(json_files, desc="Writing split JSON files")):
    start_index = i * data_per_file
    end_index = start_index + data_per_file
    split_data = dict(list(all_data.items())[start_index:end_index])
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(split_data, f, ensure_ascii=False, indent=4)
