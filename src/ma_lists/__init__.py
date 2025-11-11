"""

"""
from .sports_formats_2025.match_labs import find_teams_2025
from .utils.match_sport_keys import match_sport_key
from .sports.olympics_data import olympics
# from .sports.teams_new_data import Teams_new
from .sports import sport_formts_en_ar_is_p17, sport_formts_en_p17_ar_nat
from .sports.Sport_key import Sports_Keys_For_Team, Sports_Keys_For_Label, Sports_Keys_For_Jobs
from .sports.nat_p17 import sport_formts_for_p17, nat_p17_oioi

from .sports.games_labs import summer_winter_games

from .sports_formats_national.sport_lab_nat import Get_sport_formts_female_nat

from .sports_formats_teams.sport_lab import Get_New_team_xo, Get_Sport_Format_xo_en_ar_is_P17

from .geo.Cities import CITY_TRANSLATIONS_LOWER

from .jobs.Jobs import Jobs_key_mens, Jobs_key_womens, womens_Jobs_2017, Female_Jobs, Men_Womens_Jobs, Nat_Before_Occ, Men_Womens_with_nato, Jobs_new, Jobs_key

from .geo.Labels_Contry import New_P17_Finall

from .geo.us_counties import US_State_lower, kk_end_US_State, party_end_keys

from .nats.Nationality import All_Nat, Nat_women, All_contry_ar, All_contry_with_nat, All_contry_with_nat_keys_is_en, All_contry_with_nat_ar, contries_from_nat, Nat_mens, Nat_Womens, Nat_men, ar_Nat_men, nats_to_add, en_nats_to_ar_label

from .mixed.all_keys2 import pf_keys2, pop_of_without_in, pop_of_football_lower, Word_After_Years

from .mixed.all_keys3 import typeTable_7, albums_type, film_production_company, NN_table, Ambassadors_tab

from .mixed.all_keys4 import Inter_Feds_lower

from .mixed.all_keys5 import Clubs_key_2

from .by_type import By_table, By_orginal2, By_table_orginal, Music_By_table

from .tv.films_mslslat import Films_TT, typeTable_4, Films_key_CAO, Films_key_For_nat, Films_key_CAO_new_format, television_keys_female, Films_key_333, Films_key_man, film_key_women_2, films_mslslat_tab, film_Keys_For_female, Films_keys_both_new

from .jobs.jobs_data import RELIGIOUS_KEYS_PP

from .mixed.keys2 import Add_in_table2
from .mixed.keys2 import Parties

from .languages import languages_pop, lang_ttty, languages_key, lang_key_m

from .mixed.male_keys import New_female_keys, New_male_keys

from .companies import New_Company

from .politics.military_keys import military_format_women_without_al_from_end, military_format_women_without_al, military_format_women, military_format_men

from .politics.ministers import ministrs_tab_for_pop_format

from .numbers1 import change_numb_to_word

from .others.peoples import People_key

from .mix_data import pop_All_2018_bot

from .mixed.test_4_list import en_is_nat_ar_is_P17, en_is_nat_ar_is_al_mens, en_is_nat_ar_is_man, en_is_nat_ar_is_al_women, en_is_nat_ar_is_women, change_male_to_female, priffix_lab_for_2018, Main_priffix, Main_priffix_to, Multi_sport_for_Jobs, en_is_nat_ar_is_women_2, en_is_P17_ar_is_mens, en_is_P17_ar_is_P17, replace_labels_2022, Mens_suffix, Mens_priffix, Women_s_priffix, en_is_P17_ar_is_al_women

from .utils.json_dir import open_json_file

__all__ = [
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
    "Jobs_key_mens",
    "Jobs_key_womens",
    "womens_Jobs_2017",
    "Female_Jobs",
    "Men_Womens_Jobs",
    "Nat_Before_Occ",
    "Men_Womens_with_nato",
    "Jobs_new",
    "Jobs_key",
    #
    "New_P17_Finall",
    "All_Nat",
    "Nat_women",
    "All_contry_ar",
    "All_contry_with_nat",
    "All_contry_with_nat_keys_is_en",
    "All_contry_with_nat_ar",
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
    "Word_After_Years",
    #
    "typeTable_7",
    "albums_type",
    "film_production_company",
    "NN_table",
    "Ambassadors_tab",
    "summer_winter_games",
    #
    "Inter_Feds_lower",
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
    "Add_in_table2",
    "Parties",
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
    # "Teams_new",
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
