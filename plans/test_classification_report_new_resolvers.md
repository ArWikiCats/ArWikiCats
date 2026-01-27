# Test Classification Report: tests/new_resolvers/

**Analysis Date**: 2026-01-27
**Scope**: All test files under `tests/new_resolvers/`

---

## Executive Summary

| Metric | Count |
|--------|-------|
| **Total Files Analyzed** | 82 |
| **Files to Move (Unit)** | 9 |
| **Files to Move (Integration)** | 64 |
| **Files to Move (E2E)** | 8 |
| **Files to Split** | 2 |
| **Files to Delete** | 1 |

---

## Classification Criteria

### Unit Tests
- Tests isolated functions/classes with mocks or single module focus
- Uses `@pytest.mark.unit` decorator
- Tests `FormatData`, `FormatDataV2`, or similar formatters directly
- Does NOT use `resolve_label_ar()` or full pipeline

### Integration Tests
- Tests interaction between 2-3 components
- Uses resolver functions directly (not `resolve_label_ar()`)
- Tests component-level functionality
- No mocks, tests actual integration

### E2E Tests
- Uses `resolve_label_ar()` or `resolve_arabic_category_label()`
- Tests the full system end-to-end
- Uses real category inputs

---

## Detailed Classification Table

### 1. Translations Formats - FormatData (8 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `translations_formats/FormatData/test_format_data_nat.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_extended.py` | integration | MOVE_ONLY | 11 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_1.py` | integration | MOVE_ONLY | 17 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_add_after_pattern.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_format_data_hot.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_format_data_unit.py` | **unit** | MOVE_ONLY | 13 | `tests/unit/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_format_data.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/translations_formats/FormatData/` |
| `translations_formats/FormatData/test_handle_texts_before_after.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/translations_formats/FormatData/` |

### 2. Translations Formats - FormatDataV2 (5 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `translations_formats/FormatDataV2/test_one_ex.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/translations_formats/FormatDataV2/` |
| `translations_formats/FormatDataV2/test_multi_with_v2.py` | integration | MOVE_ONLY | 19 | `tests/integration/new_resolvers/translations_formats/FormatDataV2/` |
| `translations_formats/FormatDataV2/test_multi_with_v2_more.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/translations_formats/FormatDataV2/` |
| `translations_formats/FormatDataV2/test_model_data_2.py` | integration | MOVE_ONLY | 10 | `tests/integration/new_resolvers/translations_formats/FormatDataV2/` |
| `translations_formats/FormatDataV2/test_ministries_V2.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/translations_formats/FormatDataV2/` |

### 3. Time and Jobs Resolvers (3 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `time_and_jobs_resolvers/test_resolve_v3i_unit.py` | **unit** | MOVE_ONLY | 3 | `tests/unit/new_resolvers/time_and_jobs_resolvers/` |
| `time_and_jobs_resolvers/test_multi_data_formatter_year_from.py` | **unit** | MOVE_ONLY | 3 | `tests/unit/new_resolvers/time_and_jobs_resolvers/` |
| `time_and_jobs_resolvers/year_job_resolver/test_resolve_v3ii.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_resolver/` |
| `time_and_jobs_resolvers/year_job_origin_resolver/test_resolve_v3i.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/` |
| `time_and_jobs_resolvers/year_job_origin_resolver/test_get_label_new.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/` |

### 4. Jobs Resolvers (12 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `jobs_resolvers/relegin_jobs_nats_jobs/test_new_jobs_resolver_label.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_nats_jobs/` |
| `jobs_resolvers/test_t4_2018_jobs_unit.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/jobs_resolvers/` |
| `jobs_resolvers/test_nats_jobs_resolver.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/jobs_resolvers/` |
| `jobs_resolvers/mens/test_mens.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/jobs_resolvers/mens/` |
| `jobs_resolvers/mens/test_prefix_bot_mens.py` | integration | MOVE_ONLY | 6 | `tests/integration/new_resolvers/jobs_resolvers/mens/` |
| `jobs_resolvers/relegin_jobs_new/test_relegin_jobs.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/` |
| `jobs_resolvers/relegin_jobs_new/test_relegin_jobs_new.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/` |
| `jobs_resolvers/relegin_jobs_new/test_relegin_jobs_with_suffix.py` | integration | MOVE_ONLY | 6 | `tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/` |
| `jobs_resolvers/test_t4_2018_jobs.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/jobs_resolvers/` |
| `jobs_resolvers/test_t4_2018_jobs_wheelchair.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/jobs_resolvers/` |
| `jobs_resolvers/womens/test_womens.py` | integration | MOVE_ONLY | 8 | `tests/integration/new_resolvers/jobs_resolvers/womens/` |
| `jobs_resolvers/womens/test_prefix_bot_womens.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/jobs_resolvers/womens/` |

### 5. Sports Resolvers (18 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `sports_resolvers/test_main_sports_resolvers.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/sports_resolvers/` |
| `sports_resolvers/test_sports_new.py` | **e2e** | MOVE_ONLY | 3 | `tests/e2e/new_resolvers/sports_resolvers/` |
| `sports_resolvers/test_jobs_multi_sports_reslover.py` | integration | MOVE_ONLY | 5 | `tests/integration/new_resolvers/sports_resolvers/` |
| `sports_resolvers/test_nats_and_names_open.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/sports_resolvers/` |
| `sports_resolvers/test_match_labs.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/sports_resolvers/` |
| `sports_resolvers/test_resolve_team_suffix.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/sports_resolvers/` |
| `sports_resolvers/nationalities_and_sports/test_normalize.py` | **unit** | MOVE_ONLY | 3 | `tests/unit/new_resolvers/sports_resolvers/nationalities_and_sports/` |
| `sports_resolvers/nationalities_and_sports/test_federation.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/` |
| `sports_resolvers/nationalities_and_sports/test_nats_sport_multi_v2.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/` |
| `sports_resolvers/nationalities_and_sports/test_need_improvements.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/` |
| `sports_resolvers/nationalities_and_sports/test_sports_formats_oioioi.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/` |
| `sports_resolvers/countries_names_and_sports/test_countries_names_sport_multi_v2.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/sports_resolvers/countries_names_and_sports/` |
| `sports_resolvers/countries_names_and_sports/test_resolve_with_ends.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/sports_resolvers/countries_names_and_sports/` |
| `sports_resolvers/sport_lab_nat/test_sport_lab_nat_compare.py` | **e2e** | MOVE_ONLY | 4 | `tests/e2e/new_resolvers/sports_resolvers/sport_lab_nat/` |
| `sports_resolvers/sport_lab_nat/test_sport_lab_nat_unit.py` | **unit** | MOVE_ONLY | 3 | `tests/unit/new_resolvers/sports_resolvers/sport_lab_nat/` |
| `sports_resolvers/raw_sports/test_raw_sports.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/sports_resolvers/raw_sports/` |
| `sports_resolvers/raw_sports/raw_sports_jobs_key/test_sport_lab_jobs.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/` |
| `sports_resolvers/raw_sports/raw_sports_jobs_key/test_raw_sports_jobs_key.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/` |
| `sports_resolvers/raw_sports/raw_sports_labels_key/test_sport_lab_labels.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_labels_key/` |
| `sports_resolvers/raw_sports/raw_sports_teams_key/test_sport_lab_teams.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_teams_key/` |

### 6. Countries Names Resolvers (11 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `countries_names_resolvers/countries_names_v2/test_countries_names_v2.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/` |
| `countries_names_resolvers/countries_names_v2/test_countries_names_v2_more.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/` |
| `countries_names_resolvers/countries_names_v2/test_countries_names_v2_unit.py` | **unit** | MOVE_ONLY | 6 | `tests/unit/new_resolvers/countries_names_resolvers/countries_names_v2/` |
| `countries_names_resolvers/countries_names_v2/test_army.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/` |
| `countries_names_resolvers/test_countries_names.py` | **mixed** | **SPLIT** | 4 | See split details below |
| `countries_names_resolvers/test_countries_names2.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/countries_names_resolvers/` |
| `countries_names_resolvers/test_geo_names_formats.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/countries_names_resolvers/` |
| `countries_names_resolvers/test_us_states.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/countries_names_resolvers/` |
| `countries_names_resolvers/medalists_resolvers/test_countries_names_medalists.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/countries_names_resolvers/medalists_resolvers/` |
| `countries_names_resolvers/medalists_resolvers/test_olympic_event_translations_type_tables.py` | **e2e** | MOVE_ONLY | 2 | `tests/e2e/new_resolvers/countries_names_resolvers/medalists_resolvers/` |
| `countries_names_resolvers/medalists_resolvers/test_with_olympics.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/countries_names_resolvers/medalists_resolvers/` |

### 7. Films Resolvers (12 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `films_resolvers/test_compare/test_with_time.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/test_compare/` |
| `films_resolvers/test_compare/test_Films.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/test_compare/` |
| `films_resolvers/test_compare/test_resolve_films_with_nat.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/test_compare/` |
| `films_resolvers/test_films_and_others_bot.py` | **e2e** | MOVE_ONLY | 2 | `tests/e2e/new_resolvers/films_resolvers/` |
| `films_resolvers/film_keys_bot/test_films_keys2.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/film_keys_bot/` |
| `films_resolvers/film_keys_bot/test_films_keys2_batch.py` | integration | MOVE_ONLY | 2 | `tests/integration/new_resolvers/films_resolvers/film_keys_bot/` |
| `films_resolvers/film_keys_bot/test_get_Films_key_CAO.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/film_keys_bot/` |
| `films_resolvers/film_keys_bot/test_film_keys_bot_resolve.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/film_keys_bot/` |
| `films_resolvers/test_resolve_films.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/films_resolvers/` |
| `films_resolvers/test_resolve_films_labels_and_time.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/films_resolvers/` |
| `films_resolvers/test_resolve_films_main.py` | integration | MOVE_ONLY | 1 | `tests/integration/new_resolvers/films_resolvers/` |

### 8. Relations Resolver (10 files)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `relations_resolver/test_rele.py` | integration | MOVE_ONLY | 16 | `tests/integration/new_resolvers/relations_resolver/` |
| `relations_resolver/test_work_relations_conflicts_p17.py` | **unit** | MOVE_ONLY | 6 | `tests/unit/new_resolvers/relations_resolver/` |
| `relations_resolver/test_work_relations_male.py` | **unit** | MOVE_ONLY | 6 | `tests/unit/new_resolvers/relations_resolver/` |
| `relations_resolver/test_work_relations_female.py` | **mixed** | **SPLIT** | 11 | See split details below |
| `relations_resolver/test_work_relations_new.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/relations_resolver/` |
| `relations_resolver/test_countries_names_double_v2.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/relations_resolver/` |
| `relations_resolver/test_nationalities_not_double.py` | integration | MOVE_ONLY | 3 | `tests/integration/new_resolvers/relations_resolver/` |
| `relations_resolver/nationalities_double/test_nationalities_double_v2.py` | integration | MOVE_ONLY | 4 | `tests/integration/new_resolvers/relations_resolver/nationalities_double/` |
| `relations_resolver/nationalities_double/test_nats_double_v2.py` | **DELETE** | - | 0 | File has empty test data |

### 9. Top-level Files (1 file)

| File | Type | Action | Tests | Destination |
|------|------|--------|-------|-------------|
| `test_sport_cup.py` | integration | MOVE_ONLY | 7 | `tests/integration/new_resolvers/` |

---

## Files Requiring Split

### 1. `tests/new_resolvers/countries_names_resolvers/test_countries_names.py`

**Reason**: Contains both E2E and integration tests

**Split Strategy:**

#### Create `tests/e2e/new_resolvers/countries_names_resolvers/test_countries_names_e2e.py`
```python
# Contains:
- test_resolve_main (uses resolve_label_ar)
```

#### Create `tests/integration/new_resolvers/countries_names_resolvers/test_countries_names_integration.py`
```python
# Contains:
- test_resolve_by_countries_names (uses resolve_by_countries_names)
- test_political_data_v1 (uses resolve_by_countries_names)
- test_all_dump (uses resolve_by_countries_names)
```

**Original file**: DELETE after split

---

### 2. `tests/new_resolvers/relations_resolver/test_work_relations_female.py`

**Reason**: Contains both unit and integration tests

**Split Strategy:**

#### Create `tests/unit/new_resolvers/relations_resolver/test_work_relations_female_unit.py`
```python
# Contains (marked with @pytest.mark.unit):
- test_burma_cambodia_relations_from_country_table
- test_burundi_canada_military_relations
- test_nat_women_fallback_for_singapore_luxembourg
- test_dash_variants_en_dash
- test_dash_variants_minus_sign
- test_female_suffix_not_matched_returns_empty
```

#### Create `tests/integration/new_resolvers/relations_resolver/test_work_relations_female_integration.py`
```python
# Contains (no @pytest.mark.unit):
- test_relations_big_data (uses main_relations_resolvers)
- test_work_relations_female (uses main_relations_resolvers)
- test_nato_relations_special_case (uses main_relations_resolvers)
```

**Original file**: DELETE after split

---

## Git Commands

### Create directory structure

```bash
# Create unit directories
mkdir -p tests/unit/new_resolvers/translations_formats/FormatData
mkdir -p tests/unit/new_resolvers/translations_formats/FormatDataV2
mkdir -p tests/unit/new_resolvers/time_and_jobs_resolvers
mkdir -p tests/unit/new_resolvers/sports_resolvers/nationalities_and_sports
mkdir -p tests/unit/new_resolvers/sports_resolvers/sport_lab_nat
mkdir -p tests/unit/new_resolvers/countries_names_resolvers/countries_names_v2
mkdir -p tests/unit/new_resolvers/relations_resolver

# Create integration directories
mkdir -p tests/integration/new_resolvers/translations_formats/FormatData
mkdir -p tests/integration/new_resolvers/translations_formats/FormatDataV2
mkdir -p tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_resolver
mkdir -p tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver
mkdir -p tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_nats_jobs
mkdir -p tests/integration/new_resolvers/jobs_resolvers/mens
mkdir -p tests/integration/new_resolvers/jobs_resolvers/womens
mkdir -p tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new
mkdir -p tests/integration/new_resolvers/sports_resolvers
mkdir -p tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports
mkdir -p tests/integration/new_resolvers/sports_resolvers/countries_names_and_sports
mkdir -p tests/integration/new_resolvers/sports_resolvers/sport_lab_nat
mkdir -p tests/integration/new_resolvers/sports_resolvers/raw_sports
mkdir -p tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2
mkdir -p tests/integration/new_resolvers/countries_names_resolvers/medalists_resolvers
mkdir -p tests/integration/new_resolvers/films_resolvers/test_compare
mkdir -p tests/integration/new_resolvers/films_resolvers/film_keys_bot
mkdir -p tests/integration/new_resolvers/relations_resolver
mkdir -p tests/integration/new_resolvers/relations_resolver/nationalities_double

# Create e2e directories
mkdir -p tests/e2e/new_resolvers/sports_resolvers
mkdir -p tests/e2e/new_resolvers/sports_resolvers/sport_lab_nat
mkdir -p tests/e2e/new_resolvers/countries_names_resolvers/medalists_resolvers
mkdir -p tests/e2e/new_resolvers/films_resolvers
```

### Move Unit Tests

```bash
# FormatData unit tests
git mv tests/new_resolvers/translations_formats/FormatData/test_format_data_unit.py \
    tests/unit/new_resolvers/translations_formats/FormatData/

# Time and jobs unit tests
git mv tests/new_resolvers/time_and_jobs_resolvers/test_resolve_v3i_unit.py \
    tests/unit/new_resolvers/time_and_jobs_resolvers/
git mv tests/new_resolvers/time_and_jobs_resolvers/test_multi_data_formatter_year_from.py \
    tests/unit/new_resolvers/time_and_jobs_resolvers/

# Sports unit tests
git mv tests/new_resolvers/sports_resolvers/nationalities_and_sports/test_normalize.py \
    tests/unit/new_resolvers/sports_resolvers/nationalities_and_sports/
git mv tests/new_resolvers/sports_resolvers/sport_lab_nat/test_sport_lab_nat_unit.py \
    tests/unit/new_resolvers/sports_resolvers/sport_lab_nat/

# Countries names unit tests
git mv tests/new_resolvers/countries_names_resolvers/countries_names_v2/test_countries_names_v2_unit.py \
    tests/unit/new_resolvers/countries_names_resolvers/countries_names_v2/

# Relations unit tests
git mv tests/new_resolvers/relations_resolver/test_work_relations_conflicts_p17.py \
    tests/unit/new_resolvers/relations_resolver/
git mv tests/new_resolvers/relations_resolver/test_work_relations_male.py \
    tests/unit/new_resolvers/relations_resolver/
```

### Move Integration Tests

```bash
# FormatData integration tests
git mv tests/new_resolvers/translations_formats/FormatData/test_format_data_nat.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_extended.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_1.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_add_after_pattern.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_format_data_hot.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_format_data.py \
    tests/integration/new_resolvers/translations_formats/FormatData/
git mv tests/new_resolvers/translations_formats/FormatData/test_handle_texts_before_after.py \
    tests/integration/new_resolvers/translations_formats/FormatData/

# FormatDataV2 integration tests
git mv tests/new_resolvers/translations_formats/FormatDataV2/test_one_ex.py \
    tests/integration/new_resolvers/translations_formats/FormatDataV2/
git mv tests/new_resolvers/translations_formats/FormatDataV2/test_multi_with_v2.py \
    tests/integration/new_resolvers/translations_formats/FormatDataV2/
git mv tests/new_resolvers/translations_formats/FormatDataV2/test_multi_with_v2_more.py \
    tests/integration/new_resolvers/translations_formats/FormatDataV2/
git mv tests/new_resolvers/translations_formats/FormatDataV2/test_model_data_2.py \
    tests/integration/new_resolvers/translations_formats/FormatDataV2/
git mv tests/new_resolvers/translations_formats/FormatDataV2/test_ministries_V2.py \
    tests/integration/new_resolvers/translations_formats/FormatDataV2/

# Time and jobs integration tests
git mv tests/new_resolvers/time_and_jobs_resolvers/year_job_resolver/test_resolve_v3ii.py \
    tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_resolver/
git mv tests/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/test_resolve_v3i.py \
    tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/
git mv tests/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/test_get_label_new.py \
    tests/integration/new_resolvers/time_and_jobs_resolvers/year_job_origin_resolver/

# Jobs resolvers integration tests
git mv tests/new_resolvers/jobs_resolvers/relegin_jobs_nats_jobs/test_new_jobs_resolver_label.py \
    tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_nats_jobs/
git mv tests/new_resolvers/jobs_resolvers/test_t4_2018_jobs_unit.py \
    tests/integration/new_resolvers/jobs_resolvers/
git mv tests/new_resolvers/jobs_resolvers/test_nats_jobs_resolver.py \
    tests/integration/new_resolvers/jobs_resolvers/
git mv tests/new_resolvers/jobs_resolvers/mens/test_mens.py \
    tests/integration/new_resolvers/jobs_resolvers/mens/
git mv tests/new_resolvers/jobs_resolvers/mens/test_prefix_bot_mens.py \
    tests/integration/new_resolvers/jobs_resolvers/mens/
git mv tests/new_resolvers/jobs_resolvers/relegin_jobs_new/test_relegin_jobs.py \
    tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/
git mv tests/new_resolvers/jobs_resolvers/relegin_jobs_new/test_relegin_jobs_new.py \
    tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/
git mv tests/new_resolvers/jobs_resolvers/relegin_jobs_new/test_relegin_jobs_with_suffix.py \
    tests/integration/new_resolvers/jobs_resolvers/relegin_jobs_new/
git mv tests/new_resolvers/jobs_resolvers/test_t4_2018_jobs.py \
    tests/integration/new_resolvers/jobs_resolvers/
git mv tests/new_resolvers/jobs_resolvers/test_t4_2018_jobs_wheelchair.py \
    tests/integration/new_resolvers/jobs_resolvers/
git mv tests/new_resolvers/jobs_resolvers/womens/test_womens.py \
    tests/integration/new_resolvers/jobs_resolvers/womens/
git mv tests/new_resolvers/jobs_resolvers/womens/test_prefix_bot_womens.py \
    tests/integration/new_resolvers/jobs_resolvers/womens/

# Sports resolvers integration tests
git mv tests/new_resolvers/sports_resolvers/test_main_sports_resolvers.py \
    tests/integration/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/test_jobs_multi_sports_reslover.py \
    tests/integration/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/test_nats_and_names_open.py \
    tests/integration/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/test_match_labs.py \
    tests/integration/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/test_resolve_team_suffix.py \
    tests/integration/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/nationalities_and_sports/test_federation.py \
    tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/
git mv tests/new_resolvers/sports_resolvers/nationalities_and_sports/test_nats_sport_multi_v2.py \
    tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/
git mv tests/new_resolvers/sports_resolvers/nationalities_and_sports/test_need_improvements.py \
    tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/
git mv tests/new_resolvers/sports_resolvers/nationalities_and_sports/test_sports_formats_oioioi.py \
    tests/integration/new_resolvers/sports_resolvers/nationalities_and_sports/
git mv tests/new_resolvers/sports_resolvers/countries_names_and_sports/test_countries_names_sport_multi_v2.py \
    tests/integration/new_resolvers/sports_resolvers/countries_names_and_sports/
git mv tests/new_resolvers/sports_resolvers/countries_names_and_sports/test_resolve_with_ends.py \
    tests/integration/new_resolvers/sports_resolvers/countries_names_and_sports/
git mv tests/new_resolvers/sports_resolvers/raw_sports/test_raw_sports.py \
    tests/integration/new_resolvers/sports_resolvers/raw_sports/
git mv tests/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/test_sport_lab_jobs.py \
    tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/
git mv tests/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/test_raw_sports_jobs_key.py \
    tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_jobs_key/
git mv tests/new_resolvers/sports_resolvers/raw_sports/raw_sports_labels_key/test_sport_lab_labels.py \
    tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_labels_key/
git mv tests/new_resolvers/sports_resolvers/raw_sports/raw_sports_teams_key/test_sport_lab_teams.py \
    tests/integration/new_resolvers/sports_resolvers/raw_sports/raw_sports_teams_key/

# Countries names integration tests
git mv tests/new_resolvers/countries_names_resolvers/countries_names_v2/test_countries_names_v2.py \
    tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/
git mv tests/new_resolvers/countries_names_resolvers/countries_names_v2/test_countries_names_v2_more.py \
    tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/
git mv tests/new_resolvers/countries_names_resolvers/countries_names_v2/test_army.py \
    tests/integration/new_resolvers/countries_names_resolvers/countries_names_v2/
git mv tests/new_resolvers/countries_names_resolvers/test_countries_names2.py \
    tests/integration/new_resolvers/countries_names_resolvers/
git mv tests/new_resolvers/countries_names_resolvers/test_geo_names_formats.py \
    tests/integration/new_resolvers/countries_names_resolvers/
git mv tests/new_resolvers/countries_names_resolvers/test_us_states.py \
    tests/integration/new_resolvers/countries_names_resolvers/
git mv tests/new_resolvers/countries_names_resolvers/medalists_resolvers/test_countries_names_medalists.py \
    tests/integration/new_resolvers/countries_names_resolvers/medalists_resolvers/
git mv tests/new_resolvers/countries_names_resolvers/medalists_resolvers/test_with_olympics.py \
    tests/integration/new_resolvers/countries_names_resolvers/medalists_resolvers/

# Films integration tests
git mv tests/new_resolvers/films_resolvers/test_compare/test_with_time.py \
    tests/integration/new_resolvers/films_resolvers/test_compare/
git mv tests/new_resolvers/films_resolvers/test_compare/test_Films.py \
    tests/integration/new_resolvers/films_resolvers/test_compare/
git mv tests/new_resolvers/films_resolvers/test_compare/test_resolve_films_with_nat.py \
    tests/integration/new_resolvers/films_resolvers/test_compare/
git mv tests/new_resolvers/films_resolvers/film_keys_bot/test_films_keys2.py \
    tests/integration/new_resolvers/films_resolvers/film_keys_bot/
git mv tests/new_resolvers/films_resolvers/film_keys_bot/test_films_keys2_batch.py \
    tests/integration/new_resolvers/films_resolvers/film_keys_bot/
git mv tests/new_resolvers/films_resolvers/film_keys_bot/test_get_Films_key_CAO.py \
    tests/integration/new_resolvers/films_resolvers/film_keys_bot/
git mv tests/new_resolvers/films_resolvers/film_keys_bot/test_film_keys_bot_resolve.py \
    tests/integration/new_resolvers/films_resolvers/film_keys_bot/
git mv tests/new_resolvers/films_resolvers/test_resolve_films.py \
    tests/integration/new_resolvers/films_resolvers/
git mv tests/new_resolvers/films_resolvers/test_resolve_films_labels_and_time.py \
    tests/integration/new_resolvers/films_resolvers/
git mv tests/new_resolvers/films_resolvers/test_resolve_films_main.py \
    tests/integration/new_resolvers/films_resolvers/

# Relations integration tests
git mv tests/new_resolvers/relations_resolver/test_rele.py \
    tests/integration/new_resolvers/relations_resolver/
git mv tests/new_resolvers/relations_resolver/test_work_relations_new.py \
    tests/integration/new_resolvers/relations_resolver/
git mv tests/new_resolvers/relations_resolver/test_countries_names_double_v2.py \
    tests/integration/new_resolvers/relations_resolver/
git mv tests/new_resolvers/relations_resolver/test_nationalities_not_double.py \
    tests/integration/new_resolvers/relations_resolver/
git mv tests/new_resolvers/relations_resolver/nationalities_double/test_nationalities_double_v2.py \
    tests/integration/new_resolvers/relations_resolver/nationalities_double/

# Top-level integration
git mv tests/new_resolvers/test_sport_cup.py \
    tests/integration/new_resolvers/
```

### Move E2E Tests

```bash
# Sports e2e
git mv tests/new_resolvers/sports_resolvers/test_sports_new.py \
    tests/e2e/new_resolvers/sports_resolvers/
git mv tests/new_resolvers/sports_resolvers/sport_lab_nat/test_sport_lab_nat_compare.py \
    tests/e2e/new_resolvers/sports_resolvers/sport_lab_nat/

# Countries names e2e
git mv tests/new_resolvers/countries_names_resolvers/medalists_resolvers/test_olympic_event_translations_type_tables.py \
    tests/e2e/new_resolvers/countries_names_resolvers/medalists_resolvers/

# Films e2e
git mv tests/new_resolvers/films_resolvers/test_films_and_others_bot.py \
    tests/e2e/new_resolvers/films_resolvers/
```

### Handle Split Files (Manual)

```bash
# For test_countries_names.py - needs manual split first
# For test_work_relations_female.py - needs manual split first
```

### Delete Empty/Invalid File

```bash
# File with empty test data
git rm tests/new_resolvers/relations_resolver/nationalities_double/test_nats_double_v2.py
```

---

## Summary by Type

| Type | Count | Percentage |
|------|-------|------------|
| **Unit** | 9 | 11% |
| **Integration** | 64 | 78% |
| **E2E** | 8 | 10% |
| **Mixed (Split)** | 2 | 2% |
| **Delete** | 1 | 1% |

---

## Notes

1. **test_t4_2018_jobs_unit.py** is misnamed - it's actually an integration test, not a unit test

2. **test_nats_double_v2.py** is marked for deletion as it contains only empty test data dictionaries

3. Two files require manual splitting before moving:
   - `test_countries_names.py` (E2E + Integration)
   - `test_work_relations_female.py` (Unit + Integration)

4. No `conftest.py` files are included in this report - they should be preserved in their current locations

5. After moving tests, ensure `pytest.ini` or `pyproject.toml` test discovery patterns are updated if necessary
