"""

https://quarry.wmcloud.org/query/99983

"""

import json
from pathlib import Path

json_paths = Path("D:/categories_bot/make2_new/_work_files/genders_data").glob("*.json")
json_data = {}
for file in json_paths:
    data = json.loads(file.read_text(encoding="utf-8"))
    json_data.update({
        v["job_males"] : v["both_jobs"]
        for v in data.values()
    })


SAVE_PATH = Path("D:/categories_bot/make2_new/_work_files/move.wiki")
CATS_PATH = Path("D:/categories_bot/make2_new/examples/data/males.json")
CATS_DATA = json.loads(CATS_PATH.read_text(encoding="utf-8"))

rows = []
for n, cat in enumerate(CATS_DATA.values(), 1):
    cat_new = cat.replace(" ذكور ", " ")
    cat2 = cat.replace("تصنيف:", "").split("ذكور")[0].strip()
    cat_both = json_data.get(cat2)
    if cat_both:
        cat_both = cat_new.replace(cat2, cat_both)
        cat_both = f"[[:{cat_both}]]"
    line = f"| {n} | [[:{cat}]] | [[:{cat_new}]] | {cat_both} "
    rows.append(line)

wikitext = """
{|
|-
!#
| 1
| 2
| 3
|-
"""

wikitext += "\n|-\n".join(rows)

wikitext += """
|}
"""
with open(SAVE_PATH, "w", encoding="utf-8") as f:
    f.write(wikitext)
