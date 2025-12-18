#!/usr/bin/python3
"""
TODO: use this code in flowworks
"""
import functools
import re

from ..helps import logger
from ..translations_formats import FormatData, YearFormatData, MultiDataFormatterBase, V3Formats, MultiDataFormatterBaseYearV3
from ..translations_resolvers.new_jobs_resolver.mens import mens_resolver_labels


class FormatDataXX:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(self, key_placeholder: str, value_placeholder: str) -> None:
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        return text.replace(" from {en}", "")

    def get_key_label(self, key: str) -> str:
        """Convert the year expression to Arabic."""
        if not key:
            return ""
        result = mens_resolver_labels(key)
        return result

    def normalize_category(self, text: str, key: str) -> str:
        """Replace matched year with placeholder."""
        if not key:
            return text
        result = re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)
        return result

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
        return key, result

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        result = label.replace(self.value_placeholder, value)
        return result

    def search(self, text: str) -> str:
        """place holders"""
        return ""


@functools.lru_cache(maxsize=1)
def multi_bot() -> MultiDataFormatterBase:
    """Create a format_multi_data instance for testing."""

    # Sample data for nationality translations
    nationality_data = {
        "yemen": "اليمن",
        "Crown of Aragon": "تاج أرغون",
    }

    # Template data with both nationality and job placeholders
    formatted_data = {
        "{en_job} from {en}": "{job_ar} من {ar}",
    }
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
    )

    other_bot = FormatDataXX(
        key_placeholder="{en_job}",
        value_placeholder="{job_ar}",
    )
    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
    )


@functools.lru_cache(maxsize=10000)
def resolve_job_from_country(category: str) -> str:
    """Resolve job from countries using the provided multi_bot."""
    logger.debug(f"<<yellow>> start resolve_job_from_country: {category=}")

    _bot = multi_bot()
    result = _bot.search_all(category)

    logger.debug(f"<<yellow>> end resolve_job_from_country: {category=}, {result=}")
    return result


@functools.lru_cache(maxsize=1)
def multi_bot_vv3() -> MultiDataFormatterBaseYearV3:

    other_bot = YearFormatData(
        key_placeholder="{year1}",
        value_placeholder="{year1}",
    )
    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = V3Formats(
        formatted_data=formatted_data,
        bot=multi_bot(),
        key_placeholder="{country1}",
        value_placeholder="{country1}",
    )
    return MultiDataFormatterBaseYearV3(
        country_bot=country_bot,
        other_bot=other_bot,
        other_key_first=True,
    )


@functools.lru_cache(maxsize=10000)
def resolve_yearjob_from_country(category: str) -> str:
    """Resolve year and job from countries using yc_bot2."""
    bot = multi_bot_vv3()
    return bot.search_all(category)
