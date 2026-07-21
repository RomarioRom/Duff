# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: VisitTracker
def print_visit_summary(visit):
    print(f"{'─' * 50}")
    print(f"📍 {visit.get('place', 'Место')}")
    print(f"   Дата:        {visit.get('date')}")
    print(f"   Контакт:     {visit.get('contact_name', '—')} ({visit.get('contact_phone', '')})")
    print(f"   Цель:        {visit.get('goal', '—')}")
    print(f"   Итог/заметка: {visit.get('note', '—') or 'Нет'}")
