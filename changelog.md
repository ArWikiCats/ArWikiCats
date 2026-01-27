## [Add unit tests for legacy_bots module] - 2026-01-27

### Added
* **Unit tests for event_lab_bot.py:**
  - Tests for module constants (SUFFIX_EPISODES, SUFFIX_TEMPLATES, etc.)
  - Tests for `_resolve_via_chain` function
  - Tests for `translate_general_category_wrap` function
  - Tests for `event_label_work` function
  - Tests for `EventLabResolver` class methods
  - Tests for `_finalize_category_label` and `_process_category_formatting` functions
  - Tests for `event_Lab` main entry point
  - Integration-style tests for various input combinations

* **Unit tests for mk3.py:**
  - Tests for `check_country_in_tables` function
  - Tests for `add_the_in` function with various preposition scenarios
  - Tests for `added_in_new` function
  - Tests for `new_func_mk2` function
  - Tests for module constants (PREPOSITION_IN, PREPOSITION_AT, country_before_year)

* **Unit tests for year_or_typeo.py:**
  - Tests for `label_for_startwith_year_or_typeo` function
  - Tests for `LabelForStartWithYearOrTypeo` class initialization and methods
  - Tests for `replace_cat_test` static method
  - Tests for year parsing, country handling, and label finalization
  - Integration-style tests for various year formats

* **Unit tests for country_resolver.py:**
  - Tests for fallback resolver functions
  - Tests for `_validate_separators` function
  - Tests for `check_historical_prefixes` function
  - Tests for `Get_country2` function
  - Tests for `CountryLabelRetriever` class methods
  - Tests for `event2_d2` function

* **Unit tests for common_resolver_chain.py:**
  - Tests for `_lookup_country_with_in_prefix` function
  - Tests for `get_con_label` function
  - Tests for `get_lab_for_country2` function
  - Tests for `con_lookup_both` dictionary

* **Unit tests for interface.py:**
  - Tests for all Protocol classes (CountryLabelResolver, TermLabelResolver, etc.)
  - Tests for protocol implementation compliance

* **Unit tests for joint_class.py:**
  - Tests for `CountryLabelAndTermParent` class
  - Tests for prefix handling and regex year patterns

* **Unit tests for check_bot.py:**
  - Tests for `check_key_in_tables` function
  - Tests for `check_key_new_players` function
  - Tests for `add_key_new_players` function

### Changed
* Coverage for `event_lab_bot.py`: 34% → 84%
* Coverage for `mk3.py`: 19% → 83%
* Coverage for `year_or_typeo.py`: 16% → 66%
* Coverage for `country_resolver.py`: 71% → 92%
* Coverage for `common_resolver_chain.py`: 65% → 93%
* Coverage for `interface.py`: 0% → 100%
* Coverage for `joint_class.py`: 70% → 100%
* Coverage for `check_bot.py`: 65% → 100%
* Total legacy_bots module coverage: 70% → 87%
* 206 new tests added

## [Add unit and integration tests for translations_formats module] - 2026-01-27

This pull request adds comprehensive unit and integration tests for the `translations_formats` module to improve test coverage.

### Added
* **Unit tests for factory functions:**
  - `test_data_with_time.py`: Tests for `format_year_country_data` and `format_year_country_data_v2`
  - `test_data_new_model.py`: Tests for `format_films_country_data`
* **Unit tests for time patterns:**
  - `test_time_patterns_formats.py`: Tests for `LabsYearsFormat` and `MatchTimes` classes
* **Unit tests for DataModelMulti:**
  - `test_model_multi_data_base.py`: Tests for `NormalizeResult` and `MultiDataFormatterBaseHelpers`
  - `test_model_multi_data.py`: Tests for `MultiDataFormatterBase`, `MultiDataFormatterBaseYear`, `MultiDataFormatterBaseYearV2`
  - `test_model_multi_data_year_from.py`: Tests for `MultiDataFormatterYearAndFrom`
  - `test_model_multi_data_year_from_2.py`: Tests for `MultiDataFormatterYearAndFrom2`
* **Unit tests for DataModelDouble:**
  - `test_model_multi_data_double.py`: Tests for `MultiDataFormatterDataDouble`
* **Unit tests for DataModel:**
  - `test_model_data_form.py`: Tests for `FormatDataFrom`
* **Integration tests for DataModel:**
  - `test_model_data_inte.py`: Integration tests for `FormatData`
  - `test_model_data_time_inte.py`: Integration tests for `YearFormatData`
  - `test_model_data_form_inte.py`: Integration tests for `FormatDataFrom`
  - `test_model_data_base_inte.py`: Integration tests for `FormatDataBase`
  - `test_model_data_v2_inte.py`: Integration tests for `FormatDataV2`
* **Integration tests for DataModelDouble:**
  - `test_model_multi_data_double_inte.py`: Integration tests for `MultiDataFormatterDataDouble`

### Changed
* Total of 430+ new tests added across unit and integration test suites
## [Update documentation for new test categories] - 2026-01-27

This pull request updates all documentation to reflect the new test organization into 3 categories: unit, integration, and e2e.

### Changed
* Updated `README.md`:
  - Reorganized Section 8 (الاختبارات) to document the 3 test categories
  - Added examples for running tests by category (`tests/unit/`, `tests/integration/`, `tests/e2e/`)
  - Added marker-based test running (`-m unit`, `-m integration`, `-m e2e`)
  - Updated project structure to show test subdirectories
* Updated `CLAUDE.md`:
  - Added table documenting the 3 test categories with descriptions
  - Added test running commands for each category
  - Updated directory structure to show tests subdirectories
* Updated `.github/copilot-instructions.md`:
  - Updated Project Structure section to describe the 3 test categories
  - Updated test count to 28,500+ tests

## [Refactor legacy_bots package to eliminate circular dependencies] - 2026-01-26

This pull request refactors the `legacy_bots/` package to break circular dependencies using a callback injection pattern.

### Added
* Created new `resolvers/` package with clean DAG architecture:
  - `interface.py`: Protocol definitions for resolvers
  - `country_resolver.py`: Country-based label resolution
  - `arabic_label_builder.py`: Arabic label construction
  - `separator_based_resolver.py`: Separator-based resolution
  - `sub_resolver.py`: Sub-category resolution utilities
  - `factory.py`: Wires together and sets up callbacks

### Changed
* Implemented callback injection pattern to break circular imports:
  - `country_resolver.py` uses `set_fallback_resolver()` for fallback resolution
  - `country2_label_bot.py` uses `set_term_label_resolver()` for term label resolution
  - `with_years_bot.py` uses `set_translate_callback()` for translation
* Updated all dependent files to import from new resolvers package:
  - `event_lab_bot.py`, `with_years_bot.py`, `year_or_typeo.py`
* Updated all test files to import from `resolvers` instead of `circular_dependency`

### Fixed
* Eliminated circular import chain: `country_bot → general_resolver → ar_lab_bot → country_bot`
* All 4609 legacy_bots tests passing

## [Update test expectations for corrected translation outputs] - 2026-01-25

This pull request updates test expectations to align with improved Arabic translations for National Assembly categories and the Croatian War of Independence.

### Changed
* Updated test expectations in `tests/event_lists/test_south_african.py`:
  - "Women members of the National Assembly of South Africa" now expects "عضوات الجمعية الوطنية الجنوب الإفريقية" (was "عضوات الجمعية الوطنية في جنوب إفريقيا")
  - "Speakers of the National Assembly of South Africa" now expects "رؤساء الجمعية الوطنية الجنوب الإفريقية" (was "رؤساء الجمعية الوطنية في جنوب إفريقيا")
  - "Members of the National Assembly of South Africa" now expects "أعضاء الجمعية الوطنية الجنوب الإفريقية" (was "أعضاء الجمعية الوطنية في جنوب إفريقيا")
* Updated test expectation in `tests/legacy_bots/circular_dependency/country2_label_bot/test_country2_label_bot.py`:
  - "Croatian war of independence" now expects "الحرب الكرواتية في استقلال" (was "حرب الاستقلال الكرواتية")

### Fixed
* Resolved 4 test failures that occurred after translation engine improvements
* All 33,438 tests now pass with no regressions

## [Refactor RESOLVER_PIPELINE into LegacyBotsResolver class] - 2026-01-21

This pull request refactors the legacy resolver pipeline from a list-based approach to a clean, class-based implementation while maintaining 100% backward compatibility.

### Changed
* Refactored `RESOLVER_PIPELINE` list into `LegacyBotsResolver` class in `legacy_bots/__init__.py`:
  - Created structured class with 6 internal resolver methods (university, country/event, years, year/typeo, event_lab, general)
  - Each resolver method delegates to the original implementation for compatibility
  - Implemented `resolve()` public method that processes input through all resolvers in exact original order
  - Maintained `@lru_cache` decorator on `resolve()` method for performance
  - Preserved backward-compatible `legacy_resolvers()` function that delegates to class instance
* Added shared utility methods to reduce code duplication:
  - `_normalize_input()` - Common input normalization
  - `_has_blocked_prepositions()` - Shared preposition filtering logic used by multiple resolvers
* Enhanced logging with debug messages to trace which resolver modified the text

### Fixed
* Consolidated duplicated preposition-blocking logic that was previously repeated across multiple resolver implementations

### Implementation Details
* The new class maintains the exact same resolution order as the original pipeline:
  1. University categories (highest priority)
  2. Country and event-based patterns
  3. Year-based categories
  4. Year prefix patterns and typo handling
  5. General event labeling
  6. General category translation (lowest priority, catch-all)
* All 20,534 fast tests pass with 100% success rate
* Zero performance regression due to maintained caching strategy
* Code is cleaner, more maintainable, and easier to extend with new resolvers

## [Refactor legacy_bots directory for improved maintainability] - 2026-01-21

This pull request introduces a comprehensive refactoring of the `legacy_bots` directory to improve code organization, maintainability, and performance. The main themes are: centralizing data and regex patterns, creating a core module for shared functions, and refactoring the entry point to use a pipeline pattern.

### Added
* Created new directory structure under `legacy_bots/`:
  - `data/` - Centralized data mappings module
  - `utils/` - Utilities and regex patterns module
  - `core/` - Shared resolver functions module
* Added `data/mappings.py` - Pure data file containing all major dictionaries and mapping tables:
  - Number translations (`change_numb`, `change_numb_to_word`)
  - Suffix mappings (`pp_ends_with_pase`, `pp_ends_with`, `combined_suffix_mappings`)
  - Prefix mappings (`pp_start_with`)
  - Type table (`typeTable_7`)
* Added `utils/regex_hub.py` - Centralized pre-compiled regex patterns:
  - Year patterns (RE1_compile, RE2_compile, RE3_compile, RE33_compile, REGEX_SUB_YEAR)
  - General patterns (REGEX_SUB_MILLENNIUM_CENTURY, REGEX_SUB_CATEGORY_LOWERCASE)
  - "By" patterns (DUAL_BY_PATTERN, BY_MATCH_PATTERN, AND_PATTERN)
* Added `core/base_resolver.py` - Central import point for shared resolver functions:
  - Get_country2, get_KAKO, get_lab_for_country2

### Changed
* Refactored `legacy_resolvers()` function in `__init__.py` to use a pipeline pattern:
  - Replaced long `or` chains with iterable `RESOLVER_PIPELINE` list
  - Improved readability and maintainability
  - Made it easier to add/remove/reorder resolvers
* Updated legacy files to re-export from centralized modules for backward compatibility:
  - `legacy_utils/numbers1.py` - Re-exports from `data.mappings`
  - `legacy_utils/ends_keys.py` - Re-exports from `data.mappings`
  - `legacy_utils/reg_lines.py` - Re-exports from `utils.regex_hub`
  - `make_bots/bot.py` - Imports typeTable_7 from `data.mappings`
* Standardized imports across multiple files to use centralized modules:
  - `tmp_bot.py` - Updated to import from `data.mappings`
  - `make_bots/reg_result.py` - Updated to import from `utils.regex_hub`
  - `legacy_resolvers_bots/bys.py` - Updated to import from `utils.regex_hub`
  - `legacy_resolvers_bots/with_years_bot.py` - Updated to import from `data.mappings` and `utils.regex_hub`
  - `legacy_resolvers_bots/event_lab_bot.py` - Updated to import from `data.mappings`

### Fixed
* Prevented potential circular import issues by:
  - Maintaining original import patterns for modules in circular dependency chains
  - Creating core module as optional import point for future use
  - Documenting shared functions for better visibility

These changes collectively improve the maintainability and organization of the legacy_bots module while maintaining full backward compatibility. The refactoring lays the groundwork for easier future enhancements and reduces the risk of circular dependencies.

## [#314](https://github.com/MrIbrahem/ArWikiCats/pull/314) - 2026-01-07
This pull request introduces several improvements and refactoring changes to how job, language, and nationality labels are resolved and formatted across the codebase. The main themes are: expanding language and job label resolution, updating data sources for nationality mappings, and reorganizing legacy bot files for clarity. These changes enhance the flexibility and accuracy of label generation in various bots and resolvers.

**Label Resolution and Expansion**
* Added new label resolution functions for jobs and languages, notably `Lang_work` and `resolve_languages_labels`, and incorporated them into key label lookup chains and bot functions such as `event_label_work`, `_create_type_lookup_chain`, and `te_films`. This allows for more comprehensive and accurate label generation for categories involving jobs and languages.
* Expanded the formatted data used for language and job label generation with new templates for language-based categories (e.g., comedy films, singers, activists) and for jobs with nationality and religious context, improving coverage and output quality.

**Nationality Data Source Updates**
* Changed the nationality data source from `all_country_with_nat_ar` to `All_Nat` in both men's and women's job resolvers, ensuring more consistent and comprehensive country/nationality mappings.

**Bot Refactoring and Organization**
* Moved legacy bot files (`bot_te_4.py`, `prefix_bot.py`) from `make_bots/jobs_bots/` to `old_bots/` and updated import paths across the codebase to reflect this reorganization, improving maintainability and clarity.

**Job Label Resolution Logic**
* Enhanced job label resolution logic in `jobs_in_multi_sports` to use a prioritized chain of resolvers: `resolve_languages_labels`, `te4_2018_Jobs`, `Lang_work`, and `main_jobs_resolvers`, ensuring the most relevant label is selected.

**Job Data Filtering and Formatting**
* Improved filtering and formatting of job data by using a local copy (`jobs_mens_data_f`) and refining logic to exclude false or irrelevant keys, as well as supporting new label patterns such as "Dutch political artists". (Fc675d55L3R3,

These changes collectively make label generation for jobs, languages, and nationalities more robust and easier to maintain.
## [#313](https://github.com/MrIbrahem/ArWikiCats/pull/313) - 2026-01-07
This pull request includes a mix of data updates, refactoring, and performance improvements across several modules related to job, country, and by-label resolution in the ArWikiCats codebase. The most significant changes involve refactoring the job label resolution logic for better maintainability, updating and correcting translation data, and introducing caching to optimize performance for functions that load static data.

**Key changes include:**

### Refactoring and Logic Improvements

* Refactored the job label resolution pipeline to move the `new_religions_jobs_with_suffix` resolver into the main jobs resolver, simplifying logic in `t4_2018_jobs.py` and ensuring all job-related resolution routes are handled in one place. (`ArWikiCats/new_resolvers/jobs_resolvers/__init__.py`, `ArWikiCats/make_bots/countries_names_with_sports/t4_2018_jobs.py`)
* Moved definitions of `Mens_prefix`, `Mens_suffix`, and `womens_prefixes` directly into `prefix_bot.py` for better encapsulation and maintainability. (`ArWikiCats/make_bots/jobs_bots/prefix_bot.py`)
* Improved gender transformation logic to use `short_womens_jobs` instead of `Female_Jobs` for more accurate label transformations. (`ArWikiCats/make_bots/jobs_bots/prefix_bot.py`)
* Expanded and restructured gender-related keys and filtering logic in `mens.py` to better handle false positives and edge cases in job label resolution. (`ArWikiCats/new_resolvers/jobs_resolvers/mens.py`)

### Data and Translation Updates

* Added new mappings and corrected Arabic translations for various job and category labels, including updates to activists, priests, and removal of "executed" categories from multiple data files. (`ArWikiCats/jsons/jobs/activists_keys.json`, `ArWikiCats/jsons/jobs/jobs_3.json`, `ArWikiCats/jsons/jobs/jobs_Men_Womens_PP.json`, `ArWikiCats/jsons/keys/keys2_py.json`)
* Updated debug logging to use `logger.info_if_or_debug` for more informative output in several resolver modules. (`ArWikiCats/new/resolve_films_bots/__init__.py`, `ArWikiCats/new_resolvers/countries_names_resolvers/__init__.py`, `ArWikiCats/new_resolvers/jobs_resolvers/__init__.py`)

### Performance and Code Quality Enhancements

* Introduced `functools.lru_cache` to cache results of functions that load static data, improving performance for repeated lookups in multiple modules. (`ArWikiCats/ma_bots/year_or_typeo/reg_result.py`, `ArWikiCats/make_bots/reslove_relations/rele.py`, `ArWikiCats/new_resolvers/bys_new.py`)
* Renamed debug output keys in `bys_new.py` for clarity. (`ArWikiCats/new_resolvers/bys_new.py`)

### Minor Fixes and Cleanups

* Removed obsolete or redundant code, such as legacy data lookups and unused imports, to streamline the codebase. (`ArWikiCats/ma_bots/ar_lab/lab.py`, [ArWikiCats/ma_bots/ar_lab/lab.pyL320-L326](diffhunk://#diff-8896f6af8a78eac3d9c1663d38f82a01bda9e696b6a3e71c635264dbf0cd1793L320-L326))
* Improved logging in `fixlabel` for better tracking of label transformations. (`ArWikiCats/fix/fixtitle.py`)

These changes collectively improve the maintainability, accuracy, and performance of the job and category label resolution logic in the project.

## [#311](https://github.com/MrIbrahem/ArWikiCats/pull/311) - 2026-01-06

* **New Features**
  * Added comprehensive gendered nationality forms, continent/regional nationality sets, and directional nationality entries for better localization.

* **Improvements**
  * Standardized Arabic translations and adjective ordering; normalized nationality data layout and unified definite-form labels.

* **API Changes**
  * Public resolver renamed to resolve_label_ar.

* **Data Updates**
  * Added nationality keys (e.g., Northern Ireland, Botswana, Hindustani); removed numerous legacy entries (multiple South Africa items, Antigua & Barbuda, Kazakh Khanate, Monaco, and other outdated mappings).

## [#304](https://github.com/MrIbrahem/ArWikiCats/pull/304) - 2026-01-05

* **New Features**
  * Added comprehensive film and novel translation reference files and an enhanced films category lookup.

* **Bug Fixes**
  * Standardized Arabic transliterations for Oregon across geography, cities, institutions, and category labels.

* **Chores**
  * Updated test data and example datasets to reflect corrected translations and removed/added example categories.

## [#301](https://github.com/MrIbrahem/ArWikiCats/pull/301) - 2026-01-04

* **New Features**
  * Added comprehensive support for classical composers and musicians categories with improved Arabic translations.

* **Bug Fixes**
  * Corrected Arabic translations for multiple category labels across sports, jobs, regional classifications, and geophysics.

* **Tests**
  * Expanded test coverage with new parametrized test suites for validating category translations and label resolution accuracy.

## [#300](https://github.com/MrIbrahem/ArWikiCats/pull/300) - 2026-01-04

* **New Features**
  * Added Arabic translations for additional geographic locations and administrative regions.
  * Introduced new entries for jobs (baptists) and educational institution types.
  * Expanded category label support for films and nationality-based classifications.

* **Bug Fixes**
  * Corrected Arabic transliterations for multiple city and county names.
  * Updated nationality and geographic term translations for accuracy.

* **Tests**
  * Added comprehensive test coverage for category label resolution and mapping validation.

## [#299](https://github.com/MrIbrahem/ArWikiCats/pull/299) - 2026-01-04

* **Chores**
  * Removed numerous translation entries and public category mappings related to conviction/crime classifications across datasets and examples.
  * Updated CI workflow action versions.

* **Refactor**
  * Replaced dynamic JSON loading for a large mapping with an embedded in-code definition, removing the runtime file dependency.

* **Tests**
  * Pruned multiple test data cases that referenced the removed translation/category entries.

## [#298](https://github.com/MrIbrahem/ArWikiCats/pull/298) - 2025-12-31

* **Refactor**
  * Consolidated country label resolution logic across modules with expanded data sources for improved accuracy.
  * Reorganized internal label retrieval mechanisms to streamline country-based lookups.

* **Chores**
  * Updated test configuration to reduce output verbosity.

## [Update README documentation to reflect current codebase] - 2026-01-01

* **Documentation**
  * Updated test count badge from 20,000+ to 28,500+ to reflect actual test coverage.
  * Rewrote project structure section with accurate directory descriptions.
  * Added new API reference section with exported functions and classes.
  * Enhanced usage examples with new methods (resolve_label_ar, EventProcessor).
  * Updated configuration options with table format and environment variable examples.
  * Added FormatData usage examples to system extension section.
  * Updated contributor guidelines with linting tools (Black, isort, Ruff).
  * Updated roadmap with completed items (Sport Formatter v3).
  * Fixed table of contents anchor links for better navigation.

## [#285](https://github.com/MrIbrahem/ArWikiCats/pull/285) - 2025-12-31

* **Bug Fixes**
  * Standardized Arabic transliterations for geographic locations and personal names to ensure consistent terminology across all translations.

* **New Features**
  * Enhanced mapping support for female-related job categories with additional variants.
  * Improved sports category text normalization for better translation accuracy.

* **Documentation**
  * Added comprehensive refactoring strategy and testing plans to guide future development.

* **Tests**
  * Expanded test coverage with new test utilities and updated test data to reflect translation improvements.

## [#280](https://github.com/MrIbrahem/ArWikiCats/pull/280) - 2025-12-28

* **Localization Updates**
  * Added Arabic translations for newly supported countries and regions
  * Updated existing Arabic translations to improve accuracy and consistency

## [#278](https://github.com/MrIbrahem/ArWikiCats/pull/278) - 2025-12-27
This pull request introduces several improvements and refactorings to the job, nationality, and category label resolution logic, with a focus on normalization, maintainability, and improved translation accuracy. The main themes are normalization of input keys, improved label resolution order, codebase cleanup, and enhanced support for gendered and religious job categories.

**Key changes:**

### Normalization and Key Handling

* Introduced the `fix_keys` function to standardize category strings by replacing certain words (e.g., "expatriates" → "expatriate", "womens"/"women" → "female") and removing apostrophes, which is now used in multiple places to ensure consistent input for resolvers.
* Added regular expressions for handling "the" and gendered terms in category names to improve normalization.

### Label Resolution Logic

* Updated the job label resolution pipeline (`te4_2018_Jobs`) to first try `main_jobs_resolvers`, then fall back to religious jobs and nationality prefix label resolvers, improving accuracy and flexibility.
* In the main film and country name resolvers, clarified and reordered the resolution pipeline to prioritize more accurate or recent resolvers, with explanatory comments.

### Gendered and Religious Job Handling

* Refactored the handling of female job/religious category formatting to consistently use "female" instead of "womens" or "{female}", simplifying the mapping and improving match reliability.
* Updated male and female occupation label construction to use a single-line call and improved logging.
* Added new gendered key translations (e.g., "abolitionists") and improved the way gendered keys are expanded in job data formatting.

### Codebase Maintenance and Cleanup

* Removed unused imports and legacy function aliases, and consolidated logger/dump_data imports for consistency.
* Added or adjusted caching decorators and logging for better performance and traceability.

### Miscellaneous Fixes

* Corrected and clarified comments regarding the order of resolvers to prevent misresolution in edge cases.
* Made minor data corrections in job/religion mappings (e.g., "expatriates" → "expatriate", "female rights activists" instead of "womens rights activists").

These changes collectively improve the robustness, maintainability, and correctness of the category and label resolution system.

## [#277](https://github.com/MrIbrahem/ArWikiCats/pull/277) - 2025-12-27

* **New Features**
  * Added translation entry for "sports seasons" in Arabic.

* **Performance**
  * Implemented caching for country-related lookups to improve response times.

* **Improvements**
  * Enhanced logging visibility to surface successful resolutions more prominently.
  * Refactored internal resolution logic for better maintainability.

## [#276](https://github.com/MrIbrahem/ArWikiCats/pull/276) - 2025-12-27

### Highlights

* **Sports Team Category Resolution Logic**: The sports team category mapping logic in `raw_sports_with_suffixes.py` has been refactored to use `{sport_jobs}` placeholders and `FormatDataV2` with `SPORT_KEY_RECORDS` for more accurate and flexible label generation. This includes updates to the `teams_2025` data structure and the main lookup logic to utilize `load_v2` and `search_all_category` for improved cache efficiency and category matching.
* **Test Coverage and Reliability**: Test cases in `test_raw_sports_with_suffixes.py` were updated to cover the new sports team label logic, including new mappings and edge cases. Fixtures in `test_extended.py` now use `{sport_label}`-based mapping for better test decoupling. Additionally, numerous tests in `test_labs_years.py` and `test_with_years_bot.py` have been marked with `pytest.mark.unit` and `pytest.mark.fast` for improved test suite organization and performance tracking.
* **Performance and Data Accuracy**: Timing measurements in `compare.py` were upgraded from `time.time()` to `time.perf_counter()` for enhanced accuracy. A duplicate entry in `COUNTRY_YEAR_DATA` was corrected, and new test cases were added to `test_country_time_pattern.py` to improve coverage for country-year categories.
* **Codebase Streamlining**: Unused imports and legacy code, such as `len_print` and deprecated data exports, have been removed from `raw_sports_with_suffixes.py` to streamline the module and reduce technical debt.

## [#275](https://github.com/MrIbrahem/ArWikiCats/pull/275) - 2025-12-27

* **New Features**
  * Sports category resolution capability introduced for enhanced data classification

* **Tests**
  * Expanded test coverage with improved organization and categorization
  * Test execution efficiency enhanced through refactored loading mechanisms

* **Chores**
  * Internal resolver architecture optimized for better maintainability and clarity
  * Data entries cleaned up for consistency

## [#273](https://github.com/MrIbrahem/ArWikiCats/pull/273) - 2025-12-27

* **Refactor**
  * Reorganized internal resolver module structure to improve code organization and maintainability
  * Consolidated resolver modules into specialized categories for better clarity
  * Updated import paths throughout the codebase to reflect the new structure
  * No changes to public functionality or user-facing features

## [#272](https://github.com/MrIbrahem/ArWikiCats/pull/272) - 2025-12-26

* **New Features**
  * Added broader sports and teams translations (Olympic, wheelchair, clubs & teams) and new team/league templates.

* **Bug Fixes**
  * Improved Arabic feminine agreement for player labels (ensures feminine plural where appropriate).
  * Corrected several sports federation and competition translations and spelling fixes.

* **Improvements**
  * Expanded coverage of sports-related translation keys and national/team variants.

* **Tests**
  * Added and updated data-driven tests covering team and women's sports translations.

## [#265](https://github.com/MrIbrahem/ArWikiCats/pull/265) - 2025-12-24

* **Bug Fixes**
  * Corrected many Arabic translations (Uruguay name variants, standardized "technology" wording to "تقانة", refined political candidate phrasing and related gendered labels).

* **New Features**
  * Added debug logging around label resolution and introduced a unified resolver to improve detection and consistency of generated labels.

* **Refactor**
  * Consolidated resolution flows and reorganized sports/role label mappings for more consistent outputs.

* **Tests**
  * Updated existing tests, added new technology/category resolution tests and test data.

## [#263](https://github.com/MrIbrahem/ArWikiCats/pull/263) - 2025-12-23

* **New Features**
  * Enhanced sports category translation with improved suffix-based resolution for better accuracy in categorizing national teams, leagues, and gender-specific variants.
  * Added support for comprehensive youth and age-group sports category recognition.

* **Bug Fixes**
  * Improved handling of gender-specific player and team terminology in sports translations.

* **Tests**
  * Expanded test coverage for sports category resolution and translation validation.

## [#262](https://github.com/MrIbrahem/ArWikiCats/pull/262) - 2025-12-23

* **New Features**
  * Replaced legacy hard-coded sport label resolution with a data-driven pipeline and improved suffix handling, including gendered form adjustments.

* **Bug Fixes**
  * Standardized sport-format constant names and removed outdated mappings for consistent outputs.

* **Documentation / Data**
  * Added sorted team-label mappings and many new translations for national, youth, staff, leagues and multinational categories.

* **Tests**
  * Updated and added tests to validate the new resolution flow and revised expected outputs.

* **Chores**
  * Public API names and exports updated to align with the new resolution pipeline.

## [#260](https://github.com/MrIbrahem/ArWikiCats/pull/260) - 2025-12-23

* **New Features**
  * Broader Arabic labeling for many sport categories, including additional team, youth, amateur and women's variants
  * Improved suffix-aware resolution so category endings yield more natural combined labels

* **Refactor**
  * Simplified internal data sources and initialization to streamline label generation and normalization

* **Tests**
  * Added tests exercising sport category resolution and new label outputs

* **Chores**
  * Cleaned up exports and reduced redundant runtime data reporting

## [#259](https://github.com/MrIbrahem/ArWikiCats/pull/259) - 2025-12-23

* **Refactor**
  * Consolidated squad label resolution logic and simplified related processing workflows
  * Reorganized internal data structures for sports team and national category translations
  * Updated label resolution pathways to use unified translation resolvers

* **New Features**
  * Expanded sports category translations with additional locale variants including Olympics, managerial history, and age-group categories
  * Enhanced data structures for improved organization of team and national sports labels

* **Documentation & Chores**
  * Removed outdated comments and placeholder code
  * Updated test coverage badge from 13,900+ to 20,000+ successful tests
  * Cleaned up module documentation and imports

## [#258](https://github.com/MrIbrahem/ArWikiCats/pull/258) - 2025-12-23

* **Refactor**
  * Streamlined squad label resolution by consolidating processing logic
  * Simplified religion-related job label generation by removing legacy function
  * Updated internal data formatting to accept category relation mappings via constructor parameter

* **Chores**
  * Removed outdated comments and documentation cleanup

## [Integrate MultiDataFormatterYearAndFrom with category_relation_mapping] [#257](https://github.com/MrIbrahem/ArWikiCats/pull/257) - 2025-12-22

* **New Features**
  * Enhanced `MultiDataFormatterYearAndFrom` class with `category_relation_mapping` integration
  * Added `get_relation_word()` method to find relation words (prepositions like "from", "in", "by") in categories
  * Added `resolve_relation_label()` method to append Arabic relation words to base labels
  * Added `get_relation_mapping()` method to access the full relation word mapping

* **Documentation**
  * Added comprehensive docstrings to all classes in `ArWikiCats/translations_formats/DataModel/`:
    - `model_data_base.py`: FormatDataBase class
    - `model_data.py`: FormatData class
    - `model_data_double.py`: FormatDataDouble class
    - `model_data_time.py`: YearFormatDataLegacy class and YearFormatData function
    - `model_data_v2.py`: FormatDataV2 and MultiDataFormatterBaseV2 classes
    - `model_multi_data.py`: MultiDataFormatterBase, MultiDataFormatterBaseYear, MultiDataFormatterBaseYearV2, MultiDataFormatterDataDouble classes
    - `model_multi_data_base.py`: NormalizeResult dataclass and MultiDataFormatterBaseHelpers class
    - `model_multi_data_year_from.py`: FormatDataFrom and MultiDataFormatterYearAndFrom classes
  * Added comprehensive docstrings to files in `ArWikiCats/translations_formats/`:
    - `__init__.py`: Package-level documentation with all exports
    - `data_new_model.py`: format_films_country_data function
    - `data_with_time.py`: format_year_country_data and format_year_country_data_v2 functions
    - `multi_data.py`: format_multi_data, format_multi_data_v2, and get_other_data functions
  * Added module-level documentation with usage examples
  * Added inline comments explaining key logic

* **Tests**
  * Added 37 new test cases for `MultiDataFormatterYearAndFrom` functionality
  * Tests cover: get_relation_word, resolve_relation_label, get_relation_mapping
  * Tests include edge cases: empty inputs, duplicate relations, case sensitivity
  * Integration tests verify backward compatibility with existing functionality

## [#253](https://github.com/MrIbrahem/ArWikiCats/pull/253) - 2025-12-22

* **New Features**
  * Enhanced Arabic category label translations for international sports and historical categories
  * Added support for burial sites and dynasty-related translations
  * Expanded country-specific leader and position translations

* **Bug Fixes**
  * Corrected translation typos in category mappings
  * Fixed Arabic label generation for squad categories
  * Improved historical category translations

* **Data Updates**
  * Expanded translation database with new mappings
  * Updated category label examples with corrections

## [#249](https://github.com/MrIbrahem/ArWikiCats/pull/249) - 2025-12-22

* **Bug Fixes**
  * Improved handling of missing Arabic templates to prevent resolution errors.
  * Corrected Arabic spelling and diacritics in category labels.

* **New Features**
  * Added support for gendered Arabic translations of political titles.
  * Enhanced translation resolution system with improved fallback handling.
  * Removed obsolete multi-sport category mapping.

* **Tests**
  * Expanded test coverage for political leader category translations.
  * Added fast and slow path testing for improved test efficiency.

## [#248](https://github.com/MrIbrahem/ArWikiCats/pull/248) - 2025-12-22

* **Bug Fixes**
  * Corrected Arabic spelling/diacritics across many category labels (notably Moldova and sidebar template texts).

* **New Features**
  * Removed an obsolete "multi-sport" category key from sports metadata.

* **Tests**
  * Added and updated tests covering multi-sport and Olympics-related category label resolution and diff workflows.

* **Chores**
  * Updated example/data bundles with many category additions, deletions and reorders.
  * Switched the source used for Olympic-event translations to a revised translations dataset.

## [#247](https://github.com/MrIbrahem/ArWikiCats/pull/247) - 2025-12-22

* **New Features**
  * New language-label resolver for Arabic (resolve_languages_labels) and a new country-medalists resolver for Olympic-related categories.

* **Bug Fixes**
  * Widespread Arabic wording corrections: adjective/noun order, gender agreement, preposition placement across film, media, games, and sports categories.
  * Fixed typos and normalized category key formats and mappings.

* **Tests**
  * Added and updated tests to cover language resolution, medalist mappings, and related label outputs.

## [#246](https://github.com/MrIbrahem/ArWikiCats/pull/246) - 2025-12-21

* **Bug Fixes**
  * More precise Arabic label normalization to avoid accidental removals; improved handling of trailing tokens.

* **Data Updates**
  * Updated Arabic translations for Santa Fe entries to use consistent hyphenation/formatting.

* **Tests**
  * Adjusted and added tests to reflect reordered inputs and the updated label-normalization behavior.

* **Refactor**
  * Label-resolution logic updated to use a consolidated resolver and related legacy translation mappings removed.

## [#245](https://github.com/MrIbrahem/ArWikiCats/pull/245) - 2025-12-21

* **Bug Fixes**
  * Prevented duplicate Arabic prepositions in generated labels and ensured no doubled "في".
  * Standardized geographic phrasing: "province" terminology updated consistently to "المقاطعة" across categories.

* **New Features**
  * New, improved bilingual label-resolution system with broader translation coverage.
  * Added translations for several non‑profit organization category variants.

* **Tests**
  * Expanded and reorganized tests with more parameterized cases and explicit type hints.

## [#244](https://github.com/MrIbrahem/ArWikiCats/pull/244) - 2025-12-21

* **Bug Fixes**
  * Corrected Arabic label for "Oxford University Cricket Club" and removed an obsolete person alias.

* **Refactor**
  * Reorganized translation lookup and mapping resources for more consistent resolution and smaller public surface.

* **Tests**
  * Added and updated tests to cover renamed/expanded translation mappings and lookup behavior.

* **Chores**
  * Updated changelog and gitignore entries.

## [#243](https://github.com/MrIbrahem/ArWikiCats/pull/243) - 2025-12-21

* **New Features**
  * Added new Arabic translations and expanded category mappings (including sports and medalist categories).
  * New example scripts and a reusable compare-and-export utility for label comparisons.

* **Bug Fixes**
  * Updated Arabic translations for educational institution and event-related categories.
  * Corrected several branch/category translation strings.

* **Refactor**
  * Renamed and reorganized translation resources and mapping keys for clearer public interfaces.

* **Tests**
  * Added and updated test fixtures to cover new/changed category mappings.

## [#242](https://github.com/MrIbrahem/ArWikiCats/pull/242) - 2025-12-20

* **Tests**
  * Expanded test coverage for separator resolution and text-splitting functionality with multiple edge cases
  * Enhanced test datasets for military and personnel-related translations
  * Improved test validation scenarios for dictionary operations and data integrity
  * Removed obsolete test code and consolidated test structure

## [#240](https://github.com/MrIbrahem/ArWikiCats/pull/240) - 2025-12-20

* **Tests**
  * Expanded test coverage for separator resolution and text-splitting functionality with multiple edge cases
  * Enhanced test datasets for military and personnel-related translations
  * Improved test validation scenarios for dictionary operations and data integrity
  * Removed obsolete test code and consolidated test structure

* **New Features**
  * Extended translation support for additional category types including saints, eugenicists, political figures, religious workers, and contemporary artists.
  * Improved handling of composite category labels with enhanced key normalization.

* **Updates**
  * Refined translation mappings for location-based categories.
  * Updated category naming conventions for improved clarity.

* **Tests**
  * Expanded test coverage for translation resolution across multiple category types.

## [#239](https://github.com/MrIbrahem/ArWikiCats/pull/239) - 2025-12-19

* **Refactor**
  * Consolidated multiple resolver functions into a single unified resolver for improved efficiency.
  * Reorganized internal module structure to streamline dependencies and reduce code complexity.
  * Removed deprecated formatting classes to improve system stability.

* **Bug Fixes**
  * Fixed category resolution for certain year-based and establishment-related categories.
  * Corrected module import paths to ensure proper resolution across the system.

## [#238](https://github.com/MrIbrahem/ArWikiCats/pull/238) - 2025-12-19

* **New Features**
  * Enhanced event processing with new resolver logic for category labeling.
  * Expanded translation resolution capabilities with improved label generation and multi-resolver chains.

* **Refactor**
  * Reorganized internal codebase structure for better modularity and maintainability; consolidated resolver utilities and time-related functions into centralized locations.
  * Updated import paths across numerous modules to reflect new package hierarchy.

## [#237](https://github.com/MrIbrahem/ArWikiCats/pull/237) - 2025-12-19

* **New Features**
  * Added a v2 nationality‑gendered Arabic label resolver and exposed it via the package namespace.

* **Data / Behavior**
  * Expanded patterns and mappings for jobs, sports and nationality variants to improve label coverage and accuracy.
  * Normalization and caching added to improve matching and performance.

* **Tests**
  * Expanded and added parametrized tests and dump-based validations to ensure correctness.

* **Chores**
  * Adjusted public exports and import surface to align with the new resolver.

## [#236](https://github.com/MrIbrahem/ArWikiCats/pull/236) - 2025-12-18

* **Improvements**
  * Widespread memoization added to many resolvers for faster repeated lookups; increased debug logging and reduced noisy debug output.
  * Adjusted data merge/precedence for nationality and label mappings; refined some normalization behaviors.

* **New Features**
  * Added a new year/country-job resolver and several helper normalization utilities.

* **Bug Fixes**
  * Simplified resolution chains by removing an unused fallback step.

* **Tests**
  * Reorganized and updated many test fixtures, added targeted resolver integration/unit tests.

* **Documentation**
  * Updated changelog with recent entries.

## [#235](https://github.com/MrIbrahem/ArWikiCats/pull/235) - 2025-12-18

* **New Features**
  * Added airstrike-related death categorization translations
  * Expanded nationality categorization support for country data

* **Improvements**
  * Enhanced Arabic text normalization for death-attribution phrases
  * Improved category label resolution with better data consistency and handling

* **Tests**
  * Expanded test coverage for category-to-label resolution across multiple datasets

## [#234](https://github.com/MrIbrahem/ArWikiCats/pull/234) - 2025-12-18

* **New Features**
  * Ireland nationality support added.
  * Exposed a formatting helper for external use.

* **Enhancements**
  * Relation-label resolution improved: input trimming/normalization, caching, deterministic ordering, suffix/template handling.
  * Added a sorting utility to prioritize label keys.
  * Replaced ad-hoc prints with structured logging.
  * Typing and data-model clarity improvements for nationality mappings.

* **Tests**
  * Added extensive test suites and datasets for relation-label resolution.

## [#233](https://github.com/MrIbrahem/ArWikiCats/pull/233) - 2025-12-18

* **Bug Fixes**
  * Corrected Arabic spellings/diacritics across pan‑African related translations.

* **New Features**
  * Added additional regional classification data and related category entries.
  * Improved label resolution for relation/category labels.

* **Refactor**
  * Consolidated resolution logic and updated public exports for clearer APIs.

* **Tests**
  * Updated test data and expectations to match corrected translations and new classifications.

## [#232](https://github.com/MrIbrahem/ArWikiCats/pull/232) - 2025-12-18

* **Bug Fixes**
  * Corrected country name spelling in geography data.
  * Updated nationality naming inconsistencies and standardized regional designations.

* **New Features**
  * Expanded nationality dataset with enhanced multilingual translations and gendered forms.
  * Improved country-nationality mappings for multiple regions.

* **Chores**
  * Consolidated and cleaned up redundant nationality entries.
  * Updated test data to reflect current data mappings.

## [#231](https://github.com/MrIbrahem/ArWikiCats/pull/231) - 2025-12-18

* **Bug Fixes**
  * Corrected Arabic spellings/translations for Eritrea and Saint Vincent and Grenadines across multiple data categories and examples
  * Fixed a naming typo in public exports for consistency

* **Tests**
  * Updated test fixtures and expectations to match corrected Arabic translations

* **Refactor**
  * Consolidated label-resolution logic to improve maintainability

## [#230](https://github.com/MrIbrahem/ArWikiCats/pull/230) - 2025-12-17

* **Documentation**
  * Added resolver documentation examples with an external reference link.

* **Tests**
  * Replaced a large test dataset with a smaller focused set and adjusted related expectations; added a new case for a year-country translation.

* **Chores**
  * Updated many Arabic translation strings (economic history phrasing and Ottoman Iraq grammatical fixes) and removed one obsolete mapping; added a new Arabic label for the Republic of Venice; standardized input normalization for some resolver inputs.

## [#229](https://github.com/MrIbrahem/ArWikiCats/pull/229) - 2025-12-17

* **New Features**
  * Integrated an improved translation resolver and normalization for label resolution.
  * Added translations for Safavid Iran and Northern Ireland; expanded related regional/historical mappings.
  * Exposed additional female jobs data and extended sports/job terminology.

* **Bug Fixes**
  * Corrected a sports-category label and fixed a nationality key formatting issue.
  * Minor data count adjustments in metadata.

* **Tests**
  * Expanded and reorganized test datasets; updated test expectations and execution markers; some tests/data entries commented or removed.

## [#228](https://github.com/MrIbrahem/ArWikiCats/pull/228) - 2025-12-17

* **New Features**
  * Added nationality gender pattern resolution for Arabic categories
  * Geographic mapping for Ottoman Arabia

* **Updates**
  * Improved Arabic translations for sports terminology
  * Enhanced gender-specific phrasing consolidation

* **Tests**
  * Expanded and reorganized translation resolver test coverage
  * Added comprehensive test validation for new features

* **Chores**
  * Standardized internal data handling and structure

## [#227](https://github.com/MrIbrahem/ArWikiCats/pull/227) - 2025-12-17

* **New Features**
  * Added geographic mapping for Ottoman Arabia.

* **Updates**
  * Improved Arabic translations for sports terminology (acrobatic gymnastics, motorboat) and related labels.
  * Exposed additional sport key records for broader lookup coverage.
  * Consolidated gender-specific category phrasing.

* **Tests**
  * Updated, expanded and reorganized multiple translation and resolver tests (some cases removed, others extended).

* **Chores**
  * Standardized internal data handling and changelog entry added.

## [#226](https://github.com/MrIbrahem/ArWikiCats/pull/226) - 2025-12-17

* **New Features**
  * Added geographic mapping for Ottoman Arabia

* **Updates**
  * Updated Kingdom of Aragon translation for improved accuracy

* **Chores**
  * Standardized internal data handling conventions
  * Improved data structure consistency across gender-specific categories

* **Tests**
  * Expanded test coverage for gender-specific regional categories
  * Refactored test structure for better maintainability

## [#225](https://github.com/MrIbrahem/ArWikiCats/pull/225) - 2025-12-17

* **New Features**
  * Introduced a dynamic "from"-style resolver and a new combined year+country formatter for richer label composition
  * Reworked resolver flow to produce more flexible, multi-part translations

* **Bug Fixes**
  * Safer defaults and more reliable search/matching to reduce incorrect or empty lookups

* **Tests**
  * Extensive new and updated integration/unit tests covering job, label and year-country resolution

* **Documentation**
  * Changelog updated with PR details

## [#224](https://github.com/MrIbrahem/ArWikiCats/pull/224) - 2025-12-17

* **New Features**
  * Added combined year-and-country formatter and a new translation resolution flow for richer label composition
  * Introduced a dynamic "from"-style formatter to support key/value placeholder handling

* **Bug Fixes**
  * Safer defaults for optional data mappings
  * Search now returns real lookup results; removed extraneous debug output

* **Tests**
  * Added integration/unit tests for the new resolvers; removed an outdated test file

* **Documentation**
  * Changelog updated with PR details

## [#223](https://github.com/MrIbrahem/ArWikiCats/pull/223) - 2025-12-17

* **New Features**
  * Year-aware formatting and a new V3 year/country formatter; expanded template-driven dual-data formatting for combined labels (e.g., nationality + role). Public API now exposes V3Formats and MultiDataFormatterBaseYearV3.

* **Bug Fixes**
  * Standardized gender-term normalization (women → female). Improved year-movement/label normalization to reduce mismatches.

* **Refactor**
  * Reorganized translation formatting internals and adjusted optional data mapping defaults for safer usage.

* **Tests**
  * Added extensive unit and integration tests covering year, country, and gender scenarios.

* **Documentation**
  * Changelog updated.


## [#222](https://github.com/MrIbrahem/ArWikiCats/pull/222) - 2025-12-16

* **New Features**
  * Added optional parameter to label resolution functions for controlling label transformation behavior.

* **Refactor**
  * Renamed label-fixing function to improve naming clarity across the codebase.
  * Enhanced data-dump handling with decorator application to transformation functions.

* **Tests**
  * Updated test suite to reflect function naming changes and added test coverage for conditional label transformation.

* **Documentation**
  * Updated README and changelog to reflect API changes.

## [#221](https://github.com/MrIbrahem/ArWikiCats/pull/221) - 2025-12-16

* **New Features**
  * Added comprehensive Arabic translations for film-related categories (people, directors, awards).
  * Made a new label-resolution entry point publicly available for consumers.

* **Improvements**
  * Expanded translation patterns with extra gender and film-specific variants.
  * Introduced a new startup option (TGC_RESOLVER_FIRST) in configuration and docs.

* **Tests**
  * Increased test coverage for film-related categories and label resolution.

## [#220](https://github.com/MrIbrahem/ArWikiCats/pull/220) - 2025-12-16

* **Bug Fixes**
  * Standardized New Zealand nationality naming to the plural form; updated related translation keys.

* **Refactor**
  * Consolidated country→nationality data sourcing for consistency.
  * Reworked gender-based film categorization flow with a new helper to improve mapping clarity.

* **New Features**
  * Added a country-name-derived nationality mapping for clearer entries.

* **Tests**
  * Added comprehensive tests for Papua New Guinea and Northern Ireland label resolution and dump verification.
  * Removed one obsolete nationality-normalization test.


## [#219](https://github.com/MrIbrahem/ArWikiCats/pull/219) - 2025-12-16

* **Tests**
  * Added comprehensive test coverage for Arabic category label resolution
  * New test suite for non-fiction writer categories with data-driven validation
  * Added tests for label generation and category handling functions

* **Refactor**
  * Restructured internal data mapping architecture for improved modularity and maintainability
  * Consolidated label extension workflow for better code organization

## [#218](https://github.com/MrIbrahem/ArWikiCats/pull/218) - 2025-12-16

* **New Features**
  * Added support for television series debut categories
  * Implemented automated deployment workflow for remote server updates

* **Bug Fixes**
  * Corrected Arabic grammatical forms in non-fiction writer categories
  * Fixed category pattern typos and improved sports/elections translations

* **Tests**
  * Refactored label tests to use data-driven approach
  * Added comprehensive unit tests for label functionality

* **Chores**
  * Updated GitHub Actions workflow for improved caching performance
  * Internal cleanup of decorators and module exports

## [#217](https://github.com/MrIbrahem/ArWikiCats/pull/217) - 2025-12-16

* **Bug Fixes**
  * Standardized the Arabic translation for 'non-fiction writers' across multiple files to use the correct plural form 'غير روائيين'. Added new label mappings in get_by_label.jsonl and updated category patterns for year and country in COUNTRY_YEAR.py and YEAR_PATTERNS.py.
  * Corrected Arabic grammatical forms in category translations for non-fiction writers and related categories.
  * Fixed typo in category pattern (removed duplicate "in").

* **New Features**
  * Added support for election year category patterns.
  * Added support for television series debut year categories.

* **Improvements**
  * Enhanced category mappings for sports clubs and teams.
  * Updated category labels for improved accuracy and consistency across localized content.

## [#215](https://github.com/MrIbrahem/ArWikiCats/pull/215) - 2025-12-15

* **Chores**
  * Added Arabic translation mapping for "womens-events".
  * Incremented internal dataset counters by 1.
  * Inserted a harmless commented line in a utility (no behavior change).

* **New Features**
  * Added an example script for batch label resolution with progress tracking, memory reporting, and comparison outputs.

* **Refactor**
  * Simplified file path handling in an example script (no functional change).

* **Tests**
  * Removed two category entries from a time-pattern test dataset.

## [#214](https://github.com/MrIbrahem/ArWikiCats/pull/214) - 2025-12-14

* **New Features**
  * Added filters: by country/continent of setting, by period of setting location, by opening decade/year
  * New label-resolution bot and helpers for complex "by" categories
  * Added data overrides support (data_to_find) for multi-label formatting

* **Bug Fixes**
  * Removed obsolete "impacted by covid-19 pandemic" category

* **Chores**
  * Reorganized translation and by-label mapping structures; removed deprecated exports and consolidated fallback logic

## [#213](https://github.com/MrIbrahem/ArWikiCats/pull/213) - 2025-12-14

* **Refactor**
  * Simplified internal label resolution logic by consolidating conditional fallback chains into cleaner expressions, improving code maintainability with no user-visible impact.
  * Added new helper functions to enhance label derivation for specialized categories.

* **Chores**
  * Removed deprecated function aliases that were maintained for backwards compatibility.

## [#212](https://github.com/MrIbrahem/ArWikiCats/pull/212) - 2025-12-14

* **Refactor**
  * Restructured translation key organization system for improved consistency and maintainability
  * Enhanced translation mapping format across minister and ministry categories

* **New Features**
  * Added support for additional labour ministry-related category combinations


## [#211](https://github.com/MrIbrahem/ArWikiCats/pull/211) - 2025-12-14

* **New Features**
  * Added american-football and canadian-football translation entries and exposed a new data-dump utility in the public API.

* **Improvements**
  * Expanded and normalized sports & job translation coverage (hyphenation and key normalization); reorganized Canadian football variants and some lookup keys.

* **Performance**
  * Added caching to translation resolution for faster repeated lookups.

* **Tests**
  * Added Canadian football tests and renamed/updated several test cases.

* **Documentation**
  * Updated README resource paths to reflect reorganized JSON locations.

## [#210](https://github.com/MrIbrahem/ArWikiCats/pull/210) - 2025-12-13

* **New Features**
  * Expanded Arabic translations for ministerial positions (electricity and water) and sports-related job titles with male/female variant mappings.

* **Bug Fixes**
  * Corrected typos in test data and removed invalid test entries to improve data quality.

* **Tests**
  * Removed obsolete test cases for improved test suite maintenance.

## [#209](https://github.com/MrIbrahem/ArWikiCats/pull/209) - 2025-12-13

* **Updates**
  * Expanded Arabic translations for sports-related and occupation-based job titles with comprehensive variant mappings for male and female roles.
  * Improved translation resource loading infrastructure for better performance.

* **Bug Fixes**
  * Corrected typos in test data and removed invalid test entries to improve overall data quality and test reliability.

## [#208](https://github.com/MrIbrahem/ArWikiCats/pull/208) - 2025-12-13

* **New Features**
  * Added sport job variants with gendered translations and expanded singer/classical musician mappings
  * Added extensive film & TV translation resources and additional translation JSONs

* **Bug Fixes**
  * Corrected Arabic grammatical forms for several musician and illustrator categories
  * Adjusted various sport-related translation phrasings

* **Refactor**
  * Shifted several translation data sources to JSON-backed loading and consolidated utilities
  * Standardized test parametrization style across the suite

* **Chores**
  * Updated ignore list and revised build/metrics inventory files

## [#207](https://github.com/MrIbrahem/ArWikiCats/pull/207) - 2025-12-13

* **New Features**
  * Added new resolver function for handling religion/nationality job categories
  * Extended public exports to expose new translation/resolver entry points

* **Bug Fixes**
  * Corrected female singers label in Arabic translations

* **Data Updates**
  * Added recognition for "baháís" variant alongside existing religious entries
  * Updated religious keys and occupational data mappings
  * Expanded translation datasets for improved coverage

* **Tests**
  * Added and expanded tests covering religion/nationality job translations and big-data cases

## [#206](https://github.com/MrIbrahem/ArWikiCats/pull/206) - 2025-12-13

* **New Features**
  * New job-category resolvers with broader fallback and richer variants for masculine and feminine labels (expanded sports, cycling, film, music, gendered and nationality forms).

* **Bug Fixes**
  * Removed duplicate football key and adjusted related test expectations.

* **Refactor**
  * Reworked translation builders to return assembled variant maps; simplified resolution flow and consolidated resolver logic.

* **Tests**
  * Added comprehensive resolver and formatting tests; updated and removed obsolete tests to match new behavior.

## [#205](https://github.com/MrIbrahem/ArWikiCats/pull/205) - 2025-12-12

* **New Features**
  - Expanded coverage for secretary and ministry-related category translations with additional wording variants and improved input normalization for better lookup accuracy

* **Bug Fixes**
  - Removed redundant runtime processing logic and consolidated translation resolution approach

* **Tests**
  - Updated test cases to reflect new translation mappings and normalization changes

* **Documentation**
  - Updated changelog entries for recent changes

## [#204](https://github.com/MrIbrahem/ArWikiCats/pull/204) - 2025-12-12

* **Bug Fixes**
  * Simplified category label resolution by removing redundant fallback logic and redundant runtime population of some translation maps.

* **Features**
  * Expanded secretary/ministry translation coverage, adding more U.S. department and wording variants and improved input normalization.

* **Tests**
  * Added and adjusted multiple secretary and minister translation tests to reflect new mappings.

* **Documentation**
  * Updated changelog entries for recent PRs.

## [#203](https://github.com/MrIbrahem/ArWikiCats/pull/203) - 2025-12-12

* **New Features**
  * Added a public category search method and a unified secretary/ministry label resolver for more consistent lookups.

* **Bug Fixes**
  * Corrected Arabic spellings for Delaware and Minnesota; fixed pluralization for secretary titles.

* **Improvements**
  * Consolidated and expanded ministry keys, streamlined resolution paths, and added more country/state translation coverage.

* **Tests**
  * Added comprehensive tests for secretary/ministry label resolution and related resolvers.

## [#202](https://github.com/MrIbrahem/ArWikiCats/pull/202) - 2025-12-12

* **Refactor**
  * Reorganized military category translation mappings for improved fallback resolution. Enhanced suffix resolution logic to provide better localization of military-related category labels through additional translation sources when primary templates are unavailable.

## [#200](https://github.com/MrIbrahem/ArWikiCats/pull/200) - 2025-12-11

* **Bug Fixes**
  * Corrected Arabic transliteration for Malawi and standardized African Cup of Nations labels.
  * Improved Arabic labels for some religious and women's sports/TV categories.

* **New Data**
  * Added "African Cup of Nations" translation and expanded wheelchair-related occupation mappings.
  * Broadened female-oriented translation entries for sports/nationality terms.

* **Behavior Changes**
  * Nationality-resolution sources reduced — some nationality label lookups may now return fewer candidates.

* **Documentation & Exports**
  * Public translation export surface trimmed and reorganized.

## [#199](https://github.com/MrIbrahem/ArWikiCats/pull/199) - 2025-12-11

* **New Features**
  * Expanded category label resolution with support for women's sports categories, including Women's Africa Cup of Nations and national teams.
  * Enhanced fallback mechanisms for improved label resolution across sports and nationality-related categories.
  * Added translation coverage for under-age sports groups and women's sports variants.

* **Bug Fixes**
  * Corrected fallback resolution order for category labels to improve accuracy.

* **Documentation**
  * Updated changelog with new features and enhancements to label resolution workflows.

## [#198](https://github.com/MrIbrahem/ArWikiCats/pull/198) - 2025-12-11

* **New Features**
  * Added alternative data sources for category label resolution to improve coverage of sports and nationality-related categorizations.

* **Refactor**
  * Reorganized label lookup workflows with enhanced fallback logic across multiple labeling systems.
  * Consolidated and relocated translation data structures to a new centralized resolver module.

* **Tests**
  * Updated test coverage to verify label resolution through both legacy and new data sources.

## [#197](https://github.com/MrIbrahem/ArWikiCats/pull/197) - 2025-12-11

* **Refactor**
  * Category label resolution updated to use a new nationality-pattern resolver and improved data formats.
  * Nationality/diaspora translation handling reorganized for richer mappings.

* **Documentation / Data**
  * Added an example country mapping for reference.

* **Tests**
  * Removed obsolete test module and one deprecated test; minor test comment cleanup.

* **Chores**
  * Removed an unused public export from translations API.


## [#196](https://github.com/MrIbrahem/ArWikiCats/pull/196) - 2025-12-10

* **Bug Fixes**
  * Corrected terminology used throughout the application to consistently reference "religion" instead of an outdated variant.

* **Translations**
  * Added numerous new translation mappings for organizations, political bodies, and cultural entities.
  * Removed outdated entries from translation data to improve accuracy.

* **Tests**
  * Enhanced test coverage for religion-related categories with comprehensive validation of Arabic translations.
  * Updated existing tests to reflect terminology corrections.

## [#195](https://github.com/MrIbrahem/ArWikiCats/pull/195) - 2025-12-10

* **New Features**
  * Support for gender-variant nationality translations and expanded diaspora mappings.

* **Bug Fixes**
  * Corrected Arabic diaspora translation and deactivated invalid election category mappings.

* **Improvements**
  * Improved translation resolution for sports, championships and nationality labels; more robust data handling.

* **Tests**
  * Expanded and reorganized tests to cover new nationality and sports label behaviors.

* **Refactor**
  * Simplified translation resolver architecture and removed legacy fallback paths.

## [#194](https://github.com/MrIbrahem/ArWikiCats/pull/194) - 2025-12-10

* **Bug Fixes**
  * Fixed multiple translation typos (e.g., "inscriptionss" → "inscriptions") and improved Arabic labels.
  * Corrected category name typo ("presidential primarie" → "presidential primaries").

* **Improvements**
  * More robust category pattern matching and fallback resolution to improve label detection.
  * Enhanced pattern construction to better handle complex category keys.

* **Tests**
  * Added and enabled additional test cases to cover new/edge translations and patterns.

## [#193](https://github.com/MrIbrahem/ArWikiCats/pull/193) - 2025-12-10

* **New Features**
  * Expanded Arabic translations for elections, national bodies and additional national-language term variants; added more year-aware label variants.

* **Bug Fixes**
  * Standardized category key formatting (removed stray commas/spacing) to improve lookup reliability.

* **Tests**
  * Added and updated tests for election, nationality and year-based category translations.


## [#192](https://github.com/MrIbrahem/ArWikiCats/pull/192) - 2025-12-10

* **New Features**
  * Added translation support for "bodies of water" categories across multiple languages.
  * Expanded translation database with new entity mappings including cultural institutions, sports organizations, and historical figures.

* **Bug Fixes**
  * Corrected Arabic translation for "Third Punic War" to use proper definite article form.

* **Improvements**
  * Enhanced category naming standardization and reorganized translation data for better consistency.

## [#191](https://github.com/MrIbrahem/ArWikiCats/pull/191) - 2025-12-10

* **New Features**
  * Enhanced translation resolution for sports-related categories, including improved federation label formatting and nationality translations.
  * Expanded Arabic translations for nationality entries.

* **Tests**
  * Added comprehensive test coverage for sports category translations, including football, rugby, and Olympics-related categories.
  * Extended test data for nationality and sports translations across multiple countries.

## [#190](https://github.com/MrIbrahem/ArWikiCats/pull/190) - 2025-12-10

* **New Features**
  * Added enhanced sport format resolution with improved fallback mechanisms for category translation
  * Introduced new utility functions for retrieving team labels, job titles, and category identifiers

* **Bug Fixes**
  * Removed outdated translation entries and updated deprecated mappings across translation datasets
  * Improved data consistency for sports team and job category translations

* **Tests**
  * Reorganized test suite with a new data-driven framework for better coverage and maintainability
  * Removed obsolete test cases and consolidated validation approaches

## [#189](https://github.com/MrIbrahem/ArWikiCats/pull/189) - 2025-12-08

* **New Features**
  * Added multiple localized translation resolvers and expanded country/sport/nationality translation entries, plus new localized entries for universities, airports, military institutions, theaters, and test phrases.

* **Bug Fixes**
  * Improved Arabic phrasing, key normalization, and added fallback label resolution logic.

* **Tests**
  * Added and updated fast, parametric, and dump tests validating new resolvers and datasets.

* **Chores**
  * Consolidated translation datasets and removed legacy dynasty translations; updated changelog.

## [#185](https://github.com/MrIbrahem/ArWikiCats/pull/185) - 2025-12-08

* **New Features**
  * Gender-specific nationality translations added (the_female / the_male).
  * New translation entries added (e.g., "sports clubs and teams", "border war", many taxonomy and location terms).

* **Bug Fixes / Tweaks**
  * Improved Arabic phrasing for multiple sports-club and year-by-country category labels.
  * Normalized some keys (e.g., lowercase city names) and adjusted label ordering.

* **Chores**
  * Large consolidation/pruning and reorganization of translation datasets; changelog updated.

## [#184](https://github.com/MrIbrahem/ArWikiCats/pull/184) - 2025-12-07

* **New Features**
  * Improved filtering for geographic vs non‑geographic and city vs non‑city entries

* **Bug Fixes**
  * Removed an incorrect country-prefix mapping that affected some country label resolutions
  * Corrected and normalized many Arabic translation mappings

* **Chores**
  * Reorganized and consolidated translation datasets; removed and added large translation resources
  * Added a JSON scanning/validation utility; refined region-suffix handling and public exports

* **Tests**
  * Updated test data to reflect mapping removals and translation changes; some test cases adjusted or removed

## [#183](https://github.com/MrIbrahem/ArWikiCats/pull/183) - 2025-12-07

* **New Features**
  * Implemented enhanced filtering for geographic vs. non-geographic translation entries.
  * Added city vs. non-city categorization for location data.

* **Chores**
  * Reorganized translation data file structure and consolidated data sources.
  * Updated Arabic translation mappings across multiple content categories.

## [#182](https://github.com/MrIbrahem/ArWikiCats/pull/182) - 2025-12-07

* **New Features**
  * Added filtering functionality to separate geographic and non-geographic entries in translation data
  * Added filtering functionality to separate city and non-city entries

* **Documentation**
  * Added comprehensive documentation for new filtering scripts

* **Tests**
  * Added test suite for filtering functionality to ensure data integrity

* **Chores**
  * Enhanced translation data for Arabic localization
  * Updated file exclusion rules

## [#178](https://github.com/MrIbrahem/ArWikiCats/pull/178) - 2025-12-07

* **New Features**
  * Greatly expanded Arabic translation coverage across cities, regions, historical polities, media titles and occupations (notably many Jerusalem/place entries).

* **Bug Fixes**
  * Normalized keys and labels: removed leading articles, standardized capitalization, fixed hyphenation (e.g., sports-people) and corrected concatenation glitches.

* **Chores**
  * Reorganized translation maps, added/removed/relocated many entries and updated dataset counts.

* **Tests**
  * Updated test data and fixtures to reflect normalized keys and the expanded translations.

## [#176](https://github.com/MrIbrahem/ArWikiCats/pull/176) - 2025-12-06

# Release Notes

* **Bug Fixes**
  * Standardized Arabic translations for cricket-related terminology across all translation databases
  * Corrected Arabic translations for wheelchair rugby event categories
  * Fixed data consistency issues in geographic, city, and sports translation mappings
  * Cleaned up obsolete translation entries for sports competitions and national teams

* **Chores**
  * Reorganized and updated translation datasets for improved accuracy and coverage
  * Improved lookup logic for geographic label resolution
  * Updated data metrics to reflect cleaned translation datasets

## [#175](https://github.com/MrIbrahem/ArWikiCats/pull/175) - 2025-12-06

* **New Features**
  * Added translations for empire-related terms and refugee Olympic team categories.
  * Enhanced label resolution with case-insensitive lookups for improved accuracy.

* **Bug Fixes**
  * Corrected Arabic translation for "internees".
  * Fixed JSON file formatting.

* **Data Updates**
  * Expanded category mappings for people-by-country-year combinations.
  * Removed obsolete historical entries (ancient BCE years, deprecated geopolitical terms).
  * Streamlined outdated category references.

* **Tests**
  * Added new test coverage for Arabic category label resolution.
  * Updated test cases to reflect translation changes.

## [#174](https://github.com/MrIbrahem/ArWikiCats/pull/174) - 2025-12-06

* **New Features**
  * Enhanced geographic label generation for Japan and Turkey with improved mapping consolidation and language-specific variants.

* **Refactor**
  * Optimized country label index building and loading processes.
  * Improved label mapping consolidation to reduce redundancy.

* **Chores**
  * Added diagnostic logging throughout the system to improve monitoring and debugging capabilities.

## [#173](https://github.com/MrIbrahem/ArWikiCats/pull/173) - 2025-12-06

* **Refactor**
  * Refactored translation lookup mechanism for improved code maintainability across multiple modules.
  * Updated job categories data structure with clearer field naming (males_jobs and females_jobs).

* **Chores**
  * Removed obsolete tests and updated test mocks accordingly.

## [#172](https://github.com/MrIbrahem/ArWikiCats/pull/172) - 2025-12-06

* **New Features**
  * Added a new localized data source and an alias-based resolver to improve translation hits.

* **Refactor**
  * Streamlined lookup flow and removed the previous lazy-loading cache in favor of direct in-memory updates.
  * Simplified post-lookup fallback behavior and reduced lookup surface.

* **Chores**
  * Normalized capitalization of "prefecture" across example and test data.

* **Tests**
  * Removed lazy-load-specific test; adjusted test data ordering.

## [#170](https://github.com/MrIbrahem/ArWikiCats/pull/170) - 2025-12-06

* **New Features**
  * Better geographic translations for alpine-skiing categories; new country+sport resolver
  * Added multi-part formatting (v2) and broader sports/media translation entries

* **Bug Fixes**
  * Corrected Arabic translations for sports-related occupational categories and media keys

* **Tests**
  * Expanded coverage for geographic translations, date-to-Arabic (decades, BC/BCE), and sports coach terminology

* **Refactor**
  * Reorganized sports/media translation data and improved label-resolution fallbacks

## [#168](https://github.com/MrIbrahem/ArWikiCats/pull/168) - 2025-12-05

* **Refactor**
  * Restructured Arabic translation mappings for films and television content to improve maintainability and consistency.
  * Reorganized how gendered and nationality-based translation variants are handled and accessed.
  * Updated the public translation interface while maintaining backward compatibility with existing integrations.

## [#167](https://github.com/MrIbrahem/ArWikiCats/pull/167) - 2025-12-05

- **Refactor**
  - Reorganized internal code structure for label and country processing to improve maintainability and code modularity. No changes to user-facing functionality or features.

## [#166](https://github.com/MrIbrahem/ArWikiCats/pull/166) - 2025-12-05

- **New Features**

  - Improved job/category labeling with better nationality, gender and multi-sport phrasing in Arabic.
  - Added registry-driven lookup utilities to improve translation and prefix/suffix handling.

- **Refactor**

  - Major modularization of label-generation and normalization flows for more consistent outputs and easier maintenance.

- **Tests**

  - Replaced bulk diff test with parameterized per-case assertions for clearer failures.

- **Chores**
  - Normalized and reformatted changelog entries.

## [#165](https://github.com/MrIbrahem/ArWikiCats/pull/165) - 2025-12-05

- **Refactor**

  - Consolidated formatting/templating logic into a shared base to reduce duplication and centralize behavior.
  - Subclasses trimmed to focus on value replacement; end-to-end resolution now handled by the base.

- **New Features**

  - Label generation logic modularized into smaller helpers for clearer, ordered fallback resolution.

- **Chores**
  - Moved a local mapping to the shared translations source; observable behavior preserved.

## [#162](https://github.com/MrIbrahem/ArWikiCats/pull/162) - 2025-12-05

- **Chores**
  - Standardized internal gender classification terminology across the system from "mens" to "males" for improved consistency and clarity in data labeling and category naming conventions.

## [#161](https://github.com/MrIbrahem/ArWikiCats/pull/161) - 2025-12-05

- **Chores**
  - Standardized gender terminology across category labels and translations.
  - Consolidated gender key naming for consistency in data structures ("male"/"males"/"females" instead of "men"/"womens").
  - Updated data formatting to align with revised gender classification standards.
  - Refined import paths and internal symbol naming for improved code organization.

## [#159](https://github.com/MrIbrahem/ArWikiCats/pull/159) - 2025-12-05

- **New Features**

  - Support for translating country+year/decade category titles (e.g., national film categories with years or decades).

- **Improvements**

  - Broadened label resolution to consider additional pattern sources for better matches.
  - Simplified resolution flow by removing legacy fallback paths and enabling updated templates for film/TV national labels.

- **Tests**
  - Added and expanded tests covering nationality/year templates, multi-template combinations, and many edge cases.

## [#158](https://github.com/MrIbrahem/ArWikiCats/pull/158) - 2025-12-05

- **Refactor**

  - Reorganized translation resolution to prefer federation and nationality+sport resolvers, improving fallback reliability.
  - Introduced a dedicated nationality+sport resolver for more accurate combined labels.

- **Bug Fixes**

  - Corrected Arabic phrasing for a people-by-nationality category.

- **Chores**

  - Consolidated and renamed translation mappings and exposed a smaller, clearer resolver API.

- **Tests**
  - Updated and added tests to reflect new resolvers and placeholder-based templates.

## [#157](https://github.com/MrIbrahem/ArWikiCats/pull/157) - 2025-12-04

- **New Features**

  - Improved gender-aware translation handling with separate masculine/feminine loaders and broader profession coverage.

- **Bug Fixes**

  - Corrected feminine job forms and role translation terminology; earlier resolution now prefers the new gendered lookup.

- **Tests**

  - Updated test suite and reference data; removed an obsolete test fixture and rewired tests to the new lookup path.

- **Changelog**
  - Added entries documenting translation, data, and test updates (includes a data tweak marking a fictional religious worker).

## [#156](https://github.com/MrIbrahem/ArWikiCats/pull/156) - 2025-12-04

- **Bug Fixes**

  - Corrected terminology in football-related role translations to use more accurate terminology.
  - Fixed feminine form translations for various job titles.

- **New Features**
  - Expanded translation coverage for additional profession and nationality combinations, including eugenicists, contemporary artists, and politicians.
  - Added translations for female-specific job category variants and new profession classifications.
  - Enhanced multi-data formatting with improved search capabilities.

## [#154](https://github.com/MrIbrahem/ArWikiCats/pull/154) - 2025-12-04

- **New Features**

  - Added localized label resolution for masculine/feminine job and nationality categories, including combined and specialized variants.
  - Implemented faster exact-match prioritized category lookups.

- **Improvements**

  - Faster, more accurate category lookups via exact-match prioritization.
  - Expanded music-genre translations and updated several job/nationality translation strings.
  - Removed obsolete and duplicate translation entries.

- **Tests**
  - Added parametrized test coverage for masculine and feminine label resolution across category variants.

## [#153](https://github.com/MrIbrahem/ArWikiCats/pull/153) - 2025-12-03

- **New Features**

  - Added broad nationality-based category translations, including gender and temporal variants.
  - Updated label resolution to consult multiple category pattern handlers for better matches.

- **Refactor**

  - Enhanced translation lookup with a cached, reusable formatter to improve lookup consistency and performance.

- **Tests**
  - Added comprehensive tests validating nationality translation and formatter behavior.

## [#152](https://github.com/MrIbrahem/ArWikiCats/pull/152) - 2025-12-03

- **New Features**

  - New parsing utility to normalize categories and extract year/type fields.
  - Multi-language lookup for certain job/category labels and expanded feminine job mappings.

- **Bug Fixes**

  - Improved matching order with tie-breaker (space count then length) for more accurate key selection.
  - Template handling now returns an empty label when no template applies.

- **Tests**

  - Added/updated tests for shooting, longest-match priority, template parsing, suffix-prefix behavior, and large-data test coverage.

- **Chores**
  - Consolidated pattern-building and removed an old utility.

## [#151](https://github.com/MrIbrahem/ArWikiCats/pull/151) - 2025-12-03

- **New Features**

  - Improved film/media labeling: template-driven formatting, enhanced multi-key matching, a new film-text mapping/resolution path, and a newly exported formatter available for use.

- **Tests**

  - Expanded unit and integration tests to cover new matching paths and parallel implementations.

- **Style**

  - Multiple formatting cleanups for sorting expressions (no behavior change).

- **Bug Fixes**
  - Updated Arabic translation for "Burma".

## [#150](https://github.com/MrIbrahem/ArWikiCats/pull/150) - 2025-12-02

- **New Features**

  - Added film-related formatting: time-aware category handling, Arabic conversions, and placeholder-based normalization.
  - Exposed a new public formatter entry for composing film + country transformations.

- **Tests**
  - Added integration tests covering film category translations and country-based combinations.
  - Adjusted test skip behavior for an existing entertainment test.

## [#149](https://github.com/MrIbrahem/ArWikiCats/pull/149) - 2025-12-02

- **Refactor**

  - Improved film nationality labeling and centralized nationality-based resolution; adjusted fallback order across film, team, and job category lookups for more consistent labels.
  - Removed an older jobs-category fallback so job label resolution now uses the revised strategies only.

- **Tests**
  - Expanded, reorganized, and added tests for films and large data sets; updated test data and harnesses to validate the new resolution paths and mappings.

## [#148](https://github.com/MrIbrahem/ArWikiCats/pull/148) - 2025-12-02

- **Bug Fixes**

  - Standardized film category key names and removed obsolete LGBT/LGBTQ key variants to ensure consistent labels.

- **Improvements**

  - Improved film label resolution with multi-part matching, prioritization, caching and better suffix handling via a new resolution entry point.
  - Updated key sets and summary data to reflect consistent naming.

- **Tests**
  - Expanded and updated tests to cover new resolution logic and mappings.

## [#146](https://github.com/MrIbrahem/ArWikiCats/pull/146) - 2025-12-01

- **New Features**

  - Enhanced film and media category translation resolution with improved accuracy.
  - Extended ministerial title translations with gender-specific and format variants.

- **Tests**

  - Added comprehensive test coverage for film category translations.
  - Added test coverage for ministerial category label resolution.

- **Refactoring**
  - Restructured translation table construction for better maintainability and modularity.
  - Optimized data handling for television and media-related category mappings.

## [#143](https://github.com/MrIbrahem/ArWikiCats/pull/143) - 2025-12-01

- **Bug Fixes**

  - More reliable separator-based text splitting and added validation to ensure Arabic labels contain only Arabic characters.

- **Refactor**

  - Terminology unified across the labeling pipeline: the former toggle term was replaced with "separator" for consistent inputs and logs.

- **Data / Public API**

  - Film mappings revised: introduced a female-focused film mapping and an additional film dataset exposed publicly.

- **Tests**
  - Test data and cases updated to use the new "separator" terminology and parsing behavior.

## [#142](https://github.com/MrIbrahem/ArWikiCats/pull/142) - 2025-12-01

- **Refactor**

  - Standardized naming and reworked Arabic label assembly flow.

- **Bug Fixes**

  - Improved Arabic label normalization and war-related label consistency.

- **Tests**

  - Expanded and reorganized unit tests for label creation and text-splitting logic; removed some legacy tests.

- **Chores**
  - Added city translations and parties data entries; updated changelog.
- **Compatibility**
  - Minor change to a data-dump decorator may require updating affected call sites.

## [#141](https://github.com/MrIbrahem/ArWikiCats/pull/141) - 2025-12-01

- **Refactor**

  - Internal naming and label assembly were standardized for clearer, safer Arabic label construction.

- **Bug Fixes**

  - Improved Arabic label normalization and war-related adjustments for more consistent final labels.

- **Compatibility**

  - Streamlined label-creation surface: legacy entry points replaced with a consolidated creation flow (call sites updated).

- **Tests**

  - Tests and imports updated and expanded to reflect the new label-creation API.

- **Chores**
  - Changelog entry added documenting the changes.

## [#140](https://github.com/MrIbrahem/ArWikiCats/pull/140) - 2025-12-01

- **Refactor**

  - Consolidated logging and removed legacy printing helpers; unified time-label flow and updated team-title resolver/fallback order.

- **Bug Fixes**

  - Time conversion normalizes inputs (e.g., strips leading "The ") for more consistent Arabic mappings.

- **Data**

  - Added comprehensive region JSON, refreshed people and taxon translation sources, and adjusted region export surface.

- **Tests**
  - Updated tests to align with new time conversion and team resolver behavior; removed obsolete tests.

## [#136](https://github.com/MrIbrahem/ArWikiCats/pull/136) - 2025-11-30

- **New Features**

  - Added a new translation resolver for non-feminine nationality-based labels, improving category translation coverage.

- **Improvements**

  - Applied result caching to core lookup functions, enhancing performance for repeated queries across the application.

- **Refactoring**

  - Consolidated internal helper functions for improved code organization and maintainability in formatting, translation, and job-processing modules.

- **Tests**
  - Expanded test coverage for translation resolvers and label resolution scenarios with new integration tests.

## [#134](https://github.com/MrIbrahem/ArWikiCats/pull/134) - 2025-11-30

- **Refactoring**

  - Reorganized and consolidated internal data structures across modules for improved maintainability.
  - Removed deprecated and unused data definitions.
  - Streamlined import paths and module dependencies.

- **Bug Fixes**

  - Enhanced category label resolution with improved fallback mechanisms for better translation coverage.

- **Tests**
  - Added comprehensive test coverage for label resolution and data formatting scenarios.

## [#132](https://github.com/MrIbrahem/ArWikiCats/pull/132) - 2025-11-30

- **Refactor**

  - Labels produced by year/type analysis are now consistently trimmed, removing unintended leading/trailing spaces for cleaner output.
  - Result structure for year/type analysis improved for clearer, more reliable metadata exposure.

- **Chores**
  - Tests and validations updated to require exact label matches, enforcing stricter output consistency.

## [#131](https://github.com/MrIbrahem/ArWikiCats/pull/131) - 2025-11-30

- **New Features**

  - Added comprehensive sports-to-Arabic label mappings and new lookup helpers for broader category coverage.
  - New helper for safely registering resolved media labels.

- **Bug Fixes**

  - Improved fallback logic for sports/national team label resolution and trimmed whitespace in results.

- **Refactor**

  - Reorganized sports translation data and streamlined label-formatting helpers for more reliable lookups.

- **Tests**
  - Added extensive data-driven tests covering sports and category label resolution.

## [#130](https://github.com/MrIbrahem/ArWikiCats/pull/130) - 2025-11-30

- **Bug Fixes**

  - Improved label resolution for sports and nationality-related categories with better fallback handling.
  - Fixed whitespace handling in label formatting for consistent output.

- **Refactor**

  - Reorganized sports translation module structure for better maintainability.
  - Enhanced data update mechanism with improved encapsulation.
  - Optimized data loading with caching for improved performance.

- **Tests**
  - Added comprehensive test coverage for sports category label translations.

## [#129](https://github.com/MrIbrahem/ArWikiCats/pull/129) - 2025-11-30

- **Added**

  - None.

- **Changed**

  - Refactored the sports match resolver to rely on the shared `FormatData` formatter with cached initialization and expanded template variants.

- **Fixed**

  - Preserved relaxed template matching by generating fallback keys within the formatter instead of manual regex handling.

- **Removed**
  - None.

## [#125](https://github.com/MrIbrahem/ArWikiCats/pull/125) - 2025-11-29

- **New Features**

  - Added pattern recognition and label creation for combined year+country categories to improve temporal/geographic translations.

- **Improvements**

  - Modularized formatting to unify multi-format template handling and package exports for more consistent labeling.

- **Bug Fixes**

  - Fixed a mapping typo that affected one year–country label and harmonized import surfaces.

- **Tests**

  - Expanded test coverage for year+country patterns and multi-format label generation.

- **Chores**
  - Consolidated API exports for better internal consistency.
  - Updated test coverage for new translation pattern functionality.

## [#124](https://github.com/MrIbrahem/ArWikiCats/pull/124) - 2025-11-29

- **New Features**

  - Improved category formatting with automatic country and year detection, plus time-aware label generation.

- **Data & Translations**

  - Added 100+ gendered job translations and an empty jobs template; updated several job entries and a sports commentator term; standardized country-year category keys and adjusted dataset counts.

- **Bug Fixes**

  - Minor wording replacement added for a sports profession.

- **Tests & Infrastructure**
  - New integration and unit tests for year/country formatting and jobs data; added an example comparison script.

## [#122](https://github.com/MrIbrahem/ArWikiCats/pull/122) - 2025-11-28

- **New Features**
  - Improved US state/territory resolution and party-role translation mappings; added a sports-term alternation for more reliable matching.
- **Bug Fixes**
  - Arabic state-name normalization refined (e.g., Washington, D.C. label corrected to drop duplicate/state prefix).
  - Simplified and more consistent key-pattern matching logic.
- **Tests**
  - Test suite reorganized: many tests retagged for targeted runs and new integration/unit tests added for state/party resolution.

## [#120](https://github.com/MrIbrahem/ArWikiCats/pull/120) - 2025-11-28

- **New Features**

  - Added new example scripts for processing 1,000 and 5,000 category datasets with performance metrics.
  - New example data file for category processing demonstrations.
  - Added batch processing and a public Arabic category label resolver; new example scripts for bulk runs and demos.

- **Documentation**

  - Updated project branding to ArWikiCats across all documentation.
  - Refreshed project metadata and build configuration.

- **Chores**
  - Reorganized internal package structure for improved maintainability.
  - Updated project build system and dependencies.

## [#119](https://github.com/MrIbrahem/ArWikiCats/pull/119) - 2025-11-28

- **Refactor**
  - Reorganized internal module structure by consolidating label resolution and normalization utilities across packages. Restructured dependencies and import paths to improve code organization and maintainability while preserving all existing functionality and public APIs with no impact to user-facing features.

## [#118](https://github.com/MrIbrahem/ArWikiCats/pull/118) - 2025-11-27

- **New Features**

  - Improved Arabic label resolution for sports and federation categories, with new translation fallbacks and broader coverage.

- **Bug Fixes**

  - Strengthened fallback logic and streamlined resolution flows for more consistent category matching and earlier, more reliable label selection.
  - Removed obsolete sport mappings to reduce ambiguity.

- **Tests**
  - Expanded and parameterized test suites covering sports, federation, squads and non-sports label resolution.

## [#117](https://github.com/MrIbrahem/ArWikiCats/pull/117) - 2025-11-27

- **New Features**

  - Added enhanced Arabic label resolution for sports-related content, enabling improved nationality and country classification mapping.

- **Bug Fixes**

  - Improved fallback mechanisms for label resolution to ensure more reliable category matching.

- **Tests**
  - Removed test markers to streamline test selection and filtering.
  - Expanded test coverage for label resolution functionality across multiple domains.

## [#114](https://github.com/MrIbrahem/ArWikiCats/pull/114) - 2025-11-26

- **Refactor [skeys.py](ArWikiCats/ma_lists/sports/skeys.py)**

- **New Features**

  - Expanded nationality and P17-style role/label coverage with additional country keys and improved label resolution/fallbacks.
  - Centralized definite-article handling for Arabic labels for more consistent output.

- **Bug Fixes**

  - Cleaned spacing/punctuation in city and sports club names.

- **Tests**
  - Added and expanded comprehensive tests for nationality, P17 label resolution, and definite-article formatting.

## [#113](https://github.com/MrIbrahem/ArWikiCats/pull/113) - 2025-11-26

- **New Features**

  - Added century/millennium date pattern recognition.
  - Extended category data structure with country information.

- **Bug Fixes**

  - Improved data dumping and logging functionality for specific operations.
  - Refined test coverage with expanded validation scenarios.

- **Refactor**

  - Simplified internal resolution logic to reduce code duplication.
  - Restructured team job generation using a more data-driven approach.

- **Style**
  - Enhanced code formatting and readability throughout the codebase.

## [#112](https://github.com/MrIbrahem/ArWikiCats/pull/112) - 2025-11-26

- Expanded Arabic language support by adding gender-specific translations for numerous job and occupation titles across sports and professional categories, improving localization coverage for multilingual users.

## [#111](https://github.com/MrIbrahem/ArWikiCats/pull/111) - 2025-11-26

- **New Features**

  - Added public helpers ethnic_label and add_all for improved label generation.

- **Chores**

  - Reorganized modules and updated import paths.
  - Removed NN_table/related gendered tables from the public translations API.

- **Public API**

  - Renamed get_con_3 → get_suffix and updated parameter names/signatures that callers see.

- **Tests**

  - Added and updated unit tests to cover new helpers and adjusted imports.

- **Documentation**
  - Expanded docstrings and examples for several public functions.

## [#110](https://github.com/MrIbrahem/ArWikiCats/pull/110) - 2025-11-25

- **New Features**
  - Added Arabic translations for several category terms and new occupational labels, including a "non-fiction writers" role and new population/occupation labels.
- **Chores**
  - Expanded translation datasets and reorganized translation/region mappings to improve coverage.
  - Added runtime diagnostic reporting to many translation modules.
- **Tests**
  - Updated test data to reflect new category translations and removed one outdated case.

## [#109](https://github.com/MrIbrahem/ArWikiCats/pull/109) - 2025-11-25

- **New Features**

  - Large expansion of category and label datasets (many sports, events, nationality and organization entries).

- **Improvements**

  - Improved label resolution with additional fallback strategies for jobs, nationalities and multi-sport contexts.
  - Added runtime deduplication to avoid duplicate exported records.
  - Minor log-format refinement for clearer resolved-label messages.

- **Tests**

  - Expanded and reorganized tests covering prefixes, multi-sport mappings and job/nationality labeling.

- **Breaking Changes**
  - Removed several previously exported prefix/mapping symbols.

## [#106](https://github.com/MrIbrahem/ArWikiCats/pull/106) - 2025-11-24

- **New Features**

  - Consolidated category label resolution and new sport-localization loaders.
  - Dual-token nationality+sport normalization for richer localized labels.
  - Added national gender count entries to diagnostics.

- **Bug Fixes**

  - Improved category matching with optional prefix handling.

- **Refactoring**

  - Simplified translation APIs and reorganized translation exports/data.

- **Tests**
  - Expanded translation coverage and consistency tests; removed noisy debug prints.

## [#105](https://github.com/MrIbrahem/ArWikiCats/pull/105) - 2025-11-24

- **New Features**

  - Added a loader for female national sport formats and expanded translation mappings for many sports/categories.

- **Refactoring**

  - Streamlined national-format resolution and removed an older nationality-aware labeling pipeline, simplifying label generation paths.

- **Tests**

  - Added multiple new test suites and expanded test data; also removed obsolete nationality-specific tests.

- **Chores**
  - General cleanup: removed extraneous commented markers and updated exports.

## [#104](https://github.com/MrIbrahem/ArWikiCats/pull/104) - 2025-11-23

- **Refactor**
  - Reorganized language and film-category label resolution for clearer, layered behavior.
- **Behavioral Improvements**
  - Improved year/time extraction and Arabic-year fallback so categories show more accurate year labels.
- **Breaking Change / API**
  - Year-handling call now supplies separate English and Arabic year values — callers and integrations may need minor updates.
- **Tests**
  - Updated tests to align with the revised year handling and resolver behavior.

## [#102](https://github.com/MrIbrahem/ArWikiCats/pull/102) - 2025-11-23

- **New Features**

  - Enhanced relation processing with improved handling of various dash formats and logging.
  - Updated sports-related data processing and labeling system.

- **Bug Fixes**

  - Fixed duplicate Arabic article generation in text processing.
  - Corrected redundant nationality mappings.
  - Resolved data independence issues to prevent unintended mutations.

- **Data Updates**

  - Updated population and employment statistics.
  - Added proper English and Arabic names for Brunei nationality.

- **Tests**
  - Expanded test coverage for geopolitical relations and sports data scenarios.

## [#101](https://github.com/MrIbrahem/ArWikiCats/pull/101) - 2025-11-23

- **New Features**

  - Added parameterized year- and country-based category translations to improve localization.

- **Updates**

  - Integrated larger translation datasets and switched several translation initializations to file-backed loads.
  - Year-handling updated across labeling flows for consistent template lookup and replacement.
  - Labeling now surfaces counts of pattern-derived category matches for better diagnostics.

- **Removals**

  - Deleted a few television translation keys and several commentator-related mappings.

- **Tests**
  - Updated tests to use parameterized placeholders and reflect dataset/reordering changes.

## [#99](https://github.com/MrIbrahem/ArWikiCats/pull/99) - 2025-11-22

- **Chores**

  - Expanded geographic lookup variants (more country/admin and India secondary regions), added lowercase lookup support, enhanced US state/party/county mappings, consolidated translation exports, removed an obsolete translation bundle and an older add-in table, and added new job-related entries including "censuses"
  - Removed a verbose startup log file

- **Tests**

  - Added dedicated US counties translation tests and adjusted related expectations

- **Bug Fixes**

  - Improved case-insensitive key lookup behavior across translation tables

- **Chores**
  - Disabled several data-dump decorators to stop auxiliary data-dumping side effects

## [#98](https://github.com/MrIbrahem/ArWikiCats/pull/98) - 2025-11-22

- **Chores**
  - Updated Arabic transliterations for Minnesota-related terms across translation databases and tests, correcting the spelling from "مينيسوتا" to "منيسوتا" for improved accuracy in geographic names, sports teams, and related entries.

## [#97](https://github.com/MrIbrahem/ArWikiCats/pull/96) - 2025-11-21

- Expanded geographic lookup APIs: more country, admin-region and India/secondary-region translation variants and lowercased lookup support.
- More comprehensive US location variant mappings for states, parties and counties.

- **Tests**

  - Added dedicated US counties translation tests.
  - Adjusted test data by removing specific deprecated entries.

- **Chores**
  - Consolidated and reorganized translation data and exports.
  - Removed an obsolete translation entry.

## [#96](https://github.com/MrIbrahem/ArWikiCats/pull/96) - 2025-11-21

- **New Features**

  - Expanded geographic translation coverage with lowercased key variants and richer region/province labels.
  - Added utilities to load and normalize JSON-based translation data for more consistent lookups.

- **Refactor**

  - Reorganized translation data into clearer subdirectories and consolidated redundant translation sets.
  - Streamlined public translation exports and simplified composition of region mappings.

- **Tests**

  - Updated fixtures to match reorganized data paths and added tests for JSON loading/filtering.

- **Chores**
  - Minor formatting cleanups (removed extraneous comments/blank lines).

## [#94](https://github.com/MrIbrahem/ArWikiCats/pull/94) - 2025-11-21

- **Documentation**

  - Added a new English README and updated the main README header/branding.

- **New Features / Refactor**

  - Reorganized Arabic label generation: new modular pipeline and public exports; legacy implementation removed.

- **Bug Fixes**

  - Strengthened whitespace normalization to collapse and trim spaces for more consistent labels.

- **Tests**
  - Updated tests to ignore surrounding whitespace during normalization.

## [#93](https://github.com/MrIbrahem/ArWikiCats/pull/93) - 2025-11-21

- **New Features**

  - Enhanced Arabic labeling system with improved category and type resolution capabilities.

- **Tests**

  - Added comprehensive validation coverage for Arabic labeling edge cases and data quality checks.
  - Updated test datasets with additional category mappings for validation.

- **Chores**
  - Optimized label caching performance with increased cache limits.
  - Internal code restructuring and refactoring for improved maintainability.

## [#87](https://github.com/MrIbrahem/ArWikiCats/pull/87) - 2025-11-20

- **New Features**

  - Added enhanced Arabic labeling system with comprehensive category and type resolution capabilities.

- **Tests**

  - Expanded test coverage with new bug-check test cases for Arabic labeling validation.
  - Added targeted test cases for label generation with edge-case data.

- **Chores**
  - Introduced refactoring plan document for system architecture improvements.
  - Internal code restructuring for maintainability and modularity.

## [#86](https://github.com/MrIbrahem/ArWikiCats/pull/86) - 2025-11-20

- **Tests**

  - Added extensive dataset-driven and parameterized tests covering Arabic label generation, event-driven differences, edge cases, and diff dumps for mismatches.

- **Refactor**

  - Modularized and simplified the label-generation flow, standardized input normalization, and added caching and diagnostics for more consistent, faster lookups.

- **Chore**
  - Enhanced dump utility to optionally skip writing when output matches a specified field to reduce redundant logs.

## [#85](https://github.com/MrIbrahem/ArWikiCats/pull/85) - 2025-11-20

- **New Features**

  - Added public utilities for text normalization and relation-word detection
  - New configurable data-dump decorator that can be enabled per call
  - Exposed additional helpers and logging wrapper to package API

- **Improvements**

  - Better runtime logging control with ability to disable printing
  - Expanded translation data and conditional initialization for some datasets
  - Centralized and tightened code-formatting/tooling settings

- **Tests**
  - Expanded test coverage and new fast/parametrized tests
  - Updated test markers to a new default skip marker (skip2)

## [#84](https://github.com/MrIbrahem/ArWikiCats/pull/84) - 2025-11-20

- **New Features**

  - Expanded time parsing: BC/BCE, decades, centuries, month–year and range patterns.

- **Refactors**

  - Consolidated label-resolution logic and updated public exports to expose the revised label utilities.

- **Bug Fixes**

  - Fixed translation data quoting/syntax to ensure correct label generation.

- **Style**

  - Widespread formatting, import-style and logging-message cleanups.

- **Tests**
  - Many test import/style refinements, some test data scope reductions and a few altered test call sites.

## [#82](https://github.com/MrIbrahem/ArWikiCats/pull/82) - 2025-11-19

- **New Features**

  - Added data-saving decorators to key functions for improved performance.
  - Enhanced helper functions for better code organization in language and team processing.

- **Bug Fixes & Improvements**

  - Migrated debugging output from print-based system to centralized logging for better diagnostics.
  - Expanded test coverage with additional language and translation mappings.

- **Code Cleanup**
  - Removed print utility module and unused public exports.
  - Cleaned up placeholder comments throughout the codebase.

## [#81](https://github.com/MrIbrahem/ArWikiCats/pull/81) - 2025-11-19

- **New Features**

  - Restructured and expanded data metadata with 50+ new keys for improved categorization of regions, sports, films, and people data.
  - Added people data query integration.

- **Tests**

  - Expanded test coverage with parametrized data-driven tests across multiple modules.

- **Refactor**
  - Improved imports and removed unused code; transitioned to runtime data loading.

## [#79](https://github.com/MrIbrahem/ArWikiCats/pull/79) - 2025-11-19

- **New Features**

  - Optional JSONL data capture decorator added; enabled for one title extraction function to persist inputs/outputs.

- **Tests**

  - Vastly expanded parameterized test coverage and datasets across many modules to improve translation and mapping validations.

- **Chores**
  - Safer file creation and write behavior for persistence.
  - Several automated persistence hooks disabled/commented out to reduce runtime writes.

## [#78](https://github.com/MrIbrahem/ArWikiCats/pull/78) - 2025-11-18

- **New Features**

  - Expanded gendered prefix/suffix translations, year-based variants, and improved suffix-aware nationality/religion labeling with optional persistence.

- **Refactor**

  - Reorganized translation exports, consolidated label-generation logic, and standardized logging/label handling.

- **Bug Fixes**

  - Prevent duplicate "racing" variants by adding guarded generation rules.

- **Tests**
  - Added many parameterized tests for suffix/expatriate scenarios and removed several legacy tests.

## [#77](https://github.com/MrIbrahem/ArWikiCats/pull/77) - 2025-11-18

- **New Features**

  - Enhanced job categorization with richer nationality and gendered labels and example data export.

- **Bug Fixes**

  - Normalized single-item serialization and safer file I/O with error handling.

- **Refactor**

  - Streamlined label-resolution flow; removed several external fallback lookups and redundant boolean flags.

- **Tests**
  - Extensive new unit and integration tests covering job-label logic and real examples.

## [#74](https://github.com/MrIbrahem/ArWikiCats/pull/74) - 2025-11-17

- **Bug Fixes**

  - Enhanced input validation and type-checking across modules to prevent processing of invalid data.
  - Fixed caching issue with dictionary-type parameters.

- **Refactor**
  - Streamlined country data resolution pipeline with centralized logic.
  - Optimized data structure handling for improved performance.

## [#73](https://github.com/MrIbrahem/ArWikiCats/pull/73) - 2025-11-17

- **Refactor**
  - Optimized pattern matching throughout the application for improved performance.

## [#69](https://github.com/MrIbrahem/ArWikiCats/pull/69) - 2025-11-17

- **New Features**

  - Streamlined event/category processing pipeline with batch label helpers
  - New parsing utilities for templates, episodes, and footballer/player suffixes

- **Improvements**

  - More consistent category normalization and standardized label prefixing
  - Reduced logging verbosity for test/output flows
  - Expanded translation entries for several cities/clubs

- **Tests**
  - Added and reorganized unit tests covering parsing, episodes, templates, and label resolution

## [#68](https://github.com/MrIbrahem/ArWikiCats/pull/68) - 2025-11-17

- **Refactor**

  - Reorganized internal module structure for better code maintainability and clarity.
  - Consolidated category labeling logic into streamlined components.
  - Simplified API signatures to improve consistency across bot modules.
  - Improved logging infrastructure for better system monitoring.

- **Bug Fixes**
  - Removed erroneous internal imports that could cause module initialization issues.

## [#67](https://github.com/MrIbrahem/ArWikiCats/pull/67) - 2025-11-17

- **Refactor**
  - Large internal reorganization: many modules and tests now reference a consolidated "translations" package and a new "translations_formats" area.
  - Formatting utility relocated into the translations_formats package; legacy formatting module removed.
  - Helper imports consolidated under a helps area.
  - No changes to public APIs or end-user behavior; functionality and external interfaces remain the same.

## [#65](https://github.com/MrIbrahem/ArWikiCats/pull/65) - 2025-11-16

- **Refactor [Nationality.py](ArWikiCats/translations/nats/Nationality.py)**

  - Reorganized labeling engine and moved label construction into a focused start-with-year/type workflow; simplified mapping usage and renamed a public category mapping for clarity.
  - Overhauled nationality data and normalization to improve country/name lookups and translations.

- **Bug Fixes**

  - Fixed month+year/BC regex in time-to-Arabic conversion.

- **Tests**
  - Updated, added, and relocated tests to cover the new labeling flow and time parsing; removed obsolete test harnesses.

## [#64](https://github.com/MrIbrahem/ArWikiCats/pull/64) - 2025-11-16

- **New Features**

  - Added modular event labeling with improved country and type processing
  - New time-matching utility for first-match retrieval
  - Added century labeling variant support

- **Bug Fixes**

  - Updated regex patterns for consistent dash character handling
  - Improved category normalization logic

- **Refactors [bot_lab.py](ArWikiCats/ma_bots/year_or_typeo/bot_lab.py)**

  - Refactored event labeling into modular helper functions
  - Simplified category normalization
  - Replaced legacy parsing functions with efficient aliases

- **Tests**
  - Added unit tests for event labeling with century-focused coverage
  - Expanded pattern matching test coverage
  - Added slow test markers for performance-intensive tests

## [#62](https://github.com/MrIbrahem/ArWikiCats/pull/62) - 2025-11-15

- **Refactor**

  - Modernized internal caching mechanisms across the application to use Python's built-in caching utilities instead of manual implementations, improving code maintainability and performance consistency.

- **Tests**
  - Added skeleton test files across multiple modules to establish testing infrastructure and improve code coverage foundation.

## [#59](https://github.com/MrIbrahem/ArWikiCats/pull/59) - 2025-11-14

- **Refactor [Sport_key.py](ArWikiCats/translations/sports/Sport_key.py)**

  - Restructured sport key data handling into a modular pipeline with validation and alias expansion for improved maintainability.
  - Standardized constant naming conventions across the codebase for consistency.

- **New Features**

  - Added template rendering utilities for generating sport labels with year-based and formatted variants.

- **Bug Fixes**

  - Removed deprecated method from sports formatting module.
  - Updated test fixtures to reflect current data requirements.

- **Tests**
  - Removed obsolete test file for normalization logic.
  - Updated test coverage to align with refactored APIs and new data structure.

## [#58](https://github.com/MrIbrahem/ArWikiCats/pull/58) - 2025-11-14

- Refactor [fixtitle.py](ArWikiCats/fix/fixtitle.py)
- **New Features**

  - Added comprehensive Arabic text normalization with improved handling of formulas, prepositions, time expressions, and category-specific replacements.

- **Performance Improvements**

  - Implemented function-level caching across multiple modules to enhance response times.

- **API Updates**
  - Standardized naming convention for exported constants to uppercase format for consistency.

## [#54](https://github.com/MrIbrahem/ArWikiCats/pull/54) - 2025-11-13

- **Refactor [all_keys2.py](ArWikiCats/translations/mixed/all_keys2.py)**

  - Restructured internal data mapping generation for improved maintainability and scalability of data definitions.

- **New Features**

  - Expanded available data mappings to include international federations, educational institutions, maritime vessels, religious traditions, and political categories.

- **Chores**
  - Updated naming conventions for consistency across the public API.

## [#53](https://github.com/MrIbrahem/ArWikiCats/pull/53) - 2025-11-13

- **Bug Fixes**

  - Corrected Arabic translations for sports categories, publications, and cultural topics.
  - Improved consistency of multilingual mappings across datasets.

- **Tests**

  - Added comprehensive test coverage for wheelchair sports categories and classifications.
  - Expanded validation for cultural and ethnic category translations.
  - Implemented regression tests for Arabic label accuracy.

- **Chores**
  - Refactored internal data structure organization for improved maintainability.
  - Standardized naming conventions across core mappings.

## [#50](https://github.com/MrIbrahem/ArWikiCats/pull/50) - 2025-11-12

- **Refactor [Jobs.py](ArWikiCats/translations/jobs/Jobs.py)**
  - Updated job data API naming conventions and restructured internal data assembly pipeline for improved maintainability and consistency.
  - Enhanced data normalization for automatic sorting and deduplication of lists and dictionaries.

## [#47](https://github.com/MrIbrahem/ArWikiCats/pull/47) - 2025-11-11

- **New Features**

  - Added support for wheelchair racers and expanded wheelchair sport coverage (rugby, tennis, handball, curling, fencing) with localized labels and metadata.
  - New country title processing aid to improve place/category labeling.

- **Bug Fixes**

  - Updated translations: discus throwers and figure skating on television.
  - Removed an obsolete wheelchair basketball key from the sports index.

- **Tests**

  - Added comprehensive wheelchair labeling tests.

- **Chores**
  - Added changelog entry and general internal string-handling cleanups.

## [#46](https://github.com/MrIbrahem/ArWikiCats/pull/46) - 2025-11-11

- **New Features [format_data.py](ArWikiCats/translations_formats/format_data.py)**
  - Introduces FormatData class with template-based string transformation logic, including regex pattern matching from sport keys, placeholder replacement, category normalization, and a unified search() method orchestrating the lookup pipeline. Includes a sample usage function.

## [#45](https://github.com/MrIbrahem/ArWikiCats/pull/45) - 2025-11-11

- **New Features**

  - Improved organization and categorization of sports team-related data
  - Enhanced support for sports category mappings and labels

- **Chores**
  - Reorganized internal data structures for better sports information management
  - Updated code formatting and test annotations

## [#44](https://github.com/MrIbrahem/ArWikiCats/pull/44) - 2025-11-10

- **Refactor [jobs_players_list.py](ArWikiCats/translations/jobs/jobs_players_list.py)**

## [#42](https://github.com/MrIbrahem/ArWikiCats/pull/42) - 2025-11-10

- **Refactor**

  - Optimized data loading performance through lazy initialization and caching mechanisms.
  - Reorganized internal data structures and standardized naming conventions for consistency.
  - Expanded public API to expose additional utility functions and data resources.

- **Performance Improvements**

  - Enhanced lookup efficiency with memoized function calls and cached data retrieval.

- **Tests**
  - Added slow-test markers for improved test categorization and execution management.

## [#41](https://github.com/MrIbrahem/ArWikiCats/pull/41) - 2025-11-09

- **Refactor [pop_All_2018_bot.py](ArWikiCats/translations/mix_data/pop_All_2018_bot.py)**
  - Reorganized internal data-loading and resolution flows for consistency.
  - Removed deprecated backward-compatibility aliases and an obsolete resolver.
  - Consolidated imports and simplified name-resolution logic to improve maintainability.

## [#37](https://github.com/MrIbrahem/ArWikiCats/pull/37) - 2025-11-09

- **New Features**

  - Centralized runtime configuration controlling printing, Wikidata, Kooora, stubs, and other app flags.
  - New colored text formatting helper for styled output.

- **Refactor**

  - Replaced argv-driven flags with settings-driven behavior across the app.
  - Unified logging via a wrapper and simplified printing API to delegate to the logger.

- **Chores**
  - Updated ignore list (added generated start file).

## [#36](https://github.com/MrIbrahem/ArWikiCats/pull/36) - 2025-11-09

- **Refactor [jobs_singers.py](ArWikiCats/translations/jobs/jobs_singers.py)**

  - Updated public constant names to follow Python naming conventions (MEN_WOMENS_SINGERS, FILMS_TYPE, SINGERS_TAB)
  - Reorganized data generation with modular helper functions
  - Consolidated internal data mappings and improved code organization

- **Tests**
  - Updated tests to align with refactored constant names

## [#35](https://github.com/MrIbrahem/ArWikiCats/pull/35) - 2025-11-09

- **New Features**

  - Expanded job and place name datasets with additional job categories and extensive place-name translations for improved Arabic localization.

- **Refactor [Cities.py](ArWikiCats/translations/geo/Cities.py), [jobs_defs.py](ArWikiCats/translations/jobs/jobs_defs.py)**

  - Switched to centralized data-driven loading for geographic names and job labels to simplify updates and reduce hardcoded entries.

- **Chores**
  - Added new data assets and updated changelog with two new entries and an expanded existing entry.

## [#34](https://github.com/MrIbrahem/ArWikiCats/pull/34) - 2025-11-09

- **New Features**

  - Expanded and enriched job, player and singer datasets with additional entries and gendered labels, improving localized display.

- **Refactor**

  - Migrated data loading to centralized JSON sources for jobs, singers and players to enable data-driven updates and consistency.

- **Chores**
  - Added new JSON data files to supply the updated datasets and translations.

## [#32](https://github.com/MrIbrahem/ArWikiCats/pull/32) - 2025-11-08

### Changed

- Refactored all modules under `ArWikiCats/make_bots/o_bots` with comprehensive type hints, PEP 8 naming, and Google-style documentation.
- Centralised shared suffix-matching and caching helpers to eliminate duplicated logic across bots.
- Standardised logging usage and cache handling, adding inline comments to clarify complex resolution flows.
- Updated dependent bots to consume the new PEP 8 interfaces and refreshed formatting across touched files.

### Added

- Introduced `ArWikiCats/make_bots/o_bots/utils.py` to host reusable helpers for cache keys, suffix resolution, and article handling.

## #31

- **Bug Fixes**

  - Improved template and label resolution with fallbacks
  - Consolidated year-handling logic

- **Tests**

  - Expanded test coverage for locale, year, and historical-period data

- **Improvements**
  - Refined public API with clearer naming conventions
  - Enhanced text normalization pipeline for Arabic label processing

---

## #30

- **Bug Fixes**

  - Improved template/label resolution with additional fallback steps for more accurate mapping.

- **Tests**

  - Reorganized and expanded locale/year and historical-period test data; trimmed other year mappings for focused coverage.

- **Documentation**

  - Standardized and simplified changelog structure and headers.

- **Chores**
  - Removed the automatic type-hint injector module; consolidated dependency imports and removed optional local fallbacks; minor typing and config adjustments.

---

## #13

- **Refactor**

  - Reorganized package structure with new submodules for improved organization (sports, politics, companies, utilities).
  - Updated import paths across modules for better maintainability.

- **New Features**
  - Added comprehensive localization mappings for sports, companies, buildings, and medical terminology.
  - Expanded translation data for enhanced language support and domain coverage.

---

## #5 [Enhance event label processing and test suite reorganization] - 2025-11-05

This update improves label processing accuracy and restructures the test architecture for better maintainability.

### Added

- Introduced new event label processing functionality with enhanced category handling.
- Expanded structured test suites covering various event domains such as culture, entertainment, geography, institutions, people, places, politics, science, sports, and temporal data.

### Changed

- Refactored imports and package-level exports for consistency.
- Updated pytest configuration for broader and more efficient test discovery.
- Improved data consistency and label comparison logic.

### Fixed

- Corrected import paths and unified test result assertions.

### Removed

- Cleaned up deprecated test scripts and legacy helpers replaced by the unified pytest structure.

---

## #3 - 2025-11-03

### Added

- New module `ArWikiCats/make_bots/reg_lines.py` for centralized regular expression definitions.
- "solar eclipses" added to the country add-ins list.

### Changed

- Refactored multiple Python files to utilize centralized and precompiled regex patterns.
- Simplified the event labeling flow in `ArWikiCats/make_bots/ma_bots/year_or_typeo/bot_lab.py` and `ArWikiCats/make_bots/ma_bots/event2bot.py` by using centralized regex definitions.

---

## Pull Request 2

- Removed the old `ma_lists_bots` module and updated various modules to use the new submodules under `translations`.
- Unified JSON file loading via the `open_json_file` function, reorganized public exports, and adjusted relative imports.
- Added a new logger and HTTP helper utilities, updating dependent modules accordingly.
- Removed old scripts and tools from the `others` directory and reorganized import tests.
- Updated tests and documentation to align with the new module structure.

---

## Pull Request 1

- **New Features:** Added a unified logger and web request utilities, enabling team/player and Wikidata searches through simple command-line tools.
- **Refactor:** Unified JSON and data file loading with expanded public exports; cleaned up old tools and scripts.
- **Documentation:** Removed an outdated diagram from the README and updated the changelog in line with new policies.
- **Tests:** Added tests for external search operations and updated import paths.
- **Maintenance Tasks:** Added ignore rules for files generated during local development.
