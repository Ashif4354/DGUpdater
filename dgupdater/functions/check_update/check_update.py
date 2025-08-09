from subprocess import Popen
from sys import exit, executable
from os.path import join
from tempfile import gettempdir
from shutil import copyfile
import platform

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
    
    # Determine the updater command based on platform
    if platform.system() == "Windows":
        # On Windows, use the .exe file if it exists
        temp_dir = gettempdir()
        temp_file = join(temp_dir, 'dgupdaterupdate.exe')
        updater_file = join(root_dir, 'dgupdaterupdate.exe')
        
        # Check if the exe file exists, otherwise fallback to Python script
        try:
            copyfile(updater_file, temp_file)
            updater_cmd = [temp_file]
        except FileNotFoundError:
            # Fallback to Python script
            updater_cmd = [executable, join(root_dir, 'update.py')]
    else:
        # On Unix-like systems (Mac/Linux), use Python script directly
        updater_cmd = [executable, join(root_dir, 'update.py')]
    
    # Add arguments
    updater_cmd.extend(['-r', root_dir])
    
    # Platform-specific subprocess flags
    if platform.system() == "Windows":
        Popen(updater_cmd, cwd=root_dir, creationflags=0x00000010)  # CREATE_NEW_CONSOLE
    else:
        Popen(updater_cmd, cwd=root_dir, start_new_session=True)
    
    exit()
    
if __name__ == '__main__':
    check_update()





