```
ArWikiCats/
│
├── fix/
│   ├── __init__.py
│   ├── filter_en.py
│   ├── fixlists.py
│   ├── fixtitle.py
│   ├── mv_years.py
│   └── specific_normalizations.py
│
├── format_bots/
│   ├── __init__.py
│   ├── pf_keys.py
│   └── relation_mapping.py
│
├── helps/
│   ├── __init__.py
│   ├── jsonl_dump.py
│   ├── len_print.py
│   └── memory.py
│
├── jsons/
│   │
│   ├── _splited_data/
│   │   ├── cities_full_non.json
│   │   ├── P17_2_final_ll_non.json
│   │   └── yy2_non.json
│   │
│   ├── cities/
│   │   ├── cities_full.json
│   │   └── yy2.json
│   │
│   ├── geography/
│   │   ├── India_dd.json
│   │   ├── New_Keys.json
│   │   ├── P17_2_final_ll.json
│   │   ├── P17_PP.json
│   │   ├── popopo.json
│   │   ├── regions.json
│   │   ├── regions2.json
│   │   └── us_counties.json
│   │
│   ├── jobs/
│   │   ├── activists_keys.json
│   │   ├── jobs.json
│   │   ├── Jobs_22.json
│   │   ├── Jobs_22_empty.json
│   │   ├── jobs_3.json
│   │   ├── jobs_Football_Keys_players.json
│   │   ├── jobs_Men_Womens_PP.json
│   │   ├── jobs_Men_Womens_Singers.json
│   │   ├── Jobs_players.json
│   │   └── singers_tab.json
│   │
│   ├── keys/
│   │   ├── companies_data.json
│   │   ├── COMPANY_TYPE_TRANSLATIONS.json
│   │   ├── keys2.json
│   │   └── keys2_py.json
│   │
│   ├── media/
│   │   ├── film_keys_for_female.json
│   │   ├── Films_key_For_nat.json
│   │   ├── Films_key_O_multi.json
│   │   ├── Films_keys_both_new_female_found.json
│   │   ├── Films_keys_male_female.json
│   │   └── films_mslslat_tab_found.json
│   │
│   ├── nationalities/
│   │   ├── all_nat_as_en.json
│   │   ├── continents.json
│   │   ├── nationalities_data.json
│   │   ├── nationalities_data_with_directions.json
│   │   ├── sub_nats.json
│   │   └── sub_nats_with_ar_or_en.json
│   │
│   ├── people/
│   │   └── peoples.json
│   │
│   ├── population/
│   │   ├── keys_of_with_in.json
│   │   ├── pop_All_2018.json
│   │   └── pop_final_3.json
│   │
│   ├── sports/
│   │   ├── Clubs_key.json
│   │   ├── clubs_teams_leagues.json
│   │   ├── inter_federations.json
│   │   └── Sports_Keys_New.json
│   │
│   ├── taxonomy/
│   │   ├── Taxons.json
│   │   └── Taxons2.json
│   │
│   ├── MEN_WOMENS_SINGERS_found.json
│   ├── people_variants_found.json
│   ├── SPORT_JOB_VARIANTS_found.json
│   └── sport_variants_found.json
│
├── legacy_bots/
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── mappings.py
│   │
│   ├── end_start_bots/
│   │   ├── __init__.py
│   │   ├── end_start_match.py
│   │   ├── fax2.py
│   │   ├── fax2_episodes.py
│   │   ├── fax2_temp.py
│   │   └── utils.py
│   │
│   ├── legacy_resolvers_bots/
│   │   ├── __init__.py
│   │   ├── bot_2018.py
│   │   ├── bys.py
│   │   ├── country2_label_bot.py
│   │   ├── event_lab_bot.py
│   │   ├── with_years_bot.py
│   │   └── year_or_typeo.py
│   │
│   ├── legacy_utils/
│   │   ├── __init__.py
│   │   ├── data.py
│   │   ├── fixing.py
│   │   ├── joint_class.py
│   │   └── utils.py
│   │
│   ├── make_bots/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── check_bot.py
│   │   ├── reg_result.py
│   │   └── table1_bot.py
│   │
│   ├── resolvers/
│   │   ├── __init__.py
│   │   ├── arabic_label_builder.py
│   │   ├── country_resolver.py
│   │   ├── factory.py
│   │   ├── interface.py
│   │   ├── separator_based_resolver.py
│   │   └── sub_resolver.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── regex_hub.py
│   │
│   ├── __init__.py
│   ├── common_resolver_chain.py
│   ├── cov-report.md
│   └── tmp_bot.py
│
├── main_processers/
│   ├── __init__.py
│   ├── main_resolve.py
│   └── main_utils.py
│
├── new/
│   ├── __init__.py
│   ├── handle_suffixes.py
│   └── handle_time_with_callback.py
│
├── new_resolvers/
│   │
│   ├── countries_names_resolvers/
│   │   ├── __init__.py
│   │   ├── countries_names.py
│   │   ├── countries_names_data.py
│   │   ├── countries_names_v2.py
│   │   ├── geo_names_formats.py
│   │   ├── medalists_resolvers.py
│   │   └── us_states.py
│   │
│   ├── countries_names_with_sports/
│   │   ├── __init__.py
│   │   ├── p17_bot_sport.py
│   │   └── p17_sport_to_move_under.py
│   │
│   ├── films_resolvers/
│   │   ├── __init__.py
│   │   ├── resolve_films_labels.py
│   │   └── resolve_films_labels_and_time.py
│   │
│   ├── genders_resolvers/
│   │   ├── __init__.py
│   │   ├── jobs_and_genders_resolver.py
│   │   ├── sports_and_genders_resolver.py
│   │   └── utils.py
│   │
│   ├── jobs_resolvers/
│   │   ├── __init__.py
│   │   ├── mens.py
│   │   ├── relegin_jobs_nats_jobs.py
│   │   ├── relegin_jobs_new.py
│   │   ├── utils.py
│   │   └── womens.py
│   │
│   ├── jobs_resolvers_male/
│   │   ├── __init__.py
│   │   ├── mens.py
│   │   ├── relegins.py
│   │   └── relegins_nats.py
│   │
│   ├── languages_resolves/
│   │   ├── __init__.py
│   │   ├── resolve_languages.py
│   │   └── resolve_languages_films.py
│   │
│   ├── nationalities_resolvers/
│   │   ├── __init__.py
│   │   ├── data.py
│   │   ├── ministers_resolver.py
│   │   ├── nationalities_time_v2.py
│   │   └── nationalities_v2.py
│   │
│   ├── relations_resolver/
│   │   ├── __init__.py
│   │   ├── countries_names_double_v2.py
│   │   ├── nationalities_double_v2.py
│   │   └── nationalities_not_double.py
│   │
│   ├── sports_resolvers/
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── formated_data.py
│   │   │
│   │   ├── __init__.py
│   │   ├── countries_names_and_sports.py
│   │   ├── jobs_multi_sports_reslover.py
│   │   ├── nationalities_and_sports.py
│   │   ├── pre_defined.py
│   │   ├── raw_sports.py
│   │   ├── raw_sports_with_suffixes.py
│   │   └── sport_lab_nat.py
│   │
│   ├── time_and_jobs_resolvers/
│   │   ├── __init__.py
│   │   ├── year_job_origin_resolver.py
│   │   └── year_job_resolver.py
│   │
│   ├── __init__.py
│   ├── base_worker.py
│   ├── bys_new.py
│   ├── config.py
│   ├── make2_new_ArWikiCats_new_resolvers.svg
│   ├── nats_as_country_names.py
│   ├── teams_mappings_ends.py
│   └── worker.py
│
├── patterns_resolvers/
│   │
│   ├── categories_patterns/
│   │   ├── __init__.py
│   │   ├── COUNTRY_YEAR.py
│   │   ├── NAT_males.py
│   │   └── YEAR_PATTERNS.py
│   │
│   ├── __init__.py
│   ├── country_nat_pattern.py
│   ├── country_time_pattern.py
│   ├── nat_males_pattern.py
│   └── time_patterns_resolvers.py
│
├── sub_new_resolvers/
│   ├── __init__.py
│   ├── parties_resolver.py
│   ├── peoples_resolver.py
│   ├── team_work.py
│   └── university_resolver.py
│
├── time_formats/
│   ├── __init__.py
│   ├── time_to_arabic.py
│   └── utils_time.py
│
├── translations/
│   │
│   ├── build_data/
│   │   └── __init__.py
│   │
│   ├── data_builders/
│   │   ├── __init__.py
│   │   ├── build_all_keys2.py
│   │   ├── build_films_mslslat.py
│   │   ├── build_jobs.py
│   │   ├── build_jobs_data_basic.py
│   │   ├── build_jobs_players_list.py
│   │   ├── build_labels_country.py
│   │   ├── build_nationalities.py
│   │   ├── build_sport_keys.py
│   │   └── jobs_defs.py
│   │
│   ├── geo/
│   │   ├── __init__.py
│   │   ├── _shared.py
│   │   ├── Cities.py
│   │   ├── labels_country.py
│   │   ├── labels_country2.py
│   │   ├── regions.py
│   │   ├── regions2.py
│   │   └── us_counties.py
│   │
│   ├── jobs/
│   │   ├── __init__.py
│   │   ├── Jobs.py
│   │   ├── Jobs2.py
│   │   ├── jobs_data_basic.py
│   │   ├── jobs_players_list.py
│   │   ├── jobs_singers.py
│   │   └── jobs_womens.py
│   │
│   ├── mixed/
│   │   ├── __init__.py
│   │   ├── all_keys2.py
│   │   ├── all_keys3.py
│   │   ├── all_keys4.py
│   │   ├── all_keys5.py
│   │   ├── female_keys.py
│   │   ├── key_registry.py
│   │   ├── keys2.py
│   │   ├── keys_23.py
│   │   └── Newkey.py
│   │
│   ├── nats/
│   │   ├── __init__.py
│   │   └── Nationality.py
│   │
│   ├── others/
│   │   ├── __init__.py
│   │   ├── languages.py
│   │   ├── ministers.py
│   │   └── tax_table.py
│   │
│   ├── sports/
│   │   ├── __init__.py
│   │   ├── _helpers.py
│   │   ├── cycling.py
│   │   ├── games_labs.py
│   │   ├── Sport_key.py
│   │   └── tennis.py
│   │
│   ├── tv/
│   │   ├── __init__.py
│   │   └── films_mslslat.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── json_dir.py
│   │
│   ├── __init__.py
│   ├── funcs.py
│   ├── helps.py
│   └── make2_new_ArWikiCats_translations.svg
│
├── translations_formats/
│   │
│   ├── DataModel/
│   │   ├── __init__.py
│   │   ├── model_data.py
│   │   ├── model_data_base.py
│   │   ├── model_data_form.py
│   │   ├── model_data_time.py
│   │   └── model_data_v2.py
│   │
│   ├── DataModelDouble/
│   │   ├── __init__.py
│   │   ├── model_data_double.py
│   │   ├── model_data_double_v2.py
│   │   └── model_multi_data_double.py
│   │
│   ├── DataModelMulti/
│   │   ├── __init__.py
│   │   ├── model_data_v2_formater.py
│   │   ├── model_multi_data.py
│   │   ├── model_multi_data_base.py
│   │   ├── model_multi_data_year_from.py
│   │   └── model_multi_data_year_from_2.py
│   │
│   ├── __init__.py
│   ├── classes.py
│   ├── data_new_model.py
│   ├── data_with_time.py
│   ├── multi_data.py
│   └── time_patterns_formats.py
│
├── utils/
│   ├── __init__.py
│   ├── check_it.py
│   └── match_relation_word.py
│
├── __init__.py
├── event_processing.py
└── logging_config.py

```