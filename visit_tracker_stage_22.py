# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: VisitTracker
def check_overdue_reminders(visits, today=None):
    if today is None:
        import datetime
        today = datetime.date.today()
    overdue = []
    for v in visits:
        if 'next_visit' in v and isinstance(v['next_visit'], datetime.datetime):
            if v['next_visit'].date() < today:
                overdue.append({
                    'visit': v,
                    'days_overdue': (today - v['next_visit'].date()).days
                })
    return overdue
