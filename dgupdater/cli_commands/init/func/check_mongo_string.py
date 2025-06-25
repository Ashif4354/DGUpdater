from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from click import BadParameter, UsageError, echo

def check_mongo_string(ctx, param, value: str) -> str|None:

    # start: detecting second execution of callback of click.options
    if value.endswith('*VERIFIEDONCE*'):
        return value[:-14]    
    # end: detecting second execution of callback of click.options

    echo('Verifying MongoDB Connection String...')

    if not value.startswith('mongodb'):
        raise BadParameter("Enter a Valid MongoDB Connection String")

    try:
        client = MongoClient(value, serverSelectionTimeoutMS = 3000)
        client.admin.command('ping')
        
        echo("Verified !!\n")
        return value + '*VERIFIEDONCE*'  # *VERIFIEDONCE* is added to the end of the string to detect second execution of callback of click.options()
    except ConnectionFailure as _:
        echo()
        raise BadParameter("Enter a Valid MongoDB Connection String")
    except Exception as e:
        raise UsageError("Some error occurred. Try again." + str(e))
