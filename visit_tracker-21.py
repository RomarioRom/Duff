# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: VisitTracker
class Reminder:
    def __init__(self, title, date, notes=""):
        self.title = title
        self.date = date  # datetime object
        self.notes = notes
        self.is_done = False

    @staticmethod
    def from_input():
        print("=== Напоминание ===")
        t = input("Заголовок: ").strip()
        while True:
            d_str = input("Дата (YYYY-MM-DD): ").strip()
            if not d_str: break
            try:
                from datetime import datetime
                date = datetime.strptime(d_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")
        n = input("Заметки (нажмите Enter если нет): ").strip()
        return Reminder(t, date, n)

    def save(self, filename="reminders.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{self.date.strftime('%Y-%m-%d')}] {self.title}\n")
            if self.notes:
                f.write(f"  Заметки: {self.notes}\n")

    def load(filename="reminders.txt"):
        reminders = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("["):
                    continue
                if line.startswith("Заметки:"):
                    continue
                parts = line.split("\n")[0]  # title line
                reminders.append(parts)
        return reminders

    def check_upcoming(start_date=None):
        today = datetime.now().date() if start_date is None else start_date
        upcoming = []
        with open("reminders.txt", "r", encoding="utf-8") as f:
            content = f.read()
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("["):
                date_part, title = line.split("]", 1)
                date_str = date_part[1:].strip()
                try:
                    d = datetime.strptime(date_str, "%Y-%m-%d").date()
                    if d >= today and not d.isoweekday():  # skip weekends
                        upcoming.append((d, title))
                except ValueError:
                    pass
        return sorted(upcoming)

    def mark_done(title):
        with open("reminders.txt", "r+", encoding="utf-8") as f:
            content = f.read()
            new_content = content.replace(f"{title}\n", f"[{title} ✅]\n")
            if new_content == content:
                return False
            f.seek(0)
            f.truncate()
            f.write(new_content)
        return True
