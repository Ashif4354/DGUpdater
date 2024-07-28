from os import makedirs, getcwd
from json import load, dump, dumps
from shutil import rmtree

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
    # print(release_files)

    for file in release_files:

        file_path = f'{getcwd()}{file}'
        try:
            with open(file_path, 'r') as f:
                # print(file_path)
                release_json[file] = f.read()
        except UnicodeDecodeError as _:
            with open(file_path, 'rb') as f:  
                content = str(f.read())
                release_json[file] = content
                # print(content[:10])

    release_json_str = dumps(release_json)

    with open('dgupdaterconf.json') as f:
        dgupdaterconf_json = load(f)

    no_of_chunks = create_chunks(release_json_str, dgupdaterconf_json['app_name']) #creating chunks as well as getting the number of chunks
    
    dgupdaterconf_json['no_of_files'] = len(release_files)
    dgupdaterconf_json['update_ready'] = False
    dgupdaterconf_json['no_of_chunks'] = no_of_chunks
    dgupdaterconf_json['files_in_latest_version'] = release_files

    with open(f'{getcwd()}/dgupdater_release/dgupdaterconf.json', 'w') as f:
        dump(dgupdaterconf_json, f, indent = 4)


if __name__ == "__main__":
    commit_changes()