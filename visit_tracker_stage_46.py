# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: VisitTracker
# Версия структуры данных для VisitTracker
CURRENT_VERSION = 1

def migrate_to_version(current_version):
    """
    Выполняет миграции структуры данных до целевой версии.
    Эта функция должна поддерживаться при изменении структуры данных.
    """
    if current_version < CURRENT_VERSION:
        global DATA
        if current_version < 2:
            # Старая версия 1: простая структура данных
            # Перемещаем данные в новую структуру
            if 'visits' in DATA:
                new_visits = []
                for visit in DATA['visits']:
                    new_visits.append({
                        'place': visit['place'],
                        'contact': visit['contact'],
                        'goal': visit.get('goal', ''),
                        'notes': visit.get('notes', ''),
                        'timestamp': visit.get('timestamp', ''),
                    })
                DATA['visits'] = new_visits
                print("Миграция: версия 1 -> 2 завершена")

def load_data():
    """Загружает данные из файла, с учётом текущей версии структуры."""
    global DATA
    DATA = {}
    
    try:
        with open('visit_data.json', 'r') as f:
            raw_data = json.load(f)
            DATA = raw_data
            current_version = DATA.get('version', 1)
            migrate_to_version(current_version)
            print(f"Данные загружены. Текущая версия: {current_version}")
    except FileNotFoundError:
        print("Файл с данными не найден. Начиная с пустой структуры...")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")

def save_data():
    """Сохраняет текущую структуру данных в файл."""
    global DATA
    try:
        with open('visit_data.json', 'w') as f:
            json.dump(DATA, f, indent=2, ensure_ascii=False)
        print("Данные сохранены успешно")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")
