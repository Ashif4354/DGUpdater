from os import makedirs, getcwd
from json import load, dump, dumps
from .find_files import find_files

from .create_chunks import create_chunks

def commit_changes() -> None:

    makedirs('release/chunks', exist_ok = True)

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


    # with open('release/release.json', 'w') as f:
    #     dump(release_json, f, indent = 4)

    release_json_str = dumps(release_json)

    # with open('release/testrelease.json', 'w') as f:
    #     dump({'release': release_json_str}, f, indent = 4)
    
    # print(len(release_json_str))

    with open('dgupdaterconf.json') as f:
        dgupdaterconf_json = load(f)

    no_of_chunks = create_chunks(release_json_str, dgupdaterconf_json['app_name']) #creating chunks as well as getting the number of chunks
    
    dgupdaterconf_json['files_in_latest_version'] = release_files
    dgupdaterconf_json['no_of_chunks'] = no_of_chunks

    with open(f'{getcwd()}/release/dgupdaterconf.json', 'w') as f:
        dump(dgupdaterconf_json, f, indent = 4)


if __name__ == "__main__":
    commit_changes()