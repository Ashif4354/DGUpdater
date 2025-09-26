from os import _exit
from os.path import join
from platform import system
from tempfile import gettempdir
from threading import Thread
from shutil import copyfile

from .func.find_root_directory import find_root_directory
from .func.check_update_from_db import check_update_from_db
from .func.ask_to_be_updated import ask_to_be_updated
from .func.open_updater import open_updater

def check_update(parallel: bool = False) -> None:
    def _check_update() -> None:
        try:
            root_dir = find_root_directory()
        except FileNotFoundError as _:
            print("'dgupdaterconf.json' file not found, cant check for new updates. But you can still use the application.")
            return
        
        update_available= check_update_from_db(root_dir) 

        if not update_available:
            return
        
        this_os = system()
        
        if not ask_to_be_updated(this_os):
            return
        
        # Update the application

        temp_dir = gettempdir()
        temp_file = join(temp_dir, 'dgupdaterupdate.exe')
        copyfile(join(root_dir, 'dgupdaterupdate.exe'), temp_file)

        open_updater(temp_file, root_dir, this_os)

        _exit(0)
    
    if parallel:
        Thread(target=_check_update, daemon=True).start()
    else:
        _check_update()
    
if __name__ == '__main__':
    check_update()





