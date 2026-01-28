""" """

from ..helps import len_print

deaths_from = {
    "lung cancer": "سرطان الرئة",
    "brain cancer": "سرطان الدماغ",
    "cancer": "السرطان",
    "amyloidosis": "داء نشواني",
    "mastocytosis": "كثرة الخلايا البدينة",
    "autoimmune disease": "أمراض المناعة الذاتية",
    "blood disease": "أمراض الدم",
    "cardiovascular disease": "أمراض قلبية وعائية",
    "digestive disease": "أمراض الجهاز الهضمي",
    "infectious disease": "أمراض معدية",
    "musculoskeletal disorders": "إصابة الإجهاد المتكرر",
    "neurological disease": "أمراض عصبية",
    "organ failure": "فشل عضوي",
    "respiratory disease": "أمراض الجهاز التنفسي",
    "skin disease": "مرض جلدي",
    "urologic disease": "أمراض الجهاز البولي",
    "endocrine disease": "أمراض الغدد الصماء",
    "genetic disorders": "اضطرابات وراثية",
    "reproductive system disease": "أمراض الجهاز التناسلي",
}
# ---
deaths_by = {
    "by airstrike": "بضربات جوية",
    "by airstrikes": "بضربات جوية",
    "by firearm": "بسلاح ناري",
}
# ---
medical_keys = {}
# ---
for cause_key, cause_label in deaths_from.items():
    medical_keys[cause_key] = cause_label
    medical_keys[f"deaths from {cause_key}"] = f"وفيات {cause_label}"

for by_key, by_label in deaths_by.items():
    medical_keys[f"deaths {by_key}"] = f"وفيات {by_label}"


def get_death_label(text: str) -> str:
    """Get the Arabic label for a death-related category text.

    Args:
        text: The category text to look up (e.g., "lung cancer", "deaths from cancer").

    Returns:
        The Arabic translation if found, otherwise None.
    """
    result = medical_keys.get(text)
    return result


len_print.data_len("deaths.py", {"medical_keys": medical_keys})
