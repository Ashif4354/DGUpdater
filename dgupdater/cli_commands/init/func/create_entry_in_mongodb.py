from pymongo import MongoClient
from click import UsageError

def create_entry_in_mongodb(dgupdaterconf_json: dict[str:any], mongodbstrd: str, over_write: bool) -> None:
    try:
        with MongoClient(mongodbstrd) as client:

            db = client['DGUPDATER']
            collection = db[dgupdaterconf_json["app_name"]]

            if over_write:
                collection.delete_one({"_id": dgupdaterconf_json["_id"]})
                

            collection.insert_one(dgupdaterconf_json)
    except Exception as _:
        raise UsageError("Error while creating entry in MongoDB: ")
