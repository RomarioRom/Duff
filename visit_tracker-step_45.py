# === Stage 45: Добавь восстановление из резервной копии ===
# Project: VisitTracker
import json, os
from datetime import datetime

def load_backup(path="backup.json"):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "visits" in data:
            return data
        return None
    except (json.JSONDecodeError, IOError):
        return None

def save_backup(data, path="backup.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return True
