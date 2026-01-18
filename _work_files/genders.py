"""
D:/categories_bot/make2_new/ArWikiCats/jsons/nationalities/nationalities_data.json

قراءة الملف
إضافة لكل مدخلة مفتاح جديد باسم

"""

import json
from pathlib import Path


def save_file(data, file_path):
    # sort keys
    data = dict(sorted(data.items()))
    with open(Path(__file__).parent / f"genders_data/{file_path}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


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

print(f">>> new_data: {len(new_data)=}")
save_file(new_data, "jobs_data_multi_one_word")

keys_in_both_2_words = [x for x in keys_in_both if len(mens_data.get(x).split(" ")) == 2]
print(f"Keys in both mens and womens data (two words): {len(keys_in_both_2_words)}")

new_data2 = {}
new_data3 = {}

for key in keys_in_both_2_words:
    try:
        word1_mens, word2_mens = mens_data[key].split(" ")
        word1_womens, word2_womens = womens_data[key].split(" ")
    except ValueError:
        print(f"ValueError for key: {key} with mens_data: {mens_data[key]} and womens_data: {womens_data[key]}")
        continue

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

print(f">>> new_data2: {len(new_data2)=}")
print(f">>> new_data3: {len(new_data3)=}")

save_file(new_data2, "jobs_data_multi_two_words_same")
save_file(new_data3, "jobs_data_multi_two_words_not_same")

keys_in_both_more_2_words = [x for x in keys_in_both if len(mens_data.get(x).split(" ")) > 2]
print(f"Keys in both mens and womens data (more than two words): {len(keys_in_both_more_2_words)}")

new_data4 = {}
new_data5 = {}

for key in keys_in_both_more_2_words:
    word1_mens, word2_mens = mens_data[key].split(" ", maxsplit=1)
    word1_womens, word2_womens = womens_data[key].split(" ", maxsplit=1)

    if word2_mens == word2_womens:
        new_data4[key] = {
            "job_males": mens_data[key],
            "job_females": womens_data[key],
            "both_jobs": f"{word1_mens} و{word1_womens} {word2_mens}",
        }
    else:
        new_data5[key] = {
            "job_males": mens_data[key],
            "job_females": womens_data[key],
            "both_jobs": f"{word1_mens} و{word1_womens} {word2_mens}",
        }


print(f">>> new_data4: {len(new_data4)=}")
print(f">>> new_data5: {len(new_data5)=}")

save_file(new_data4, "jobs_data_multi_more_than_two_words_same")
save_file(new_data5, "jobs_data_multi_more_than_two_words_not_same")

len_all_dumps = len(new_data2) + len(new_data3) + len(new_data4) + len(new_data5)
print(f"Total entries in all dumps: {len_all_dumps}")
