# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: VisitTracker
APP_CONFIG = {
    "app_name": "VisitTracker",
    "version": "0.29",
    "default_currency": "RUB",
    "max_visits_per_contact": 10,
    "data_dir": "./visit_data",
    "log_file": "visit_log.txt",
    "notifications_enabled": True,
}


def get_config_value(key: str) -> str:
    return APP_CONFIG.get(key, "")


def set_config_value(key: str, value: str):
    if key in APP_CONFIG:
        APP_CONFIG[key] = value


def print_app_info():
    name = get_config_value("app_name")
    version = get_config_value("version")
    currency = get_config_value("default_currency")
    print(f"\n{APP_CONFIG['app_name']} v{APP_CONFIG['version']}\n")
    print(f"Default Currency: {currency}")
