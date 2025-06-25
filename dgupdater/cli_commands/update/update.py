from click import command, option, echo
from json import load, loads
from tqdm import tqdm
from pymongo import MongoClient
from os.path import join, normpath, dirname
from os import makedirs
from sys import exit
from base64 import b64decode

from .func.delete_deprecated_files import delete_deprecated_files
from .func.acknowledge_update_to_client import acknowledge_update_to_client

@command()
@option("--root", '-r', required=True, prompt = 'rootdir', help = "Root directory of the application")
def update(root: str) -> None:

    echo("\nUpdating...\n")

    try:
        with open(join(root, 'dgupdaterconf.json'), 'r') as f:
            conf = load(f)
    except FileNotFoundError as e:
        echo("dgupdaterconf.json not found. Cant update the application.")
        return
    
    mongodbstrc = conf['mongodb_connection_string_client']
    app_name = conf['app_name'] 
    
    new_files_json_string = ''

    with MongoClient(mongodbstrc) as client:
        db = client['DGUPDATER']
        collection = db[app_name]
        new_update_conf = collection.find_one({'_id': f'{app_name}_config'})

        with tqdm(total = new_update_conf['no_of_chunks'], desc = "Downloading chunks", ncols = 110, unit='chunks') as pbar: #progress bar
            for i in range(new_update_conf['no_of_chunks']):
                chunk_part = i + 1
                chunk_name = f'{app_name}_part{chunk_part}'

                chunk = collection.find_one({'_id': chunk_name})
                new_files_json_string += chunk['chunk_data']
                pbar.update(1)
        echo() # empty line

    new_files_json = loads(new_files_json_string)
    
    with tqdm(total = len(new_files_json), desc = "Updating files", ncols = 110, unit='files') as pbar: #progress bar

        for file in new_files_json:                
            file_data = new_files_json[file]
            file = file.strip('\\')

            dirs = normpath(join(root, dirname(file)))
            makedirs(dirs, exist_ok = True)
            
            if isinstance(file_data, dict):

                if file_data['type'] == 'base64':
                    file_data = b64decode(file_data['content'])
                    with open(normpath(join(root, file)), 'wb') as f:
                        f.write(file_data)

            else: # file_data is a string
                with open(normpath(join(root, file)), 'w') as f:
                    f.write(file_data)

            pbar.update(1) 

    try:
        delete_deprecated_files(root, conf['files_in_latest_version'], new_update_conf['files_in_latest_version'])
    except KeyError as _:
        pass

    acknowledge_update_to_client()

    exit()

