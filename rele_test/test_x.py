"""
python D:/categories_bot/make2_new/rele_test/test_x.py
"""

from tqdm import tqdm
from pathlib import Path
import sys
import json

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats import resolve_arabic_category_label
from ArWikiCats.make_bots.jobs_bots.relegin_jobs import (
    get_suffix_prefix,
    try_relegins_jobs_with_suffix,
)

file_path = Path("D:/categories_bot/langlinks/source/RELIGIOUS_CATEGORIES.csv")
data = {}
data_labels = {}
with file_path.open("r", encoding="utf-8") as f:
    lines = f.readlines()

with_category_suffix = 0
with_country_prefix = 0
no_labels={}
for line in tqdm(lines):
    line = line.replace("Category:", "").strip()
    category_suffix, country_prefix = get_suffix_prefix(line)

    with_country_prefix += bool(country_prefix)
    with_category_suffix += bool(category_suffix)

    if category_suffix and country_prefix:
        data[line] = [category_suffix, country_prefix]

    label = try_relegins_jobs_with_suffix(line)
    if label:
        data_labels[line] = label
    else:
        no_labels[line] = resolve_arabic_category_label(line)

save_path = Path(__file__).parent / "data.json"
with open(save_path, "w", encoding="utf-8") as f:
    json.dump(data_labels, f, ensure_ascii=False, indent=4)

save_path = Path(__file__).parent / "no_labels.json"
with open(save_path, "w", encoding="utf-8") as f:
    json.dump(no_labels, f, ensure_ascii=False, indent=4)

print(f"{with_country_prefix=:,}, {with_category_suffix=:,}, ")

print(f"{len(data_labels)=:,}, ")
print(f"{len(no_labels)=:,}, ")
