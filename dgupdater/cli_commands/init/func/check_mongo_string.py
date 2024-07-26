from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from click import BadParameter, UsageError

def check_mongo_string(ctx, param, value: str) -> str|None:
    # print(ctx, param.name, value)
    try:
        client = MongoClient(value, serverSelectionTimeoutMS = 3000)
        # print(client)
        client.admin.command('ping')
        # print(client.list_database_names())
        return value
    except ConnectionFailure as e:
        print()
        raise BadParameter("Enter a Valid MongoDB Connection String")
    except Exception as e:
        raise UsageError("Some error occured. Please try again.")
        
    

if __name__ == "__main__":
    print(check_mongo_string(1, 1, 'a'))