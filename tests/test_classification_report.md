# Test Classification Report for ArWikiCats

**Generated:** 2026-01-27
**Analysis Agent:** Task tool with Explore subagent

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **Total Files Analyzed** | 168 |
| **Files to Move Only** | 21 |
| **Files to Split** | 6 |
| **Files to Delete** | 38 |
| **Already Classified** | 103 |

## Test Type Breakdown

| Type | File Count | Est. Test Cases |
|------|------------|-----------------|
| **Unit** | 108 | ~6,500+ |
| **Integration** | 7 | ~2,800+ |
| **E2E** | 53 | ~4,500+ |

---

## Classification Criteria

### Unit Tests (`tests/unit/`)
- Test individual functions/classes in isolation
- Do NOT use `resolve_label_ar()` or `resolve_arabic_category_label()`
- Do NOT use `batch_resolve_labels()` or `EventProcessor`
- Test a single function from a single module
- May use mocks for dependencies (monkeypatch, unittest.mock)

### Integration Tests (`tests/integration/`)
- Test interaction between 2-3 components
- May use a resolver directly but not the full chain
- Do NOT use `resolve_label_ar()` (that's e2e)

### E2E Tests (`tests/e2e/`)
- Use `resolve_label_ar()` or `resolve_arabic_category_label()`
- Use real category inputs
- Test the final result only

---

## Detailed Classification Table: Files Requiring Action

### E2E Tests (MOVE_ONLY to `tests/e2e/`)

| File | Tests | Destination |
|------|-------|-------------|
| `tests/event_lists/deaths/test_deaths.py` | ~188 | `tests/e2e/deaths/test_deaths.py` |
| `tests/event_lists/deaths/test_deaths_2.py` | ~382 | `tests/e2e/deaths/test_deaths_2.py` |
| `tests/event_lists/test_2.py` | ~353 | `tests/e2e/test_2.py` |
| `tests/event_lists/test_3.py` | ~768 | `tests/e2e/test_3.py` |
| `tests/event_lists/test_sports_events.py` | ~770 | `tests/e2e/test_sports_events.py` |
| `tests/event_lists/test_sports_events2.py` | ~200 | `tests/e2e/test_sports_events2.py` |
| `tests/event_lists/test_classical_musicians.py` | ~650 | `tests/e2e/test_classical_musicians.py` |
| `tests/event_lists/test_classical_composers_fix.py` | ~650 | `tests/e2e/test_classical_composers_fix.py` |
| `tests/event_lists/globals/*.py` (30 files) | ~300+ | `tests/e2e/event_lists_globals/` |
| `tests/event_lists/importants/*.py` (10 files) | ~15+ | `tests/e2e/event_lists_importants/` |
| `tests/event_lists/jobs_bots/*.py` (4 files) | ~30+ | `tests/e2e/event_lists_jobs_bots/` |
| `tests/event_lists/new_data_new_update/*.py` (4 files) | ~4 | `tests/e2e/event_lists_new_data/` |
| `tests/event_lists/people/*.py` (2 files) | ~100+ | `tests/e2e/event_lists_people/` |
| `tests/event_lists/squad_title_bot/*.py` (2 files) | ~2 | `tests/e2e/event_lists_squad_title_bot/` |
| `tests/event_lists/womens/*.py` (3 files) | ~50+ | `tests/e2e/event_lists_womens/` |
| `tests/event_lists/papua_new_guinea/test_papua_new_guinea.py` | 1 | `tests/e2e/test_papua_new_guinea.py` |
| `tests/event_lists/test_northern_ireland/test_northern_ireland.py` | 1 | `tests/e2e/test_northern_ireland.py` |
| `tests/event_lists/test_nuns.py` | 1 | `tests/e2e/test_nuns.py` |
| `tests/event_lists/test_non/*.py` (3 files) | ~8 | `tests/e2e/event_lists_test_non/` |
| `tests/event_lists/test_religions/*.py` (2 files) | ~3 | `tests/e2e/event_lists_test_religions/` |
| `tests/event_lists/test_south_african.py` | 1 | `tests/e2e/test_south_african.py` |
| `tests/event_lists/test_yy2_non.py` | 1 | `tests/e2e/test_yy2_non.py` |
| `tests/event_lists/test_t4_2018_jobs_old_data.py` | 1 | `tests/e2e/test_t4_2018_jobs_old_data.py` |
| `tests/legacy_bots/circular_dependency/arabic_label_builder/*.py` (7 files) | ~150+ | `tests/e2e/legacy_bots/arabic_label_builder/` |
| `tests/legacy_bots/circular_dependency/country2_label_bot/*.py` (3 files) | ~80+ | `tests/e2e/legacy_bots/country2_label_bot/` |
| `tests/legacy_bots/common_resolver_chain/*.py` (2 files) | ~40+ | `tests/e2e/legacy_bots/common_resolver_chain/` |
| `tests/legacy_bots/end_start_bots/*.py` (2 files) | ~15+ | `tests/e2e/legacy_bots/end_start_bots/` |
| `tests/legacy_bots/event_lab_bot/*.py` (2 files) | ~10+ | `tests/e2e/legacy_bots/event_lab_bot/` |
| `tests/legacy_bots/make_bots/*.py` (2 files) | ~10+ | `tests/e2e/legacy_bots/make_bots/` |

### Unit Tests (MOVE_ONLY to `tests/unit/`)

| File | Tests | Destination |
|------|-------|-------------|
| `tests/fix/fixtitle/test_fixtitle.py` | ~5 | `tests/unit/fix/fixtitle/test_fixtitle.py` |
| `tests/fix/fixtitle/test_fixtitle_expended.py` | ~15 | `tests/unit/fix/fixtitle/test_fixtitle_expended.py` |
| `tests/fix/fixtitle/test_fixtitle_refactor.py` | ~30 | `tests/unit/fix/fixtitle/test_fixtitle_refactor.py` |
| `tests/fix/mv_years/*.py` (4 files) | ~50+ | `tests/unit/fix/mv_years/` |
| `tests/fix/specific_normalizations/*.py` (2 files) | ~10+ | `tests/unit/fix/specific_normalizations/` |
| `tests/time_resolvers/test_time_to_arabic/*.py` (4 files) | ~160+ | `tests/unit/time_resolvers/test_time_to_arabic/` |
| `tests/main_processers/test_list_cat_format.py` | 1 | `tests/unit/main_processers/test_list_cat_format.py` |
| `tests/sub_new_resolvers/test_peoples_resolver.py` | ~150+ | `tests/unit/resolvers/test_peoples_resolver.py` |
| `tests/sub_new_resolvers/test_parties_resolver.py` | 6 | `tests/unit/resolvers/test_parties_resolver.py` |
| `tests/sub_new_resolvers/test_team_work.py` | ~150+ | `tests/unit/resolvers/test_team_work.py` |
| `tests/sub_new_resolvers/test_university_resolver.py` | ~100+ | `tests/unit/resolvers/test_university_resolver.py` |
| `tests/translations/geo/test_geo_shared.py` | ~50+ | `tests/unit/translations/geo/test_geo_shared.py` |
| `tests/translations/mixed/*.py` (2 files) | ~20+ | `tests/unit/translations/mixed/` |
| `tests/translations/sports/*.py` (2 files) | ~30+ | `tests/unit/translations/sports/` |
| `tests/translations/jobs/*.py` (2 files) | ~25+ | `tests/unit/translations/jobs/` |

### Integration Tests (MOVE_ONLY to `tests/integration/`)

| File | Tests | Destination |
|------|-------|-------------|
| `tests/patterns_resolvers/country_time_pattern/test_country_time_pattern_main.py` | 6 | `tests/integration/patterns_resolvers/test_country_time_pattern_main.py` |
| `tests/patterns_resolvers/time_patterns_resolvers/test_time_patterns_resolvers_extended.py` | ~100+ | `tests/integration/patterns_resolvers/test_time_patterns_extended.py` |
| `tests/new_resolvers/relations_resolver/test_rele_big_data.py` | ~2500+ | `tests/integration/resolvers/test_relations_big_data.py` |

---

## Files Requiring Split (SPLIT)

| Source File | Split Details |
|-------------|---------------|
| `tests/new_resolvers/films_resolvers/test_films_key_cao_keys.py` | **Split into:**<br>- `tests/unit/resolvers/films/test_films_key_cao_keys_unit.py` (unit tests)<br>- `tests/integration/resolvers/films/test_films_key_cao_keys_integration.py` (integration tests) |
| `tests/new_resolvers/genders_resolvers/test_male_female_todo.py` | **Split into:**<br>- `tests/unit/resolvers/genders/test_male_female_unit.py` (unit tests)<br>- `tests/e2e/genders/test_male_female_e2e.py` (e2e tests with dump markers) |
| `tests/translations/test_by_type.py` | **Split into:**<br>- `tests/unit/translations/test_by_type_unit.py` (unit tests)<br>- `tests/e2e/translations/test_by_type_e2e.py` (e2e tests with dump_runner) |
| `tests/patterns_resolvers/country_time_pattern/test_country_time_pattern.py` | **Split into:**<br>- `tests/unit/patterns_resolvers/test_country_time_pattern_unit.py` (unit tests)<br>- `tests/integration/patterns_resolvers/test_country_time_pattern_integration.py` (integration tests) |
| `tests/new_resolvers/countries_names_resolvers/test_countries_names_v2.py` | **Split into:**<br>- `tests/unit/resolvers/countries/test_countries_names_v2_unit.py` (unit tests)<br>- `tests/integration/resolvers/countries/test_countries_names_v2_integration.py` (integration tests) |
| `tests/new_resolvers/countries_names_resolvers/test_countries_names_v2_more.py` | **Split into:**<br>- `tests/unit/resolvers/countries/test_countries_names_v2_more_unit.py` (unit tests)<br>- `tests/integration/resolvers/countries/test_countries_names_v2_more_integration.py` (integration tests) |

---

## Files to Delete (DELETE)

These are skip/test-fix files that should be removed:

| File | Reason |
|------|--------|
| `tests/to_fix_skip/test_empty.py` | Empty/placeholder |
| `tests/to_fix_skip/test_Jobs_22_empty.py` | Empty test data |
| `tests/to_fix_skip/test_papua_new_guinean.py` | Empty test data |
| `tests/to_fix_skip/text_cultural_depictions_2.py` | Tests to fix |
| `tests/to_fix_skip/text_non_fiction.py` | Tests to fix |
| `tests/to_fix_skip/text_to_fix.py` | Tests to fix |
| `tests/load_one_data.py` | Utility file (not a test) |

---

## Git Commands

```bash
# =====================================================
# E2E: Move event_lists to tests/e2e/ ✔️
# =====================================================
# git mv tests/event_lists/deaths tests/e2e/deaths
# git mv tests/event_lists/test_2.py tests/e2e/test_2.py
# git mv tests/event_lists/test_3.py tests/e2e/test_3.py
# git mv tests/event_lists/test_sports_events.py tests/e2e/test_sports_events.py
# git mv tests/event_lists/test_sports_events2.py tests/e2e/test_sports_events2.py
# git mv tests/event_lists/test_classical_musicians.py tests/e2e/test_classical_musicians.py
# git mv tests/event_lists/test_classical_composers_fix.py tests/e2e/test_classical_composers_fix.py
# git mv tests/event_lists/globals tests/e2e/event_lists_globals
# git mv tests/event_lists/importants tests/e2e/event_lists_importants
# git mv tests/event_lists/jobs_bots tests/e2e/event_lists_jobs_bots
# git mv tests/event_lists/new_data_new_update tests/e2e/event_lists_new_data
# git mv tests/event_lists/people tests/e2e/event_lists_people
# git mv tests/event_lists/squad_title_bot tests/e2e/event_lists_squad_title_bot
# git mv tests/event_lists/womens tests/e2e/event_lists_womens
# git mv tests/event_lists/papua_new_guinea tests/e2e/event_lists_papua_new_guinea
# git mv tests/event_lists/test_northern_ireland tests/e2e/test_northern_ireland
# git mv tests/event_lists/test_non tests/e2e/event_lists_test_non
# git mv tests/event_lists/test_religions tests/e2e/event_lists_test_religions
# git mv tests/event_lists/test_nuns.py tests/e2e/test_nuns.py
# git mv tests/event_lists/test_south_african.py tests/e2e/test_south_african.py
# git mv tests/event_lists/test_yy2_non.py tests/e2e/test_yy2_non.py
# git mv tests/event_lists/test_t4_2018_jobs_old_data.py tests/e2e/test_t4_2018_jobs_old_data.py

# =====================================================
# E2E: Move legacy_bots to tests/e2e/legacy_bots/
# =====================================================
# git mv tests/legacy_bots/circular_dependency/arabic_label_builder tests/e2e/legacy_bots/arabic_label_builder
git mv tests/legacy_bots/circular_dependency/country2_label_bot tests/e2e/legacy_bots/country2_label_bot
git mv tests/legacy_bots/common_resolver_chain tests/e2e/legacy_bots/common_resolver_chain
git mv tests/legacy_bots/end_start_bots tests/e2e/legacy_bots/end_start_bots
git mv tests/legacy_bots/event_lab_bot tests/e2e/legacy_bots/event_lab_bot
git mv tests/legacy_bots/make_bots tests/e2e/legacy_bots/make_bots

# =====================================================
# UNIT: Move fix/ to tests/unit/fix/ ✔️
# =====================================================
# git mv tests/fix/fixtitle tests/unit/fix/fixtitle
# git mv tests/fix/mv_years tests/unit/fix/mv_years
# git mv tests/fix/specific_normalizations tests/unit/fix/specific_normalizations

# =====================================================
# UNIT: Move time_resolvers/ to tests/unit/time_resolvers/ ✔️
# =====================================================
# git mv tests/time_resolvers/test_time_to_arabic tests/unit/time_resolvers

# =====================================================
# UNIT: Move main_processers/ to tests/unit/main_processers/ ✔️
# =====================================================
# git mv tests/main_processers/test_list_cat_format.py tests/unit/main_processers/

# =====================================================
# UNIT: Move sub_new_resolvers/ to tests/unit/resolvers/ ✔️
# =====================================================
# git mv tests/sub_new_resolvers/test_peoples_resolver.py tests/unit/resolvers/
# git mv tests/sub_new_resolvers/test_parties_resolver.py tests/unit/resolvers/
# git mv tests/sub_new_resolvers/test_team_work.py tests/unit/resolvers/
# git mv tests/sub_new_resolvers/test_university_resolver.py tests/unit/resolvers/

# =====================================================
# UNIT: Move translations/ to tests/unit/translations/
# =====================================================
# git mv tests/translations/geo/test_geo_shared.py tests/unit/translations/geo/
# git mv tests/translations/mixed tests/unit/translations/
# git mv tests/translations/sports tests/unit/translations/
git mv tests/translations/jobs tests/unit/translations/

# =====================================================
# INTEGRATION: Move patterns_resolvers/ to tests/integration/patterns_resolvers/
# =====================================================
git mv tests/patterns_resolvers/country_time_pattern/test_country_time_pattern_main.py tests/integration/patterns_resolvers/
git mv tests/patterns_resolvers/time_patterns_resolvers/test_time_patterns_resolvers_extended.py tests/integration/patterns_resolvers/

# =====================================================
# INTEGRATION: Move relations_resolver/ to tests/integration/resolvers/
# =====================================================
git mv tests/new_resolvers/relations_resolver/test_rele_big_data.py tests/integration/resolvers/test_relations_big_data.py

# =====================================================
# DELETE: Remove to_fix_skip files
# =====================================================
git rm tests/to_fix_skip/test_empty.py
git rm tests/to_fix_skip/test_Jobs_22_empty.py
git rm tests/to_fix_skip/test_papua_new_guinean.py
git rm tests/to_fix_skip/text_cultural_depictions_2.py
git rm tests/to_fix_skip/text_non_fiction.py
git rm tests/to_fix_skip/text_to_fix.py

# =====================================================
# SPLIT: Files that need manual splitting
# =====================================================
# These files need to be manually split into unit/integration/e2e components:
#
# 1. tests/new_resolvers/films_resolvers/test_films_key_cao_keys.py
# 2. tests/new_resolvers/genders_resolvers/test_male_female_todo.py
# 3. tests/translations/test_by_type.py
# 4. tests/patterns_resolvers/country_time_pattern/test_country_time_pattern.py
# 5. tests/new_resolvers/countries_names_resolvers/test_countries_names_v2.py
# 6. tests/new_resolvers/countries_names_resolvers/test_countries_names_v2_more.py
```

---

## Already Classified (Skip)

The following directories are already properly organized:

- `tests/unit/` - All files are properly placed unit tests
- `tests/integration/` - All files are properly placed integration tests
- `tests/e2e/` - All files are properly placed e2e tests
- `tests/conftest.py` - Root conftest (keep)
- `tests/utils/resolver_runner.py` - Shared utility (keep)
- `tests/event_lists/unit/test_with_by.py` - Already in unit location

Most files in `tests/new_resolvers/` are properly placed unit tests and do not require moving.
