from os import walk, getcwd
from os.path import normpath


def find_files() -> list:
    
    files_ = []
    retrieved_files = []

    ignored_list = get_ignore_list()
    ignored_list.append('dgupdater_release')

    for root, dirs, files in walk(getcwd()):

        # start: Ignore files logic
        ignore = False
        for ignored in ignored_list:
            if ignored in root:
                ignore = True
        if ignore:
            ignore = False
            continue
        # end: Ignore files logic

        dirs = [dir for dir in dirs if dir not in ignored_list]
        files = [file for file in files if file not in ignored_list]
     
        files_.append((normpath(root), dirs, files))

    for files in files_:
        for file in files[2]:
            file = files[0].split(getcwd())[1] + '\\' + file
            retrieved_files.append(file)   
    

    return retrieved_files


def get_ignore_list() -> list:
    try:
        with open('.dgupdaterignore', 'r') as file:
            return [line.split('\n')[0] for line in file.readlines()]
    except FileNotFoundError as _:
        return []
