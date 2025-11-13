"""

"""
from .sports_formats_2025.match_labs import find_teams_2025
from .sports_formats_2025.teamsnew_bot import teams_new_founder
from .utils.match_sport_keys import match_sport_key
from .sports.olympics_data import olympics
# from .sports.teams_new_data import TEAMS_NEW
from .sports import sport_formts_en_ar_is_p17, sport_formts_en_p17_ar_nat
from .sports.Sport_key import Sports_Keys_For_Team, Sports_Keys_For_Label, Sports_Keys_For_Jobs
from .sports.nat_p17 import sport_formts_for_p17, nat_p17_oioi

from .sports.games_labs import SUMMER_WINTER_GAMES

from .sports_formats_national.sport_lab_nat import Get_sport_formts_female_nat

from .sports_formats_teams.sport_lab import Get_New_team_xo, Get_Sport_Format_xo_en_ar_is_P17

from .geo.Cities import CITY_TRANSLATIONS_LOWER

from .jobs.jobs_data import NAT_BEFORE_OCC, MEN_WOMENS_WITH_NATO, RELIGIOUS_KEYS_PP

from .jobs.Jobs import jobs_mens_data, jobs_womens_data, Jobs_new

from .jobs.jobs_womens import Female_Jobs, short_womens_jobs

from .geo.labels_country import New_P17_Finall

from .geo.us_counties import US_State_lower, kk_end_US_State, party_end_keys

from .nats.Nationality import (
    All_Nat,
    Nat_women,
    all_country_ar,
    all_country_with_nat,
    all_country_with_nat_keys_is_en,
    all_country_with_nat_ar,
    contries_from_nat,
    Nat_mens,
    Nat_Womens,
    Nat_men,
    ar_Nat_men,
    nats_to_add,
    en_nats_to_ar_label,
)

from .mixed.all_keys2 import pf_keys2, pop_of_without_in, pop_of_football_lower, WORD_AFTER_YEARS

from .mixed.all_keys3 import typeTable_7, ALBUMS_TYPE, FILM_PRODUCTION_COMPANY, NN_table, Ambassadors_tab

from .mixed.all_keys4 import INTER_FEDS_LOWER

from .mixed.all_keys5 import Clubs_key_2

from .by_type import By_table, By_orginal2, By_table_orginal, Music_By_table

from .tv.films_mslslat import (
    Films_TT,
    typeTable_4,
    Films_key_CAO,
    Films_key_For_nat,
    Films_key_CAO_new_format,
    television_keys_female,
    Films_key_333,
    Films_key_man,
    film_key_women_2,
    films_mslslat_tab,
    film_Keys_For_female,
    Films_keys_both_new,
)

from .mixed.keys2 import ADD_IN_TABLE2
from .mixed.keys2 import PARTIES

from .languages import languages_pop, lang_ttty, languages_key, lang_key_m

from .mixed.male_keys import New_female_keys, New_male_keys

from .companies import New_Company

from .politics.military_keys import (
    military_format_women_without_al_from_end,
    military_format_women_without_al,
    military_format_women,
    military_format_men
)

from .politics.ministers import ministrs_tab_for_pop_format

from .numbers1 import change_numb_to_word

from .others.peoples import People_key

from .mix_data import pop_All_2018_bot

from .mixed.test_4_list import (
    en_is_nat_ar_is_P17,
    en_is_nat_ar_is_al_mens,
    en_is_nat_ar_is_man,
    en_is_nat_ar_is_al_women,
    en_is_nat_ar_is_women,
    change_male_to_female,
    priffix_lab_for_2018,
    Main_priffix,
    Main_priffix_to,
    Multi_sport_for_Jobs,
    en_is_nat_ar_is_women_2,
    en_is_P17_ar_is_mens,
    en_is_P17_ar_is_P17,
    replace_labels_2022,
    Mens_suffix,
    Mens_priffix,
    Women_s_priffix,
    en_is_P17_ar_is_al_women
)

from .utils.json_dir import open_json_file

__all__ = [
    "teams_new_founder",
    "find_teams_2025",
    "match_sport_key",
    "olympics",
    "open_json_file",
    "en_nats_to_ar_label",
    "Get_New_team_xo",

    "Get_sport_formts_female_nat",
    "Get_Sport_Format_xo_en_ar_is_P17",

    "CITY_TRANSLATIONS_LOWER",
    #
    "jobs_mens_data",
    "jobs_womens_data",

    "short_womens_jobs",
    "Female_Jobs",
    "NAT_BEFORE_OCC",
    "MEN_WOMENS_WITH_NATO",
    "Jobs_new",
    #
    "New_P17_Finall",
    "All_Nat",
    "Nat_women",
    "all_country_ar",
    "all_country_with_nat",
    "all_country_with_nat_keys_is_en",
    "all_country_with_nat_ar",
    "contries_from_nat",
    "Nat_mens",
    "Nat_Womens",
    "Nat_men",
    "ar_Nat_men",
    "nats_to_add",
    #
    "Sports_Keys_For_Team",
    "Sports_Keys_For_Label",
    "Sports_Keys_For_Jobs",
    #
    "pf_keys2",
    "pop_of_without_in",
    "pop_of_football_lower",
    "WORD_AFTER_YEARS",
    #
    "typeTable_7",
    "ALBUMS_TYPE",
    "FILM_PRODUCTION_COMPANY",
    "NN_table",
    "Ambassadors_tab",
    "SUMMER_WINTER_GAMES",
    #
    "INTER_FEDS_LOWER",
    #
    "Clubs_key_2",
    #
    "By_table",
    "By_orginal2",
    "By_table_orginal",
    "Music_By_table",
    #
    "Films_TT",
    "typeTable_4",
    "Films_key_CAO",
    "Films_key_For_nat",
    "Films_key_CAO_new_format",
    "television_keys_female",
    "Films_key_man",
    "film_key_women_2",
    "films_mslslat_tab",
    "film_Keys_For_female",
    "Films_keys_both_new",
    "Films_key_333",
    #
    "RELIGIOUS_KEYS_PP",
    #
    "ADD_IN_TABLE2",
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
    "sport_formts_en_ar_is_p17",
    "sport_formts_en_p17_ar_nat",
    #
    "sport_formts_for_p17",
    "nat_p17_oioi",
    #
    "en_is_nat_ar_is_P17",
    "en_is_nat_ar_is_al_mens",
    "en_is_nat_ar_is_man",
    "en_is_nat_ar_is_al_women",
    "en_is_nat_ar_is_women",
    "change_male_to_female",
    "priffix_lab_for_2018",
    "Main_priffix",
    "Main_priffix_to",
    "Multi_sport_for_Jobs",
    "en_is_nat_ar_is_women_2",
    "en_is_P17_ar_is_mens",
    "en_is_P17_ar_is_al_women",
    "en_is_P17_ar_is_P17",
    "replace_labels_2022",
    "Mens_suffix",
    "Mens_priffix",
    "Women_s_priffix",
    #
    "US_State_lower",
    "kk_end_US_State",
    "party_end_keys",
    #
]
