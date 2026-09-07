# === Stage 43: Добавь пагинацию длинных списков ===
# Project: VisitTracker
def paginate(items, page_size=10, page=1):
    total_pages = (len(items) + page_size - 1) // page_size if items else 1
    start = (page - 1) * page_size
    end = start + page_size
    page_items = items[start:end]
    return {
        "items": page_items,
        "current_page": page,
        "total_pages": total_pages,
        "total_items": len(items),
        "has_prev": page > 1,
        "has_next": page < total_pages,
    }
