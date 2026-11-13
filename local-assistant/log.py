from modules.media_log.collector import collect_media_entry
from modules.media_log.transformer import normalize_media_entry
from modules.media_log.loader import find_media_item, update_media_item_status, save_media_item, save_status_change
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
        item = MediaItem(**clean)
    except ValidationError as error:
        print(error)
        return
    
    found = find_media_item(item.title, item.category)

    if found is None:
        save_media_item(item)
        save_status_change(StatusChange(item_id=item.id, status=item.status))

    else:
        update_media_item_status(found, item.status)
        save_status_change(StatusChange(item_id=found, status=item.status))

    print("\nData collected successfully.") 

if __name__ == "__main__":
    main()

