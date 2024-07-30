from os import system

from .func.find_root_directory import find_root_directory
from .func.check_update_from_db import check_update_from_db
from .func.ask_to_be_updated import ask_to_be_updated

def check_update() -> None:
    try:
        root_dir = find_root_directory()
    except FileNotFoundError as e:
        print("'dgupdaterconf.json' file not found, cant check for new updates. But you can still use the application.")
        return
    
    update_available= check_update_from_db(root_dir) 
    if not update_available:
        return
    
    if not ask_to_be_updated():
        return
    
    # Update the application

    # system('dgupdater update -r ' + root_dir + ' -n ' + str(data['no_of_chunks'])) # type: ignore
    system(f'dgupdater update -r "{root_dir}"') # type: ignore
    exit()
    
if __name__ == '__main__':
    check_update()





