import duckdb

DB_FILE = 'assistant.db'
def get_db_connection():
    return duckdb.connect(DB_FILE)

def initialize_database():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS media_log (
            id INTEGER PRIMARY KEY,
            category TEXT,
            title TEXT,
            progress TEXT,
            logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.close()
    print(" DuckDB initialized: 'media_log' table is ready!")