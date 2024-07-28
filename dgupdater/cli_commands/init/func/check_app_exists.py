from pymongo import MongoClient
from click import echo, prompt

def check_app_exists(name: str, mongostr: str) -> bool:
    
    try:
        with MongoClient(mongostr) as client:
            db = client['DGUPDATER']
            collections = [collection.lower() for collection in db.list_collection_names()]
    except Exception as _:
        echo("Some error occured. Try again.")

    if name.lower() in collections:
        echo("\nApplication with the same name already exists in Mongodb.\n")

        if prompt("Do you want to overwrite the existing application? (y/n): ").lower() in ["y", "yes" ]:
            return True, True # App exists and overwrite
        return True, False # App exists but don't overwrite (exit)
    
    return False, False # App doesn't exist
    
