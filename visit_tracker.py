# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: VisitTracker
import json, uuid, datetime as dt
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Visit:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    location: str = ""
    contact_name: str = ""
    contact_phone: str = ""
    goal: str = ""
    notes: str = ""
    scheduled_at: Optional[dt.datetime] = None
    completed_at: Optional[dt.datetime] = None

class VisitTracker:
    def __init__(self, data_file="visits.json"):
        self.data_file = data_file
        self.visits: list[Visit] = []
        self._load()

    def _load(self) -> None:
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                raw = json.load(f)
                for item in raw.get("visits", []):
                    v = Visit(**item)
                    if v.scheduled_at:
                        v.scheduled_at = dt.datetime.fromisoformat(v.scheduled_at)
                    self.visits.append(v)
        except FileNotFoundError:
            pass

    def save(self) -> None:
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump({"visits": [v.__dict__ for v in self.visits]}, f, ensure_ascii=False, indent=2)

    def add_visit(
        self, location: str, contact_name: str, contact_phone: str, goal: str = "", notes: str = ""
    ) -> Visit:
        visit = Visit(location=location, contact_name=contact_name, contact_phone=contact_phone, goal=goal, notes=notes)
        self.visits.append(visit)
        return visit

tracker = VisitTracker()
demo1 = tracker.add_visit("Москва", "Иван Иванов", "+79001234567", "Обсуждение проекта X")
demo2 = tracker.add_visit("Санкт-Петербург", "Анна Петрова", "+79007654321", "Подписание договора Y", "Заметка: договор принят в 14:00")
tracker.save()
