# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: VisitTracker
def revert_last():
    """Откат последнего действия: удаляет последний записанный визит, если он есть."""
    if not visits:
        print("Нет визитов для отката.")
        return None

    last = visits.pop()
    print(f"Визит отменён: {last.get('title', 'Без названия')} ({last['date']})")
    return last
