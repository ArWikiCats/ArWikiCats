""" """

from .by_type import By_orginal2, By_table, By_table_orginal, Music_By_table
from .companies import New_Company
from .geo.Cities import CITY_TRANSLATIONS_LOWER
from .geo.labels_country import New_P17_Finall, US_STATES
from .jobs.Jobs import Jobs_new, jobs_mens_data, jobs_womens_data
from .jobs.jobs_data_basic import NAT_BEFORE_OCC, RELIGIOUS_KEYS_PP
from .jobs.jobs_womens import Female_Jobs, short_womens_jobs
from .languages import lang_key_m, lang_ttty, languages_key, languages_pop
from .mix_data import pop_All_2018_bot
from .mixed.all_keys2 import (
    People_key,
    WORD_AFTER_YEARS,
    pf_keys2,
    pop_of_football_lower,
    pop_of_without_in,
)
from .mixed.all_keys3 import (
    ALBUMS_TYPE,
    FILM_PRODUCTION_COMPANY,
    Ambassadors_tab,
    typeTable_7,
)
from .mixed.all_keys4 import INTER_FEDS_LOWER
from .mixed.all_keys5 import Clubs_key_2, pop_final_5
from .mixed.bot_te_4_list import (
    Multi_sport_for_Jobs,
    change_male_to_female,
    en_is_nat_ar_is_al_mens,
    en_is_nat_ar_is_al_women,
    en_is_nat_ar_is_man,
    en_is_nat_ar_is_P17,
    en_is_nat_ar_is_women,
    en_is_nat_ar_is_women_2,
    en_is_P17_ar_is_al_women,
    en_is_P17_ar_is_mens,
    replace_labels_2022,
)
from .mixed.jenders_priffix_suffix import (
    Mens_priffix,
    Mens_suffix,
    Women_s_priffix,
)
from .mixed.keys2 import PARTIES
from .mixed.male_keys import New_female_keys, New_male_keys
from .nats.Nationality import (
    All_Nat,
    Nat_men,
    Nat_mens,
    Nat_women,
    Nat_Womens,
    all_country_ar,
    all_country_with_nat,
    all_country_with_nat_ar,
    all_country_with_nat_keys_is_en,
    countries_nat_en_key,
    ar_Nat_men,
    contries_from_nat,
    en_nats_to_ar_label,
    nats_to_add,
)
from .numbers1 import change_numb_to_word
from .politics.military_keys import (
    military_format_men,
    military_format_women,
    military_format_women_without_al,
    military_format_women_without_al_from_end,
)
from .politics.ministers import ministrs_tab_for_pop_format
from .sports.games_labs import SUMMER_WINTER_GAMES
from .sports.olympics_data import olympics
from .sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from ..translations_resolvers.match_labs import find_teams_2025
from .sports_formats_2025.teamsnew_bot import teams_new_founder
from .sports_formats_national.sport_lab_nat import (
    Get_sport_formts_female_nat,
    sport_lab_nat_load,
)
from .sports_formats_oioioi.bot import sport_lab_oioioi_load
from .sports_formats_oioioi.data import NAT_P17_OIOI
from .tv.films_mslslat import (
    tyty_data,
    Films_key_333,
    Films_key_CAO,
    Films_key_CAO_new_format,
    Films_key_For_nat,
    Films_key_man,
    Films_keys_both_new_female,
    film_key_women_2,
    film_Keys_For_female,
    films_mslslat_tab,
    television_keys_female,
)
from .type_tables import typeTable
from .utils.match_sport_keys import match_sport_key

from .sports_formats_teams.te3 import SPORT_FORMTS_ENAR_P17_TEAM
from .utils import apply_pattern_replacements
from .sports_formats_teams.team_job import sport_formts_enar_p17_jobs


__all__ = [
    "US_STATES",
    "sport_formts_enar_p17_jobs",
    "apply_pattern_replacements",
    "SPORT_FORMTS_ENAR_P17_TEAM",
    "typeTable",
    "teams_new_founder",
    "find_teams_2025",
    "match_sport_key",
    "olympics",
    "en_nats_to_ar_label",
    "Get_sport_formts_female_nat",
    "sport_lab_nat_load",
    "CITY_TRANSLATIONS_LOWER",
    #
    "jobs_mens_data",
    "jobs_womens_data",
    "short_womens_jobs",
    "Female_Jobs",
    "NAT_BEFORE_OCC",
    "Jobs_new",
    #
    "New_P17_Finall",
    "All_Nat",
    "Nat_women",
    "all_country_ar",
    "all_country_with_nat",
    "all_country_with_nat_keys_is_en",
    "countries_nat_en_key",
    "all_country_with_nat_ar",
    "contries_from_nat",
    "Nat_mens",
    "Nat_Womens",
    "Nat_men",
    "ar_Nat_men",
    "nats_to_add",
    #
    "SPORTS_KEYS_FOR_TEAM",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    #
    "pf_keys2",
    "pop_of_without_in",
    "pop_of_football_lower",
    "WORD_AFTER_YEARS",
    #
    "typeTable_7",
    "ALBUMS_TYPE",
    "FILM_PRODUCTION_COMPANY",
    "Ambassadors_tab",
    "SUMMER_WINTER_GAMES",
    #
    "INTER_FEDS_LOWER",
    #
    "pop_final_5",
    "Clubs_key_2",
    #
    "By_table",
    "By_orginal2",
    "By_table_orginal",
    "Music_By_table",
    #
    "Films_key_CAO",
    "Films_key_For_nat",
    "Films_key_CAO_new_format",
    "television_keys_female",
    "Films_key_man",
    "film_key_women_2",
    "films_mslslat_tab",
    "film_Keys_For_female",
    "Films_keys_both_new_female",
    "Films_key_333",
    "tyty_data",
    #
    "RELIGIOUS_KEYS_PP",
    #
    "PARTIES",
    #
    "languages_pop",
    "lang_ttty",
    "languages_key",
    "lang_key_m",
    #
    "New_female_keys",
    "New_male_keys",
    "New_Company",
    #
    "military_format_women_without_al_from_end",
    "military_format_women_without_al",
    "military_format_women",
    "military_format_men",
    #
    "ministrs_tab_for_pop_format",
    #
    "change_numb_to_word",
    #
    "People_key",
    #
    "pop_All_2018_bot",
    #
    # "TEAMS_NEW",
    #
    "sport_lab_oioioi_load",
    "NAT_P17_OIOI",
    #
    "en_is_nat_ar_is_P17",
    "en_is_nat_ar_is_al_mens",
    "en_is_nat_ar_is_man",
    "en_is_nat_ar_is_al_women",
    "en_is_nat_ar_is_women",
    "change_male_to_female",
    "Multi_sport_for_Jobs",
    "en_is_nat_ar_is_women_2",
    "en_is_P17_ar_is_mens",
    "en_is_P17_ar_is_al_women",
    "replace_labels_2022",
    "Mens_suffix",
    "Mens_priffix",
    "Women_s_priffix",
]
