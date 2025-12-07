
import json
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

    data1 = [x.strip() for x in text.splitlines()]

    # data1 has 2,200,000 row
    data_texts = "\n".join(data1)
    return data_texts

def check_data_new(input_path: Path) -> str:
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
    m = re_compile.finditer(data_texts.lower())
    # ---
    result = defaultdict(int)
    # ---
    for match in m:
        # ---
        value = match.group(1).strip().lower()
        # ---
        result[value] = result.get(value, 0) + 1
    # ---
    not_found = {k: v for k, v in data.items() if k.lower() not in result}
    # ---
    return f"Total: {len(data):,} | Found: {len(result):,} | Not Found: {len(not_found):,}"


def main() -> None:
    files = [
        jsons_dir / "cities/yy2.json",
        jsons_dir / "cities/cities_full.json",
    ]
    status = {}
    for file in files:
        print(f"Processing file: {file}")
        stat = check_data_new(file)
        status[file.name] = stat
    # ---
    for fname, stat in status.items():
        print(f"{fname} => {stat}")
    # ---
    print("Processing complete.")


if __name__ == "__main__":
    main()
