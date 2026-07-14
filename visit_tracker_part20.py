# === Stage 20: Добавь восстановление записей из архива ===
# Project: VisitTracker
def load_from_archive(archive_path):
    """Восстанавливает записи из текстового архива."""
    if not os.path.exists(archive_path):
        return []
    with open(archive_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    records = {}
    for line in raw.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line == '---':
            continue
        parts = line.split('|||')
        if len(parts) != 4:
            continue
        date, location, contact, note = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
        records[date] = {'location': location, 'contact': contact, 'note': note}
    return records
