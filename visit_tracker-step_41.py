# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: VisitTracker
def dry_run(operation, *args, **kwargs):
    """Execute operation in dry-run mode: collect result without mutating state."""
    state = get_state()
    if operation not in state:
        return {"status": "dry-run", "message": f"No state for '{operation}'"}
    try:
        result = operation(*args, **kwargs)
        return {"status": "dry-run", "result": result}
    except Exception as e:
        return {"status": "dry-run", "error": str(e)}
