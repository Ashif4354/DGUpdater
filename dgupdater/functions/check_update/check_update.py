from os import _exit
from platform import system
from threading import Thread

from .func.find_root_directory import find_root_directory
from .func.check_update_from_db import check_update_from_db
from .func.ask_to_be_updated import ask_to_be_updated
from .func.open_updater import open_updater
from .func.get_temp_file import get_temp_file

def check_update(parallel: bool = False) -> None:
    def _check_update() -> None:
        try:
            root_dir: str = find_root_directory()
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
        temp_file = get_temp_file(root_dir, this_os)

        open_updater(temp_file, root_dir, this_os)

        _exit(0)
    
    if parallel:
        Thread(target=_check_update, daemon=True).start()
    else:
        _check_update()
    
if __name__ == '__main__':
    check_update()





