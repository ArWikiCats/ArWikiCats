"""Build comprehensive gendered job label dictionaries.

This module historically assembled several large dictionaries describing job
labels in Arabic.  The original implementation relied on implicit global state
and mutating logic that made the data construction difficult to follow.

The refactor below keeps the exported data identical while restructuring the
pipeline into typed helper functions with clear documentation.  Each helper
focuses on a single transformation—loading JSON data, combining gendered labels,
adding derived sport or film variants, or flattening the output for historic
exports.  The end result is a deterministic data set that is easier to maintain
and safe to import in other modules.
"""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from ...helps import len_print
from ..by_type import Music_By_table
from ..companies import companies_to_jobs
from ..mixed.all_keys2 import Books_table
from ..mixed.male_keys import religious_female_keys
from ..nats.Nationality import Nat_mens
from ..politics.ministers import ministrs_tab_for_Jobs_2020
from ..sports.cycling import new2019_cycling
from ..tv.films_mslslat import Films_key_For_Jobs
from ..utils.json_dir import open_json_file
from .Jobs2 import Jobs_2
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    MEN_WOMENS_JOBS_2,
    religious_keys_PP,
)
from .jobs_players_list import (
    Female_Jobs_to,
    Football_Keys_players,
    players_to_Men_Womens_Jobs,
)
from .jobs_singers import Men_Womens_Singers, films_type

LOGGER = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------


def _gendered_label(mens: str, womens: str) -> GenderedLabel:
    """Return a :class:`GenderedLabel` mapping."""

    return {"mens": mens, "womens": womens}


def _copy_gendered_map(source: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Create a deep copy of a :class:`GenderedLabelMap`.

    The original datasets occasionally reuse the same dictionary references.
    Copying the values avoids accidental mutation between helpers.
    """

    return {key: _gendered_label(value["mens"], value["womens"]) for key, value in source.items()}


def _load_gendered_label_map(filename: str) -> GenderedLabelMap:
    """Load a JSON document from ``jsons`` as a gendered label map."""

    raw_data = open_json_file(filename)
    result: GenderedLabelMap = {}
    if isinstance(raw_data, Mapping):
        for raw_key, raw_value in raw_data.items():
            if not isinstance(raw_key, str) or not isinstance(raw_value, Mapping):
                continue
            mens_value = str(raw_value.get("mens", ""))
            womens_value = str(raw_value.get("womens", ""))
            result[raw_key] = _gendered_label(mens_value, womens_value)
    return result


def _merge_gendered_maps(target: MutableMapping[str, GenderedLabel], source: Mapping[str, GenderedLabel]) -> None:
    """Update ``target`` with copies from ``source`` to avoid shared references."""

    for key, value in source.items():
        target[key] = _gendered_label(value["mens"], value["womens"])


def _append_if_absent(
    target: MutableMapping[str, GenderedLabel],
    key: str,
    value: GenderedLabel,
) -> None:
    """Add ``value`` to ``target`` if ``key`` does not already exist."""

    if key not in target:
        target[key] = _gendered_label(value["mens"], value["womens"])


def _append_list_unique(sequence: List[str], value: str) -> None:
    """Append ``value`` to ``sequence`` if it is not already present."""

    if value not in sequence:
        sequence.append(value)


# ---------------------------------------------------------------------------
# Static configuration
# ---------------------------------------------------------------------------

JOBS_2020_BASE: GenderedLabelMap = {
    "lawn bowls players": _gendered_label("", ""),
    "community activists": _gendered_label("ناشطو مجتمع", "ناشطات مجتمع"),
    "ecosocialists": _gendered_label("إيكولوجيون", "إيكولوجيات"),
    "ecosocialistes": _gendered_label("إيكولوجيون", "إيكولوجيات"),
    "horse trainers": _gendered_label("مدربو خيول", "مدربات خيول"),
    "bullfighters": _gendered_label("مصارعو ثيران", "مصارعات ثيران"),
    "supremacists": _gendered_label("عنصريون", "عنصريات"),
    "white supremacists": _gendered_label("عنصريون بيض", "عنصريات بيضوات"),
    "ceramists": _gendered_label("خزفيون", "خزفيات"),
    "bodybuilders": _gendered_label("لاعبو كمال أجسام", "لاعبات كمال أجسام"),
    "bowlers": _gendered_label("لاعبو بولينج", "لاعبات بولينج"),
    "dragon boat racers": _gendered_label("متسابقو قوارب التنين", "متسابقات قوارب التنين"),
    "ju-jitsu practitioners": _gendered_label("ممارسو جوجوتسو", "ممارسات جوجوتسو"),
    "kurash practitioners": _gendered_label("ممارسو كوراش", "ممارسات كوراش"),
    "silat practitioners": _gendered_label("ممارسو سيلات", "ممارسات سيلات"),
    "pencak silat practitioners": _gendered_label("ممارسو بنكات سيلات", "ممارسات بنكات سيلات"),
    "sambo practitioners": _gendered_label("ممارسو سامب", "ممارسات سامبو"),
    "ski orienteers": _gendered_label("متسابقو تزلج موجه", "متسابقات تزلج موجه"),
    "ski-orienteers": _gendered_label("متسابقو تزلج موجه", "متسابقات تزلج موجه"),
    "artistic swimmers": _gendered_label("سباحون فنيون", "سباحات فنيات"),
    "synchronised swimmers": _gendered_label("سباحون متزامنون", "سباحات متزامنات"),
    "powerlifters": _gendered_label("ممارسو رياضة القوة", "ممارسات رياضة القوة"),
    "rifle shooters": _gendered_label("رماة بندقية", "راميات بندقية"),
    "wheelchair curlers": _gendered_label("لاعبو كيرلنغ على الكراسي المتحركة", "لاعبات كيرلنغ على الكراسي المتحركة"),
    "wheelchair fencers": _gendered_label("مبارزون على الكراسي المتحركة", "مبارزات على الكراسي المتحركة"),
    "sepak takraw players": _gendered_label("لاعبو سيباك تاكرو", "لاعبات سيباك تاكرو"),
    "boccia players": _gendered_label("لاعبو بوتشيا", "لاعبات بوتشيا"),
    "wheelchair rugby players": _gendered_label("لاعبو رغبي على الكراسي المتحركة", "لاعبات رغبي على الكراسي المتحركة"),
    "wheelchair tennis players": _gendered_label(
        "لاعبو كرة مضرب على الكراسي المتحركة",
        "لاعبات كرة مضرب على الكراسي المتحركة",
    ),
}

DISABILITY_LABELS: GenderedLabelMap = {
    "deaf": _gendered_label("صم", "صم"),
    "blind": _gendered_label("مكفوفون", "مكفوفات"),
    "deafblind": _gendered_label("صم ومكفوفون", "صم ومكفوفات"),
}

EXECUTIVE_DOMAINS: Mapping[str, str] = {
    "railroad": "سكك حديدية",
    "media": "وسائل إعلام",
    "public transportation": "نقل عام",
    "film studio": "استوديوهات أفلام",
    "advertising": "إعلانات",
    "music industry": "صناعة الموسيقى",
    "newspaper": "جرائد",
    "radio": "مذياع",
    "television": "تلفاز",
    "media5": "",
}

NAT_BEFORE_OCC_BASE: List[str] = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "scholars of",
    "executed abroad",
    "emigrants",
]

MEN_WOMENS_WITH_NATO: GenderedLabelMap = {
    "eugenicists": _gendered_label("علماء {nato} متخصصون في تحسين النسل", "عالمات {nato} متخصصات في تحسين النسل"),
    "politicians who committed suicide": _gendered_label(
        "سياسيون {nato} أقدموا على الانتحار",
        "سياسيات {nato} أقدمن على الانتحار",
    ),
    "contemporary artists": _gendered_label("فنانون {nato} معاصرون", "فنانات {nato} معاصرات"),
}

TYPI_LABELS: Mapping[str, GenderedLabel] = {
    "classical": _gendered_label("كلاسيكيون", "كلاسيكيات"),
    "historical": _gendered_label("تاريخيون", "تاريخيات"),
}

FEMALE_JOBS_BASE: Dict[str, str] = {
    "nuns": "راهبات",
    "deafblind actresses": "ممثلات صم ومكفوفات",
    "deaf actresses": "ممثلات صم",
    "actresses": "ممثلات",
    "princesses": "أميرات",
    "video game actresses": "ممثلات ألعاب فيديو",
    "musical theatre actresses": "ممثلات مسرحيات موسيقية",
    "television actresses": "ممثلات تلفزيون",
    "stage actresses": "ممثلات مسرح",
    "voice actresses": "ممثلات أداء صوتي",
    "women in business": "سيدات أعمال",
    "women in politics": "سياسيات",
    "lesbians": "سحاقيات",
    "businesswomen": "سيدات أعمال",
}

JOBS_TYPE_TRANSLATIONS: Mapping[str, str] = {
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "anthology": "أنثولوجيا",
    "biographical": "سيرة ذاتية",
    "black comedy": "كوميديا سوداء",
    "bollywood": "بوليوود",
    "buddy": "رفقاء",
    "business and financial": "أعمال ومالية",
    "financial": "مالية",
    "business": "أعمال",
    "clay animation": "رسوم متحركة طينية",
    "comedy fiction": "خيال كوميدي",
    "comedy thriller": "كوميديا إثارة",
    "comedy": "كوميديا",
    "comedy drama": "كوميديا درامية",
    "comics": "قصص مصورة",
    "crime thriller": "إثارة وجريمة",
    "crime": "جريمة",
    "crossover fiction": "خيال متقاطع",
    "cyberpunk": "سايبربانك",
    "dance": "رقص",
    "disaster": "كوارث",
    "docudramas": "دراما وثائقية",
    "drama": "دراما",
    "dystopian": "ديستوبيا",
    "environmental fiction": "خيال بيئي",
    "environmental": "بيئة",
    "erotic thriller": "إثارة جنسية",
    "erotica": "أدب جنسي",
    "fantasy": "فنتازيا",
    "finance and investment": "تمويل واستثمار",
    "finance": "تمويل",
    "french comedy": "كوميديا فرنسية",
    "gay male pornography": "إباحية مثلية",
    "gothic horror": "رعب قوطي",
    "historical": "تاريخ",
    "horror": "رعب",
    "investment": "استثمار",
    "japanese horror": "رعب ياباني",
    "kung fu": "كونغ فو",
    "mafia comedy": "مافيا كوميدية",
    "mafia": "مافيا",
    "magazine": "مجلات",
    "magic realism": "واقعية سحرية",
    "martial arts": "فنون قتالية",
    "mystery": "غموض",
    "mysticism": "غموض",
    "newspaper": "صحف",
    "parody": "محاكاة ساخرة",
    "pirate": "قراصنة",
    "police procedural": "إجراءات الشرطة",
    "police procedurals": "إجراءات الشرطة",
    "political fiction": "خيال سياسي",
    "propaganda": "بروباغندا",
    "prussian": "بروسي",
    "psychological horror": "رعب نفسي",
    "radio": "راديو",
    "rape and revenge": "إغتصاب وإنتقام",
    "romantic comedy": "كوميديا رومانسية",
    "samurai": "ساموراي",
    "satire": "هجاء",
    "science fiction action": "خيال علمي وحركة",
    "science fiction": "خيال علمي",
    "silent": "سينما صامتة",
    "slapstick": "كوميديا تهريجية",
    "socialist realism": "واقعية اشتراكية",
    "speculative fiction": "خيال تأملي",
    "sports": "رياضة",
    "spy": "تجسس",
    "surfing": "ركمجة",
    "teen": "مراهقة",
    "television": "تلفزيون",
    "thriller": "إثارة",
    "war": "حرب",
    "yakuza": "ياكوزا",
    "zombie": "زومبي",
}

JOBS_PEOPLE_ROLES: Mapping[str, GenderedLabel] = {
    "bloggers": _gendered_label("مدونو", "مدونات"),
    "writers": _gendered_label("كتاب", "كاتبات"),
    "critics": _gendered_label("نقاد", "ناقدات"),
    "journalists": _gendered_label("صحفيو", "صحفيات"),
    "producers": _gendered_label("منتجو", "منتجات"),
    "authors": _gendered_label("مؤلفو", "مؤلفات"),
    "editors": _gendered_label("محررو", "محررات"),
    "artists": _gendered_label("فنانو", "فنانات"),
    "directors": _gendered_label("مخرجو", "مخرجات"),
    "publisherspeople": _gendered_label("ناشرو", "ناشرات"),
    "publishers (people)": _gendered_label("ناشرو", "ناشرات"),
    "personalities": _gendered_label("شخصيات", "شخصيات"),
    "presenters": _gendered_label("مذيعو", "مذيعات"),
    "creators": _gendered_label("مبتكرو", "مبتكرات"),
}

FILM_ROLE_LABELS: Mapping[str, GenderedLabel] = {
    "filmmakers": _gendered_label("صانعو أفلام", "صانعات أفلام"),
    "film editors": _gendered_label("محررو أفلام", "محررات أفلام"),
    "film directors": _gendered_label("مخرجو أفلام", "مخرجات أفلام"),
    "film producers": _gendered_label("منتجو أفلام", "منتجات أفلام"),
    "film critics": _gendered_label("نقاد أفلام", "ناقدات أفلام"),
    "film historians": _gendered_label("مؤرخو أفلام", "مؤرخات أفلام"),
    "cinema editors": _gendered_label("محررون سينمائون", "محررات سينمائيات"),
    "cinema directors": _gendered_label("مخرجون سينمائون", "مخرجات سينمائيات"),
    "cinema producers": _gendered_label("منتجون سينمائون", "منتجات سينمائيات"),
}


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------


@dataclass
class JobsDataset:
    """Aggregate all exported job dictionaries."""

    jobs_key_mens: Dict[str, str]
    jobs_key_womens: Dict[str, str]
    womens_jobs_2017: Dict[str, str]
    female_jobs: Dict[str, str]
    men_womens_jobs: GenderedLabelMap
    nat_before_occ: List[str]
    men_womens_with_nato: GenderedLabelMap
    jobs_new: Dict[str, str]
    jobs_key: Dict[str, str]


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def _build_jobs_2020() -> GenderedLabelMap:
    """Return the 2020 job dictionary merged with ministerial categories."""

    jobs_2020 = _copy_gendered_map(JOBS_2020_BASE)
    for category, labels in ministrs_tab_for_Jobs_2020.items():
        jobs_2020[category] = _gendered_label(labels["mens"], labels["womens"])
    return jobs_2020


def _extend_with_religious_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Add religious role combinations and their activist variants."""

    jobs = _copy_gendered_map(base_jobs)
    for religion_key, labels in religious_keys_PP.items():
        jobs[religion_key] = _gendered_label(labels["mens"], labels["womens"])
        activist_key = f"{religion_key} activists"
        jobs[activist_key] = _gendered_label(
            f"ناشطون {labels['mens']}",
            f"ناشطات {labels['womens']}",
        )
    return jobs


def _extend_with_disability_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Insert disability-focused job labels and executive variants."""

    jobs = _copy_gendered_map(base_jobs)
    _merge_gendered_maps(jobs, DISABILITY_LABELS)
    for domain_key, domain_label in EXECUTIVE_DOMAINS.items():
        if not domain_label:
            continue
        jobs[f"{domain_key} executives"] = _gendered_label(
            f"مدراء {domain_label}",
            f"مديرات {domain_label}",
        )
    return jobs


def _merge_jobs_sources() -> GenderedLabelMap:
    """Combine JSON sources and static configuration into a single map."""

    jobs_pp = _load_gendered_label_map("jobs_Men_Womens_PP")
    jobs_pp = _extend_with_religious_jobs(jobs_pp)
    jobs_pp = _extend_with_disability_jobs(jobs_pp)

    jobs_2020 = _build_jobs_2020()
    for job_name, labels in jobs_2020.items():
        if labels["mens"] and labels["womens"]:
            lowered = job_name.lower()
            if lowered not in jobs_pp:
                jobs_pp[lowered] = _gendered_label(labels["mens"], labels["womens"])

    for category, labels in Football_Keys_players.items():
        lowered = category.lower()
        _append_if_absent(jobs_pp, lowered, labels)

    jobs_pp["fashion journalists"] = _gendered_label("صحفيو موضة", "صحفيات موضة")
    jobs_pp["zionists"] = _gendered_label("صهاينة", "صهيونيات")

    _merge_gendered_maps(jobs_pp, companies_to_jobs)

    for religion_key, feminine_label in religious_female_keys.items():
        founder_key = f"{religion_key} founders"
        jobs_pp[founder_key] = _gendered_label(
            f"مؤسسو {feminine_label}",
            f"مؤسسات {feminine_label}",
        )

    jobs_pp["imprisoned abroad"] = _gendered_label("مسجونون في الخارج", "مسجونات في الخارج")
    jobs_pp["imprisoned"] = _gendered_label("مسجونون", "مسجونات")
    jobs_pp["escapees"] = _gendered_label("هاربون", "هاربات")
    jobs_pp["prison escapees"] = _gendered_label(
        "هاربون من السجن",
        "هاربات من السجن",
    )
    jobs_pp["missionaries"] = _gendered_label("مبشرون", "مبشرات")
    jobs_pp["venerated"] = _gendered_label("مبجلون", "مبجلات")

    return jobs_pp


def _add_jobs_from_jobs2(jobs_pp: GenderedLabelMap) -> GenderedLabelMap:
    """Merge entries from :mod:`Jobs2` that are missing from ``jobs_pp``."""

    merged = _copy_gendered_map(jobs_pp)
    for job_key, labels in Jobs_2.items():
        lowered = job_key.lower()
        if lowered not in merged and (labels["mens"] or labels["womens"]):
            merged[lowered] = _gendered_label(labels["mens"], labels["womens"])
    return merged


def _load_activist_jobs(men_womens_jobs: MutableMapping[str, GenderedLabel], nat_before_occ: List[str]) -> None:
    """Extend ``men_womens_jobs`` with activist categories from JSON."""

    activists = _load_gendered_label_map("activists_keys")
    for category, labels in activists.items():
        lowered = category.lower()
        _append_list_unique(nat_before_occ, lowered)
        men_womens_jobs[lowered] = _gendered_label(labels["mens"], labels["womens"])


def _add_sport_variants(
    men_womens_jobs: MutableMapping[str, GenderedLabel],
    base_jobs: Mapping[str, GenderedLabel],
) -> None:
    """Derive sport, professional, and wheelchair variants for job labels."""

    for base_key, base_labels in base_jobs.items():
        lowered = base_key.lower()
        men_womens_jobs[f"sports {lowered}"] = _gendered_label(
            f"{base_labels['mens']} رياضيون",
            f"{base_labels['womens']} رياضيات",
        )
        men_womens_jobs[f"professional {lowered}"] = _gendered_label(
            f"{base_labels['mens']} محترفون",
            f"{base_labels['womens']} محترفات",
        )
        men_womens_jobs[f"wheelchair {lowered}"] = _gendered_label(
            f"{base_labels['mens']} على الكراسي المتحركة",
            f"{base_labels['womens']} على الكراسي المتحركة",
        )


def _add_cycling_variants(
    men_womens_jobs: MutableMapping[str, GenderedLabel],
    nat_before_occ: List[str],
) -> None:
    """Insert variants derived from cycling events."""

    for event_key, event_label in new2019_cycling.items():
        lowered = event_key.lower()
        men_womens_jobs[f"{lowered} cyclists"] = _gendered_label(
            f"دراجو {event_label}",
            f"دراجات {event_label}",
        )
        winners_key = f"{lowered} winners"
        stage_winners_key = f"{lowered} stage winners"
        men_womens_jobs[winners_key] = _gendered_label(
            f"فائزون في {event_label}",
            f"فائزات في {event_label}",
        )
        men_womens_jobs[stage_winners_key] = _gendered_label(
            f"فائزون في مراحل {event_label}",
            f"فائزات في مراحل {event_label}",
        )
        _append_list_unique(nat_before_occ, winners_key)
        _append_list_unique(nat_before_occ, stage_winners_key)


def _add_jobs_people_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Create combinations of people-centric roles with book genres and types."""

    for role_key, role_labels in JOBS_PEOPLE_ROLES.items():
        if not (role_labels["mens"] and role_labels["womens"]):
            continue
        for book_key, book_label in Books_table.items():
            men_womens_jobs[f"{book_key} {role_key}"] = _gendered_label(
                f"{role_labels['mens']} {book_label}",
                f"{role_labels['womens']} {book_label}",
            )
        for genre_key, genre_label in JOBS_TYPE_TRANSLATIONS.items():
            men_womens_jobs[f"{genre_key} {role_key}"] = _gendered_label(
                f"{role_labels['mens']} {genre_label}",
                f"{role_labels['womens']} {genre_label}",
            )


def _add_film_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> int:
    """Create film-related job variants and return the number of generated entries."""

    count = 0
    for film_key, film_label in Films_key_For_Jobs.items():
        lowered_film_key = film_key.lower()
        for role_key, role_labels in FILM_ROLE_LABELS.items():
            men_womens_jobs[role_key] = _gendered_label(role_labels["mens"], role_labels["womens"])
            combo_key = f"{lowered_film_key} {role_key}"
            men_womens_jobs[combo_key] = _gendered_label(
                f"{role_labels['mens']} {film_label}",
                f"{role_labels['womens']} {film_label}",
            )
            count += 1
    return count


def _add_singer_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Add singer categories and stylistic combinations."""

    for category, labels in Men_Womens_Singers.items():
        men_womens_jobs[category] = _gendered_label(labels["mens"], labels["womens"])
        for style_key, style_labels in TYPI_LABELS.items():
            combo_key = f"{style_key} {category}"
            men_womens_jobs[combo_key] = _gendered_label(
                f"{labels['mens']} {style_labels['mens']}",
                f"{labels['womens']} {style_labels['womens']}",
            )


def _build_female_jobs() -> Dict[str, str]:
    """Create the combined female job mapping with derived categories."""

    female_jobs = dict(FEMALE_JOBS_BASE)
    female_jobs2: Dict[str, str] = {}
    for film_category, film_labels in films_type.items():
        female_jobs2[f"{film_category} actresses"] = f"ممثلات {film_labels['womens']}"
    female_jobs2["sportswomen"] = "رياضيات"
    for key, label in Female_Jobs_to.items():
        female_jobs2[key] = label
    female_jobs.update(female_jobs2)
    return female_jobs


def _build_jobs_new(
    jobs_key: Mapping[str, str],
    female_jobs: Mapping[str, str],
) -> Dict[str, str]:
    """Build the flattened ``Jobs_new`` mapping used by legacy bots."""

    jobs_new: Dict[str, str] = {}
    for female_key, female_label in female_jobs.items():
        if female_label:
            lowered = female_key.lower()
            jobs_new[lowered] = female_label
    for nationality_key, nationality_label in Nat_mens.items():
        if nationality_label:
            jobs_new[f"{nationality_key.lower()} people"] = nationality_label
    jobs_new["people of the ottoman empire"] = "عثمانيون"
    for job_key, job_label in jobs_key.items():
        lowered = job_key.lower()
        if job_label:
            jobs_new[lowered] = job_label
    if "2080io" in sys.argv:
        for job_key, job_label in jobs_key.items():
            if not job_label:
                continue
            for music_key, music_label in Music_By_table.items():
                if music_label:
                    combo_key = f"{job_key} {music_key}"
                    jobs_new[combo_key] = f"{job_label} {music_label}"
    return jobs_new


def _finalise_jobs_dataset() -> JobsDataset:
    """Construct the full jobs dataset from individual builders."""

    nat_before_occ = list(NAT_BEFORE_OCC_BASE)
    nat_before_occ.extend(key for key in religious_keys_PP.keys())

    jobs_pp = _merge_jobs_sources()
    jobs_pp = _add_jobs_from_jobs2(jobs_pp)

    men_womens_jobs: GenderedLabelMap = {}
    _merge_gendered_maps(men_womens_jobs, MEN_WOMENS_JOBS_2)

    _load_activist_jobs(men_womens_jobs, nat_before_occ)

    for job_key, labels in jobs_pp.items():
        men_womens_jobs[job_key.lower()] = _gendered_label(labels["mens"], labels["womens"])

    _add_sport_variants(men_womens_jobs, jobs_pp)
    _merge_gendered_maps(men_womens_jobs, players_to_Men_Womens_Jobs)
    _add_cycling_variants(men_womens_jobs, nat_before_occ)
    _add_jobs_people_variants(men_womens_jobs)
    film_variant_count = _add_film_variants(men_womens_jobs)
    _add_singer_variants(men_womens_jobs)

    jobs_key_mens: Dict[str, str] = {}
    womens_jobs_2017: Dict[str, str] = {}
    for job_key, labels in men_womens_jobs.items():
        jobs_key_mens[job_key] = labels["mens"]
        if labels["womens"]:
            womens_jobs_2017[job_key] = labels["womens"]

    jobs_key_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

    female_jobs = _build_female_jobs()
    jobs_key_womens: Dict[str, str] = {}
    for female_key, female_label in female_jobs.items():
        if female_label:
            jobs_key_womens[female_key.lower()] = female_label

    jobs_key: Dict[str, str] = {key: label for key, label in jobs_key_mens.items() if label}

    jobs_new = _build_jobs_new(jobs_key, female_jobs)

    lengths = {
        "Len_of_Films_Jobs": film_variant_count,
        "Jobs_key": len(jobs_key),
        "Jobs_new": len(jobs_new),
        "Jobs_key_mens": len(jobs_key_mens),
        "Jobs_key_womens": len(jobs_key_womens),
        "Men_Womens_Jobs": len(men_womens_jobs),
    }
    LOGGER.debug("Job label dataset sizes: %s", lengths)
    len_print.lenth_pri("jobs.py", lengths)

    return JobsDataset(
        jobs_key_mens=jobs_key_mens,
        jobs_key_womens=jobs_key_womens,
        womens_jobs_2017=womens_jobs_2017,
        female_jobs=female_jobs,
        men_womens_jobs=men_womens_jobs,
        nat_before_occ=nat_before_occ,
        men_womens_with_nato=_copy_gendered_map(MEN_WOMENS_WITH_NATO),
        jobs_new=jobs_new,
        jobs_key=jobs_key,
    )


_DATASET = _finalise_jobs_dataset()

Jobs_key_mens = _DATASET.jobs_key_mens
Jobs_key_womens = _DATASET.jobs_key_womens
womens_Jobs_2017 = _DATASET.womens_jobs_2017
Female_Jobs = _DATASET.female_jobs
Men_Womens_Jobs = _DATASET.men_womens_jobs
Nat_Before_Occ = _DATASET.nat_before_occ
Men_Womens_with_nato = _DATASET.men_womens_with_nato
Jobs_new = _DATASET.jobs_new
Jobs_key = _DATASET.jobs_key


__all__ = [
    "Female_Jobs",
    "Jobs_key",
    "Jobs_key_mens",
    "Jobs_key_womens",
    "Jobs_new",
    "Men_Womens_Jobs",
    "Men_Womens_with_nato",
    "Nat_Before_Occ",
    "womens_Jobs_2017",
]
