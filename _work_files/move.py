"""

https://quarry.wmcloud.org/query/99983

"""

import json
from pathlib import Path

SAVE_PATH = Path("D:/categories_bot/make2_new/_work_files/move.wiki")
CATS_PATH = Path("D:/categories_bot/make2_new/examples/data/males.json")
CATS_DATA = json.loads(CATS_PATH.read_text(encoding="utf-8"))

rows = []
for n, cat in enumerate(CATS_DATA.values(), 1):
    cat_new = cat.replace(" ذكور ", " ")
    line = f"| {n} | [[:{cat}]] | [[:{cat_new}]]"
    rows.append(line)

wikitext = """
{|
|-
!#
| من
| إلى
|-
"""

wikitext += "\n|-\n".join(rows)

wikitext += """
|}
"""
with open(SAVE_PATH, "w", encoding="utf-8") as f:
    f.write(wikitext)
