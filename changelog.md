## [Add comprehensive Arabic README] - 2025-11-20

* **Added**
  * README عربي شامل يصف هدف المشروع، طريقة التثبيت والاستخدام، وخريطة المجلدات.
  * إرشادات لتوسيع بيانات الترجمات وتشغيل الاختبارات للحفاظ على استقرار المنهجية.

## [#86](https://github.com/MrIbrahem/make2_new/pull/86) - 2025-11-20

* **Tests**
  * Added extensive dataset-driven and parameterized tests covering Arabic label generation, event-driven differences, edge cases, and diff dumps for mismatches.

* **Refactor**
  * Modularized and simplified the label-generation flow, standardized input normalization, and added caching and diagnostics for more consistent, faster lookups.

* **Chore**
  * Enhanced dump utility to optionally skip writing when output matches a specified field to reduce redundant logs.

## [#85](https://github.com/MrIbrahem/make2_new/pull/85) - 2025-11-20

* **New Features**
  * Added public utilities for text normalization and relation-word detection
  * New configurable data-dump decorator that can be enabled per call
  * Exposed additional helpers and logging wrapper to package API

* **Improvements**
  * Better runtime logging control with ability to disable printing
  * Expanded translation data and conditional initialization for some datasets
  * Centralized and tightened code-formatting/tooling settings

* **Tests**
  * Expanded test coverage and new fast/parametrized tests
  * Updated test markers to a new default skip marker (skip2)

## [#84](https://github.com/MrIbrahem/make2_new/pull/84) - 2025-11-20

* **New Features**
  * Expanded time parsing: BC/BCE, decades, centuries, month–year and range patterns.

* **Refactors**
  * Consolidated label-resolution logic and updated public exports to expose the revised label utilities.

* **Bug Fixes**
  * Fixed translation data quoting/syntax to ensure correct label generation.

* **Style**
  * Widespread formatting, import-style and logging-message cleanups.

* **Tests**
  * Many test import/style refinements, some test data scope reductions and a few altered test call sites.

## [#82](https://github.com/MrIbrahem/make2_new/pull/82) - 2025-11-19

* **New Features**
  * Added data-saving decorators to key functions for improved performance.
  * Enhanced helper functions for better code organization in language and team processing.

* **Bug Fixes & Improvements**
  * Migrated debugging output from print-based system to centralized logging for better diagnostics.
  * Expanded test coverage with additional language and translation mappings.

* **Code Cleanup**
  * Removed print utility module and unused public exports.
  * Cleaned up placeholder comments throughout the codebase.

## [#81](https://github.com/MrIbrahem/make2_new/pull/81) - 2025-11-19

* **New Features**
  * Restructured and expanded data metadata with 50+ new keys for improved categorization of regions, sports, films, and people data.
  * Added people data query integration.

* **Tests**
  * Expanded test coverage with parametrized data-driven tests across multiple modules.

* **Refactor**
  * Improved imports and removed unused code; transitioned to runtime data loading.

## [#79](https://github.com/MrIbrahem/make2_new/pull/79) - 2025-11-19
* **New Features**
  * Optional JSONL data capture decorator added; enabled for one title extraction function to persist inputs/outputs.

* **Tests**
  * Vastly expanded parameterized test coverage and datasets across many modules to improve translation and mapping validations.

* **Chores**
  * Safer file creation and write behavior for persistence.
  * Several automated persistence hooks disabled/commented out to reduce runtime writes.

## [#78](https://github.com/MrIbrahem/make2_new/pull/78) - 2025-11-18

* **New Features**
  * Expanded gendered prefix/suffix translations, year-based variants, and improved suffix-aware nationality/religion labeling with optional persistence.

* **Refactor**
  * Reorganized translation exports, consolidated label-generation logic, and standardized logging/label handling.

* **Bug Fixes**
  * Prevent duplicate "racing" variants by adding guarded generation rules.

* **Tests**
  * Added many parameterized tests for suffix/expatriate scenarios and removed several legacy tests.

## [#77](https://github.com/MrIbrahem/make2_new/pull/77) - 2025-11-18

* **New Features**
  * Enhanced job categorization with richer nationality and gendered labels and example data export.

* **Bug Fixes**
  * Normalized single-item serialization and safer file I/O with error handling.

* **Refactor**
  * Streamlined label-resolution flow; removed several external fallback lookups and redundant boolean flags.

* **Tests**
  * Extensive new unit and integration tests covering job-label logic and real examples.


## [#74](https://github.com/MrIbrahem/make2_new/pull/74) - 2025-11-17

* **Bug Fixes**
  * Enhanced input validation and type-checking across modules to prevent processing of invalid data.
  * Fixed caching issue with dictionary-type parameters.

* **Refactor**
  * Streamlined country data resolution pipeline with centralized logic.
  * Optimized data structure handling for improved performance.


## [#73](https://github.com/MrIbrahem/make2_new/pull/73) - 2025-11-17

* **Refactor**
  * Optimized pattern matching throughout the application for improved performance.

## [#69](https://github.com/MrIbrahem/make2_new/pull/69) - 2025-11-17

* **New Features**
  - Streamlined event/category processing pipeline with batch label helpers
  - New parsing utilities for templates, episodes, and footballer/player suffixes

* **Improvements**
  - More consistent category normalization and standardized label prefixing
  - Reduced logging verbosity for test/output flows
  - Expanded translation entries for several cities/clubs

* **Tests**
  - Added and reorganized unit tests covering parsing, episodes, templates, and label resolution
## [#68](https://github.com/MrIbrahem/make2_new/pull/68) - 2025-11-17

* **Refactor**
  * Reorganized internal module structure for better code maintainability and clarity.
  * Consolidated category labeling logic into streamlined components.
  * Simplified API signatures to improve consistency across bot modules.
  * Improved logging infrastructure for better system monitoring.

* **Bug Fixes**
  * Removed erroneous internal imports that could cause module initialization issues.

## [#67](https://github.com/MrIbrahem/make2_new/pull/67) - 2025-11-17

* **Refactor**
  * Large internal reorganization: many modules and tests now reference a consolidated "translations" package and a new "translations_formats" area.
  * Formatting utility relocated into the translations_formats package; legacy formatting module removed.
  * Helper imports consolidated under a helps area.
  * No changes to public APIs or end-user behavior; functionality and external interfaces remain the same.

## [#65](https://github.com/MrIbrahem/make2_new/pull/65) - 2025-11-16

* **Refactor [Nationality.py](src/translations/nats/Nationality.py)**
  * Reorganized labeling engine and moved label construction into a focused start-with-year/type workflow; simplified mapping usage and renamed a public category mapping for clarity.
  * Overhauled nationality data and normalization to improve country/name lookups and translations.

* **Bug Fixes**
  * Fixed month+year/BC regex in time-to-Arabic conversion.

* **Tests**
  * Updated, added, and relocated tests to cover the new labeling flow and time parsing; removed obsolete test harnesses.

## [#64](https://github.com/MrIbrahem/make2_new/pull/64) - 2025-11-16

* **New Features**
  * Added modular event labeling with improved country and type processing
  * New time-matching utility for first-match retrieval
  * Added century labeling variant support

* **Bug Fixes**
  * Updated regex patterns for consistent dash character handling
  * Improved category normalization logic

* **Refactors [bot_lab.py](src/make2_bots/ma_bots/year_or_typeo/bot_lab.py)**
  * Refactored event labeling into modular helper functions
  * Simplified category normalization
  * Replaced legacy parsing functions with efficient aliases

* **Tests**
  * Added unit tests for event labeling with century-focused coverage
  * Expanded pattern matching test coverage
  * Added slow test markers for performance-intensive tests

## [#62](https://github.com/MrIbrahem/make2_new/pull/62) - 2025-11-15

* **Refactor**
  * Modernized internal caching mechanisms across the application to use Python's built-in caching utilities instead of manual implementations, improving code maintainability and performance consistency.

* **Tests**
  * Added skeleton test files across multiple modules to establish testing infrastructure and improve code coverage foundation.
