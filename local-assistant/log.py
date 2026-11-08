from modules.media_log.collector import collect_media_entry
from modules.media_log.transformer import normalize_media_entry
from modules.media_log.loader import load_media_entry
from data.database import initialize_database
from modules.media_log.schema import MediaItem, StatusChange
from pydantic import ValidationError


def main() -> None:
    initialize_database()
    print("Enter the data: ")
    category = input("Category: ")
    title = input("Title: ")
    status = input("Status: ")
    raw = collect_media_entry(category, title, status)
    clean = normalize_media_entry(raw)
    try:
        MediaItem(**clean)
    except ValidationError as error:
        print(error)
        return
    load_media_entry(clean)
    print("\nData collected successfully.") 

if __name__ == "__main__":
    main()

