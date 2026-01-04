"""
D:/categories_bot/make2_new/ArWikiCats/jsons/nationalities/All_Nat_o.json

قراءة الملف
إضافة لكل مدخلة مفتاح جديد باسم

"""
import json
from pathlib import Path

WOMENS_PATH = Path("D:/categories_bot/len_data/jobs.py/jobs_womens_data.json")
MRNS_PATH = Path("D:/categories_bot/len_data/jobs.py/jobs_mens_data.json")

mens_data = json.loads(MRNS_PATH.read_text(encoding="utf-8"))
womens_data = json.loads(WOMENS_PATH.read_text(encoding="utf-8"))

print(f"Mens data entries: {len(mens_data)}")
print(f"Womens data entries: {len(womens_data)}")

keys_in_both = set(mens_data.keys()).intersection(set(womens_data.keys()))
print(f"Keys in both mens and womens data: {len(keys_in_both)}")

mens_example = {
    "activists": "ناشطون",
    "actors": "ممثلون",
    "actuaries": "إكتواريون",
    "admirals": "أميرالات",
    "academics": "أكاديميون",
    "accountants": "محاسبون",
}

womens_example = {
    "activists": "ناشطات",
    "actors": "ممثلات",
    "actuaries": "إكتواريات",
    "admirals": "أميرالات إناث",
    "academics": "أكاديميات",
    "accountants": "محاسبات",
}

new_data = {
    "actors": {"job_males": "ممثلون", "job_females": "ممثلات", "both_jobs": "ممثلون وممثلات"},
}

keys_in_both_one_word = [x for x in keys_in_both if " " not in mens_data.get(x)]
print(f"Keys in both mens and womens data (one word): {len(keys_in_both_one_word)}")

for key in keys_in_both_one_word:
    new_data[key] = {
        "job_males": mens_data[key],
        "job_females": womens_data[key],
        "both_jobs": f"{mens_data[key]} و{womens_data[key]}",
    }

with open(Path(__file__).parent / "genders_data/jobs_data_multi_one_word.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

keys_in_both_2_words = [x for x in keys_in_both if len(mens_data.get(x).split(" ")) == 2]
print(f"Keys in both mens and womens data (two words): {len(keys_in_both_2_words)}")

new_data2 = {}
new_data3 = {}

for key in keys_in_both_2_words:
    print(key)
    word1_mens, word2_mens = mens_data[key].split(" ")
    word1_womens, word2_womens = womens_data[key].split(" ")

    if word2_mens == word2_womens:
        new_data2[key] = {
            "job_males": mens_data[key],
            "job_females": womens_data[key],
            "both_jobs": f"{word1_mens} و{word1_womens} {word2_mens}",
        }
    else:
        new_data3[key] = {
            "job_males": mens_data[key],
            "job_females": womens_data[key],
            "both_jobs": f"{word1_mens} و{word1_womens} {word2_mens}",
        }

with open(Path(__file__).parent / "genders_data/jobs_data_multi_two_words.json", "w", encoding="utf-8") as f:
    json.dump(new_data2, f, ensure_ascii=False, indent=4)

with open(Path(__file__).parent / "genders_data/jobs_data_multi_two_words3.json", "w", encoding="utf-8") as f:
    json.dump(new_data3, f, ensure_ascii=False, indent=4)
