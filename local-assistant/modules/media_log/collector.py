from datetime import datetime, timezone

def collect_media_entry(category: str, title: str, status: str):
    """
    Collects media entry data and returns a dictionary containing the information.

    Args:
        category (str): The category of the media entry.
        title (str): The title of the media entry.
        status (str): The status of the media entry.
    """
    media_entry = {
        "category": category,
        "title": title,
        "status": status,
        "timestamp":datetime.now(timezone.utc).isoformat()
        }
    return media_entry
