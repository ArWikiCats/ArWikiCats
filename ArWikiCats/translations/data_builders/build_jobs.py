"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    copy_gendered_map,
    merge_gendered_maps,
)


@dataclass
class JobsDataset:
    """Aggregate all exported job dictionaries."""

    males_jobs: Dict[str, str]
    females_jobs: Dict[str, str]


def _append_list_unique(sequence: List[str], value: str) -> None:
    """Append ``value`` to ``sequence`` if it is not already present."""

    if value not in sequence:
        sequence.append(value)


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def _build_jobs_2020(JOBS_2020_BASE) -> GenderedLabelMap:
    """
    Return a copy of the base 2020 jobs mapping.
    
    Parameters:
        JOBS_2020_BASE (GenderedLabelMap): Base gendered job mapping for 2020.
    
    Returns:
        GenderedLabelMap: A copy of `JOBS_2020_BASE` representing the 2020 job labels.
    """

    jobs_2020 = copy_gendered_map(JOBS_2020_BASE)
    return jobs_2020


def _extend_with_religious_jobs(base_jobs: GenderedLabelMap, RELIGIOUS_KEYS_PP) -> GenderedLabelMap:
    """
    Expand a gendered job map with religious role entries and their activist variants.
    
    Parameters:
        base_jobs (GenderedLabelMap): Original mapping of job keys to gendered labels.
        RELIGIOUS_KEYS_PP (Mapping[str, Mapping[str, str]]): Mapping where each key is a religion role string and each value is a mapping with keys "males" and "females" containing the respective labels.
    
    Returns:
        GenderedLabelMap: A new mapping containing the original entries plus added religious role keys and corresponding "{role} activists" entries with gendered labels.
    """

    jobs = copy_gendered_map(base_jobs)
    for religion_key, labels in RELIGIOUS_KEYS_PP.items():
        jobs[religion_key] = {"males": labels["males"], "females": labels["females"]}
        activist_key = f"{religion_key} activists"
        jobs[activist_key] = {"males": f"ناشطون {labels['males']}", "females": f"ناشطات {labels['females']}"}
    return jobs


def _extend_with_disability_jobs(base_jobs: GenderedLabelMap, DISABILITY_LABELS, EXECUTIVE_DOMAINS) -> GenderedLabelMap:
    """
    Extend a gendered job map with disability-specific labels and add executive-role variants for executive domains.
    
    Parameters:
        base_jobs (GenderedLabelMap): Original gendered job mapping; not modified.
        DISABILITY_LABELS (Mapping[str, GenderedLabel]): Gendered labels for disability-focused jobs to merge into the result.
        EXECUTIVE_DOMAINS (Mapping[str, str]): Mapping from domain key to domain label; for each non-empty label an "{domain_key} executives" entry is added with Arabic male/female executive labels.
    
    Returns:
        GenderedLabelMap: A new gendered job map containing the merged disability labels and generated executive variants.
    """

    jobs = copy_gendered_map(base_jobs)
    merge_gendered_maps(jobs, DISABILITY_LABELS)
    for domain_key, domain_label in EXECUTIVE_DOMAINS.items():
        if not domain_label:
            continue
        jobs[f"{domain_key} executives"] = {"males": f"مدراء {domain_label}", "females": f"مديرات {domain_label}"}
    return jobs


def _merge_jobs_sources(
    jobs_pp,
    EXECUTIVE_DOMAINS,
    DISABILITY_LABELS,
    RELIGIOUS_KEYS_PP,
    FOOTBALL_KEYS_PLAYERS,
    JOBS_2020_BASE,
    companies_to_jobs,
    RELIGIOUS_FEMALE_KEYS,
) -> GenderedLabelMap:
    """
    Combine multiple job sources and static configurations into a single gendered job map.
    
    Parameters:
        jobs_pp (GenderedLabelMap): Initial mapping to augment; will be updated and returned.
        EXECUTIVE_DOMAINS (Mapping[str, str]): Domain labels used to create executive-role variants.
        DISABILITY_LABELS (GenderedLabelMap): Disability-related gendered labels to merge into the map.
        RELIGIOUS_KEYS_PP (Mapping[str, GenderedLabel]): Religious-role keys and their gendered labels to include.
        FOOTBALL_KEYS_PLAYERS (GenderedLabelMap): Football-related player categories to add when missing.
        JOBS_2020_BASE (Mapping[str, GenderedLabel]): Base 2020 job entries used to derive additional lowercase keys.
        companies_to_jobs (Mapping[str, GenderedLabel]): Company-to-job mappings to merge into the result.
        RELIGIOUS_FEMALE_KEYS (Mapping[str, str]): Mapping from religion key to its feminine label used to create founder variants.
    
    Returns:
        GenderedLabelMap: The augmented mapping of job-category keys to gendered Arabic labels (each value contains 'males' and 'females').
    """

    jobs_pp.update(
        {
            "candidates": {"males": "مرشحون", "females": "مرشحات"},
            "presidential candidates": {"males": "مرشحون رئاسيون", "females": "مرشحات رئاسيات"},
            "political candidates": {"males": "مرشحون سياسيون", "females": "مرشحات سياسيات"},
        }
    )

    jobs_pp["coaches"] = {"males": "مدربون", "females": "مدربات"}
    # jobs_pp["sports coaches"] = {"males": "مدربون رياضيون", "females": "مدربات رياضيات"}
    jobs_pp.setdefault("men", {"males": "رجال", "females": ""})

    jobs_pp = _extend_with_religious_jobs(jobs_pp, RELIGIOUS_KEYS_PP)
    jobs_pp = _extend_with_disability_jobs(jobs_pp, DISABILITY_LABELS, EXECUTIVE_DOMAINS)

    jobs_2020 = _build_jobs_2020(JOBS_2020_BASE)
    for job_name, labels in jobs_2020.items():
        if labels["males"] and labels["females"]:
            lowered = job_name.lower()
            if lowered not in jobs_pp:
                jobs_pp[lowered] = {"males": labels["males"], "females": labels["females"]}

    for category, labels in FOOTBALL_KEYS_PLAYERS.items():
        lowered = category.lower()
        if lowered not in jobs_pp:
            jobs_pp[lowered] = {"males": labels["males"], "females": labels["females"]}

    jobs_pp["fashion journalists"] = {"males": "صحفيو موضة", "females": "صحفيات موضة"}
    jobs_pp["zionists"] = {"males": "صهاينة", "females": "صهيونيات"}

    merge_gendered_maps(jobs_pp, companies_to_jobs)

    for religion_key, feminine_label in RELIGIOUS_FEMALE_KEYS.items():
        founder_key = f"{religion_key} founders"
        jobs_pp[founder_key] = {"males": f"مؤسسو {feminine_label}", "females": f"مؤسسات {feminine_label}"}

    jobs_pp["imprisoned abroad"] = {"males": "مسجونون في الخارج", "females": "مسجونات في الخارج"}
    jobs_pp["imprisoned"] = {"males": "مسجونون", "females": "مسجونات"}
    jobs_pp["escapees"] = {"males": "هاربون", "females": "هاربات"}
    jobs_pp["prison escapees"] = {"males": "هاربون من السجن", "females": "هاربات من السجن"}
    jobs_pp["missionaries"] = {"males": "مبشرون", "females": "مبشرات"}
    jobs_pp["venerated"] = {"males": "مبجلون", "females": "مبجلات"}

    return jobs_pp


def _add_jobs_from_jobs2(jobs_pp: GenderedLabelMap, JOBS_2, JOBS_3333) -> GenderedLabelMap:
    """
    Add missing job entries from JOBS_2 and JOBS_3333 into a copy of an existing gendered job map.
    
    Parameters:
        jobs_pp (GenderedLabelMap): Source gendered job map to copy and augment.
        JOBS_2 (Mapping[str, dict]): Additional job source mapping original job keys to `{"males": str, "females": str}` labels.
        JOBS_3333 (Mapping[str, dict]): Additional job source mapping original job keys to `{"males": str, "females": str}` labels.
    
    Returns:
        GenderedLabelMap: A new gendered job map containing all entries from the copy of `jobs_pp` plus any entries from `JOBS_2` and `JOBS_3333` whose lowercase key was absent and that have at least one male or female label.
    """

    merged = copy_gendered_map(jobs_pp)
    sources = [JOBS_2, JOBS_3333]
    for source in sources:
        for job_key, labels in source.items():
            lowered = job_key.lower()
            if lowered not in merged and (labels["males"] or labels["females"]):
                merged[lowered] = {"males": labels["males"], "females": labels["females"]}

    return merged


def _load_activist_jobs(
    m_w_jobs: MutableMapping[str, GenderedLabel],
    nat_before_occ: List[str],
    activists,
) -> None:
    """
    Add activist categories into the gendered jobs map and record their normalized keys.
    
    For each entry in `activists`, the category name is lowercased, appended to `nat_before_occ` if not already present, and an entry is inserted into `m_w_jobs` mapping that lowercased key to a GenderedLabel with the `males` and `females` labels from the source.
    
    Parameters:
        m_w_jobs (MutableMapping[str, GenderedLabel]): Mapping to be mutated with new activist entries.
        nat_before_occ (List[str]): List of category keys; the lowercased category is appended here if missing.
        activists (Mapping[str, Mapping[str, str]]): Source mapping where each key is a category name and each value is a mapping containing `'males'` and `'females'` labels.
    """

    for category, labels in activists.items():
        lowered = category.lower()
        _append_list_unique(nat_before_occ, lowered)
        m_w_jobs[lowered] = {"males": labels["males"], "females": labels["females"]}


def _add_sport_variants(
    base_jobs: Mapping[str, GenderedLabel],
) -> dict[str, GenderedLabel]:
    """
    Create sport-related, professional, and wheelchair variants for each job label.
    
    For each entry in `base_jobs`, produces three new keys — "sports {job}", "professional {job}", and "wheelchair {job}" — each mapped to a GenderedLabel containing corresponding male and female labels derived from the base labels.
    
    Parameters:
        base_jobs (Mapping[str, GenderedLabel]): Mapping of base job keys to gendered labels (expects 'males' and 'females' entries).
    
    Returns:
        dict[str, GenderedLabel]: Mapping from generated variant keys to their GenderedLabel.
    """
    data: dict[str, GenderedLabel] = {}
    for base_key, base_labels in base_jobs.items():
        lowered = base_key.lower()
        data[f"sports {lowered}"] = {
            "males": f"{base_labels['males']} رياضيون",
            "females": f"{base_labels['females']} رياضيات",
        }
        data[f"professional {lowered}"] = {
            "males": f"{base_labels['males']} محترفون",
            "females": f"{base_labels['females']} محترفات",
        }
        data[f"wheelchair {lowered}"] = {
            "males": f"{base_labels['males']} على الكراسي المتحركة",
            "females": f"{base_labels['females']} على الكراسي المتحركة",
        }
    return data


def _add_cycling_variants(nat_before_occ: List[str], BASE_CYCLING_EVENTS) -> dict[str, GenderedLabel]:
    """
    Generate gendered job labels for cycling event variants and append related keys to nat_before_occ.
    
    Parameters:
        nat_before_occ (List[str]): List of keys representing nationality-before-occupation phrases; this list is mutated:
            for each event the function appends the corresponding "<event> winners" and "<event> stage winners"
            keys if they are not already present.
        BASE_CYCLING_EVENTS (Mapping[str, str]): Mapping from cycling event name to its display label used in generated Arabic labels.
    
    Returns:
        dict[str, GenderedLabel]: Mapping of generated variant keys to their gendered labels. For each event key in
        BASE_CYCLING_EVENTS the returned mapping includes:
          - "<event> cyclists" -> male/female cyclist labels
          - "<event> winners" -> male/female winner labels
          - "<event> stage winners" -> male/female stage-winner labels
    """
    data: dict[str, GenderedLabel] = {}
    for event_key, event_label in BASE_CYCLING_EVENTS.items():
        lowered = event_key.lower()
        data[f"{lowered} cyclists"] = {"males": f"دراجو {event_label}", "females": f"دراجات {event_label}"}

        winners_key = f"{lowered} winners"
        stage_winners_key = f"{lowered} stage winners"

        data[winners_key] = {"males": f"فائزون في {event_label}", "females": f"فائزات في {event_label}"}
        data[stage_winners_key] = {
            "males": f"فائزون في مراحل {event_label}",
            "females": f"فائزات في مراحل {event_label}",
        }
        _append_list_unique(nat_before_occ, winners_key)
        _append_list_unique(nat_before_occ, stage_winners_key)

    return data


def _add_jobs_people_variants(JOBS_PEOPLE_ROLES, BOOK_CATEGORIES, JOBS_TYPE_TRANSLATIONS) -> dict[str, GenderedLabel]:
    """
    Generate gendered job labels by combining people-centric roles with book categories and job-type translations.
    
    Parameters:
        JOBS_PEOPLE_ROLES (Mapping[str, GenderedLabel]): Mapping from role key to gendered labels with keys "males" and "females". Only roles that have both male and female labels are used.
        BOOK_CATEGORIES (Mapping[str, str]): Mapping from book-category key to its label suffix (e.g., "children's", "history").
        JOBS_TYPE_TRANSLATIONS (Mapping[str, str]): Mapping from type/genre key to its label suffix (e.g., "fiction", "biography").
    
    Returns:
        dict[str, GenderedLabel]: A mapping where each key is "{category_key} {role_key}" or "{genre_key} {role_key}" and each value is a GenderedLabel with the role's male/female label suffixed by the category or genre label.
    """
    data: dict[str, GenderedLabel] = {}
    for role_key, role_labels in JOBS_PEOPLE_ROLES.items():
        if not (role_labels["males"] and role_labels["females"]):
            continue
        for book_key, book_label in BOOK_CATEGORIES.items():
            data[f"{book_key} {role_key}"] = {
                "males": f"{role_labels['males']} {book_label}",
                "females": f"{role_labels['females']} {book_label}",
            }
        for genre_key, genre_label in JOBS_TYPE_TRANSLATIONS.items():
            data[f"{genre_key} {role_key}"] = {
                "males": f"{role_labels['males']} {genre_label}",
                "females": f"{role_labels['females']} {genre_label}",
            }

    return data


def _add_film_variants() -> dict[str, GenderedLabel]:
    """
    Builds a mapping of film-related job keys to their gendered Arabic labels.
    
    Returns:
        dict[str, GenderedLabel]: A dictionary mapping English job keys (lowercase phrases) to a GenderedLabel,
        where each GenderedLabel contains "males" and "females" Arabic labels.
    """

    data = {
        "film directors": {"males": "مخرجو أفلام", "females": "مخرجات أفلام"},
        "filmmakers": {"males": "صانعو أفلام", "females": "صانعات أفلام"},
        "film producers": {"males": "منتجو أفلام", "females": "منتجات أفلام"},
        "film critics": {"males": "نقاد أفلام", "females": "ناقدات أفلام"},
        "film editors": {"males": "محررو أفلام", "females": "محررات أفلام"},
        "documentary filmmakers": {"males": "صانعو أفلام وثائقية", "females": "صانعات أفلام وثائقية"},
        "documentary film directors": {"males": "مخرجو أفلام وثائقية", "females": "مخرجات أفلام وثائقية"},
        "animated film directors": {"males": "مخرجو أفلام رسوم متحركة", "females": "مخرجات أفلام رسوم متحركة"},
        "experimental filmmakers": {"males": "صانعو أفلام تجريبية", "females": "صانعات أفلام تجريبية"},
        "animated film producers": {"males": "منتجو أفلام رسوم متحركة", "females": "منتجات أفلام رسوم متحركة"},
        "pornographic film directors": {"males": "مخرجو أفلام إباحية", "females": "مخرجات أفلام إباحية"},
        "lgbtq film directors": {"males": "مخرجو أفلام إل جي بي تي كيو", "females": "مخرجات أفلام إل جي بي تي كيو"},
        "comedy film directors": {"males": "مخرجو أفلام كوميدية", "females": "مخرجات أفلام كوميدية"},
        "science fiction film directors": {"males": "مخرجو أفلام خيال علمي", "females": "مخرجات أفلام خيال علمي"},
        "fiction film directors": {"males": "مخرجو أفلام خيالية", "females": "مخرجات أفلام خيالية"},
        "pornographic film producers": {"males": "منتجو أفلام إباحية", "females": "منتجات أفلام إباحية"},
        "documentary film producers": {"males": "منتجو أفلام وثائقية", "females": "منتجات أفلام وثائقية"},
        "horror film directors": {"males": "مخرجو أفلام رعب", "females": "مخرجات أفلام رعب"},
        "film historians": {"males": "مؤرخو أفلام", "females": "مؤرخات أفلام"},
        "silent film directors": {"males": "مخرجو أفلام صامتة", "females": "مخرجات أفلام صامتة"},
        "action film directors": {"males": "مخرجو أفلام حركة", "females": "مخرجات أفلام حركة"},
        "cinema editors": {"males": "محررون سينمائون", "females": "محررات سينمائيات"},
        "silent film producers": {"males": "منتجو أفلام صامتة", "females": "منتجات أفلام صامتة"},
        "propaganda film directors": {"males": "مخرجو أفلام دعائية", "females": "مخرجات أفلام دعائية"},
        "war filmmakers": {"males": "صانعو أفلام حربية", "females": "صانعات أفلام حربية"},
        "fantasy film directors": {"males": "مخرجو أفلام فانتازيا", "females": "مخرجات أفلام فانتازيا"},
        "feminist filmmakers": {"males": "صانعو أفلام نسوية", "females": "صانعات أفلام نسوية"},
        "horror film producers": {"males": "منتجو أفلام رعب", "females": "منتجات أفلام رعب"},
        "japanese horror film directors": {"males": "مخرجو أفلام رعب يابانية", "females": "مخرجات أفلام رعب يابانية"},
        "lgbtq film producers": {"males": "منتجو أفلام إل جي بي تي كيو", "females": "منتجات أفلام إل جي بي تي كيو"},
        "parody film directors": {"males": "مخرجو أفلام ساخرة", "females": "مخرجات أفلام ساخرة"},
    }

    return data


def _add_singer_variants() -> dict[str, GenderedLabel]:
    """
    Return a mapping of classical and singer-related job keys to their gendered Arabic labels.
    
    Returns:
        dict[str, GenderedLabel]: Mapping from job category key (lowercase English phrase) to a GenderedLabel
        containing `males` and `females` Arabic strings for that category.
    """

    data: dict[str, GenderedLabel] = {
        "classical composers": {"males": "ملحنون كلاسيكيون", "females": "ملحنات كلاسيكيات"},
        "classical musicians": {"males": "موسيقيون كلاسيكيون", "females": "موسيقيات كلاسيكيات"},
        "classical pianists": {"males": "عازفو بيانو كلاسيكيون", "females": "عازفات بيانو كلاسيكيات"},
        "classical violinists": {"males": "عازفو كمان كلاسيكيون", "females": "عازفات كمان كلاسيكيات"},
        "classical cellists": {"males": "عازفو تشيلو كلاسيكيون", "females": "عازفات تشيلو كلاسيكيات"},
        "classical guitarists": {"males": "عازفو قيثارة كلاسيكيون", "females": "عازفات قيثارة كلاسيكيات"},
        "historical novelists": {"males": "روائيون تاريخيون", "females": "روائيات تاريخيات"},
        "classical singers": {"males": "مغنون كلاسيكيون", "females": "مغنيات كلاسيكيات"},
        "classical mandolinists": {"males": "عازفو مندولين كلاسيكيون", "females": "عازفات مندولين كلاسيكيات"},
        "classical saxophonists": {"males": "عازفو سكسفون كلاسيكيون", "females": "عازفات سكسفون كلاسيكيات"},
        "classical percussionists": {"males": "فنانون إيقاعيون كلاسيكيون", "females": "فنانات إيقاعيات كلاسيكيات"},
        "classical music critics": {"males": "نقاد موسيقى كلاسيكيون", "females": "ناقدات موسيقى كلاسيكيات"},
        "classical painters": {"males": "رسامون كلاسيكيون", "females": "رسامات كلاسيكيات"},
        "classical writers": {"males": "كتاب كلاسيكيون", "females": "كاتبات كلاسيكيات"},
        "classical choreographers": {"males": "مصممو رقص كلاسيكيون", "females": "مصممات رقص كلاسيكيات"},
        "classical dancers": {"males": "راقصون كلاسيكيون", "females": "راقصات كلاسيكيات"},
    }

    return data


def _finalise_jobs_dataset(
    jobs_pp,
    sport_variants,
    people_variants,
    MEN_WOMENS_JOBS_2,
    NAT_BEFORE_OCC,
    MEN_WOMENS_SINGERS_BASED,
    MEN_WOMENS_SINGERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
    SPORT_JOB_VARIANTS,
    RELIGIOUS_FEMALE_KEYS,
    BASE_CYCLING_EVENTS,
    JOBS_2,
    JOBS_3333,
    RELIGIOUS_KEYS_PP,
    FOOTBALL_KEYS_PLAYERS,
    EXECUTIVE_DOMAINS,
    DISABILITY_LABELS,
    JOBS_2020_BASE,
    companies_to_jobs,
    activists,
) -> JobsDataset:
    """
    Assemble a complete gendered jobs dataset from multiple source maps and generated variants.
    
    Merges the provided job source maps and derived variant maps into two flattened mappings of job keys to Arabic labels, populating male labels for every key and female labels only where available; removes entries with empty male labels and includes a few explicit entries required by downstream consumers.
    
    Returns:
        JobsDataset: An object with `males_jobs` (mapping of job key -> male Arabic label) and `females_jobs` (mapping of job key -> female Arabic label when present).
    """

    m_w_jobs: GenderedLabelMap = {}
    males_jobs: Dict[str, str] = {}
    females_jobs: Dict[str, str] = {}

    jobs_sources = _merge_jobs_sources(
        jobs_pp,
        EXECUTIVE_DOMAINS,
        DISABILITY_LABELS,
        RELIGIOUS_KEYS_PP,
        FOOTBALL_KEYS_PLAYERS,
        JOBS_2020_BASE,
        companies_to_jobs,
        RELIGIOUS_FEMALE_KEYS,
    )
    jobs_pp = _add_jobs_from_jobs2(jobs_sources, JOBS_2, JOBS_3333)  # 1,369

    merge_gendered_maps(m_w_jobs, MEN_WOMENS_JOBS_2)  # 534
    _load_activist_jobs(m_w_jobs, NAT_BEFORE_OCC, activists)  # 95
    cycling_variants = _add_cycling_variants(NAT_BEFORE_OCC, BASE_CYCLING_EVENTS)  # 27
    film_variants = _add_film_variants()  # 1,881
    singer_variants = _add_singer_variants()  # 16

    m_w_jobs.update(MEN_WOMENS_SINGERS_BASED)  # 65
    m_w_jobs.update(MEN_WOMENS_SINGERS)  # 7,181 > to > 433
    m_w_jobs.update(jobs_pp)
    m_w_jobs.update(sport_variants)
    m_w_jobs.update(cycling_variants)
    m_w_jobs.update(people_variants)
    m_w_jobs.update(film_variants)
    m_w_jobs.update(singer_variants)

    merge_gendered_maps(m_w_jobs, PLAYERS_TO_MEN_WOMENS_JOBS)  # 1,345
    merge_gendered_maps(m_w_jobs, SPORT_JOB_VARIANTS)  # 61,486

    m_w_jobs["sports coaches"] = {"males": "مدربو رياضة", "females": "مدربات رياضة"}

    for job_key, labels in m_w_jobs.items():
        males_jobs[job_key] = labels["males"]
        if labels["females"]:
            females_jobs[job_key] = labels["females"]

    males_jobs["men's footballers"] = "لاعبو كرة قدم رجالية"

    # males_jobs["sports coaches"] = "مدربو رياضة"
    # females_jobs["sports coaches"] = "مدربات رياضة"

    males_jobs = {key: label for key, label in males_jobs.items() if label}

    return JobsDataset(
        males_jobs=males_jobs,
        females_jobs=females_jobs,
    )


def _build_jobs_new(
    female_jobs: Mapping[str, str],
    Nat_mens: Mapping[str, str],
) -> Dict[str, str]:
    """
    Create a flattened mapping of job and nationality keys to Arabic labels for legacy consumers.
    
    Parameters:
        female_jobs: Mapping from job key to female Arabic label; entries with empty labels are skipped.
        Nat_mens: Mapping from nationality key to Arabic label used for people of that nationality; entries with empty labels are skipped.
    
    Returns:
        A dict where:
          - each female job key is lowercased and mapped to its female label,
          - each nationality key is lowercased and mapped as "<nationality> people" to its label,
          - includes the fixed entry "people of the ottoman empire" -> "عثمانيون".
    """

    data: Dict[str, str] = {}

    for female_key, female_label in female_jobs.items():
        if female_label:
            lowered = female_key.lower()
            data[lowered] = female_label

    for nationality_key, nationality_label in Nat_mens.items():
        if nationality_label:
            data[f"{nationality_key.lower()} people"] = nationality_label

    data["people of the ottoman empire"] = "عثمانيون"

    return data


__all__ = [
    "_finalise_jobs_dataset",
    "_build_jobs_new",
]