from os import walk, getcwd
from os.path import normpath, getsize




def find_files():
    files_ = []
    retrieved_files = []

    for root, dirs, files in walk(getcwd()):

        # if 'venv' in root or '.git' in root or '.vscode' in root or 'build' in root or 'dist' in root or 'dgupdater.egg-info' in root or 'tests' in root:
        #     continue
        
        files_.append((normpath(root), dirs, files))

    for files in files_:
        for file in files[2]:
            file = files[0].split(getcwd())[1] + '\\' + file
            retrieved_files.append(file)

    
    

    return retrieved_files
    

if __name__ == "__main__":
    # for file in find_files():
    #     print(file)

    # print(normpath('D:\\PROGRAMMING\\PROJECTS\\dgupdater'))

    print(getsize('D:\PROGRAMMING\PROJECTS\dgupdater\dgupdaterconf.json'))
    print(getsize('ashif'))

        
        