from datetime import datetime

def collect_media_entry(category: str, title: str, progress: str):
    """
    Collects media entry data and returns a dictionary containing the information.

    Args:
        category (str): The category of the media entry.
        title (str): The title of the media entry.
        progress (str): The progress status of the media entry.
    """
    media_entry = {
        "category": category,
        "title": title,
        "progress": progress,
        "timestamp": datetime.now()
        }
    return media_entry