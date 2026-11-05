from modules.analytics_pipeline.collector import collect_media_entry
from modules.analytics_pipeline.transformer import normalize_media_entry
from modules.analytics_pipeline.loader import load_media_entry
from data.database import initialize_database, initialize_database 


def main():
    initialize_database()
    print("Enter the data: ")
    category = input("Category: ")
    title = input("Title: ")
    progress = input("Progress: ")
    raw = collect_media_entry(category, title, progress)
    clean = normalize_media_entry(raw)
    load_media_entry(clean)
    print("\nData collected successfully.") 

if __name__ == "__main__":
    main()

