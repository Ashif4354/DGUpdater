from os import makedirs, getcwd
from os.path import join
from json import load, dump, dumps
from shutil import rmtree
from tqdm import tqdm
from click import echo
from base64 import b64encode

from .find_files import find_files
from .create_chunks import create_chunks

def commit_changes() -> None:

    try:
        rmtree('dgupdater_release/chunks') # Removing the chunks directory and its contents if it exists
    except FileNotFoundError as _:
        pass

    makedirs('dgupdater_release/chunks', exist_ok = True)

    release_json = {}

    release_files = find_files()

    with open('dgupdaterconf.json', 'r') as f:
        dgupdaterconf_json = load(f)

        dgupdaterconf_json['no_of_files'] = len(release_files)
        dgupdaterconf_json['files_in_latest_version'] = release_files

        with open('dgupdaterconf.json', 'w') as f:          
            dump(dgupdaterconf_json, f, indent = 4)
    
    with tqdm(total = len(release_files), desc = "Loading files", ncols = 110, unit='files') as pbar: # progress bar
        for file in release_files:

            file_path = f'{getcwd()}{file}'

            try:
                with open(file_path, 'r') as f:
                    release_json[file] = f.read()

            except UnicodeDecodeError as _:
                with open(file_path, 'rb') as f:  
                    release_json[file] = {
                        'type': 'base64',
                        'content': b64encode(f.read()).decode('utf-8')
                    }
            finally:
                pbar.update(1)
    echo() # empty line

    release_json_str = dumps(release_json)

    with open('dgupdaterconf.json', 'r') as f:
        dgupdaterconf_json = load(f)

    no_of_chunks = create_chunks(release_json_str, dgupdaterconf_json['app_name']) #creating chunks as well as getting the number of chunks
    
    dgupdaterconf_json['update_ready'] = False
    dgupdaterconf_json['no_of_chunks'] = no_of_chunks

    with open(join(getcwd(), 'dgupdater_release', 'dgupdaterconf.json'), 'w') as f:
        dump(dgupdaterconf_json, f, indent = 4)
