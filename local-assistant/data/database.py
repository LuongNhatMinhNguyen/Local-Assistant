import duckdb

DB_FILE = "data/assistant.db"

def get_db_connection() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(DB_FILE)
    conn.execute( "SET TimeZone = 'UTC'")
    return conn

def initialize_database() -> None:
    conn = get_db_connection()
    # Legacy table for testing
    conn.execute("""
        CREATE TABLE IF NOT EXISTS media_logs (     
            category TEXT,
            title TEXT,
            status TEXT,
            timestamp TIMESTAMP
        )
    """)
    # Data entries go here
    conn.execute( """
        CREATE TABLE IF NOT EXISTS media_items(
            id UUID PRIMARY KEY,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL,
            note TEXT,
            url TEXT,
            added_at TIMESTAMP NOT NULL
         )
    """ )
    # Table for status change
    conn.execute("""
        CREATE TABLE IF NOT EXISTS status_changes(
            item_id UUID NOT NULL REFERENCES media_items(id),
            status TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL
        )
    """)

    conn.close()
    print("Database initialized and table created if it didn't exist.")