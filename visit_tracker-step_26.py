# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: VisitTracker
def demo_commands():
    """Демо-команды для ручного тестирования VisitTracker."""
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    from models import Place, Contact, Goal, Note
    from app import App
    app = App()
    
    # Демо места
    places_demo = [
        ("Парк Горького", "Москва"),
        ("Ленинградский проспект, 10", "Спб"),
        ("ТЦ Авиапарк", "Москва"),
    ]
    for name, city in places_demo:
        app.add_place(Place(name=name, address=city))
    
    # Демо контакты
    contacts_demo = [
        ("Иванов Иван", "+7-903-123-4567"),
        ("Петров Петр", "+7-911-876-5432"),
    ]
    for name, phone in contacts_demo:
        app.add_contact(Contact(name=name, phone=phone))
    
    # Демо цель
    goal = Goal(title="Обновить парк Горького", description="Улучшить инфраструктуру")
    app.add_goal(goal)
    
    # Демо заметка
    note = Note(text="Первый визит в новый парк", date="2024-01-15")
    app.add_note(note)
    
    print("Демо-данные добавлены. Запустите app.run() для просмотра.")

if __name__ == "__main__":
    demo_commands()
