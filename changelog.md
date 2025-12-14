## [#211](https://github.com/MrIbrahem/ArWikiCats/pull/211) - 2025-12-14

* **New Features**
  * Added american-football and canadian-football translation entries with job/label mappings.

* **Improvements**
  * Expanded and normalized sports & job translation coverage (hyphenation and key normalization).
  * Cleaned up and reorganized Canadian football variant entries.

* **Performance**
  * Added caching to resolution logic for faster repeated lookups.

* **Tests**
  * Added Canadian football test coverage and renamed tests for clarity.

* **Documentation**
  * Updated README resource paths to reorganized JSON locations.

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

- **Refactors [bot_lab.py](ArWikiCats/make_bots/ma_bots/year_or_typeo/bot_lab.py)**

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
