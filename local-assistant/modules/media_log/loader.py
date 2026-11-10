from data.database import get_db_connection


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
