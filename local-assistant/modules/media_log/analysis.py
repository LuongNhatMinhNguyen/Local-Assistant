import pandas as pd

from data.database import get_db_connection


def load_media_items() -> pd.DataFrame:
    conn = get_db_connection()
    df = conn.execute("""
        SELECT title,category,status,note,url,id,added_at
        FROM media_items
    """).df()
    conn.close()
    return df


if __name__ == "__main__":
    print(load_media_items())
