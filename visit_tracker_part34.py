# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: VisitTracker
TEMPLATE = {
    "name": "Quick Visit",
    "description": "Standard visit template",
    "fields": {
        "place": "Local Coffee Shop",
        "contact": "John Doe",
        "target": "Discuss project progress",
        "notes": "Great meeting, next step is to schedule follow-up.",
    },
}


def load_templates():
    templates = {}
    with open("visit_tracker_templates.json", "r") as f:
        templates = json.load(f)
    return templates


def save_templates(templates):
    with open("visit_tracker_templates.json", "w") as f:
        json.dump(templates, f, indent=2)


def apply_template(visit_id, template_name):
    templates = load_templates()
    if template_name not in templates:
        print(f"Template '{template_name}' not found.")
        return
    template = templates[template_name]
    visit = visits[visit_id]
    for key, value in template["fields"].items():
        if key in visit:
            visit[key] = value
    save_visits()
    print(f"Template '{template_name}' applied to Visit #{visit_id}.")
