# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: VisitTracker
def edit_visit(visit_id: int, updates: dict) -> Visit | None:
    """Редактирует запись по ID, возвращая обновлённую или None если не найдена."""
    for visit in visits:
        if visit.id == visit_id:
            update_fields = {k: v for k, v in updates.items() if k in visit.__dict__}
            if not update_fields:
                print("Не указаны поля для редактирования.")
                return None
            visit.update(**update_fields)
            save_visits()
            print(f"Запись #{visit_id} обновлена успешно.")
            return visit
    print(f"Запись с ID {visit_id} не найдена.")
    return None

# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: VisitTracker
def edit_visit(visit_id: int, updates: dict) -> bool:
    if not isinstance(updates, dict):
        raise ValueError("Обновления должны быть словарем")
    for key in ["place", "contact", "goal", "notes"]:
        if key in updates and updates[key] is None:
            del updates[key]
    try:
        index = next((i for i, v in enumerate(visits) if v["id"] == visit_id), -1)
        if index < 0:
            return False
        visits[index].update(updates)
        return True
    except Exception as e:
        print(f"Ошибка при редактировании визита {visit_id}: {e}")
        return False
