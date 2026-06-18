# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: VisitTracker
class VisitTracker:
    def __init__(self):
        self.records = []

    def add_visit(self, location: str, contact: str, goal: str, notes: str) -> dict:
        record = {
            "id": len(self.records) + 1,
            "location": location,
            "contact": contact,
            "goal": goal,
            "notes": notes,
            "timestamp": self._get_timestamp()
        }
        self.records.append(record)
        return record

    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()
