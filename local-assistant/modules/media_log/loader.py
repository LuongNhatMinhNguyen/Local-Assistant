from data.database import get_db_connection
from modules.media_log.schema import MediaItem, StatusChange


def load_media_entry(entry: dict) -> None:
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO media_logs (category, title, status, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
            entry["category"], 
            entry["title"], 
            entry["status"], 
            entry["timestamp"]))
    conn.close()
    

def save_media_item(item: MediaItem) -> None:
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO media_items (title, category, status, note, url, id, added_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
            item.title,
            item.category,
            item.status,
            item.note,
            item.url,
            item.id,
            item.added_at))
    conn.close()

def save_status_change(change: StatusChange) -> None:
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO status_changes (item_id, status, timestamp)
        VALUES (?, ?, ?)
    """, (
            change.item_id,
            change.status,
            change.timestamp))
    conn.close()
    
