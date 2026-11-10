def normalize_media_entry(entry: dict) -> dict:
    """
    Normalizes the media entry data by cleaning and formatting the fields.
    """
    cleaned = {
        "category": entry["category"].lower().strip(),
        "title": entry["title"].strip(),
        "status": entry["status"].strip().lower(),
        "timestamp": entry["timestamp"]
    }
    return cleaned
