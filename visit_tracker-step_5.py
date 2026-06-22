# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: VisitTracker
def remove_visit(visit_id: int) -> bool:
    """Удалить запись по ID, обрабатывая случай отсутствия записи."""
    if visit_id not in visits_db:
        print(f"Запись с ID {visit_id} не найдена.")
        return False
    
    del visits_db[visit_id]
    print(f"Запись с ID {visit_id} успешно удалена.")
    return True

def remove_contact(contact_name: str) -> bool:
    """Удалить контакт по имени, обрабатывая случай отсутствия контакта."""
    if contact_name not in contacts_db:
        print(f"Контакт '{contact_name}' не найден.")
        return False
    
    del contacts_db[contact_name]
    print(f"Контакт '{contact_name}' успешно удален.")
    return True

def remove_location(location_name: str) -> bool:
    """Удалить локацию по имени, обрабатывая случай отсутствия локации."""
    if location_name not in locations_db:
        print(f"Локация '{location_name}' не найдена.")
        return False
    
    del locations_db[location_name]
    print(f"Локация '{location_name}' успешно удалена.")
    return True
