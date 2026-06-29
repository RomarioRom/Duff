# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: VisitTracker
def export_to_json():
    import json
    data = {
        "visits": visits,
        "contacts": contacts,
        "goals": goals,
        "notes": notes
    }
    return json.dumps(data, indent=2)
