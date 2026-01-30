import json
from collections import defaultdict
from pathlib import Path

import ahocorasick
from tqdm import tqdm

base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / "ArWikiCats" / "translations" / "jsons"


def fix_keys(text) -> str:
    return text.replace("sports-people", "sportspeople").replace("-", " ").replace("–", " ")


def load_data_texts() -> str:
    wikidata_9fqzHy = Path("D:/categories_bot/langlinks/source/wikidata_9fqzHy.csv")
    text = wikidata_9fqzHy.read_text(encoding="utf-8")
    text = text.replace("Category:", "")
    text = fix_keys(text)
    return text.lower()


def check_data_new(data: dict[str, str]) -> dict[str, int]:
    # data1 has 2,200,000 rows
    data_texts = load_data_texts().splitlines()
    A = ahocorasick.Automaton()
    for k in data:
        A.add_word(f" {k.lower()} ", k)
    A.make_automaton()

    keys_found = defaultdict(int)
    for line in tqdm(data_texts):
        for _end, key in A.iter(f" {line} "):
            if key in data:
                keys_found[key] += 1

    return keys_found


def main() -> None:
    files = [
        # jsons_dir / "cities/yy2.json",
        # jsons_dir / "cities/cities_full.json",
        # jsons_dir / "taxonomy/Taxons.json",
        # jsons_dir / "taxonomy/Taxons2.json",
        # Path("D:/categories_bot/len_data/jobs.py/singer_variants.json"),
        # Path("D:/categories_bot/len_data/jobs_singers.py/MEN_WOMENS_SINGERS.json"),
        # Path("D:/categories_bot/len_data/films_mslslat.py/Films_keys_both_new_female.json"),
        # Path("D:/categories_bot/len_data/films_mslslat.py/films_mslslat_tab.json"),
        # Path("D:/categories_bot/len_data/films_mslslat.py/Films_key_For_nat_extended.json"),
        # Path("D:/categories_bot/len_data/jobs.py/jobs_mens_data.json"),
        # Path("D:/categories_bot/len_data/jobs.py/film_variants.json"),
        # Path("D:/categories_bot/len_data/jobs.py/sport_variants.json"),
        # Path("D:/categories_bot/len_data/jobs.py/people_variants.json"),
        # Path("D:/categories_bot/len_data/jobs_players_list.py/SPORT_JOB_VARIANTS.json"),
        # Path("D:/categories_bot/len_data/bot_te_4_list.py/en_is_nat_ar_is_women.json"),
        # Path("D:/categories_bot/len_data/male_keys.py/New_male_keys.json"),
        # Path("D:/categories_bot/len_data/female_keys.py/films_data.json"),
        # Path("D:/categories_bot/len_data/female_keys.py/religious_entries.json"),
        # Path("D:/categories_bot/len_data/structures.py/structures_data.json"),
        # Path("D:/categories_bot/len_data/structures.py/pop_final_3_update.json"),
        # Path("D:/categories_bot/len_data/companies.py/companies_data.json"),
        # Path("D:/categories_bot/len_data/companies.py/companies_keys3.json"),
        # Path("D:/categories_bot/len_data/companies.py/typeTable_update.json"),
        # Path("D:/categories_bot/len_data/jobs.py/companies_to_jobs.json"),
        # Path("D:/categories_bot/len_data/bot_te_4_list.py/en_is_nat_ar_is_women.json"),
        Path("D:/categories_bot/len_data/films_mslslat.py/Films_key_CAO.json"),
    ]
    status = {}
    for file in files:
        print(f"Processing file: {file}")
        data = json.loads(file.read_text(encoding="utf-8"))
        fixed = {fix_keys(k): k for k in data.keys()}
        data = {fix_keys(k): v for k, v in data.items()}

        keys_found = check_data_new(data)
        keys_found = {fixed.get(x, x): v for x, v in keys_found.items()}
        status[file] = keys_found
    # ---
    for fname, keys_found in status.items():
        data = json.loads(fname.read_text(encoding="utf-8"))

        print(f"{fname} => ")
        not_found = {k: v for k, v in data.items() if k not in keys_found}
        print(f"Total: {len(data):,} | Found: {len(keys_found):,} | Not Found: {len(not_found):,}")
        # ---
        keys_found = dict(sorted(keys_found.items(), key=lambda item: item[1], reverse=True))

        for k, v in list(keys_found.items())[:25]:
            print(f"  {k}: {v}")
        print("...")
        # ---
        keys_found_dump = {x: data[x] for x, v in keys_found.items()}  # if v > 50}
        output_path = fname.parent / f"{fname.stem}_found.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(keys_found_dump, f, ensure_ascii=False, indent=4)
    # ---
    print("Processing complete.")


if __name__ == "__main__":
    main()
