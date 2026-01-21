"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools
import re
from typing import Callable

from ..config import app_settings
from ..fix import fixtitle
from ..format_bots import change_cat
from ..helps import logger
from ..main_processers.main_utils import list_of_cat_func_foot_ballers, list_of_cat_func_new
from ..new_resolvers import all_new_resolvers
from ..format_bots.relation_mapping import translation_category_relations
from ..sub_new_resolvers import team_work
from ..time_formats import convert_time_to_arabic, match_time_en_first
from ..translations import (
    Ambassadors_tab,
    CITY_TRANSLATIONS_LOWER,
    Nat_mens,
    New_female_keys,
    People_key,
    WORD_AFTER_YEARS,
    get_from_new_p17_final,
    get_from_pf_keys2,
    jobs_mens_data,
    keys_of_without_in,
    religious_entries,
)
from ..translations_formats import FormatData
from . import tmp_bot
from .common_resolver_chain import get_lab_for_country2
from .data.mappings import change_numb_to_word, combined_suffix_mappings
from .end_start_bots import get_episodes, get_list_of_and_cat3, get_templates_fo
from .legacy_resolvers_bots import (
    bot_2018,
    country2_label_bot,
)
from .legacy_utils import Add_in_table
from .utils import RE1_compile, RE2_compile, RE3_compile
from .make_bots import get_cats, get_reg_result, get_KAKO
from .utils.regex_hub import REGEX_SUB_YEAR, RE33_compile


class LegacyBotsResolver:
    """
    A unified resolver class for legacy category translation logic.
    Encapsulates multiple resolution strategies into a single pipeline.
    """

    def __init__(self) -> None:
        """Initialize the resolver pipeline in priority order."""
        # Initialize specialized bots
        self._university_bot = self._init_university_bot()

        # Define the pipeline as a list of bound methods
        self._pipeline: list[Callable[[str], str]] = [
            self._resolve_country_event,
            self._resolve_with_years,
            self._resolve_year_or_typo,
            self._resolve_event_lab,
            self._resolve_general,
        ]

    def _init_university_bot(self) -> FormatData:
        """Initialize the university-specific FormatData bot."""
        city_lower = {
            "chandler, oklahoma": "تشاندلر (أوكلاهوما)",
            "changchun": "تشانغتشون",
            "changde": "تشانغده",
            "changhua county": "مقاطعة تشانغوا",
            "changning, hunan": "تشانغ نينغ، هونان",
            "changnyeong county": "محافظة تشانغنيونغ",
            "changsha": "تشانغشا",
            "changzhi": "تشانغ تشى",
            "changzhou": "تشانغتشو",
            "chanhassen, minnesota": "تشانهاسين (منيسوتا)",
            "chania": "خانية",
            "channahon, illinois": "تشاناهون (إلينوي)",
            "chaohu": "شاوهو",
            "chaoyang, liaoning": "تشاويانغ",
            "chaozhou": "شاوزو",
            "chapayevsk": "تشاباييفسك",
            "chapin, south carolina": "تشابين (كارولاينا الجنوبية)",
            "chaplin, connecticut": "تشابين (كونيتيكت)",
            "chapmanville, west virginia": "تشامبانفيل (فرجينيا الغربية)",
            "chardon, ohio": "تشاردن",
            "port townsend, washington": "بورت تاونسند",
            "portage": "بورتج",
            "portage la prairie": "بورتاج لابريري",
            "portage, indiana": "بورتاغ",
            "portage, wisconsin": "بورتاغ (ويسكونسن)",
            "portalegre, portugal": "بورتاليغري (البرتغال)",
            "portales, new mexico": "بورتاليس",
            "porter": "بورتر",
            "porterville, california": "بورتيرفيل (كاليفورنيا)",
            "portland, maine": "بورتلاند (مين)",
            "portland, oregon": "بورتلاند (أوريغن)",
            "porto": "بورتو",
            "porto alegre": "بورتو أليغري",
            "porto-novo": "بورتو نوفو",
            "portola valley, california": "بورتولا فالي (كاليفورنيا)",
            "portorož": "بورتوروز",
            "portsmouth, new hampshire": "بورتسموث (نيوهامشير)",
            "portsmouth, ohio": "بورتسموث (أوهايو)",
            "portsmouth, rhode island": "بورتسموث (رود آيلاند)",
            "portsmouth, virginia": "بورتسموث (فرجينيا)",
            "portuguese malacca": "ملقا البرتغالية",
            "porvoo": "بورفو",
            "posadas, misiones": "بوساداس (ميسيونيس)",
            "posey": "بوسي",
            "potenza": "بوتنسا",
        }
        city_lower.update(CITY_TRANSLATIONS_LOWER)

        majors = {
            "medical sciences": "للعلوم الطبية",
            "international university": "الدولية",
            "art": "للفنون",
            "arts": "للفنون",
            "biology": "للبيولوجيا",
            "chemistry": "للشيمية",
            "computer science": "للكمبيوتر",
            "economics": "للاقتصاد",
            "education": "للتعليم",
            "engineering": "للهندسة",
            "geography": "للجغرافيا",
            "geology": "للجيولوجيا",
            "history": "للتاريخ",
            "law": "للقانون",
            "mathematics": "للرياضيات",
            "technology": "للتكنولوجيا",
            "physics": "للفيزياء",
            "psychology": "للصحة",
            "sociology": "للأمن والسلوك",
            "political science": "للسياسة",
            "social science": "للأمن والسلوك",
            "social sciences": "للأمن والسلوك",
            "science and technology": "للعلوم والتكنولوجيا",
            "science": "للعلوم",
            "reading": "للقراءة",
            "applied sciences": "للعلوم التطبيقية",
        }

        universities_tables = {
            "national maritime university": "جامعة {} الوطنية البحرية",
            "national university": "جامعة {} الوطنية",
        }

        for major, arabic_label in majors.items():
            normalized_major = major.lower()
            template = f"جامعة {{}} {arabic_label}"
            universities_tables[f"university of {normalized_major}"] = template
            universities_tables[f"university-of-{normalized_major}"] = template
            universities_tables[f"university of the {normalized_major}"] = template
            universities_tables[f"university-of-the-{normalized_major}"] = template

        formatted_university_data = {}
        for key, template in universities_tables.items():
            ar_template = template.replace("{}", "{city_ar}")
            formatted_university_data[f"{{city}} {key}"] = ar_template
            formatted_university_data[f"{key}, {{city}}"] = ar_template
            formatted_university_data[f"{key} {{city}}"] = ar_template

        return FormatData(
            formatted_data=formatted_university_data,
            data_list=city_lower,
            key_placeholder="{city}",
            value_placeholder="{city_ar}",
        )

    def _normalize(self, text: str) -> str:
        """Standard normalization for category strings."""
        normalized = text.lower().strip()
        if normalized.startswith("category:"):
            normalized = normalized[len("category:") :].strip()
        return normalized

    def _has_blocked_prepositions(self, text: str) -> bool:
        """Check if the string contains blocked English prepositions."""
        blocked = ("in", "of", "from", "by", "at")
        # Ensure we check for whole words by adding spaces around the preposition
        return any(f" {word} " in text for word in blocked)

    def _common_lookup(self, text: str, start_get_country2: bool = False) -> str:
        """Perform a standard set of fallbacks common to multiple resolvers."""
        normalized = text.lower().strip()
        label = (
            all_new_resolvers(normalized)
            or get_lab_for_country2(normalized)
            or get_KAKO(normalized)
            or bot_2018.get_pop_All_18(normalized)
        )
        if not label and start_get_country2:
            label = self._get_country_2_logic(normalized)
        return label or ""

    def _get_country_2_logic(self, country: str) -> str:
        """Enhanced multi-source country lookup logic (from Get_country2)."""
        normalized = country.lower().strip()
        label = (
            country2_label_bot.country_2_title_work(normalized, with_years=True)
            or get_lab_for_country2(normalized)
            or get_KAKO(normalized)
            or bot_2018.get_pop_All_18(normalized)
            or bot_2018.get_pop_All_18(normalized.lower(), "")
            or ""
        )
        if label:
            label = self._fix_label(label, normalized)
        return label

    def _check_basic_lookups(self, country: str) -> str:
        """Lookup country in simple/local resolver tables."""
        if country.strip().isdigit():
            return country.strip()

        return (
            New_female_keys.get(country, "")
            or religious_entries.get(country, "")
            or People_key.get(country)
            or all_new_resolvers(country)
            or team_work.resolve_clubs_teams_leagues(country)
            or ""
        )

    def _check_historical_prefixes(self, country: str) -> str:
        """Resolve labels with historical prefixes (e.g., 'defunct national')."""
        historical_prefixes = {"defunct national": "{} وطنية سابقة"}
        normalized = country.lower().strip()

        # Simple separator validation
        blocked = ["based in", "in", "by", "about", "to", "of", "-of ", "from", "at", "on"]
        for sep in blocked:
            if (f" {sep} " if sep != "-of " else sep) in normalized:
                return ""

        for prefix, template in historical_prefixes.items():
            if normalized.startswith(f"{prefix} "):
                remainder = normalized[len(prefix) :].strip()
                remainder_label = self._common_lookup(remainder)
                if remainder_label:
                    label = template.format(remainder_label)
                    if remainder_label.strip().endswith(" في") and prefix.startswith("defunct "):
                        label = f"{remainder_label.strip()[: -len(' في')]} سابقة في"
                    return label
        return ""

    @functools.lru_cache(maxsize=1024)
    def _get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Consolidated country label resolution logic."""
        country_lower = country.lower().strip()
        label = self._check_basic_lookups(country_lower)

        if not label and start_get_country2:
            label = self._get_country_2_logic(country_lower)

        if not label:
            label = (
                self._common_lookup(country_lower)
                or self._check_gender_prefixes(country_lower)
                or self._check_historical_prefixes(country_lower)
                or all_new_resolvers(country_lower)
                or self._check_regex_years(country_lower)
                or self._check_members(country_lower)
                or ""
            )

        if label and "سنوات في القرن" in label:
            label = re.sub(r"سنوات في القرن", "سنوات القرن", label)

        return label

    def _check_gender_prefixes(self, country: str) -> str:
        """Handle 'women's' and 'men's' prefixes."""
        prefix_labels = {"women's ": "نسائية", "men's ": "رجالية"}
        for prefix, suffix in prefix_labels.items():
            if country.startswith(prefix):
                remainder = country[len(prefix) :].strip()
                remainder_label = self._common_lookup(remainder, start_get_country2=True)
                if remainder_label:
                    return f"{remainder_label} {suffix}"
        return ""

    def _check_regex_years(self, country: str) -> str:
        """Detect year patterns using regex."""
        if (
            RE1_compile.match(country)
            or RE2_compile.match(country)
            or RE3_compile.match(country)
            or RE33_compile.match(country)
        ):
            return self._try_with_years_logic(country)
        return ""

    def _check_members(self, country: str) -> str:
        """Handle 'members of' suffix."""
        if country.endswith(" members of"):
            base = country.replace(" members of", "").strip()
            label = Nat_mens.get(base, "")
            if label:
                return f"{label} أعضاء في  "
        return ""

    @functools.lru_cache(maxsize=1024)
    def _get_term_label_logic(
        self, term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
    ) -> str:
        """Logic from CountryLabelRetriever.get_term_label."""
        # Check for numeric/empty terms
        test_numeric = re.sub(r"\d+", "", term_lower.strip())
        if test_numeric in ["", "-", "–", "−"]:
            return term_lower

        term_label = New_female_keys.get(term_lower, "") or religious_entries.get(term_lower, "")
        if not term_label:
            from ..time_formats import time_to_arabic
            term_label = time_to_arabic.convert_time_to_arabic(term_lower)

        if term_label == "" and lab_type != "type_label":
            if term_lower.startswith("the "):
                term_without_the = term_lower[len("the ") :]
                term_label = bot_2018.get_pop_All_18(term_without_the, "")
                if not term_label:
                    term_label = self._get_country_label(term_without_the, start_get_country2=start_get_country2)

        if not term_label:
            if re.sub(r"\d+", "", term_lower) == "":
                term_label = term_lower
            else:
                from ..time_formats import time_to_arabic
                term_label = time_to_arabic.convert_time_to_arabic(term_lower)

        if term_label == "":
            term_label = self._get_country_label(term_lower, start_get_country2=start_get_country2)

        if not term_label and lab_type == "type_label":
            term_label = self._handle_type_lab_logic(term_lower, separator, start_get_country2)

        if not term_label and separator.strip() == "for" and term_lower.startswith("for "):
            return self._get_term_label_logic(term_lower[len("for ") :], "", lab_type=lab_type)

        return term_label

    def _handle_type_lab_logic(self, term_lower: str, separator: str, start_get_country2: bool) -> str:
        """Logic from CountryLabelRetriever._handle_type_lab_logic."""
        suffixes = [" of", " in", " at"]
        for suffix in suffixes:
            if not term_lower.endswith(suffix):
                continue
            base_term = term_lower[: -len(suffix)]
            translated_base = jobs_mens_data.get(base_term, "")
            if translated_base:
                return f"{translated_base} من "

            if not translated_base:
                translated_base = bot_2018.get_pop_All_18(base_term, "")
            if not translated_base:
                translated_base = self._get_country_label(base_term, start_get_country2=start_get_country2)

            if translated_base:
                if term_lower in keys_of_without_in:
                    return translated_base
                else:
                    return f"{translated_base} في "

        if separator.strip() == "in":
            term_label = bot_2018.get_pop_All_18(f"{term_lower} in", "")
            if term_label:
                return term_label

        return self._get_country_label(term_lower, start_get_country2=start_get_country2)

    def _fix_label(self, label: str, en_context: str) -> str:
        """Fix label title and normalize whitespace."""
        if not label:
            return ""
        fixed = fixtitle.fixlabel(label, en=en_context)
        return " ".join(fixed.strip().split())

    def _resolve_country_event(self, text: str) -> str:
        """2. Country and event-based resolution."""
        normalized = self._normalize(text)
        if self._has_blocked_prepositions(normalized):
            return ""

        # Original logic: only if it DOES NOT start with a digit
        if re.sub(r"^\d", "", normalized) == normalized:
            return self._get_country_label(normalized)
        return ""

    def _handle_political_terms(self, category: str) -> str:
        """Logic from with_years_bot.handle_political_terms."""
        known_bodies = {
            "iranian majlis": "المجلس الإيراني",
            "united states congress": "الكونغرس الأمريكي",
        }
        body_pattern = re.compile(
            rf"^(\d+)(th|nd|st|rd) ({'|'.join(known_bodies.keys())})$", re.IGNORECASE
        )
        match = body_pattern.match(category.lower())
        if match:
            ordinal_number = match.group(1)
            body_key = match.group(3).lower()
            body_label = known_bodies.get(body_key, "")
            ordinal_label = change_numb_to_word.get(ordinal_number, f"الـ{ordinal_number}")
            return f"{body_label} {ordinal_label}"
        return ""

    @functools.lru_cache(maxsize=1024)
    def _try_with_years_logic(self, category: str) -> str:
        """Consolidated logic for year-aware labels (from Try_With_Years)."""
        category = category.strip().replace("−", "-")
        if category.isdigit():
            return category

        # Political terms
        if label := self._handle_political_terms(category):
            return label

        # Year at start/end
        label = self._handle_year_at_start(category)
        if not label:
            label = self._handle_year_at_end(category)

        return label or ""

    def _handle_year_at_start(self, text: str) -> str:
        """Logic for cases where year is at the start."""
        year = REGEX_SUB_YEAR.sub(r"\g<1>", text)
        if not year or year == text:
            return ""

        remainder = text[len(year) :].strip().lower()
        remainder_label = WORD_AFTER_YEARS.get(remainder, "")

        if not remainder_label:
            remainder_label = (
                self._common_lookup(remainder)
                or get_from_pf_keys2(remainder)
                or self._resolve_general_logic(remainder, fix_title=False)
            )

        if not remainder_label:
            return ""

        arabic_labels_preceding_year = [
            "كتاب بأسماء مستعارة",
            "بطولات اتحاد رجبي للمنتخبات الوطنية",
        ]
        separator = " في " if (remainder_label in arabic_labels_preceding_year or remainder in Add_in_table) else " "
        return remainder_label + separator + year

    def _handle_year_at_end(self, text: str) -> str:
        """Logic for cases where year is at the end."""
        year_at_end = RE2_compile.sub(r"\g<1>", text.strip())
        range_match = RE33_compile.match(text)
        if range_match:
            year_at_end = RE33_compile.sub(r"\g<1>", text.strip())

        if year_at_end == text or not year_at_end:
            return ""

        remainder = text[: -len(year_at_end)].strip()
        remainder_label = (
            self._common_lookup(remainder)
            or self._resolve_general_logic(remainder, fix_title=False)
        )
        if not remainder_label:
            return ""

        formatted_year = year_at_end.replace("–present", "–الآن")
        return f"{remainder_label} {formatted_year}"

    def _resolve_with_years(self, text: str) -> str:
        """3. Year-based category resolution."""
        normalized = self._normalize(text)
        if self._has_blocked_prepositions(normalized):
            return ""

        # Original logic: only if it DOES start with a digit
        if re.sub(r"^\d", "", normalized) != normalized:
            return self._try_with_years_logic(normalized)
        return ""

    def _resolve_year_or_typo(self, text: str) -> str:
        """4. Year prefix patterns and typo handling."""
        normalized = text.lower().replace("category:", "").strip()

        if match_time_en_first(normalized):
            return convert_time_to_arabic(normalized)

        return self._label_for_startwith_year_or_typeo_logic(normalized)

    def _label_for_startwith_year_or_typeo_logic(self, category_r: str) -> str:
        """Logic from LabelForStartWithYearOrTypeo builder."""
        cate, cate3 = get_cats(category_r)
        result = get_reg_result(category_r)

        year_at_first = result.year_at_first
        in_word = result.In
        cat_test = result.cat_test
        country = result.country.strip()

        if not year_at_first:
            return ""

        # Handle Country
        country_label = ""
        if country:
            cmp_val = year_at_first.strip() + " " + country.lower()
            country_label = all_new_resolvers(country.lower()) or self._get_country_label_for_typo(
                country.lower(), country, cate3, cmp_val
            )
            if country_label:
                cat_test = cat_test.lower().replace(country.lower().strip(), "")

        # Handle Year
        year_label = convert_time_to_arabic(year_at_first)
        if not year_label:
            return ""

        cat_test = cat_test.lower().replace(year_at_first.lower().strip(), "")
        arlabel = " " + year_label

        if in_word.strip() in ("in", "at"):
            arlabel += " في "
            cat_test = cat_test.lower().replace(in_word.lower().strip(), "")

        # Handle relation mapping
        if in_word.strip():
            if in_word.strip() in translation_category_relations:
                if translation_category_relations[in_word.strip()].strip() in arlabel:
                    cat_test = cat_test.lower().replace(in_word.lower().strip(), "")
            else:
                cat_test = cat_test.lower().replace(in_word.lower().strip(), "")

        cat_test = re.sub(r"category:", "", cat_test).strip()

        # Finalize
        if not arlabel.strip():
            return ""

        category2 = cate[len("category:") :].lower() if cate.lower().startswith("category:") else cate.lower()
        no_lab = False

        if not cat_test:
            pass
        elif cat_test == country.lower() or cat_test == ("in " + country.lower()):
            no_lab = True
        elif cat_test.lower() == category2.lower():
            pass
        else:
            no_lab = True

        if not no_lab:
            # Check if result contains only Arabic characters
            if re.sub("[abcdefghijklmnopqrstuvwxyz]", "", arlabel, flags=re.IGNORECASE) == arlabel:
                return self._fix_label(arlabel, category_r)

        return ""

    def _get_country_label_for_typo(self, country_lower: str, country_not_lower: str, cate3: str, compare_lab: str) -> str:
        """Logic from year_or_typeo.get_country_label."""
        label = bot_2018.get_pop_All_18(country_lower, "")
        if not label:
            label = self._get_country_label(country_not_lower)

        if not label and cate3 == compare_lab:
            label = Nat_mens.get(country_lower, "")
            if label:
                label += " في"
        return label or ""

    def _resolve_event_lab(self, text: str) -> str:
        """5. General event labeling."""
        cate_r = text.lower().replace("_", " ")
        category3 = cate_r.split("category:")[1] if cate_r.startswith("category:") else cate_r
        category3 = change_cat(category3)

        label = self._process_event_category(category3, cate_r)
        if label:
            label = self._fix_label(label, cate_r)
            if label:
                return f"تصنيف:{label}"
        return ""

    def _process_event_category(self, category3: str, cate_r: str) -> str:
        """Logic from EventLabResolver.process_category."""
        original_cat3 = category3
        category_lab = ""
        foot_ballers = False
        list_of_cat = ""

        # Special suffixes
        if category3.endswith(" episodes"):
            list_of_cat, category3 = get_episodes(category3)
        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)
        else:
            list_of_cat, foot_ballers, category3 = get_list_of_and_cat3(
                category3, find_stubs=app_settings.find_stubs
            )

        # Country-based label
        if not category_lab and list_of_cat == "لاعبو {}":
            category_lab = (
                country2_label_bot.country_2_title_work(original_cat3)
                or get_lab_for_country2(original_cat3)
                or get_KAKO(original_cat3)
                or bot_2018.get_pop_All_18(original_cat3)
                or self._resolve_general_logic(original_cat3, start_get_country2=False, fix_title=False)
            )
            if category_lab:
                list_of_cat = ""

        # General label functions
        if not category_lab:
            category_lab = (
                self._resolve_general_logic(category3, fix_title=False)
                or country2_label_bot.country_2_title_work(category3)
                or get_lab_for_country2(category3)
                or get_KAKO(category3)
                or bot_2018.get_pop_All_18(category3)
            )

        # Suffix patterns
        if not category_lab and not list_of_cat:
            for suffix, template in combined_suffix_mappings.items():
                if category3.endswith(suffix.lower()):
                    list_of_cat = template
                    category3 = category3[: -len(suffix)].strip()
                    break

        # event_label_work logic
        if not category_lab:
            category_lab = self._event_label_work(category3)

        if list_of_cat and category3.lower().strip() == "sports events":
            category_lab = "أحداث رياضية"

        # Process list category
        if list_of_cat and category_lab:
            if foot_ballers:
                category_lab = list_of_cat_func_foot_ballers(cate_r, category_lab, list_of_cat)
            else:
                category_lab = list_of_cat_func_new(cate_r, category_lab, list_of_cat)

        if list_of_cat and not category_lab:
            category_lab = self._event_label_work(original_cat3)

        if not category_lab:
            category_lab = tmp_bot.Work_Templates(original_cat3)

        if not category_lab:
            category_lab = self._resolve_general_logic(original_cat3, fix_title=False)

        return category_lab

    def _event_label_work(self, country: str) -> str:
        """Logic from event_lab_bot.event_label_work."""
        country2 = country.lower().strip()
        if country2 == "people":
            return "أشخاص"

        return (
            get_lab_for_country2(country2)
            or get_KAKO(country2)
            or bot_2018.get_pop_All_18(country2)
            or get_from_new_p17_final(country2, "")
            or Ambassadors_tab.get(country2, "")
            or self._get_country_label(country2)
            or self._try_with_years_logic(country2)
            or self._label_for_startwith_year_or_typeo_logic(country2)
            or self._resolve_general_logic(country2, fix_title=False)
        )

    def _resolve_general(self, text: str) -> str:
        """6. Catch-all general resolution (lowest priority)."""
        return self._resolve_general_logic(text)

    @functools.lru_cache(maxsize=4096)
    def _resolve_general_logic(self, category_r: str, start_get_country2: bool = True, fix_title: bool = True) -> str:
        """Consolidated logic for general category translation."""
        category = category_r.replace("_", " ")
        category = re.sub(r"category:", "", category, flags=re.IGNORECASE).strip()

        # Implementation from _translate_general_category
        arlabel = bot_2018.get_pop_All_18(category, "")
        if not arlabel:
            arlabel = self._find_lab(category, category_r)

        if not arlabel:
            arlabel = self._work_separator_names(category, start_get_country2=start_get_country2)

        if arlabel and fix_title:
            arlabel = self._fix_label(arlabel, category_r)

        return arlabel or ""

    def _find_lab(self, category: str, category_r: str) -> str:
        """Logic from general_resolver.find_lab."""
        from ..translations import Jobs_new
        from ..utils import get_value_from_any_table
        from .make_bots import Films_O_TT, players_new_keys
        from ..time_formats import time_to_arabic

        cate_low = category.lower()
        return (
            Films_O_TT.get(cate_low, "")
            or bot_2018.get_pop_All_18(cate_low, "")
            or get_value_from_any_table(cate_low, [players_new_keys, jobs_mens_data, Jobs_new])
            or time_to_arabic.convert_time_to_arabic(cate_low)
            or ""
        )

    def _work_separator_names(self, category: str, start_get_country2: bool = False) -> str:
        """Logic from general_resolver.work_separator_names."""
        from ..utils import get_relation_word
        from .legacy_resolvers_bots.ar_lab_bot import find_ar_label

        separator, separator_name = get_relation_word(category, translation_category_relations)
        if not separator:
            return ""

        arlabel = find_ar_label(category, separator, start_get_country2=start_get_country2)
        if not arlabel:
            return ""

        if re.sub("[abcdefghijklmnopqrstuvwxyz]", "", arlabel, flags=re.IGNORECASE) != arlabel:
            return ""

        return arlabel

    def resolve(self, text: str) -> str:
        """
        Processes the input through all legacy resolvers in priority order.

        Returns the first non-empty result from the pipeline.
        """
        for method in self._pipeline:
            result = method(text)
            if result:
                logger.debug(f"LegacyBotsResolver: {method.__name__} matched for input: {text}")
                return result
        return ""


# Instantiate the resolver for global use
_resolver = LegacyBotsResolver()

# Maintain the pipeline list for backward compatibility with __all__
RESOLVER_PIPELINE: list[Callable[[str], str]] = _resolver._pipeline


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat: str) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    This function implements a pipeline pattern using the LegacyBotsResolver class.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        category_label (str): The resolved category label, or an empty string
            if no legacy resolver produces a value.
    """
    return _resolver.resolve(changed_cat)


__all__ = [
    "legacy_resolvers",
    "RESOLVER_PIPELINE",
]
