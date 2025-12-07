
import json
import re
from pathlib import Path
from tqdm import tqdm

base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons'

wikidata_9fqzHy = Path("D:/categories_bot/langlinks/source/wikidata_9fqzHy.csv")
text = wikidata_9fqzHy.read_text(encoding="utf-8")
text = text.replace("Category:", "")

data1 = [x.strip() for x in text.splitlines()]

# data1 has 2,200,000 row
data_texts = "\n".join(data1)


def check_data(input_path: Path) -> str:
    """Read → classify → write outputs."""
    data = json.loads(input_path.read_text(encoding="utf-8"))
    # check each entry key if it exists in data_texts with rf"(?<!\w){re.escape(keyword)}(?!\w)"
    found = 0
    not_found = 0
    for key in tqdm(data.keys()):
        lowered = key.lower()
        if re.search(rf"(?<!\w){re.escape(lowered)}(?!\w)", data_texts.lower()):
            found += 1
        else:
            not_found += 1

    return f"Total: {len(data):,} | Found: {found:,} | Not Found: {not_found:,}"


def main() -> None:
    files = [
        jsons_dir / "cities/cities_full.json",
        jsons_dir / "cities/yy2.json",
    ]
    status = {}
    for file in files:
        print(f"Processing file: {file}")
        stat = check_data(file)
        status[file.name] = stat
    # ---
    for fname, stat in status.items():
        print(f"{fname} => {stat}")
    # ---
    print("Processing complete.")


if __name__ == "__main__":
    main()
