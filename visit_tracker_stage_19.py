# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: VisitTracker
def archive_visit(visit, cutoff_days=30):
    """Archive completed or old visits older than cutoff_days."""
    if visit.get("status") == "completed":
        return True
    if visit["date"] and (datetime.now() - datetime.fromisoformat(visit["date"]).replace(tzinfo=datetime.now().astimezone())) > timedelta(days=cutoff_days):
        return True
    return False

def archive_old_visits(visits, cutoff_days=30):
    """Return a list of visit IDs that should be archived."""
    return [vid for vid, v in visits.items() if archive_visit(v, cutoff_days)]

visits_to_archive = archive_old_visits(visits)
for vid in visits_to_archive:
    visits[vid]["status"] = "archived"
