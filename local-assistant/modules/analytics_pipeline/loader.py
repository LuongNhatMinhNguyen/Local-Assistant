from data.database import get_db_connection


def load_media_entry(entry: dict):
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO media_logs (category, title, progress, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
            entry["category"], 
            entry["title"], 
            entry["progress"], 
            entry["timestamp"]))
    conn.close()
