from json import load
from os import getcwd
from os.path import join
from pymongo import MongoClient
from click import UsageError, echo
from tqdm import tqdm
from rich import print as richprint

def publish_changes()-> None:
    echo("Publishing changes...\n")

    dgupdaterconf_json = get_dgupdaterconf_json()
    
    app_name = dgupdaterconf_json['app_name']
    to_be_pushed = []
    
    with tqdm(total = dgupdaterconf_json['no_of_chunks'], desc = "Loading chunks", ncols=110, unit='chunks') as pbar: # progress bar
        for i in range(1, dgupdaterconf_json['no_of_chunks'] + 1):
            try:
                with open(join(getcwd(), 'dgupdater_release', 'chunks', f'{app_name}_part{i}.json'), "r") as f:
                    to_be_pushed.append(load(f))
                    pbar.update(1)
            except FileNotFoundError as _:
                raise UsageError(f"File {app_name}_part{i}.json not found. Commit the changes again.")
    
    mongodb_connection_string_write = get_mongodb_connection_string_write(app_name)

    mongodb_push(mongodb_connection_string_write, dgupdaterconf_json, app_name, to_be_pushed)

    echo("Changes published successfully and made ready for update.")
    richprint("\nKeep Coding!:computer: :v: ")
    richprint(':clap: :clap: :clap: :clap: :clap: :clap:')


def get_dgupdaterconf_json()-> dict:    
    try:
        with open(join(getcwd(), 'dgupdater_release', 'dgupdaterconf.json'), "r") as f:
            return load(f)
    except FileNotFoundError as _:
        raise UsageError("'dgupdaterconf.json' file in dgupdater_release directory not found. Commit the changes again.")
    
    
def get_mongodb_connection_string_write(app_name: str)-> str:
    from platformdirs import user_data_dir

    try:
        with open(join(user_data_dir("dgupdater", "DarkGlance"), 'dgupdaterconf.json'), "r") as f:
            return load(f)['mongodbstrds'][app_name]
    except (FileNotFoundError, KeyError) as _:
        error_message = "An error occurred while getting the mongodb write string. Initialize the directory and commit the changes again."   
        raise UsageError(error_message)
    

def mongodb_push(connection_string: str, conf: dict, app_name: str, data: list)-> None:
    echo('\nUploading files to the database...\n')

    with MongoClient(connection_string) as client:
        db = client['DGUPDATER']
        collection = db[app_name]

        collection.update_one({'_id':f'{app_name}_config'}, {'$set': conf}, upsert = True)

        try:
            collection.delete_many({'obj_type': 'chunk'})
        except Exception as _:
            raise UsageError("An error occurred while deleting the previous version files. Try again.")

        try:
            with tqdm(total = len(data), desc = "Uploading chunks", ncols=110, unit='chunks') as pbar:
                for chunk in data:
                    collection.insert_one(chunk)
                    pbar.update(1)

        except Exception as _:
            raise UsageError("An error occurred while pushing the chunks. Try again.")
        
        echo('\nFiles uploaded successfully...')
        
        make_update_ready(collection, app_name)


def make_update_ready(collection: any, app_name: str)-> None:
    try:
        collection.update_one({'_id':f'{app_name}_config'}, {'$set': {'update_ready': True}})
    except Exception as _:
        raise UsageError("An error occurred while making the update ready. Try publishing again.")


if __name__ == '__main__':
    pass

    