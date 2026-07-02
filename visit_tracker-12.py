# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: VisitTracker
import json, os, sys

def load_visits_from_file(file_path: str) -> list[dict]:
    if not file_path or not isinstance(file_path, str):
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("Ошибка: Файл должен содержать массив объектов.")
                sys.exit(1)
            return data
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Загрузка из памяти...")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        sys.exit(1)
    except PermissionError:
        print(f"Нет прав для чтения файла '{file_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {type(e).__name__}: {e}")
        return []
