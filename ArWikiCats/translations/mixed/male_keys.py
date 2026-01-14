"""Mappings for gender specific mixed keys."""

from ...helps import len_print

POP3_KEYS: dict[str, dict[str, str]] = {
    "educational": {"male": "تعليمي", "female": "تعليمية"},
    "masonic": {"male": "ماسوني", "female": "ماسونية"},
    "office": {"male": "إداري", "female": "إدارية"},
    "religious": {"male": "ديني", "female": "دينية"},
    "residential": {"male": "سكني", "female": "سكنية"},
    "agricultural": {"male": "زراعي", "female": "زراعية"},
    "air defence": {"male": "دفاع جوي", "female": "دفاع جوية"},
    "anarchism": {"male": "لاسلطوي", "female": "لاسلطوية"},
    "anarchist": {"male": "لاسلطوي", "female": "لاسلطوية"},
    "anti-revisionist": {"male": "مناهض للتحريف", "female": "مناهضة للتحريفية"},
    "arts": {"male": "فني", "female": "فنية"},
    "astronomical": {"male": "فلكي", "female": "فلكية"},
    "chemical": {"male": "كيميائي", "female": "كيميائية"},
    "christian": {"male": "مسيحي", "female": "مسيحية"},
    "commercial": {"male": "تجاري", "female": "تجارية"},
    "constitutional": {"male": "دستوري", "female": "دستورية"},
    "consultative": {"male": "إستشاري", "female": "إستشارية"},
    "cultural": {"male": "ثقافي", "female": "ثقافية"},
    "defense": {"male": "دفاعي", "female": "دفاعية"},
    "economic": {"male": "اقتصادي", "female": "اقتصادية"},
    "environmental": {"male": "بيئي", "female": "بيئية"},
    "fraternal": {"male": "أخوي", "female": "أخوية"},
    "government": {"male": "حكومي", "female": "حكومية"},
    "industrial": {"male": "صناعي", "female": "صناعية"},
    "legal": {"male": "قانوني", "female": "قانونية"},
    "legislative": {"male": "تشريعي", "female": "تشريعية"},
    "logistics": {"male": "لوجستي", "female": "لوجستية"},
    "maritime": {"male": "بحري", "female": "بحرية"},
    "medical and health": {"male": "طبي وصحي", "female": "طبية وصحية"},
    "medical": {"male": "طبي", "female": "طبية"},
    "military": {"male": "عسكري", "female": "عسكرية"},
    "naval": {"male": "عسكرية بحري", "female": "عسكرية بحرية"},
    "paramilitary": {"male": "شبه عسكري", "female": "شبه عسكرية"},
    "political": {"male": "سياسي", "female": "سياسية"},
    "realist": {"male": "واقعي", "female": "واقعية"},
    "research": {"male": "بحثي", "female": "بحثية"},
    "strategy": {"male": "استراتيجي", "female": "استراتيجية"},
    "student": {"male": "طلابي", "female": "طلابية"},
    "training": {"male": "تدريبي", "female": "تدريبية"},
    "warfare": {"male": "حربي", "female": "حربية"},
    "youth": {"male": "شبابي", "female": "شبابية"},
}

MALE_SUFFIXES: dict[str, str] = {
    "riots": "شغب",
    "food": "طعام",
    "impact": "أثر",
    "broadcasting": "بث لاسلكي",
    "science": "علم",
    "medicine": "طب",
    "outbreaks": "تفشي",
    "exchange": "تبادل",
    "repression": "قمع",
    "orientation": "توجه",
    "fiction": "خيال",
    "union": "اتحاد",
    "violence": "عنف",
}


def build_male_keys() -> dict[str, str]:
    """Return the expanded mapping used for male-labelled categories."""

    data = {}

    for base, labels in POP3_KEYS.items():
        lowered = base.lower()
        if labels.get("male"):
            for suffix, suffix_label in MALE_SUFFIXES.items():
                data[f"{lowered} {suffix}"] = f"{suffix_label} {labels.get('male')}"

    return data


New_male_keys: dict[str, str] = build_male_keys()

__all__ = [
    "New_male_keys",
]

len_print.data_len(
    "male_keys.py",
    {
        "New_male_keys": New_male_keys,
    },
)
