# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: VisitTracker
def monthly_stats(visits):
    """Return a dictionary of month -> {total, avg_duration_min, avg_rating, places}.
    
    Args:
        visits (list[dict]): each dict has keys 'date' (YYYY-MM-DD), 
                              'duration_min', 'rating'.
    
    Returns:
        dict: keys are YYYY-MM strings; values contain aggregated stats.
    """
    from collections import defaultdict
    
    grouped = defaultdict(lambda: {'total': 0, 'durations': [], 'ratings': [], 'places': []})
    
    for v in visits:
        month_key = v['date'][:7]  # YYYY-MM
        g = grouped[month_key]
        g['total'] += 1
        g['durations'].append(v.get('duration_min', 0))
        if 'rating' in v and v['rating'] is not None:
            g['ratings'].append(v['rating'])
        g['places'].append(v.get('place', ''))
    
    result = {}
    for month, data in grouped.items():
        avg_dur = sum(data['durations']) / len(data['durations']) if data['durations'] else 0
        avg_rate = sum(data['ratings']) / len(data['ratings']) if data['ratings'] else 0
        unique_places = list(set(data['places']))
        result[month] = {
            'total': data['total'],
            'avg_duration_min': round(avg_dur, 1),
            'avg_rating': round(avg_rate, 2) if avg_rate > 0 else None,
            'unique_places_count': len(unique_places)
        }
    
    return result

# Пример использования:
# stats = monthly_stats(visits_list)
# print(stats)
