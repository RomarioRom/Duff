# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: VisitTracker
def print_metrics(visits):
    if not visits:
        return
    total = len(visits)
    print(f"  Всего визитов: {total}")
    cities = {}
    for v in visits:
        c = v.get("city", "Unknown")
        cities[c] = cities.get(c, 0) + 1
    if cities:
        top3 = sorted(cities.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"  Топ-3 города: {[(c, n) for c, n in top3]}")
    contacts = []
    for v in visits:
        if v.get("contact"):
            contacts.append(v["contact"])
    if contacts:
        unique_contacts = list(set(contacts))
        print(f"  Уникальных контактов: {len(unique_contacts)} / {len(contacts)}")
    goals = [v for v in visits if v.get("goal")]
    if goals:
        goal_list = sorted(set(g["goal"] for g in goals))
        print(f"  Уникальные цели: {goal_list}")
