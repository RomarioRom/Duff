# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: VisitTracker
def search_visits(query: str) -> list[dict]:
    if not query.strip():
        return []
    q = query.lower()
    results = []
    for visit in visits_data:
        fields_to_check = [
            visit.get("place", ""),
            visit.get("contact_name", ""),
            visit.get("company", ""),
            visit.get("notes", "")
        ]
        if any(q in field.lower() for field in fields_to_check):
            results.append(visit)
    return results
