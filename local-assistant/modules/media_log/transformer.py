def normalize_media_entry(entry: dict):
    """
    Normalizes the media entry data by cleaning and formatting the fields.
    """
    cleaned = {
        "category": entry["category"].lower().strip(),
        "title": entry["title"].strip(),
        "progress": entry["progress"].strip(),
        "timestamp": entry["timestamp"]
    }
    return cleaned
