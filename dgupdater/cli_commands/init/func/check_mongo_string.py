from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from click import BadParameter

def check_mongo_string(ctx, param, value):
    # print(ctx, param, value)
    try:
        client = MongoClient(value, serverSelectionTimeoutMS = 1000)
        # print(client)
        client.admin.command('ping')
        # print(client.list_database_names())
        return value
    except ConnectionFailure as e:
       raise BadParameter("Enter a Valid MongoDB Connection String")
    

if __name__ == "__main__":
    print(check_mongo_string(1, 1, 'a'))