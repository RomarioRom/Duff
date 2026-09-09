# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: VisitTracker
def backup_data_file(file_path, backup_dir="backups"):
    """Создаёт резервную копию файла данных в директории backups."""
    import shutil, os, datetime
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(file_path)}")
    shutil.copy2(file_path, new_path)
    print(f"Backup saved to {new_path}")
