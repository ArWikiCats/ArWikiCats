"""
D:/categories_bot/make2_new/ArWikiCats/jsons/nationalities/All_Nat_o.json
{
    "zanzibari": {
        "male": "زنجباري",
        "males": "زنجباريون",
        "female": "زنجبارية",
        "females": "زنجباريات",
        "en": "zanzibar",
        "ar": "زنجبار"
    },
    "anguillan": {
        "male": "أنغويلاني",
        "males": "أنغويلانيون",
        "female": "أنغويلانية",
        "females": "أنغويلانيات",
        "en": "anguilla",
        "ar": "أنغويلا"
    },
    "afghan": {
        "male": "أفغاني",
        "males": "أفغان",
        "female": "أفغانية",
        "females": "أفغانيات",
        "en": "afghanistan",
        "ar": "أفغانستان"
    },
    "prussian": {
        "male": "بروسي",
        "males": "بروسيون",
        "female": "بروسية",
        "females": "بروسيات",
        "en": "prussia",
        "ar": "بروسيا"
    },

قراءة الملف
إضافة لكل مدخلة مفتاح جديد باسم
the_female

"female": "بروسية",
"the_female": "البروسية",

"female": "شمالية إفريقية",
"the_female": "الشمالية الإفريقية",


"female": "جنوبية إفريقية",
"the_female": "الجنوبية الإفريقية",
"""
import json
from pathlib import Path

# JSON_PATH = Path(r"d:/categories_bot/make2_new/ArWikiCats/jsons/nationalities/All_Nat_o.json")
JSON_PATH = Path(r"d:/categories_bot/make2_new/ArWikiCats/jsons/nationalities/sub_nats.json")


def add_definite_article(word: str) -> str:
    """Prefix Arabic definite article 'ال' to each space-separated token if missing.
    Examples:
      - "بروسية" -> "البروسية"
      - "شمالية إفريقية" -> "الشمالية الإفريقية"
      - "جنوبية إفريقية" -> "الجنوبية الإفريقية"
    """
    if not word:
        return word
    tokens = word.split()

    def add_al(token: str) -> str:
        # Skip if already definite
        if token.startswith("ال"):
            return token
        return "ال" + token

    return " ".join(add_al(t) for t in tokens)


def process_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for key, entry in data.items():
        if not isinstance(entry, dict):
            continue
        female = entry.get("female")
        if female:
            the_female = add_definite_article(female)
            if entry.get("the_female") != the_female:
                entry["the_female"] = the_female
                updated += 1
        # Also process male -> the_male
        male = entry.get("male")
        if male:
            the_male = add_definite_article(male)
            if entry.get("the_male") != the_male:
                entry["the_male"] = the_male
                updated += 1

    # Write back to the same file, preserving UTF-8
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Updated 'the_female'/'the_male' for {updated} entries. Saved to: {path}")


if __name__ == "__main__":
    process_file(JSON_PATH)
