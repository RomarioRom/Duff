# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: VisitTracker
def reset_demo_data():
    """Replace current contacts, venues, visits with demo data and clear notes."""
    global contacts, venues, visits, notes
    
    contacts = [
        {"name": "Иван Иванов", "phone": "+7 (900) 111-22-33", "email": "ivan@example.com"},
        {"name": "Мария Петрова", "phone": "+7 (900) 444-55-66", "email": "maria@example.com"},
    ]
    
    venues = [
        {"name": "Кофейня 'Угловая'", "address": "ул. Ленина, 15", "type": "coffee"},
        {"name": "Офис компании X", "address": "пр. Мира, 42", "type": "office"},
    ]
    
    visits = [
        {"venue_id": 0, "contact_id": 0, "date": "2026-01-15", "goal": "Обсудить проект", "note": "Все прошло отлично"},
        {"venue_id": 1, "contact_id": 1, "date": "2026-02-20", "goal": "Представить новый продукт", "note": ""},
    ]
    
    notes = {
        "summary": "В январе прошел первый визит в кофейню, в феврале — встреча с Марией.",
        "total_visits": 2,
        "last_update": "2026-03-15",
    }
