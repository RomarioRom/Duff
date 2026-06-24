# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: VisitTracker
def sort_visits(visits, key='date'):
    reverse = False
    if key == 'priority':
        visits.sort(key=lambda x: x['priority'], reverse=True)
        return visits
    elif key == 'name':
        visits.sort(key=lambda x: x['name'].lower())
        return visits
    else:  # date
        visits.sort(key=lambda x: x.get('date', ''), reverse=False)
        return visits
