from data.database import get_db_connection
from modules.media_log.schema import MediaItem, StatusChange
from uuid import UUID, uuid4

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

def find_media_item(title: str, category: str) -> UUID | None:
    conn = get_db_connection()
    row = conn.execute("""
        SELECT id FROM media_items
        WHERE lower(title) = lower(?) AND category = ?
    """,[title, category]).fetchone()
    conn.close()
    if row is None:
        return None
    return row[0]

def update_media_item_status(item_id: UUID, status: str) -> None:
    conn = get_db_connection()
    conn.execute("""
        UPDATE media_items SET status = ? WHERE id = ?
    """,[status, item_id] 
    )
    conn.close()

    
