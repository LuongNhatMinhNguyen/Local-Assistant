import pandas as pd

from data.database import get_db_connection


def load_media_items() -> pd.DataFrame:
    conn = get_db_connection()
    df = conn.execute("""
        SELECT title, category, status, note, url, id, added_at
        FROM media_items
    """).df()
    conn.close()
    return df


def count_by_status(df: pd.DataFrame) -> pd.DataFrame:
    return df["status"].value_counts().reset_index(name="count")
   

def count_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df["category"].value_counts().reset_index(name="count")


if __name__ == "__main__":
    df = load_media_items()
    print(count_by_category(df))
    print(count_by_status(df))