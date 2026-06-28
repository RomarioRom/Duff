# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: VisitTracker
import json, sys, os

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        return {
            "places": data.get("places", []),
            "contacts": data.get("contacts", []),
            "goals": data.get("goals", []),
            "notes": data.get("notes", [])
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        return {"places": [], "contacts": [], "goals": [], "notes": []}

def save_data_to_file(data: dict, filename: str = "data.json") -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except IOError as e:
        print(f"Ошибка записи файла: {e}", file=sys.stderr)

if __name__ == "__main__":
    sample_json = '''{
      "places": [{"id": 1, "name": "Офис", "address": "ул. Пушкина, 10"}],
      "contacts": [{"id": 1, "name": "Иван Иванов", "phone": "+79990000000"}],
      "goals": [{"id": 1, "text": "Обсудить проект"}],
      "notes": []
    }'''
    
    initial_data = load_initial_data(sample_json)
    save_data_to_file(initial_data)
