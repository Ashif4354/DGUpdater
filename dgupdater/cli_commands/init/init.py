from click import command, echo, option

from .func.check_mongo_string import check_mongo_string
from .func.check_app_exists import check_app_exists
from .func.create_entry_in_mongodb import create_entry_in_mongodb
from .func.create_configuration_files import create_configuration_files

parameters = {
    'name': {
        'prompt': "Name of the Application",
        'help': "The name of the Application. It should be unique for every app "
    },
    'version': {
        'prompt': "Version of the Application",
        'help': "The version of the Application."
    },
    'mongodb_connection_string_write': {
        'prompt': "MongoDB Connection String with write access",
        'help': "The MongoDB Connection String for a cloud cluster, to be used by the developer for releasing update."
    },
    'mongodb_connection_string_read': {
        'prompt': "MongoDB Connection String with read access",
        'help': "The MongoDB Connection String for a cloud cluster, to be used by the clients for updating their applications."
    }    
}

#template
dgupdaterconf_json = {
    "obj_type": "config",
    "_id": "",
    "app_name": "",
    "version": "",
    "mongodb_connection_string_client": "",
    "files_in_latest_version": []
}


@command()
@option("--name", "-n", required = True, prompt = parameters["name"]["prompt"], help = parameters["name"]["help"])  
@option("--mongodbstrd", "-md", callback = check_mongo_string, required = True, prompt = parameters["mongodb_connection_string_write"]["prompt"], help = parameters["mongodb_connection_string_write"]["help"])
@option("--mongodbstrc", "-mc", callback = check_mongo_string, required = True, prompt = parameters["mongodb_connection_string_read"]["prompt"], help = parameters["mongodb_connection_string_read"]["help"])
def init(name: str, mongodbstrd: str, mongodbstrc: str) -> None:

    echo("\nInitializing this directory for auto updation...")

    app_exists, over_write = check_app_exists(name, mongodbstrd)

    if app_exists and not over_write:
        echo("Initialization Aborted.")
        return
    elif app_exists and over_write:
        echo("Overwriting the existing application.")    
    
    dgupdaterconf_json["_id"] = name + '_config'
    dgupdaterconf_json["app_name"] = name
    dgupdaterconf_json["version"] = "Version will be updated after publishing the changes."
    dgupdaterconf_json["mongodb_connection_string_client"] = mongodbstrc
    dgupdaterconf_json["files_in_latest_version"] = 'Files will be listed after publishing the changes.'

    create_entry_in_mongodb(dgupdaterconf_json, mongodbstrd, over_write)

    create_configuration_files(dgupdaterconf_json, name, mongodbstrd)

    echo("Initialization Successful.")
    