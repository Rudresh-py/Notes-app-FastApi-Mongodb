
def note_entity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }


def notes_entity(items) -> list:
    return [note_entity(items) for item in items]
