# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: VisitTracker
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Tag {self.name!r}>"


def tag_add(tags, new_tag):
    if not isinstance(new_tag, str):
        raise TypeError("tag_add expects a string")
    for t in tags:
        if isinstance(t, Tag) and t.name == new_tag:
            return tags
    tags.append(Tag(new_tag))
    return tags


def tag_remove(tags, name_to_delete):
    if not isinstance(name_to_delete, str):
        raise TypeError("tag_remove expects a string")
    result = []
    for t in tags:
        if isinstance(t, Tag) and t.name == name_to_delete:
            continue
        result.append(t)
    return result


def tag_contains(tags, name):
    return any(isinstance(t, Tag) and t.name == name for t in tags)
