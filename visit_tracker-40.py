# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: VisitTracker
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="VisitTracker CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    for name, help_text in [
        ("add-place", "Добавить место"),
        ("add-contact", "Добавить контакт"),
        ("add-goal", "Добавить цель"),
        ("add-note", "Добавить заметку"),
        ("add-visit", "Добавить визит"),
        ("list", "Показать все"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--name", required=True, help="Имя")
        p.add_argument("--notes", help="Заметки")
    
    p = sub.add_parser("add-visit", help="Добавить визит")
    p.add_argument("--name", required=True, help="Имя визита")
    p.add_argument("--place", help="ID места")
    p.add_argument("--contact", help="ID контакта")
    p.add_argument("--goal", help="ID цели")
    p.add_argument("--notes", help="Заметки")
    p.add_argument("--date", help="Дата (YYYY-MM-DD)")
    
    p = sub.add_parser("list", help="Показать все сущности")
    p.add_argument("--type", help="Тип: place|contact|goal|visit|note")
    
    p = sub.add_parser("show", help="Показать детали по ID")
    p.add_argument("--id", required=True, help="ID сущности")
    p.add_argument("--type", required=True, help="Тип: place|contact|goal|visit|note")
    
    return parser.parse_args()
