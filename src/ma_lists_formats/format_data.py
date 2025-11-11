#!/usr/bin/python3
"""

"""
import functools
import re
from typing import Dict, Optional
from ..helps.log import logger


class FormatData:
    def __init__(
        self,
        formated_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = "xoxo",
        value_placeholder: str = "xoxo",
    ):
        # Store originals
        self.formated_data = formated_data
        self.data_list = data_list

        # Case-insensitive mirrors
        self.formated_data_ci: Dict[str, str] = {k.lower(): v for k, v in formated_data.items()}
        self.data_list_ci: Dict[str, str] = {k.lower(): v for k, v in data_list.items()}

        self.value_placeholder = value_placeholder
        self.key_placeholder = key_placeholder
        self.pattern = self.keys_to_pattern()

    @functools.lru_cache(maxsize=None)
    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """Build a case-insensitive regex over lowercased keys of data_list."""
        if not self.data_list_ci:
            return None
        keys_sorted = sorted(self.data_list_ci.keys(), key=lambda x: -x.count(" "))
        data_pattern = r"\b(" + "|".join(map(re.escape, keys_sorted)) + r")\b"
        return re.compile(data_pattern, re.I)

    @functools.lru_cache(maxsize=None)
    def match_key(self, category: str) -> str:
        """Return canonical lowercased key from data_list if found; else empty."""
        if not self.pattern:
            return ""
        match = self.pattern.search(f" {category} ")
        return match.group(1).lower() if match else ""

    @functools.lru_cache(maxsize=None)
    def apply_pattern_replacement(self, template_label: str, sport_label: str) -> str:
        """Replace value placeholder once template is chosen."""
        final_label = template_label.replace(self.value_placeholder, sport_label)

        if self.value_placeholder not in final_label:
            return final_label

        return ""

    @functools.lru_cache(maxsize=None)
    def normalize_category(self, category: str, sport_key: str) -> str:
        """Replace the matched sport key with the key placeholder."""
        normalized = re.sub(
            f" {re.escape(sport_key)} ",
            f" {self.key_placeholder} ",
            f" {category.strip()} ",
            flags=re.IGNORECASE,
        )
        return normalized.strip()

    def get_template_label(self, sport_key: str, category: str) -> str:
        """Lookup template in a case-insensitive dict."""
        normalized = self.normalize_category(category, sport_key)
        logger.debug(f"normalized: {normalized}")
        # Case-insensitive key lookup
        return self.formated_data_ci.get(normalized.lower(), "")

    @functools.lru_cache(maxsize=None)
    def search(self, category: str) -> str:
        """End-to-end resolution."""
        sport_key = self.match_key(category)
        if not sport_key:
            logger.debug(f'No sport key matched for category: "{category}"')
            return ""
        sport_label = self.data_list_ci.get(sport_key)
        if not sport_label:
            logger.debug(f'No sport label matched for sport key: "{sport_key}"')
            return ""
        template_label = self.get_template_label(sport_key, category)
        if not template_label:
            logger.debug(
                f'No template label matched for sport key: "{sport_key}" and category: "{category}"'
            )
            return ""
        return self.apply_pattern_replacement(template_label, sport_label)


def format_data_sample():
    """
    This function demonstrates how to use the FormatData class to format and transform data.
    It creates a mapping of template patterns to their localized versions and applies them.
    """
    # Define a dictionary of formatted patterns with placeholders
    formated_data = {
        "{sport}": "{sport_label}",
        "{sport} managers": "مدراء {sport_label}",
        "{sport} coaches": "مدربو {sport_label}",
        "{sport} people": "أعلام {sport_label}",
        "{sport} playerss": "لاعبو {sport_label}",
        "{sport} players": "لاعبو {sport_label}",
        "men's {sport} matches": "مباريات {sport_label} رجالية",
        "men's {sport} navigational boxes": "صناديق تصفح {sport_label} رجالية",
        "men's {sport} lists": "قوائم {sport_label} رجالية",
        "men's {sport} home stadiums": "ملاعب {sport_label} رجالية",
        "men's {sport} templates": "قوالب {sport_label} رجالية",
        "men's {sport} rivalries": "دربيات {sport_label} رجالية",
        "men's {sport} champions": "أبطال {sport_label} رجالية",
        "men's {sport} competitions": "منافسات {sport_label} رجالية",
        "men's {sport} statistics": "إحصائيات {sport_label} رجالية",
        "men's {sport} records": "سجلات {sport_label} رجالية",
        "men's {sport} records and statistics": "سجلات وإحصائيات {sport_label} رجالية",
        "men's {sport} manager history": "تاريخ مدربو {sport_label} رجالية",
        "men's {sport} receivers": "مستقبلو {sport_label} رجالية",
        "men's {sport} wide receivers": "مستقبلون واسعون {sport_label} رجالية",
        "men's {sport} tackles": "مصطدمو {sport_label} رجالية",
        "men's {sport} utility players": "لاعبو مراكز متعددة {sport_label} رجالية",
        "men's {sport} peoplee": "أعلام {sport_label} رجالية",
        "men's {sport} sprtspeople": "رياضيو {sport_label} رجالية",
        "men's {sport} sportspeople": "رياضيو {sport_label} رجالية",
        "men's {sport} directors": "مدراء {sport_label} رجالية",
        "men's {sport} journalists": "صحفيو {sport_label} رجالية",
        "men's {sport} halfbacks": "أظهرة مساعدون {sport_label} رجالية",
        "men's {sport} quarterbacks": "أظهرة رباعيون {sport_label} رجالية",
        "men's {sport} centers": "لاعبو وسط {sport_label} رجالية",
        "men's {sport} centres": "لاعبو وسط {sport_label} رجالية",
        "men's {sport} midfielders": "لاعبو وسط {sport_label} رجالية",
        "men's {sport} placekickers": "مسددو {sport_label} رجالية",
        "men's {sport} kickers": "راكلو {sport_label} رجالية",
        "men's {sport} drop kickers": "مسددو ركلات {sport_label} رجالية",
        "men's {sport} defenders": "مدافعو {sport_label} رجالية",
        "men's {sport} central defenders": "قلوب دفاع {sport_label} رجالية",
        "men's {sport} forwards": "مهاجمو {sport_label} رجالية",
        "men's {sport} inside forwards": "مهاجمون داخليون {sport_label} رجالية",
        "men's {sport} outside forwards": "مهاجمون خارجيون {sport_label} رجالية",
        "men's {sport} small forwards": "مهاجمون صغيرو الجسم {sport_label} رجالية",
        "men's {sport} power forwards": "مهاجمون أقوياء الجسم {sport_label} رجالية",
        "men's {sport} fullbacks": "مدافعو {sport_label} رجالية",
        "men's {sport} defensive backs": "مدافعون خلفيون {sport_label} رجالية",
        "men's {sport} running backs": "راكضون للخلف {sport_label} رجالية",
        "men's {sport} linebackers": "أظهرة {sport_label} رجالية",
        "men's {sport} goalkeepers": "حراس مرمى {sport_label} رجالية",
        "men's {sport} goaltenders": "حراس مرمى {sport_label} رجالية",
        "men's {sport} guards": "حراس {sport_label} رجالية",
        "men's {sport} shooting guards": "مدافعون مسددون {sport_label} رجالية",
        "men's {sport} point guards": "لاعبو هجوم خلفي {sport_label} رجالية",
        "men's {sport} offensive linemen": "مهاجمو خط {sport_label} رجالية",
        "men's {sport} defensive linemen": "مدافعو خط {sport_label} رجالية",
        "men's {sport} left wingers": "أجنحة يسار {sport_label} رجالية",
        "men's {sport} right wingers": "أجنحة يمين {sport_label} رجالية",
        "men's {sport} defencemen": "مدافعو {sport_label} رجالية",
        "men's {sport} wingers": "أجنحة {sport_label} رجالية",
        "men's {sport} wing halves": "أنصاف أجنحة {sport_label} رجالية",
        "men's {sport} referees": "حكام {sport_label} رجالية",
        "women's {sport}": "{sport_label} نسائية",
        "women's {sport} squads": "تشكيلات {sport_label} نسائية",
        "women's {sport} finals": "نهائيات {sport_label} نسائية",
        "women's {sport} positions": "مراكز {sport_label} نسائية",
        "women's {sport} tournaments": "بطولات {sport_label} نسائية",
        "women's {sport} films": "أفلام {sport_label} نسائية",
        "women's {sport} teams": "فرق {sport_label} نسائية",
        "women's {sport} venues": "ملاعب {sport_label} نسائية",
        "women's {sport} clubs": "أندية {sport_label} نسائية",
        "women's {sport} organizations": "منظمات {sport_label} نسائية",
        "women's {sport} non-profit organizations": "منظمات غير ربحية {sport_label} نسائية",
        "women's {sport} non-profit publishers": "ناشرون غير ربحيون {sport_label} نسائية",
        "women's {sport} organisations": "منظمات {sport_label} نسائية",
        "women's {sport} events": "أحداث {sport_label} نسائية",
        "women's {sport} umpires": "حكمات {sport_label} نسائية",
        "women's {sport} trainers": "مدربات {sport_label} نسائية",
        "women's {sport} scouts": "كشافة {sport_label} نسائية",
        "women's {sport} coaches": "مدربات {sport_label} نسائية",
        "women's {sport} leagues": "دوريات {sport_label} نسائية",
        "women's {sport} managers": "مديرات {sport_label} نسائية",
        "women's {sport} guards": "حراس {sport_label} نسائية",
        "women's {sport} shooting guards": "مدافعات مسددات {sport_label} نسائية",
        "women's {sport} point guards": "لاعبات هجوم خلفي {sport_label} نسائية",
        "women's {sport} offensive linemen": "مهاجمات خط {sport_label} نسائية",
        "women's {sport} defensive linemen": "مدافعات خط {sport_label} نسائية",
        "women's {sport} left wingers": "جناحات يسار {sport_label} نسائية",
        "women's {sport} right wingers": "جناحات يمين {sport_label} نسائية",
        "women's {sport} defencemen": "مدافعات {sport_label} نسائية",
        "women's {sport} wingers": "جناحات {sport_label} نسائية",
        "women's {sport} wing halves": "جناحات نصفيات {sport_label} نسائية",
        "women's {sport} referees": "حكمات {sport_label} نسائية",
        "youth {sport}": "{sport_label} شبابية",
        "youth {sport} squads": "تشكيلات {sport_label} شبابية",
        "youth {sport} finals": "نهائيات {sport_label} شبابية",
        "youth {sport} positions": "مراكز {sport_label} شبابية",
        "youth {sport} tournaments": "بطولات {sport_label} شبابية",
        "youth {sport} films": "أفلام {sport_label} شبابية",
        "youth {sport} teams": "فرق {sport_label} شبابية",
        "youth {sport} competitions": "منافسات {sport_label} شبابية",
        "youth {sport} statistics": "إحصائيات {sport_label} شبابية",
        "youth {sport} records": "سجلات {sport_label} شبابية",
        "youth {sport} records and statistics": "سجلات وإحصائيات {sport_label} شبابية",
        "youth {sport} manager history": "تاريخ مدربو {sport_label} شبابية",
        "youth {sport} receivers": "مستقبلو {sport_label} شبابية",
        "youth {sport} wide receivers": "مستقبلون واسعون {sport_label} شبابية",
        "youth {sport} tackles": "مصطدمو {sport_label} شبابية",
        "youth {sport} utility players": "لاعبو مراكز متعددة {sport_label} شبابية",
        "youth {sport} peoplee": "أعلام {sport_label} شبابية",
        "youth {sport} sprtspeople": "رياضيو {sport_label} شبابية",
        "youth {sport} sportspeople": "رياضيو {sport_label} شبابية",
        "youth {sport} directors": "مدراء {sport_label} شبابية",
        "youth {sport} journalists": "صحفيو {sport_label} شبابية",
        "youth {sport} halfbacks": "أظهرة مساعدون {sport_label} شبابية",
        "youth {sport} quarterbacks": "أظهرة رباعيون {sport_label} شبابية",
        "youth {sport} centers": "لاعبو وسط {sport_label} شبابية",
        "youth {sport} centres": "لاعبو وسط {sport_label} شبابية",
        "youth {sport} midfielders": "لاعبو وسط {sport_label} شبابية",
        "youth {sport} placekickers": "مسددو {sport_label} شبابية",
        "youth {sport} kickers": "راكلو {sport_label} شبابية",
        "youth {sport} drop kickers": "مسددو ركلات {sport_label} شبابية",
        "youth {sport} defenders": "مدافعو {sport_label} شبابية",
        "youth {sport} central defenders": "قلوب دفاع {sport_label} شبابية",
        "men's youth {sport} players": "لاعبو {sport_label} للشباب",
        "men's youth {sport} results": "نتائج {sport_label} للشباب",
        "men's youth {sport} matches": "مباريات {sport_label} للشباب",
        "men's youth {sport} navigational boxes": "صناديق تصفح {sport_label} للشباب",
        "men's youth {sport} lists": "قوائم {sport_label} للشباب",
        "men's youth {sport} home stadiums": "ملاعب {sport_label} للشباب",
        "men's youth {sport} templates": "قوالب {sport_label} للشباب",
        "men's youth {sport} rivalries": "دربيات {sport_label} للشباب",
        "men's youth {sport} champions": "أبطال {sport_label} للشباب",
        "men's youth {sport} competitions": "منافسات {sport_label} للشباب",
        "men's youth {sport} statistics": "إحصائيات {sport_label} للشباب",
        "men's youth {sport} records": "سجلات {sport_label} للشباب",
        "men's youth {sport} records and statistics": "سجلات وإحصائيات {sport_label} للشباب",
        "men's youth {sport} manager history": "تاريخ مدربو {sport_label} للشباب",
        "men's youth {sport} receivers": "مستقبلو {sport_label} للشباب",
        "men's youth {sport} wide receivers": "مستقبلون واسعون {sport_label} للشباب",
        "men's youth {sport} tackles": "مصطدمو {sport_label} للشباب",
        "men's youth {sport} utility players": "لاعبو مراكز متعددة {sport_label} للشباب",
        "men's youth {sport} peoplee": "أعلام {sport_label} للشباب",
        "men's youth {sport} sprtspeople": "رياضيو {sport_label} للشباب",
        "men's youth {sport} sportspeople": "رياضيو {sport_label} للشباب",
        "men's youth {sport} directors": "مدراء {sport_label} للشباب",
        "men's youth {sport} journalists": "صحفيو {sport_label} للشباب",
        "men's youth {sport} halfbacks": "أظهرة مساعدون {sport_label} للشباب",
        "men's youth {sport} quarterbacks": "أظهرة رباعيون {sport_label} للشباب",
        "men's youth {sport} centers": "لاعبو وسط {sport_label} للشباب",
        "men's youth {sport} centres": "لاعبو وسط {sport_label} للشباب",
        "men's youth {sport} midfielders": "لاعبو وسط {sport_label} للشباب",
        "men's youth {sport} placekickers": "مسددو {sport_label} للشباب",
        "men's youth {sport} kickers": "راكلو {sport_label} للشباب",
        "men's youth {sport} drop kickers": "مسددو ركلات {sport_label} للشباب",
        "men's youth {sport} defenders": "مدافعو {sport_label} للشباب",
        "men's youth {sport} central defenders": "قلوب دفاع {sport_label} للشباب",
        "men's youth {sport} forwards": "مهاجمو {sport_label} للشباب",
        "men's youth {sport} inside forwards": "مهاجمون داخليون {sport_label} للشباب",
        "men's youth {sport} outside forwards": "مهاجمون خارجيون {sport_label} للشباب",
        "women's youth {sport} templates": "قوالب {sport_label} للشابات",
        "women's youth {sport} rivalries": "دربيات {sport_label} للشابات",
        "women's youth {sport} champions": "أبطال {sport_label} للشابات",
        "women's youth {sport} competitions": "منافسات {sport_label} للشابات",
        "women's youth {sport} statistics": "إحصائيات {sport_label} للشابات",
        "women's youth {sport} records": "سجلات {sport_label} للشابات",
        "women's youth {sport} records and statistics": "سجلات وإحصائيات {sport_label} للشابات",
        "women's youth {sport} manager history": "تاريخ مدربو {sport_label} للشابات",
        "women's youth {sport} receivers": "مستقبلات {sport_label} للشابات",
        "women's youth {sport} wide receivers": "مستقبلات واسعات {sport_label} للشابات",
        "women's youth {sport} tackles": "مصطدمات {sport_label} للشابات",
        "women's youth {sport} utility players": "لاعبات مراكز متعددة {sport_label} للشابات",
        "women's youth {sport} peoplee": "أعلام {sport_label} للشابات",
        "women's youth {sport} sprtspeople": "رياضيات {sport_label} للشابات",
        "women's youth {sport} sportspeople": "رياضيات {sport_label} للشابات",
        "women's youth {sport} directors": "مديرات {sport_label} للشابات",
        "women's youth {sport} journalists": "صحفيات {sport_label} للشابات",
        "women's youth {sport} halfbacks": "ظهيرات مساعدات {sport_label} للشابات",
        "women's youth {sport} quarterbacks": "ظهيرات رباعيات {sport_label} للشابات",
        "women's youth {sport} centers": "لاعبات وسط {sport_label} للشابات",
        "women's youth {sport} centres": "لاعبات وسط {sport_label} للشابات",
        "women's youth {sport} midfielders": "لاعبات وسط {sport_label} للشابات",
        "women's youth {sport} placekickers": "مسددات {sport_label} للشابات",
        "women's youth {sport} kickers": "راكلات {sport_label} للشابات",
        "women's youth {sport} drop kickers": "مسددات ركلات {sport_label} للشابات",
        "women's youth {sport} defenders": "مدافعات {sport_label} للشابات",
        "women's youth {sport} central defenders": "مدافعات مركزيات {sport_label} للشابات",
        "women's youth {sport} forwards": "مهاجمات {sport_label} للشابات",
        "women's youth {sport} inside forwards": "مهاجمات داخليات {sport_label} للشابات",
        "women's youth {sport} outside forwards": "مهاجمات خارجيات {sport_label} للشابات",
        "women's youth {sport} small forwards": "مهاجمات صغيرات الجسم {sport_label} للشابات",
        "women's youth {sport} power forwards": "مهاجمات قويات الجسم {sport_label} للشابات",
        "women's youth {sport} fullbacks": "مدافعات {sport_label} للشابات",
        "women's youth {sport} defensive backs": "مدافعات خلفيات {sport_label} للشابات",
        "women's youth {sport} running backs": "راكضات للخلف {sport_label} للشابات",
        "women's youth {sport} linebackers": "ظهيرات {sport_label} للشابات",
        "women's youth {sport} goalkeepers": "حارسات مرمى {sport_label} للشابات",
        "women's youth {sport} goaltenders": "حارسات مرمى {sport_label} للشابات",
        "women's youth {sport} guards": "حراس {sport_label} للشابات",
        "women's youth {sport} shooting guards": "مدافعات مسددات {sport_label} للشابات",
        "women's youth {sport} point guards": "لاعبات هجوم خلفي {sport_label} للشابات",
        "women's youth {sport} offensive linemen": "مهاجمات خط {sport_label} للشابات",
        "women's youth {sport} defensive linemen": "مدافعات خط {sport_label} للشابات",
        "women's youth {sport} left wingers": "جناحات يسار {sport_label} للشابات",
        "women's youth {sport} right wingers": "جناحات يمين {sport_label} للشابات",
        "women's youth {sport} defencemen": "مدافعات {sport_label} للشابات",
        "women's youth {sport} wingers": "جناحات {sport_label} للشابات",
        "women's youth {sport} wing halves": "جناحات نصفيات {sport_label} للشابات",
        "women's youth {sport} referees": "حكمات {sport_label} للشابات",
        "amateur {sport}": "{sport_label} للهواة",
        "amateur {sport} squads": "تشكيلات {sport_label} للهواة",
        "amateur {sport} finals": "نهائيات {sport_label} للهواة",
        "amateur {sport} positions": "مراكز {sport_label} للهواة",
        "amateur {sport} tournaments": "بطولات {sport_label} للهواة",
        "amateur {sport} films": "أفلام {sport_label} للهواة",
        "amateur {sport} teams": "فرق {sport_label} للهواة",
        "amateur {sport} venues": "ملاعب {sport_label} للهواة",
        "amateur {sport} clubs": "أندية {sport_label} للهواة",
        "amateur {sport} organizations": "منظمات {sport_label} للهواة",
        "amateur {sport} non-profit organizations": "منظمات غير ربحية {sport_label} للهواة",
        "amateur {sport} non-profit publishers": "ناشرون غير ربحيون {sport_label} للهواة",
        "amateur {sport} organisations": "منظمات {sport_label} للهواة",
        "amateur {sport} events": "أحداث {sport_label} للهواة",
        "amateur {sport} umpires": "حكام {sport_label} للهواة",
        "amateur {sport} trainers": "مدربو {sport_label} للهواة",
        "amateur {sport} scouts": "كشافة {sport_label} للهواة",
        "amateur {sport} coaches": "مدربو {sport_label} للهواة",
        "amateur {sport} leagues": "دوريات {sport_label} للهواة",
        "amateur {sport} managers": "مدراء {sport_label} للهواة",
        "amateur {sport} playerss": "لاعبو {sport_label} للهواة",
        "amateur {sport} players": "لاعبو {sport_label} للهواة",
        "amateur {sport} results": "نتائج {sport_label} للهواة",
        "amateur {sport} matches": "مباريات {sport_label} للهواة",
        "amateur {sport} navigational boxes": "صناديق تصفح {sport_label} للهواة",
        "amateur {sport} lists": "قوائم {sport_label} للهواة",
        "amateur {sport} home stadiums": "ملاعب {sport_label} للهواة",
        "amateur {sport} templates": "قوالب {sport_label} للهواة",
        "amateur {sport} rivalries": "دربيات {sport_label} للهواة",
        "amateur {sport} champions": "أبطال {sport_label} للهواة",
        "amateur {sport} competitions": "منافسات {sport_label} للهواة",
        "amateur {sport} statistics": "إحصائيات {sport_label} للهواة",
        "amateur {sport} records": "سجلات {sport_label} للهواة",
        "amateur {sport} records and statistics": "سجلات وإحصائيات {sport_label} للهواة",
        "amateur {sport} manager history": "تاريخ مدربو {sport_label} للهواة",
        "amateur {sport} receivers": "مستقبلو {sport_label} للهواة",
        "amateur {sport} wide receivers": "مستقبلون واسعون {sport_label} للهواة",
        "amateur {sport} tackles": "مصطدمو {sport_label} للهواة",
        "amateur {sport} utility players": "لاعبو مراكز متعددة {sport_label} للهواة",
        "amateur {sport} peoplee": "أعلام {sport_label} للهواة",
        "amateur {sport} sprtspeople": "رياضيو {sport_label} للهواة",
        "amateur {sport} sportspeople": "رياضيو {sport_label} للهواة",
        "amateur {sport} directors": "مدراء {sport_label} للهواة",
        "amateur {sport} journalists": "صحفيو {sport_label} للهواة",
        "amateur {sport} halfbacks": "أظهرة مساعدون {sport_label} للهواة",
        "amateur {sport} quarterbacks": "أظهرة رباعيون {sport_label} للهواة",
        "amateur {sport} centers": "لاعبو وسط {sport_label} للهواة",
        "amateur {sport} centres": "لاعبو وسط {sport_label} للهواة",
        "amateur {sport} midfielders": "لاعبو وسط {sport_label} للهواة",
        "amateur {sport} placekickers": "مسددو {sport_label} للهواة",
        "amateur {sport} kickers": "راكلو {sport_label} للهواة",
        "amateur {sport} drop kickers": "مسددو ركلات {sport_label} للهواة",
        "amateur {sport} defenders": "مدافعو {sport_label} للهواة",
        "amateur {sport} central defenders": "قلوب دفاع {sport_label} للهواة",
        "amateur {sport} forwards": "مهاجمو {sport_label} للهواة",
        "amateur {sport} inside forwards": "مهاجمون داخليون {sport_label} للهواة",
        "amateur {sport} outside forwards": "مهاجمون خارجيون {sport_label} للهواة",
        "amateur {sport} small forwards": "مهاجمون صغيرو الجسم {sport_label} للهواة",
        "amateur {sport} power forwards": "مهاجمون أقوياء الجسم {sport_label} للهواة",
        "amateur {sport} fullbacks": "مدافعو {sport_label} للهواة",
        "amateur {sport} defensive backs": "مدافعون خلفيون {sport_label} للهواة",
        "amateur {sport} running backs": "راكضون للخلف {sport_label} للهواة",
        "amateur {sport} linebackers": "أظهرة {sport_label} للهواة",
        "amateur {sport} goalkeepers": "حراس مرمى {sport_label} للهواة",
        "amateur {sport} goaltenders": "حراس مرمى {sport_label} للهواة",
        "amateur {sport} guards": "حراس {sport_label} للهواة",
        "amateur {sport} shooting guards": "مدافعون مسددون {sport_label} للهواة",
        "amateur {sport} point guards": "لاعبو هجوم خلفي {sport_label} للهواة",
        "amateur {sport} offensive linemen": "مهاجمو خط {sport_label} للهواة",
        "amateur {sport} defensive linemen": "مدافعو خط {sport_label} للهواة",
        "amateur {sport} left wingers": "أجنحة يسار {sport_label} للهواة",
        "amateur {sport} right wingers": "أجنحة يمين {sport_label} للهواة",
        "amateur {sport} defencemen": "مدافعو {sport_label} للهواة",
        "amateur {sport} wingers": "أجنحة {sport_label} للهواة",
        "amateur {sport} wing halves": "أنصاف أجنحة {sport_label} للهواة",
        "amateur {sport} referees": "حكام {sport_label} للهواة"
    }

    # Define a dictionary with actual sport name mappings
    data_list = {
        "gridiron football": "كرة قدم أمريكية شمالية",
        "american football": "كرة قدم أمريكية",
        "canadian football": "كرة قدم كندية",
        "wheelchair australian rules football": "كرة قدم أسترالية على كراسي متحركة",
        "volleyball racing": "سباق كرة طائرة",
        "wheelchair volleyball": "كرة طائرة على كراسي متحركة",
        "middle-distance running racing": "سباق ركض مسافات متوسطة",
        "wheelchair middle-distance running": "ركض مسافات متوسطة على كراسي متحركة",
        "equestrianism racing": "سباق فروسية",
        "wheelchair equestrianism": "فروسية على كراسي متحركة",
        "kickboxing racing": "سباق كيك بوكسينغ",
        "wheelchair kickboxing": "كيك بوكسينغ على كراسي متحركة",
        "draughts racing": "سباق ضامة",
        "wheelchair draughts": "ضامة على كراسي متحركة",
        "soft tennis racing": "سباق كرة مضرب لينة",
        "wheelchair soft tennis": "كرة مضرب لينة على كراسي متحركة",
        "wheelchair baseball": "كرة قاعدة على كراسي متحركة",
        "davis cup racing": "سباق كأس ديفيز",
        "wheelchair davis cup": "كأس ديفيز على كراسي متحركة",
        "board games racing": "سباق ألعاب طاولة",
        "wheelchair board games": "ألعاب طاولة على كراسي متحركة",
        "racingxx racing": "سباق سباق سيارات",
        "wheelchair racingxx": "سباق سيارات على كراسي متحركة",
        "wheelchair automobile racing": "سباق سيارات على كراسي متحركة",
        "gaelic football racing": "سباق كرة قدم غالية",
        "wheelchair gaelic football": "كرة قدم غالية على كراسي متحركة",
        "kick boxing racing": "سباق كيك بوكسينغ",
        "wheelchair cycling road race": "سباق دراجات على الطريق على كراسي متحركة",
        "wheelchair auto racing": "سباق سيارات على كراسي متحركة"
    }

    # Create a FormatData instance with the defined patterns and mappings
    bot = FormatData(formated_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")

    # Search for a specific pattern and get its localized version
    label = bot.search("men's youth snooker records and statistics")

    # Verify if the result matches the expected output
    result = label == "سجلات وإحصائيات سنوكر للشباب"

    # Return the formatted label
    return result
