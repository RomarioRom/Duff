# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: VisitTracker
def demo():
    """Показывает основной пользовательский сценарий VisitTracker."""
    # Создаём объекты
    place = Place(name="Парк", address="ул. Ленина 1", city="Москва")
    contact = Contact(name="Иван", phone="+7 900 123 45 67", email="ivan@example.com")
    goal = Goal(text="Обсудить новый контракт", priority="high")
    note = Note(text="Встреча прошла успешно, договорились о встрече через неделю")
    visit = Visit(
        place=place,
        contact=contact,
        goal=goal,
        note=note,
        date="2024-12-20",
        duration_minutes=45,
    )

    # Создаём менеджер и добавляем визит
    manager = VisitManager()
    manager.add(visit)

    # Показываем результаты
    print(f"Визит добавлен: {visit.place.name} ({visit.place.address})")
    print(f"Контакт: {contact.name} — {contact.phone}")
    print(f"Цель: {goal.text} (приоритет: {goal.priority})")
    print(f"Продолжительность: {visit.duration_minutes} мин")
    print(f"Примечание: {note.text}")
    print(f"Всего визитов в базе: {len(manager.visits)}")


if __name__ == "__main__":
    demo()
