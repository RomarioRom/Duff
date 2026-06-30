# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: VisitTracker
import json, os

DATA_FILE = "visits.json"

def save_visits(visits):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(visits, f, ensure_ascii=False, indent=2)

def load_visits():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
