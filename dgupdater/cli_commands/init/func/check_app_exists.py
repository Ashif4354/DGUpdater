from pymongo import MongoClient
from click import echo

def check_app_exists(name, mongostr):
    
    try:
        with MongoClient(mongostr) as client:
            dbs = [db.lower() for db in client.list_database_names()]

            if name.lower() in dbs:
                return True
            return False
        
    except Exception as e:
        echo("Some error occured. Please try again.")
