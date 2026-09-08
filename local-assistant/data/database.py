import duckdb

DB_File = "data/assistant.db"

def get_db_connection():
    return duckdb.connect(DB_File)

def initialize_database():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS media_logs (
            category TEXT,
            title TEXT,
            progress TEXT,
            timestamp TIMESTAMP
        )
    """)
    conn.close()
    print("Database initialized and media_logs table created if it didn't exist.")