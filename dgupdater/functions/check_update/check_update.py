from subprocess import Popen, CREATE_NEW_CONSOLE
# from sys import exit
from signal import SIGTERM
from os import getpid, kill
from os.path import join
from tempfile import gettempdir
from shutil import copyfile

from .func.find_root_directory import find_root_directory
from .func.check_update_from_db import check_update_from_db
from .func.ask_to_be_updated import ask_to_be_updated

def check_update() -> None:
    try:
        root_dir = find_root_directory()
    except FileNotFoundError as _:
        print("'dgupdaterconf.json' file not found, cant check for new updates. But you can still use the application.")
        return
    
    update_available= check_update_from_db(root_dir) 
    if not update_available:
        return
    
    if not ask_to_be_updated():
        return
    
    # Update the application

    temp_dir = gettempdir()
    temp_file = join(temp_dir, 'dgupdaterupdate.exe')
    copyfile(join(root_dir, 'dgupdaterupdate.exe'), temp_file)

    Popen(
        [
            temp_file,
            '-r',
            root_dir,
        ],
        cwd=root_dir,
        creationflags=CREATE_NEW_CONSOLE
    )
    # exit()

    kill(getpid(), SIGTERM)
    
if __name__ == '__main__':
    check_update()





