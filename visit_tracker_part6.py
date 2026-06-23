# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: VisitTracker
def filter_records(status=None, category=None, tags=None):
    filtered = records.copy()
    if status:
        filtered = [r for r in filtered if r.get('status') == status]
    if category:
        filtered = [r for r in filtered if r.get('category') == category]
    if tags:
        filtered = [r for r in filtered if any(tag in r.get('tags', []) for tag in tags)]
    return filtered

def search_records(query):
    results = []
    query_lower = query.lower()
    for record in records:
        text_fields = ['place', 'contact_name', 'notes']
        match_found = False
        for field in text_fields:
            if record.get(field) and query_lower in str(record[field]).lower():
                match_found = True
                break
        if match_found or (query.isdigit() and int(query) == record.get('id')):
            results.append(record)
    return results

def export_to_csv(filename='visits.csv'):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'date', 'place', 'category', 'status', 'tags', 'notes'])
        writer.writeheader()
        for record in records:
            writer.writerow(record)

def export_to_json(filename='visits.json'):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
