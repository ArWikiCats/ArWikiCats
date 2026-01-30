"""
Unit tests for model_data_form.py module.

This module provides tests for FormatDataFrom class which is a dynamic wrapper
for handling category transformations with customizable callbacks.
"""

from ArWikiCats.translations_formats.DataModel.model_data_form import FormatDataFrom


class TestFormatDataFromInit:
    """Tests for FormatDataFrom initialization."""

    def test_init_basic(self):
        """Test basic initialization of FormatDataFrom."""
        formatted_data = {"{year1} {country1}": "{country1} في {year1}"}

        bot = FormatDataFrom(
            formatted_data=formatted_data,
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "اليمن",
            match_key_callback=lambda x: "yemen",
        )

        assert bot.formatted_data == formatted_data
        assert bot.key_placeholder == "{country1}"
        assert bot.value_placeholder == "{country1}"
        assert bot.formatted_data_ci == {"{year1} {country1}": "{country1} في {year1}"}

    def test_init_creates_case_insensitive_formatted_data(self):
        """Test that formatted_data_ci is created case-insensitively."""
        formatted_data = {"{Year1} {Country1}": "{country1} في {year1}"}

        bot = FormatDataFrom(
            formatted_data=formatted_data,
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        assert "{year1} {country1}" in bot.formatted_data_ci

    def test_init_with_fixing_callback(self):
        """Test initialization with fixing_callback."""

        def fix_callback(label):
            return label.replace("في", "من")

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
            fixing_callback=fix_callback,
        )

        assert bot.fixing_callback is fix_callback


class TestFormatDataFromMatchKey:
    """Tests for FormatDataFrom.match_key method."""

    def test_match_key_uses_callback(self):
        """Test that match_key uses the provided callback."""

        def match_callback(text):
            return "matched_key" if "test" in text else ""

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{key}",
            value_placeholder="{key}",
            search_callback=lambda x: "",
            match_key_callback=match_callback,
        )

        result = bot.match_key("test input")
        assert result == "matched_key"

    def test_match_key_no_match(self):
        """Test match_key when no match."""

        def match_callback(text):
            return "matched_key" if "test" in text else ""

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{key}",
            value_placeholder="{key}",
            search_callback=lambda x: "",
            match_key_callback=match_callback,
        )

        result = bot.match_key("no match here")
        assert result == ""


class TestFormatDataFromNormalizeCategory:
    """Tests for FormatDataFrom.normalize_category method."""

    def test_normalize_category_replaces_key(self):
        """Test that normalize_category replaces key with placeholder."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.normalize_category("{year1} yemen", "yemen")
        assert result == "{year1} {country1}"

    def test_normalize_category_case_insensitive(self):
        """Test that normalize_category is case-insensitive."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.normalize_category("{year1} YEMEN", "yemen")
        assert result == "{year1} {country1}"

    def test_normalize_category_empty_key(self):
        """Test normalize_category with empty key."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.normalize_category("{year1} yemen", "")
        assert result == "{year1} yemen"


class TestFormatDataFromNormalizeCategoryWithKey:
    """Tests for FormatDataFrom.normalize_category_with_key method."""

    def test_normalize_category_with_key_basic(self):
        """Test normalize_category_with_key returns key and normalized category."""

        def match_callback(text):
            return "yemen" if "yemen" in text.lower() else ""

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=match_callback,
        )

        key, result = bot.normalize_category_with_key("{year1} yemen")
        assert key == "yemen"
        assert result == "{year1} {country1}"

    def test_normalize_category_with_key_no_match(self):
        """Test normalize_category_with_key when no key matches."""

        def match_callback(text):
            return ""

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=match_callback,
        )

        key, result = bot.normalize_category_with_key("{year1} yemen")
        assert key == ""
        assert result == ""


class TestFormatDataFromReplaceValuePlaceholder:
    """Tests for FormatDataFrom.replace_value_placeholder method."""

    def test_replace_value_placeholder_basic(self):
        """Test replace_value_placeholder replaces placeholder."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.replace_value_placeholder("{country1} أحداث", "اليمن")
        assert result == "اليمن أحداث"

    def test_replace_value_placeholder_with_fixing_callback(self):
        """Test replace_value_placeholder with fixing_callback."""

        def fix_callback(label):
            return label.replace("أحداث", "فعاليات")

        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
            fixing_callback=fix_callback,
        )

        result = bot.replace_value_placeholder("{country1} أحداث", "اليمن")
        assert result == "اليمن فعاليات"


class TestFormatDataFromGetTemplateAr:
    """Tests for FormatDataFrom.get_template_ar method."""

    def test_get_template_ar_basic(self):
        """Test get_template_ar returns template."""
        bot = FormatDataFrom(
            formatted_data={"{country1} events": "أحداث {country1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.get_template_ar("{country1} events")
        assert result == "أحداث {country1}"

    def test_get_template_ar_case_insensitive(self):
        """Test get_template_ar is case-insensitive."""
        bot = FormatDataFrom(
            formatted_data={"{Country1} Events": "أحداث {country1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.get_template_ar("{country1} events")
        assert result == "أحداث {country1}"

    def test_get_template_ar_with_category_prefix(self):
        """Test get_template_ar with category: prefix."""
        bot = FormatDataFrom(
            formatted_data={"{country1} events": "أحداث {country1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.get_template_ar("category:{country1} events")
        assert result == "أحداث {country1}"

    def test_get_template_ar_no_match(self):
        """Test get_template_ar when no match found."""
        bot = FormatDataFrom(
            formatted_data={"{country1} events": "أحداث {country1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.get_template_ar("{country1} films")
        assert result == ""


class TestFormatDataFromGetKeyLabel:
    """Tests for FormatDataFrom.get_key_label method."""

    def test_get_key_label_basic(self):
        """Test get_key_label uses search callback."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "اليمن" if x == "yemen" else "",
            match_key_callback=lambda x: "",
        )

        result = bot.get_key_label("yemen")
        assert result == "اليمن"

    def test_get_key_label_empty_key(self):
        """Test get_key_label with empty key."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "should not be called",
            match_key_callback=lambda x: "",
        )

        result = bot.get_key_label("")
        assert result == ""


class TestFormatDataFromSearch:
    """Tests for FormatDataFrom.search method."""

    def test_search_uses_callback(self):
        """Test that search uses the provided search_callback."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "نتيجة البحث",
            match_key_callback=lambda x: "",
        )

        result = bot.search("test")
        assert result == "نتيجة البحث"


class TestFormatDataFromSearchAll:
    """Tests for FormatDataFrom.search_all method."""

    def test_search_all_without_prefix(self):
        """Test search_all without add_arabic_category_prefix."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "نتيجة",
            match_key_callback=lambda x: "",
        )

        result = bot.search_all("test")
        assert result == "نتيجة"

    def test_search_all_with_prefix(self):
        """Test search_all with add_arabic_category_prefix=True."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "نتيجة",
            match_key_callback=lambda x: "",
        )

        result = bot.search_all("Category:test", add_arabic_category_prefix=True)
        assert result == "تصنيف:نتيجة"


class TestFormatDataFromPrependArabicCategoryPrefix:
    """Tests for FormatDataFrom.prepend_arabic_category_prefix method."""

    def test_prepend_with_category_prefix(self):
        """Test prepend_arabic_category_prefix with category: prefix."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.prepend_arabic_category_prefix("Category:test", "نتيجة")
        assert result == "تصنيف:نتيجة"

    def test_prepend_without_category_prefix(self):
        """Test prepend_arabic_category_prefix without category: prefix."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.prepend_arabic_category_prefix("test", "نتيجة")
        assert result == "نتيجة"

    def test_prepend_already_has_prefix(self):
        """Test prepend_arabic_category_prefix when result already has prefix."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.prepend_arabic_category_prefix("Category:test", "تصنيف:نتيجة")
        assert result == "تصنيف:نتيجة"

    def test_prepend_empty_result(self):
        """Test prepend_arabic_category_prefix with empty result."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        result = bot.prepend_arabic_category_prefix("Category:test", "")
        assert result == ""
