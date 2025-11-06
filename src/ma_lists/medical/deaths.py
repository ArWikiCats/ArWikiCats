"""
"""
# ---
from ...helps import len_print

deaths_by = {
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
medical_keys = {}
# ---
for cause_key, cause_label in deaths_by.items():
    medical_keys[cause_key] = cause_label
    medical_keys[f"deaths from {cause_key}"] = f"وفيات {cause_label}"
# ---
length_stats = {"medical_keys": len(medical_keys.keys())}
# ---
len_print.lenth_pri("deaths.py", length_stats)
