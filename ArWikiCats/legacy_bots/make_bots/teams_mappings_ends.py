"""
Mappings for sports teams and organization suffixes.
This module provides Arabic translations for common English suffixes
related to sports clubs, competitions, and roles.
"""

teams_label_mappings_ends = {
    "champions": "أبطال",
    "clubs and teams": "أندية وفرق",
    "clubs": "أندية",
    "coaches": "مدربو",
    "competitions": "منافسات",
    "events": "أحداث",
    "films": "أفلام",
    "finals": "نهائيات",
    "home stadiums": "ملاعب",
    "leagues": "دوريات",
    "lists": "قوائم",
    "manager history": "تاريخ مدربو",
    "managers": "مدربو",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "organizations": "منظمات",
    "players": "لاعبو",
    "positions": "مراكز",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "results": "نتائج",
    "rivalries": "دربيات",
    "scouts": "كشافة",
    "squads": "تشكيلات",
    "statistics": "إحصائيات",
    "teams": "فرق",
    "cups": "كؤوس",
    "templates": "قوالب",
    "tournaments": "بطولات",
    "trainers": "مدربو",
    "umpires": "حكام",
    "venues": "ملاعب",
}

teams_label_mappings_ends = dict(
    sorted(
        teams_label_mappings_ends.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)
