import pytest

from ArWikiCats.make_bots.o_bots.ethnic_bot import ethnic_culture, ethnic_label

# -------------------------------------------------
# Sample comparisons for ethnic_label()  (people → شعوب)
# -------------------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,start,suffix,expected_ar",
    [
        # English: "Zanzibari people" + "Yemeni"
        # Arabic:  "زنجباريون يمنيون"
        (
            "Category:Zanzibari people of Yemeni origin",
            "yemeni",
            "zanzibari people",
            "زنجباريون يمنيون",
        ),
        # English: "Afghan people" + "Yemeni"
        # Arabic:  "أفغان يمنيون"
        (
            "Category:Afghan people of Yemeni origin",
            "yemeni",
            "afghan people",
            "أفغان يمنيون",
        ),
        # English: "Yemeni people" + "Afghan"
        # Arabic:  "يمنيون أفغان"
        (
            "Category:Yemeni people of Afghan origin",
            "afghan",
            "yemeni people",
            "يمنيون أفغان",
        ),
    ],
)
def test_ethnic_direct_mens_examples(category, start, suffix, expected_ar) -> None:
    """Check a few realistic <nat> people categories."""
    result = ethnic_label(category, start, suffix)
    assert result == expected_ar


@pytest.mark.unit
def test_ethnic_fallback_to_ethnic_culture() -> None:
    """
    Example where ethnic_label() cannot build mens-composition and falls back
    to ethnic_culture().
    """
    category = "Category:Afghan history"
    start = "afghan"
    suffix = "afghan history"

    result = ethnic_label(category, start, suffix)

    # Nat_men["afghan"] == "أفغاني"
    # MALE_TOPIC_TABLE["history"] == "تاريخ {}"
    # inner string: "أفغاني أفغاني"
    expected = "تاريخ أفغاني أفغاني"
    assert result == expected


@pytest.mark.unit
def test_ethnic_unknown_returns_empty() -> None:
    """Unknown nationalities should return empty string."""
    result = ethnic_label("Category:Unknown people", "unknown-nat", "unknown-nat people")
    assert result == ""


# -------------------------------------------------
# Sample comparisons for ethnic_culture()
# -------------------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,start,suffix,expected_ar",
    [
        # MALE path
        # English: "Afghan history"
        # Arabic (by current algorithm): "تاريخ أفغاني أفغاني"
        (
            "Category:Afghan history",
            "afghan",
            "afghan history",
            "تاريخ أفغاني أفغاني",
        ),
        # English: "Prussian literature"
        # Arabic (by current algorithm): "أدب بروسي بروسي"
        (
            "Category:Prussian literature",
            "prussian",
            "prussian literature",
            "أدب بروسي بروسي",
        ),
    ],
)
def test_ethnic_culture_male_examples(category, start, suffix, expected_ar) -> None:
    """Check a few culture-like categories for male topics."""
    result = ethnic_culture(category, start, suffix)
    assert result == expected_ar


ethnic_culture_female_examples = [
    # FEMALE path using en_is_nat_ar_is_women_2["music"] == "موسيقى {}"
    # Nat_women["zanzibari-american"] == "أمريكية زنجبارية"
    # inner string: "أمريكية زنجبارية أمريكية زنجبارية"
    (
        "Category:Zanzibari-American music",
        "zanzibari-american",
        "zanzibari-american music",
        "موسيقى أمريكية زنجبارية أمريكية زنجبارية",
    ),
    # FEMALE path using en_is_nat_ar_is_women_2["movies"] == "أفلام {}"
    # Nat_women["afghan-american"] == "أمريكية أفغانية"
    # inner string: "أمريكية أفغانية أمريكية أفغانية"
    (
        "Category:Afghan-American movies",
        "afghan-american",
        "afghan-american movies",
        "أفلام أمريكية أفغانية أمريكية أفغانية",
    ),
]


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,start,suffix,expected_ar",
    ethnic_culture_female_examples,
    ids=[x[0] for x in ethnic_culture_female_examples],
)
def test_ethnic_culture_female_examples(category, start, suffix, expected_ar) -> None:
    """Check a few culture-like categories for female topics."""
    result = ethnic_culture(category, start, suffix)
    assert result == expected_ar


@pytest.mark.unit
def test_ethnic_culture_unknown_nationality() -> None:
    """If nationality not in Nat_men or Nat_women, result must be empty."""
    result = ethnic_culture(
        "Category:Unknown culture",
        "unknown-nat",
        "unknown-nat culture",
    )
    assert result == ""
