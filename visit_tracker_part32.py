# === Stage 32: Добавь журнал действий пользователя ===
# Project: VisitTracker
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type, details, user=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": action_type,
            "details": details,
            "user": user or "system",
        }
        self.entries.append(entry)

    def get_recent(self, count=10):
        return self.entries[-count:]


log = ActionLog()
