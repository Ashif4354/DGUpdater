from os import walk, getcwd
from os.path import normpath


def find_files() -> list:
    
    files_ = []
    retrieved_files = []

    ignored_list = get_ignore_list()

    for root, dirs, files in walk(getcwd()):

        # Ignore logic start
        ignore = False
        for ignored in ignored_list:
            if ignored in root:
                ignore = True
        if ignore:
            ignore = False
            continue
        # Ignore logic end

        dirs = [dir for dir in dirs if dir not in ignored_list]
        files = [file for file in files if file not in ignored_list]
     
        files_.append((normpath(root), dirs, files))

    for files in files_:
        for file in files[2]:
            file = files[0].split(getcwd())[1] + '\\' + file
            retrieved_files.append(file)   
    

    return retrieved_files


def get_ignore_list() -> list:
    with open('.dgupdaterignore', 'r') as file:
        return [line.split('\n')[0] for line in file.readlines()]

if __name__ == "__main__":
    print(get_ignore_list())
    find_files()
    


    # for file in find_files():
    #     print(file)

    # print(normpath('D:\\PROGRAMMING\\PROJECTS\\dgupdater'))

    # print(getsize('D:\PROGRAMMING\PROJECTS\dgupdater\dgupdaterconf.json'))
    # print(getsize('ashif'))


        
        