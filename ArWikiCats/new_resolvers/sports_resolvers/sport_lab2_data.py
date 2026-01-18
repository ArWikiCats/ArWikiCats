#!/usr/bin/python3
"""
"""

# NOTE: used in countries_names_sport_multi_v2.py and nats_and_sports.py
labels_formatted_data = {
    "{en_sport}": "{sport_label}",
    "{en_sport} finals": "نهائيات {sport_label}",
    "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
    "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
    "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} champions": "أبطال {sport_label}",
    "olympics {en_sport}": "{sport_label} في الألعاب الأولمبية",
    "summer olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الصيفية",
    "winter olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الشتوية",
}


teams_formatted_data = {
    "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
    "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
    "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
    "{en_sport} world cup": "كأس العالم {sport_team}",
    "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
    "international {en_sport} council": "المجلس الدولي {sport_team}",
    "mens {en_sport} championship": "بطولة {sport_team} للرجال",
    "mens {en_sport} world championship": "بطولة العالم {sport_team} للرجال",
    "outdoor world {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "womens world {en_sport} championship": "بطولة العالم {sport_team} للسيدات",
    "womens {en_sport} championship": "بطولة {sport_team} للسيدات",
    "womens {en_sport} world championship": "بطولة العالم {sport_team} للسيدات",
    "world amateur {en_sport} championship": "بطولة العالم {sport_team} للهواة",
    "world champion national {en_sport} teams": "أبطال بطولة العالم {sport_team}",
    "world junior {en_sport} championship": "بطولة العالم {sport_team} للناشئين",
    "world outdoor {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "world wheelchair {en_sport} championship": "بطولة العالم {sport_team} على الكراسي المتحركة",
    "world {en_sport} amateur championship": "بطولة العالم {sport_team} للهواة",
    "world {en_sport} championship": "بطولة العالم {sport_team}",
    "world {en_sport} championship competitors": "منافسو بطولة العالم {sport_team}",
    "world {en_sport} championship medalists": "فائزون بميداليات بطولة العالم {sport_team}",
    "world {en_sport} junior championship": "بطولة العالم {sport_team} للناشئين",
    "world {en_sport} youth championship": "بطولة العالم {sport_team} للشباب",
    "world youth {en_sport} championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} amateur world championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} junior world championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world amateur championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} world championship": "بطولة العالم {sport_team}",
    "{en_sport} world junior championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world youth championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} youth world championship": "بطولة العالم {sport_team} للشباب",

    # world championships in athletics
    "world championship in {en_sport}": "بطولة العالم {sport_team}",
    "world championship in {en_sport} athletes": "عداؤو بطولة العالم {sport_team}",
}


__all__ = [
    "labels_formatted_data",
    "teams_formatted_data",
]
