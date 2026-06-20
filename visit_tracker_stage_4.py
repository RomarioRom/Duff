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
