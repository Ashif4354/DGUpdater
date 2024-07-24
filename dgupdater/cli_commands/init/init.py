from click import command, echo, option
from json import dump
from .func.check_mongo_string import check_mongo_string
from .func.check_app_exists import check_app_exists
from .func.find_files.find_files import find_files

arguments = {
    'name': {
        'prompt': "Name of the Application: ",
        'help': "The name of the Application. It should be unique for every app "
    },
    'version': {
        'prompt': "Version of the Application: ",
        'help': "The version of the Application."
    },
    'mongodb_connection_string_write': {
        'prompt': "MongoDB Connection String with write access: ",
        'help': "The MongoDB Connection String for a cloud cluster, to be used by the developer for releasing update."
    },
    'mongodb_connection_string_read': {
        'prompt': "MongoDB Connection String with read access: ",
        'help': "The MongoDB Connection String for a cloud cluster, to be used by the lients for updating their applications."
    }    
}


dgupdaterconf_json = {
    "app_name": "",
    "version": "",
    "mongodb_connection_string_developer": "",
    "mongodb_connection_string_client": "",
    "files": [],
    "files_content": {}
}

@command()
@option("--name", "-n", required = True, prompt = arguments["name"]["prompt"], help = arguments["name"]["help"])
@option("--version", "-v", required = True, prompt = arguments["version"]["prompt"], help = arguments["version"]["help"])    
@option("--mongodbstrd", "-md", callback = check_mongo_string, required = True, prompt = arguments["mongodb_connection_string_write"]["prompt"], help = arguments["mongodb_connection_string_write"]["help"])
@option("--mongodbstrc", "-mc", callback = check_mongo_string, required = True, prompt = arguments["mongodb_connection_string_read"]["prompt"], help = arguments["mongodb_connection_string_read"]["help"])
def init(name, version, mongodbstrd, mongodbstrc):
    # print(name, version, mongodbstr)
    echo("\n\nInitializing this directory for autoupdation...")
    if check_app_exists(name, mongodbstrd):
        echo("Application with the same name already exists. Please choose a different name.")
        return

    dgupdaterconf_json["app_name"] = name
    dgupdaterconf_json["version"] = version
    # dgupdaterconf_json["mongodb_connection_string"] = mongodbstr
    dgupdaterconf_json["mongodb_connection_string_developer"] = mongodbstrd
    dgupdaterconf_json["mongodb_connection_string_client"] = mongodbstrc
    dgupdaterconf_json["files"] = find_files()




    with open("dgupdaterconf.json", "w") as f:
        dump(dgupdaterconf_json, f, indent = 4)
        
if __name__ == "__main__":
    init()