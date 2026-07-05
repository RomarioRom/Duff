# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: VisitTracker
def generate_summary(data):
    if not data:
        return "Нет данных для сводки."
    
    total_visits = len(data)
    unique_places = set()
    contacts_count = 0
    goals_total = 0
    
    for visit in data:
        place_name = visit.get("place", {}).get("name") or "Без названия"
        if place_name and place_name not in unique_places:
            unique_places.add(place_name)
        
        contact = visit.get("contact")
        if contact:
            contacts_count += 1
        
        goals_total += len(visit.get("goals", []))
    
    summary_text = f"Сводка по {total_visits} визитам:\n"
    summary_text += f"- Уникальные места: {len(unique_places)}\n"
    summary_text += f"- Контакты сохранено: {contacts_count}\n"
    summary_text += f"- Всего целей поставлено: {goals_total}"
    
    return summary_text
