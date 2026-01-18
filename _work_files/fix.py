"""
D:/categories_bot/len_data/nationality.py/all_country_ar.json
D:/categories_bot/make2_new/ArWikiCats/jsons/geography/popopo.json


كود بايثون لقراءة الملفين وازالة اي مدخلة موجودة في popopo اذا كانت موجودة في all_country_ar
"""

import json

with open("D:/categories_bot/len_data/nationality.py/all_country_ar.json", "r", encoding="utf-8") as f:
    all_country_ar = json.load(f)

with open("D:/categories_bot/make2_new/ArWikiCats/jsons/geography/popopo.json", "r", encoding="utf-8") as f:
    popopo = json.load(f)

deleted = 0
diff = 0

for key in list(popopo.keys()):
    if key in all_country_ar:
        if all_country_ar[key] != popopo[key]:
            diff += 1
            print(f"Different entry for key '{key}': all_country_ar='{all_country_ar[key]}', popopo='{popopo[key]}'")
        del popopo[key]
        deleted += 1

with open("D:/categories_bot/make2_new/ArWikiCats/jsons/geography/popopo.json", "w", encoding="utf-8") as f:
    json.dump(popopo, f, ensure_ascii=False, indent=4)

print(f"Total deleted entries: {deleted}")
print(f"Total different entries: {diff}")
