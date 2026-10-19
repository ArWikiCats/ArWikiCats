```
tests/
│
├── big/
│   │
│   ├── big_data/
│   │   ├── 0.json
│   │   ├── 1.json
│   │   ├── 10.json
│   │   ├── 2.json
│   │   ├── 3.json
│   │   ├── 4.json
│   │   ├── 5.json
│   │   ├── 6.json
│   │   ├── 7.json
│   │   ├── 8.json
│   │   └── 9.json
│   │
│   ├── data/
│   │   ├── chairmen_and_investors.json
│   │   ├── endings.json
│   │   ├── establishments.json
│   │   ├── films_with_time.json
│   │   ├── language.json
│   │   ├── males.json
│   │   ├── novels.json
│   │   ├── relations_data.json
│   │   ├── teams_to_test.json
│   │   └── television series.json
│   │
│   ├── religions_data/
│   │   ├── religions.json
│   │   ├── religions2.json
│   │   ├── religions3.json
│   │   ├── religions4.json
│   │   └── religions5.json
│   │
│   └── test_big_datasets.py
│
├── diff_data/
│
├── e2e/
│   │
│   ├── deaths/
│   │   ├── test_deaths.py
│   │   └── test_deaths_2.py
│   │
│   ├── event_lists/
│   │   ├── test_antigua_and_barbuda.py
│   │   ├── test_based_on.py
│   │   ├── test_classical_composers.py
│   │   ├── test_cultural_depictions.py
│   │   ├── test_executed.py
│   │   ├── test_jesuits.py
│   │   ├── test_man_keys.py
│   │   ├── test_ministers.py
│   │   ├── test_of_the_usa.py
│   │   └── test_with_by.py
│   │
│   ├── event_lists_globals/
│   │   ├── test_2026.py
│   │   ├── test_add_in.py
│   │   ├── test_all_russia.py
│   │   ├── test_and.py
│   │   ├── test_canadian_football.py
│   │   ├── test_championships.py
│   │   ├── test_culture_and_mythology.py
│   │   ├── test_defunct.py
│   │   ├── test_entertainment.py
│   │   ├── test_film_keys.py
│   │   ├── test_institutions.py
│   │   ├── test_Keep_it_last.py
│   │   ├── test_lutenists.py
│   │   ├── test_national_assembly.py
│   │   ├── test_places_and_structures.py
│   │   ├── test_politics_and_history.py
│   │   ├── test_science_and_medicine.py
│   │   ├── test_songs.py
│   │   ├── test_sports.py
│   │   ├── test_temporal.py
│   │   ├── test_virginia.py
│   │   ├── test_virginia2.py
│   │   ├── test_womens_africa_cup_of_nations.py
│   │   └── test_yemen.py
│   │
│   ├── event_lists_importants/
│   │   ├── test_4_important.py
│   │   ├── test_5_important.py
│   │   ├── test_fix_nationalities.py
│   │   ├── test_multi_sport.py
│   │   ├── test_olympics_global.py
│   │   ├── test_political_leader.py
│   │   └── test_technology.py
│   │
│   ├── event_lists_jobs_bots/
│   │   ├── test_wheelchair.py
│   │   ├── test_wheelchair_2_part1.py
│   │   ├── test_wheelchair_2_part2.py
│   │   └── test_wheelchair_2_part3.py
│   │
│   ├── event_lists_new_data/
│   │   ├── test_africanism.py
│   │   ├── test_departments.py
│   │   ├── test_mosques.py
│   │   └── test_pan_arican.py
│   │
│   ├── event_lists_papua_new_guinea/
│   │   └── test_papua_new_guinea.py
│   │
│   ├── event_lists_people/
│   │   ├── test_people.py
│   │   └── test_people_2.py
│   │
│   ├── event_lists_squad_title_bot/
│   │   ├── test_get_list_of_and_cat3_with_lab2.py
│   │   └── test_squad_title_bot.py
│   │
│   ├── event_lists_test_non/
│   │   ├── test_non.py
│   │   ├── test_non_2.py
│   │   └── test_non_fiction_writers.py
│   │
│   ├── event_lists_test_religions/
│   │   ├── test_muslims.py
│   │   └── test_religions.py
│   │
│   ├── event_lists_womens/
│   │   ├── test_womens_players.py
│   │   ├── test_womens_sports.py
│   │   └── test_womens_sports2.py
│   │
│   ├── geo/
│   │   ├── test_geography.py
│   │   ├── test_geography_by.py
│   │   ├── test_geography_us.py
│   │   └── test_labels_country_e2e.py
│   │
│   ├── legacy_bots/
│   │   │
│   │   └── arabic_label_builder/
│   │       ├── test_ar_lab_big_data.py
│   │       ├── test_ar_lab_big_data2.py
│   │       ├── test_check_historical.py
│   │       ├── test_country2_bot.py
│   │       └── test_main.py
│   │
│   ├── new_resolvers/
│   │   │
│   │   ├── countries_names_resolvers/
│   │   │   │
│   │   │   ├── medalists_resolvers/
│   │   │   │   └── test_olympic_event_translations_type_tables.py
│   │   │   │
│   │   │   └── test_countries_names_e2e.py
│   │   │
│   │   ├── films_resolvers/
│   │   │   ├── test_films_and_others_bot.py
│   │   │   └── test_films_key_cao_keys.py
│   │   │
│   │   ├── jobs_resolvers_male/
│   │   │   └── test_non_males.py
│   │   │
│   │   ├── languages_resolves/
│   │   │   ├── test_langs_slow.py
│   │   │   └── test_language_films_main.py
│   │   │
│   │   ├── sports_resolvers/
│   │   │   │
│   │   │   ├── sport_lab_nat/
│   │   │   │   └── test_sport_lab_nat_compare.py
│   │   │   │
│   │   │   └── test_sports_new.py
│   │   │
│   │   ├── test_compare/
│   │   │   ├── test_Films.py
│   │   │   ├── test_resolve_films_with_nat.py
│   │   │   └── test_with_time.py
│   │   │
│   │   ├── test_films_keys.py
│   │   ├── test_films_keys2.py
│   │   ├── test_nats_double_v2.py
│   │   ├── test_nats_v2_extended.py
│   │   ├── test_resolve_v3i_new.py
│   │   └── test_superhero_e2e.py
│   │
│   ├── sub_new_resolvers/
│   │   └── test_team_work.py
│   │
│   ├── test_northern_ireland/
│   │   └── test_northern_ireland.py
│   │
│   ├── test_2.py
│   ├── test_3.py
│   ├── test_ar_lab_no_event22.py
│   ├── test_circular_dependency.py
│   ├── test_classical_composers_fix.py
│   ├── test_classical_musicians.py
│   ├── test_common_resolver_chain_e2e.py
│   ├── test_mk3_main.py
│   ├── test_nuns.py
│   ├── test_south_african.py
│   ├── test_sports_events.py
│   ├── test_sports_events2.py
│   ├── test_t4_2018_jobs_old_data.py
│   └── test_yy2_non.py
│
├── integration/
│   │
│   ├── fix/
│   │   └── test_mv_years_2.py
│   │
│   ├── format_bots/
│   │   ├── test_pf_keys.py
│   │   └── test_pf_keys_old.py
│   │
│   ├── legacy_bots/
│   │   │
│   │   ├── circular_dependency/
│   │   │   │
│   │   │   └── arabic_label_builder/
│   │   │       └── test_arabic_label_builder_integration.py
│   │   │
│   │   ├── common_resolver_chain/
│   │   │   ├── test_common_resolver_chain_int.py
│   │   │   └── test_get_con_lab_bot.py
│   │   │
│   │   ├── legacy_resolvers_bots/
│   │   │   │
│   │   │   ├── byc/
│   │   │   │   └── test_bys.py
│   │   │   │
│   │   │   ├── country2_label_bot/
│   │   │   │   ├── test_c_1_1_lab_3.py
│   │   │   │   ├── test_c_1_c_2_labs_in.py
│   │   │   │   └── test_c_2_1_lab.py
│   │   │   │
│   │   │   ├── event_lab_bot/
│   │   │   │   ├── test_event_lab_bot.py
│   │   │   │   └── test_lab_seoo_bot.py
│   │   │   │
│   │   │   └── test_year_or_typeo.py
│   │   │
│   │   ├── legacy_utils/
│   │   │   └── test_split_text_by_separator_inte.py
│   │   │
│   │   └── resolvers/
│   │       │
│   │       └── arabic_label_builder/
│   │           ├── test_ar_lab_bot.py
│   │           ├── test_arabic_label_builder.py
│   │           └── test_separator_fixing_integration.py
│   │
│   ├── main_processers/
│   │   └── test_list_cat_format.py
│   │
│   ├── new_resolvers/
│   │   │
│   │   ├── bys_new/
│   │   │   ├── test_bys_new.py
│   │   │   ├── test_bys_new2.py
│   │   │   ├── test_bys_new_3.py
│   │   │   └── test_bys_new_or_and_by.py
│   │   │
│   │   ├── countries_names_resolvers/
│   │   │   │
│   │   │   ├── countries_names_v2/
│   │   │   │   ├── test_army.py
│   │   │   │   ├── test_countries_names_v2.py
│   │   │   │   └── test_countries_names_v2_more.py
│   │   │   │
│   │   │   ├── medalists_resolvers/
│   │   │   │   ├── test_countries_names_medalists.py
│   │   │   │   └── test_with_olympics.py
│   │   │   │
│   │   │   ├── test_countries_names2.py
│   │   │   ├── test_countries_names_integration.py
│   │   │   ├── test_geo_names_formats.py
│   │   │   └── test_us_states.py
│   │   │
│   │   ├── countries_names_with_sports/
│   │   │   ├── test_p17_bot_sport.py
│   │   │   └── test_p17_sport_to_move_under.py
│   │   │
│   │   ├── films_resolvers/
│   │   │   │
│   │   │   ├── film_keys_bot/
│   │   │   │   ├── test_film_keys_bot_resolve.py
│   │   │   │   ├── test_films_keys2_batch.py
│   │   │   │   └── test_get_Films_key_CAO.py
│   │   │   │
│   │   │   ├── test_resolve_films.py
│   │   │   ├── test_resolve_films_labels_and_time.py
│   │   │   ├── test_resolve_films_main.py
│   │   │   └── test_superhero.py
│   │   │
│   │   ├── genders_resolvers/
│   │   │   ├── test_genders_jobs_resolver.py
│   │   │   ├── test_genders_sports_resolver.py
│   │   │   ├── test_male_female_todo.py
│   │   │   └── test_nat_genders_pattern_multi.py
│   │   │
│   │   ├── jobs_resolvers/
│   │   │   │
│   │   │   ├── mens/
│   │   │   │   ├── test_mens.py
│   │   │   │   └── test_prefix_bot_mens.py
│   │   │   │
│   │   │   ├── relegin_jobs_nats_jobs/
│   │   │   │   └── test_new_jobs_resolver_label.py
│   │   │   │
│   │   │   ├── relegin_jobs_new/
│   │   │   │   ├── test_relegin_jobs.py
│   │   │   │   ├── test_relegin_jobs_new.py
│   │   │   │   └── test_relegin_jobs_with_suffix.py
│   │   │   │
│   │   │   ├── womens/
│   │   │   │   ├── test_prefix_bot_womens.py
│   │   │   │   └── test_womens.py
│   │   │   │
│   │   │   ├── test_t4_2018_jobs.py
│   │   │   ├── test_t4_2018_jobs_unit.py
│   │   │   └── test_t4_2018_jobs_wheelchair.py
│   │   │
│   │   ├── jobs_resolvers_male/
│   │   │   ├── jobs_resolvers_male_all.py
│   │   │   ├── jobs_resolvers_male_inte.py
│   │   │   ├── test_jobs_resolvers_male_mens.py
│   │   │   ├── test_jobs_resolvers_male_pattern.py
│   │   │   └── test_resolve_v3i_new_male.py
│   │   │
│   │   ├── languages_resolves/
│   │   │   ├── test_langs_jobs.py
│   │   │   ├── test_langs_w.py
│   │   │   ├── test_language_films.py
│   │   │   └── test_language_films_with_time.py
│   │   │
│   │   ├── nationalities_resolvers/
│   │   │   │
│   │   │   ├── nationalities_v2/
│   │   │   │   ├── test_army_nat.py
│   │   │   │   ├── test_nats_v2.py
│   │   │   │   ├── test_nats_v2_jobs.py
│   │   │   │   └── test_te_2018_with_nat.py
│   │   │   │
│   │   │   ├── test_ministers_resolver.py
│   │   │   ├── test_nationalities_time_v2.py
│   │   │   └── test_secretaries.py
│   │   │
│   │   ├── relations_resolver/
│   │   │   │
│   │   │   ├── nationalities_double/
│   │   │   │   ├── test_nationalities_double_v2.py
│   │   │   │   └── test_nationalities_double_v2_rele.py
│   │   │   │
│   │   │   ├── test_countries_names_double_v2.py
│   │   │   ├── test_nationalities_not_double.py
│   │   │   ├── test_relations_resolver_int.py
│   │   │   ├── test_rele.py
│   │   │   ├── test_work_relations_female_integration.py
│   │   │   └── test_work_relations_new.py
│   │   │
│   │   ├── sports_resolvers/
│   │   │   │
│   │   │   ├── countries_names_and_sports/
│   │   │   │   ├── test_countries_names_sport_multi_v2.py
│   │   │   │   └── test_resolve_with_ends.py
│   │   │   │
│   │   │   ├── nationalities_and_sports/
│   │   │   │   ├── test_federation.py
│   │   │   │   ├── test_mans_data.py
│   │   │   │   ├── test_nats_sport_multi_v2.py
│   │   │   │   ├── test_need_improvements.py
│   │   │   │   └── test_sports_formats_oioioi.py
│   │   │   │
│   │   │   ├── raw_sports/
│   │   │   │   │
│   │   │   │   ├── raw_sports_jobs_key/
│   │   │   │   │   ├── test_raw_sports_jobs_key.py
│   │   │   │   │   └── test_sport_lab_jobs.py
│   │   │   │   │
│   │   │   │   ├── raw_sports_labels_key/
│   │   │   │   │   └── test_sport_lab_labels.py
│   │   │   │   │
│   │   │   │   ├── raw_sports_teams_key/
│   │   │   │   │   └── test_sport_lab_teams.py
│   │   │   │   │
│   │   │   │   └── test_raw_sports.py
│   │   │   │
│   │   │   ├── test_jobs_multi_sports_reslover.py
│   │   │   ├── test_main_sports_resolvers.py
│   │   │   ├── test_match_labs.py
│   │   │   ├── test_nats_and_names_open.py
│   │   │   ├── test_resolve_team_suffix.py
│   │   │   └── test_sub_teams_keys.py
│   │   │
│   │   ├── time_and_jobs_resolvers/
│   │   │   │
│   │   │   ├── year_job_origin_resolver/
│   │   │   │   ├── test_get_label_new.py
│   │   │   │   └── test_resolve_v3i.py
│   │   │   │
│   │   │   ├── year_job_resolver/
│   │   │   │   └── test_resolve_v3ii.py
│   │   │   │
│   │   │   ├── test_get_job_label.py
│   │   │   ├── test_resolve_v3i_extended.py
│   │   │   └── test_resolve_v3i_more.py
│   │   │
│   │   ├── translations_formats/
│   │   │   │
│   │   │   ├── FormatData/
│   │   │   │   ├── test_1.py
│   │   │   │   ├── test_add_after_pattern.py
│   │   │   │   ├── test_extended.py
│   │   │   │   ├── test_format_data.py
│   │   │   │   ├── test_format_data_hot.py
│   │   │   │   ├── test_format_data_nat.py
│   │   │   │   └── test_handle_texts_before_after.py
│   │   │   │
│   │   │   └── FormatDataV2/
│   │   │       ├── test_ministries_V2.py
│   │   │       ├── test_model_data_2.py
│   │   │       ├── test_multi_with_v2.py
│   │   │       ├── test_multi_with_v2_more.py
│   │   │       └── test_one_ex.py
│   │   │
│   │   ├── test_data_must_be_empty.py
│   │   └── test_sport_cup.py
│   │
│   ├── patterns_resolvers/
│   │   ├── test_country_nat_pattern.py
│   │   ├── test_country_time_pattern.py
│   │   ├── test_country_time_pattern_main.py
│   │   ├── test_nat_males_pattern.py
│   │   └── test_time_patterns_resolvers_extended.py
│   │
│   ├── sub_new_resolvers/
│   │   ├── test_parties_resolver.py
│   │   ├── test_peoples_resolver.py
│   │   ├── test_team_work_integration.py
│   │   └── test_university_resolver.py
│   │
│   ├── translations/
│   │   │
│   │   └── geo/
│   │       ├── test_labels_country_integration.py
│   │       ├── test_us_counties.py
│   │       └── test_us_counties_2.py
│   │
│   ├── translations_formats/
│   │   │
│   │   ├── DataModel/
│   │   │   ├── test_model_data_base_inte.py
│   │   │   ├── test_model_data_form_inte.py
│   │   │   ├── test_model_data_inte.py
│   │   │   ├── test_model_data_time_inte.py
│   │   │   └── test_model_data_v2_inte.py
│   │   │
│   │   ├── DataModelDouble/
│   │   │   ├── test_model_data_double_inte.py
│   │   │   ├── test_model_data_double_v2.py
│   │   │   └── test_model_multi_data_double_inte.py
│   │   │
│   │   ├── DataModelMulti/
│   │   │   └── test_model_multi_data_inte.py
│   │   │
│   │   ├── multi_data/
│   │   │   ├── test_format_multi_data.py
│   │   │   └── test_multi_data.py
│   │   │
│   │   ├── test_format_data_with_time.py
│   │   └── test_format_films_country_data_inte.py
│   │
│   └── test_by_people_or_job.py
│
├── others/
│   │
│   ├── test_some_fixes/
│   │   ├── test_fix_in_min.py
│   │   └── test_fix_in_min2.py
│   │
│   ├── test_ar_lab_no_event2.py
│   └── test_need_fixes.py
│
├── unit/
│   │
│   ├── fix/
│   │   │
│   │   ├── fixtitle/
│   │   │   ├── test_fixtitle.py
│   │   │   ├── test_fixtitle_expended.py
│   │   │   └── test_fixtitle_refactor.py
│   │   │
│   │   ├── mv_years/
│   │   │   ├── test_mv_years.py
│   │   │   ├── test_mv_years_expended.py
│   │   │   └── test_mv_years_refactor.py
│   │   │
│   │   ├── specific_normalizations/
│   │   │   ├── test_specific_normalizations.py
│   │   │   └── test_specific_normalizations_new.py
│   │   │
│   │   └── test_filter_en.py
│   │
│   ├── format_bots/
│   │   └── test_change_cat.py
│   │
│   ├── helps/
│   │   └── test_len_print.py
│   │
│   ├── legacy_bots/
│   │   │
│   │   ├── circular_dependency/
│   │   │   │
│   │   │   └── arabic_label_builder/
│   │   │       └── test_separator_fixing.py
│   │   │
│   │   ├── common_resolver_chain/
│   │   │   └── test_common_resolver_chain.py
│   │   │
│   │   ├── end_start_bots/
│   │   │   ├── test_fax2.py
│   │   │   ├── test_fax2_episodes.py
│   │   │   ├── test_fax2_temp.py
│   │   │   └── test_fax2_unit.py
│   │   │
│   │   ├── legacy_resolvers_bots/
│   │   │   │
│   │   │   ├── byc/
│   │   │   │   ├── test_bys_unit.py
│   │   │   │   └── test_make_new_by_label.py
│   │   │   │
│   │   │   ├── country2_label_bot/
│   │   │   │   ├── test_country2_label_bot.py
│   │   │   │   └── test_make_cnt_lab.py
│   │   │   │
│   │   │   ├── event_lab_bot/
│   │   │   │   └── test_event_lab_bot_unit.py
│   │   │   │
│   │   │   ├── with_years_bot/
│   │   │   │   ├── test_political_terms.py
│   │   │   │   └── test_with_years_bot.py
│   │   │   │
│   │   │   ├── year_or_typeo/
│   │   │   │   └── test_year_or_typeo_unit.py
│   │   │   │
│   │   │   └── test_bot_2018.py
│   │   │
│   │   ├── legacy_utils/
│   │   │   ├── test_joint_class.py
│   │   │   ├── test_legacy_utils.py
│   │   │   └── test_split_text.py
│   │   │
│   │   ├── make_bots/
│   │   │   ├── test_bot.py
│   │   │   ├── test_check_bot.py
│   │   │   ├── test_check_bot_unit.py
│   │   │   └── test_reg_result.py
│   │   │
│   │   ├── resolvers/
│   │   │   │
│   │   │   ├── country_resolver/
│   │   │   │   └── test_country_resolver.py
│   │   │   │
│   │   │   ├── interface/
│   │   │   │   └── test_interface.py
│   │   │   │
│   │   │   └── test_arabic_label_builder_unit.py
│   │   │
│   │   └── test_tmp_bot.py
│   │
│   ├── new/
│   │   └── test_handle_suffixes.py
│   │
│   ├── new_resolvers/
│   │   │
│   │   ├── countries_names_resolvers/
│   │   │   │
│   │   │   └── countries_names_v2/
│   │   │       └── test_countries_names_v2_unit.py
│   │   │
│   │   ├── genders_resolvers/
│   │   │   ├── test_genders_resolvers_init.py
│   │   │   ├── test_jobs_and_genders_resolver.py
│   │   │   ├── test_sports_and_genders_resolver.py
│   │   │   └── test_utils.py
│   │   │
│   │   ├── jobs_resolvers/
│   │   │   ├── test_jobs_resolvers_utils.py
│   │   │   ├── test_nats_jobs_resolver.py
│   │   │   └── test_relegin_jobs_nats_jobs.py
│   │   │
│   │   ├── jobs_resolvers_male/
│   │   │   └── test_nats_jobs_resolver_unit.py
│   │   │
│   │   ├── relations_resolver/
│   │   │   ├── test_work_relations_conflicts_p17.py
│   │   │   ├── test_work_relations_female_unit.py
│   │   │   └── test_work_relations_male.py
│   │   │
│   │   ├── sports_resolvers/
│   │   │   │
│   │   │   ├── nationalities_and_sports/
│   │   │   │   └── test_normalize.py
│   │   │   │
│   │   │   └── sport_lab_nat/
│   │   │       └── test_sport_lab_nat_unit.py
│   │   │
│   │   ├── time_and_jobs_resolvers/
│   │   │   ├── test_multi_data_formatter_year_from.py
│   │   │   └── test_resolve_v3i_unit.py
│   │   │
│   │   └── translations_formats/
│   │       │
│   │       └── FormatData/
│   │           └── test_format_data_unit.py
│   │
│   ├── patterns_resolvers/
│   │   ├── test_format_year_country_data.py
│   │   └── test_time_patterns_resolvers.py
│   │
│   ├── time_resolvers/
│   │   ├── test_match_en_return_ar.py
│   │   ├── test_time_to_arabic.py
│   │   ├── test_year_lab.py
│   │   └── test_year_lab_compare_new.py
│   │
│   ├── translations/
│   │   │
│   │   ├── data_builders/
│   │   │   ├── test_build_all_keys2.py
│   │   │   ├── test_build_films_mslslat.py
│   │   │   ├── test_build_jobs.py
│   │   │   ├── test_build_jobs_data_basic.py
│   │   │   ├── test_build_jobs_players_list.py
│   │   │   ├── test_build_labels_country.py
│   │   │   ├── test_build_nationalities.py
│   │   │   ├── test_build_sport_keys.py
│   │   │   └── test_jobs_defs.py
│   │   │
│   │   ├── geo/
│   │   │   ├── test_geo_shared.py
│   │   │   ├── test_labels_country_unit.py
│   │   │   └── test_us_counties_unit.py
│   │   │
│   │   ├── jobs/
│   │   │   ├── test_jobs_datasets.py
│   │   │   ├── test_jobs_players_and_singers.py
│   │   │   └── test_jobs_womens.py
│   │   │
│   │   ├── mixed/
│   │   │   ├── test_key_registry.py
│   │   │   └── test_mixed_translations.py
│   │   │
│   │   ├── nats/
│   │   │   ├── test_Nationality.py
│   │   │   ├── test_Nationality_2.py
│   │   │   └── test_Nationality_3.py
│   │   │
│   │   └── sports/
│   │       ├── test_games_labs.py
│   │       └── test_helpers.py
│   │
│   ├── translations_formats/
│   │   │
│   │   ├── DataModel/
│   │   │   ├── test_model_data.py
│   │   │   ├── test_model_data_base.py
│   │   │   ├── test_model_data_form.py
│   │   │   ├── test_model_data_time.py
│   │   │   └── test_model_data_v2.py
│   │   │
│   │   ├── DataModelDouble/
│   │   │   ├── test_model_data_double_unit.py
│   │   │   ├── test_model_data_double_v2_unit.py
│   │   │   └── test_model_multi_data_double.py
│   │   │
│   │   ├── DataModelMulti/
│   │   │   ├── test_model_data_v2_formater.py
│   │   │   ├── test_model_multi_data.py
│   │   │   ├── test_model_multi_data_base.py
│   │   │   ├── test_model_multi_data_year_from.py
│   │   │   └── test_model_multi_data_year_from_2.py
│   │   │
│   │   ├── test_data_new_model.py
│   │   ├── test_data_with_time.py
│   │   ├── test_import_no_cycle.py
│   │   ├── test_multi_data_unit.py
│   │   └── test_time_patterns_formats.py
│   │
│   ├── utils/
│   │   └── test_match_relation_word.py
│   │
│   └── test_event_processing.py
│
├── utils/
│   ├── dump_runner.py
│   └── resolver_runner.py
│
├── conftest.py
├── load_one_data.py
├── README.md
└── test_long_categories.py

```