# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: VisitTracker
def weekly_stats(visits):
    """Рассчитывает статистику по дням недели для списка визитов."""
    if not visits:
        return {}
    
    day_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    stats = {day: [] for day in day_names}
    
    for visit in visits:
        date_str = visit.get('date') or visit.get('visit_date')
        if not date_str:
            continue
        
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            day_name = day_names[dt.weekday()]
            stats[day_name].append({
                'date': date_str,
                'location': visit.get('location'),
                'contact': visit.get('contact'),
                'goal': visit.get('goal'),
                'notes': visit.get('summary') or visit.get('notes')
            })
        except (ValueError, TypeError):
            continue
    
    return stats

if __name__ == '__main__':
    sample_visits = [
        {'visit_date': '2024-01-15', 'location': 'Офис', 'contact': 'Иван', 'goal': 'Обсудить проект', 'summary': 'Встреча прошла успешно'},
        {'visit_date': '2024-01-16', 'location': 'Кафе', 'contact': 'Мария', 'goal': 'Кофе и идеи', 'summary': 'Дискуссия о новых функциях'},
        {'visit_date': '2024-01-17', 'location': 'Офис', 'contact': 'Иван', 'goal': 'Презентация', 'summary': 'Показали результаты'},
    ]
    
    print("Недельная статистика:")
    stats = weekly_stats(sample_visits)
    for day, visits_list in stats.items():
        if visits_list:
            print(f"\n{day}:")
            for v in visits_list:
                print(f"  Дата: {v['date']}, Место: {v['location']}, Контакт: {v['contact']}")
