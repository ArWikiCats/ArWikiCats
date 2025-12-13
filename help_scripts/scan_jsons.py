
import json
import ahocorasick
import re
from pathlib import Path
from tqdm import tqdm
from collections import defaultdict
base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons'


def load_data_texts() -> str:
    wikidata_9fqzHy = Path("D:/categories_bot/langlinks/source/wikidata_9fqzHy.csv")
    text = wikidata_9fqzHy.read_text(encoding="utf-8")
    text = text.replace("Category:", "")
    return text.lower()


def check_data_1(input_path: Path) -> str:
    """Read → classify → write outputs."""
    data_texts = load_data_texts()
    data = json.loads(input_path.read_text(encoding="utf-8"))

    keys_sorted = sorted(
        data.keys(),
        key=lambda k: (-k.count(" "), -len(k))
    )

    alternation = "|".join(map(re.escape, keys_sorted))

    re_compile = re.compile(rf"(?<!\w){alternation}(?!\w)")
    # check each entry key if it exists in data_texts with rf"(?<!\w){re.escape(keyword)}(?!\w)"
    # ---
    m = re_compile.finditer(data_texts)
    # ---
    keys_found = defaultdict(int)
    # ---
    for match in m:
        # ---
        value = match.group(1).strip().lower()
        # ---
        keys_found[value] += 1
    # ---
    not_found = {k: v for k, v in data.items() if k.lower() not in keys_found}
    # ---
    return f"Total: {len(data):,} | Found: {len(keys_found):,} | Not Found: {len(not_found):,}"


def check_data_new(data: dict[str, str]) -> dict[str, int]:
    # data1 has 2,200,000 rows
    data_texts = load_data_texts().splitlines()

    A = ahocorasick.Automaton()
    for k in data:
        A.add_word(f" {k.lower()} ", k)
    A.make_automaton()

    keys_found = defaultdict(int)
    for line in tqdm(data_texts):
        for end, key in A.iter(f" {line} "):
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
        Path("D:/categories_bot/len_data/jobs_singers.py/MEN_WOMENS_SINGERS.json"),
    ]
    status = {}
    for file in files:
        print(f"Processing file: {file}")
        data = json.loads(file.read_text(encoding="utf-8"))
        keys_found = check_data_new(data)
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
