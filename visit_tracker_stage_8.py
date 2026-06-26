# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: VisitTracker
def show_menu():
    print("\n=== VisitTracker Menu ===")
    print("1. Add new visit")
    print("2. List all visits")
    print("3. Search visits by location or date")
    print("4. Export to text file")
    print("5. Exit")
    try:
        choice = input("Select option (1-5): ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        return None
