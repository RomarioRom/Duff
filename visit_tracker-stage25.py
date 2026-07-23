# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: VisitTracker
def parse_date(date_str):
    """Parse a date string in various formats and return a datetime.date object."""
    import datetime
    formats = [
        "%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m-%d-%Y", "%m/%d/%Y",
        "%d %B %Y", "%d %b %Y", "%B %d, %Y", "%b %d, %Y",
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать дату '{date_str}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY.")
