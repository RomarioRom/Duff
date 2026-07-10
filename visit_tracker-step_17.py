# === Stage 17: Добавь группировку записей по категориям ===
# Project: VisitTracker
def group_visits_by_category(visits):
    groups = {}
    for v in visits:
        cat = v.get('category', 'other')
        if cat not in groups:
            groups[cat] = {'title': cat, 'visits': []}
        groups[cat]['visits'].append(v)
    return list(groups.values())
