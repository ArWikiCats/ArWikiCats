"""
Time-related utility functions for the ArWikiCats project.
This module provides functions for post-processing and standardizing
Arabic time expressions in category labels.
"""

import re


def standardize_time_phrases(text: str) -> str:
    """Fix text."""
    text = re.sub(r"(انحلالات|تأسيسات)\s*سنة\s*(عقد|القرن|الألفية)", r"\g<1> \g<2>", text)
    text = text.replace("بعقد عقد", "بعقد")
    text = text.replace("بعقد القرن", "بالقرن")
    return text
