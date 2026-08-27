# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: VisitTracker
def repair_data(data):
    """Проверяет целостность данных и исправляет простые проблемы.

    Args:
        data (dict): Словарь с данными VisitTracker.

    Returns:
        dict: Исправленный словарь данных.
    """
    repaired = dict(data)

    if "locations" not in repaired:
        repaired["locations"] = []
    if "contacts" not in repaired:
        repaired["contacts"] = []
    if "visits" not in repaired:
        repaired["visits"] = []
    if "notes" not in repaired:
        repaired["notes"] = []

    if not isinstance(repaired["locations"], list):
        repaired["locations"] = []
    if not isinstance(repaired["contacts"], list):
        repaired["contacts"] = []
    if not isinstance(repaired["visits"], list):
        repaired["visits"] = []
    if not isinstance(repaired["notes"], list):
        repaired["notes"] = []

    return repaired
