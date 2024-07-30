from os import getcwd, listdir
from os.path import dirname, normpath
from sys import exit as sysexit

def find_root_directory() -> str:
    cwd = getcwd()
    while True:
        if 'dgupdaterconf.json' in listdir(cwd):
            return normpath(cwd)
        
        if cwd == dirname(cwd):
            # sysexit("ERROR: 'dgupdaterconf.json' file not found. Try reinstalling the application.")
            raise FileNotFoundError("'dgupdaterconf.json' file not found. Try reinstalling the application.")
        
        cwd = dirname(cwd) # Move up one directory.

if __name__ == '__main__':
    
    print(find_root_directory())
    # print(dirname('/home/user/documents'))