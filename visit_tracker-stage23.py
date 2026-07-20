# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: VisitTracker
def print_table(headers, rows):
    """Выводит таблицу с колонками headers из списка строк."""
    if not rows:
        return
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    sep = "─" * (sum(col_widths) + len(headers) - 1)
    print(sep)
    print("│" + "│".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers)) + "│")
    print(sep)
    for row in rows:
        line = "│" + "│".join(str(row[i]).ljust(col_widths[i]) if i < len(row) else "" for i in range(len(headers))) + "│"
        print(line)
    print(sep)
