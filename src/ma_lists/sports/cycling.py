
new2019_cycling = {
    "tour de france": "سباق طواف فرنسا",
    "grand tour": "الطوافات الكبرى",
    "grand tour (cycling)": "الطوافات الكبرى",
    "vuelta a españa": "طواف إسبانيا",
    "giro d'italia": "طواف إيطاليا",
    "presidential cycling tour of turkey": "طواف تركيا",
    "tour de suisse": "طواف سويسرا",
    "vuelta a colombia": "طواف كولومبيا",
    "vuelta a venezuela": "فويلتا فنزويلا",
}

new_cy = {}

for cy, cy_lab in new2019_cycling.items():
    cy2 = cy.lower()
    new_cy[cy2] = cy_lab
    new_cy[f"{cy2} media"] = f"إعلام {cy_lab}"
    new_cy[f"{cy2} squads"] = f"تشكيلات {cy_lab}"
    new_cy[f"{cy2} cyclists"] = f"دراجو {cy_lab}"
    new_cy[f"{cy2} directors"] = f"مدراء {cy_lab}"
    new_cy[f"{cy2} journalists"] = f"صحفيو {cy_lab}"
    new_cy[f"{cy2} people"] = f"أعلام {cy_lab}"
    new_cy[f"{cy2} stages"] = f"مراحل {cy_lab}"
    new_cy[f"{cy2} stage winners"] = f"فائزون في مراحل {cy_lab}"
# ---
