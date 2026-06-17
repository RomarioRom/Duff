# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: VisitTracker
class Visit:
    def __init__(self, place_name: str, contact_phone: str, goal: str, notes: str):
        self.place_name = place_name.strip()
        self.contact_phone = contact_phone.strip()
        self.goal = goal.strip()
        self.notes = notes.strip()

    @property
    def is_valid(self) -> bool:
        return (self.place_name and len(self.place_name) <= 100 and
                self.contact_phone.isdigit() and len(self.contact_phone) >= 7 and
                self.goal and len(self.goal) <= 256 and
                self.notes and len(self.notes) <= 512)

    def to_dict(self):
        return {
            "place_name": self.place_name,
            "contact_phone": self.contact_phone,
            "goal": self.goal,
            "notes": self.notes
        }
