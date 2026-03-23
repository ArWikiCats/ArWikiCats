"""

https://quarry.wmcloud.org/query/99983

"""

import json
from pathlib import Path
import re

json_paths = Path("D:/categories_bot/make2_new/_work_files/genders_data").glob("*.json")
json_data = {}
for file in json_paths:
    data = json.loads(file.read_text(encoding="utf-8"))
    json_data.update({
        v["job_males"] : v["both_jobs"]
        for v in data.values()
    })


CATS_PATH = Path("D:/categories_bot/make2_new/examples/data/males.json")
CATS_DATA = json.loads(CATS_PATH.read_text(encoding="utf-8"))

CATS_DATA_SORTED_BY_VALUE = dict(sorted(CATS_DATA.items(), key=lambda x: x[1]))

full_data = {}

rows = []
for n, cat in enumerate(CATS_DATA_SORTED_BY_VALUE.values(), 1):
    cat_new = re.sub(r"\s*ذكور\s*", " ", cat)
    cat2 = cat.replace("تصنيف:", "").split("ذكور")[0].strip()
    cat_both = json_data.get(cat2, "")
    if not cat_both:
        continue

    cat_both = cat_new.replace(cat2, cat_both)

    full_data[cat] = {
        "cat": cat,
        "cat_new": cat_new,
        "cat_both": cat_both
    }

    cat_both = f"[[:{cat_both}]]"
    line = f"! {n}\n| [[:{cat}]]\n| [[:{cat_new}]]\n| {cat_both} "
    rows.append(line)

# for each 1000 item save into file
LIMIT = 1500
for i in range(0, len(rows), LIMIT):
    new_rows = rows[i:i+LIMIT]
    wikitext = """{| class="wikitable sortable" \n|- \n!# \n! 1 \n! 2 \n! 3 \n|-\n"""

    wikitext += "\n|-\n".join(new_rows)

    wikitext += """\n|}"""
    file_number = i // LIMIT + 1
    SAVE_PATH = Path(f"D:/categories_bot/make2_new/_work_files/move_{file_number}.wiki")
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        f.write(wikitext)

full_data_path = Path("D:/categories_bot/make2_new/examples/data/full_data.json")
with open(full_data_path, "w", encoding="utf-8") as f:
    json.dump(full_data, f, ensure_ascii=False, indent=4)
