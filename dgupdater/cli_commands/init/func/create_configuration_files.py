from json import dump, load
from json.decoder import JSONDecodeError
from os import makedirs
from os.path import join, exists
from platformdirs import user_data_dir
from importlib.resources import path as package_path
from shutil import copyfile
import platform

def create_configuration_files(data: dict, app_name: str, mongodbstrd: str) -> None:
    with open("dgupdaterconf.json", "w") as f:
        dump(data, f, indent = 4)

    dgupdater_dir = user_data_dir("dgupdater", "DarkGlance")
    makedirs(dgupdater_dir, exist_ok = True)

    dgupdaterconf_json = {
        'mongodbstrds': {}
    }

    file = join(dgupdater_dir, "dgupdaterconf.json")
    
    try:
        if exists(file):
            with open(file, 'r') as f:
                dgupdaterconf_json = load(f)
    except JSONDecodeError as _:
        pass

    dgupdaterconf_json['mongodbstrds'][app_name] = mongodbstrd    
    
    with open(file, "w") as f:
        dump(dgupdaterconf_json, f, indent = 4)

    with open('.dgupdaterignore', 'w') as f:
        if platform.system() == "Windows":
            f.write('.dgupdaterignore\nupdate.exe\ndgupdaterupdate.exe')
        else:
            f.write('.dgupdaterignore\nupdate.py')

    # Copy the appropriate updater file based on platform
    if platform.system() == "Windows":
        # For Windows, copy the exe if available
        try:
            with package_path("dgupdater") as bin_path:
                copyfile(join(bin_path, "bin", "dgupdaterupdate.exe"), "dgupdaterupdate.exe")
        except FileNotFoundError:
            # Fallback: copy the Python script
            try:
                # Try to find update.py in the package
                import pkg_resources
                update_script_path = pkg_resources.resource_filename('dgupdater', '../update.py')
                copyfile(update_script_path, "update.py")
            except:
                # Final fallback - create a minimal update.py
                with open("update.py", "w") as f:
                    f.write("from dgupdater.cli_commands.update.update import update\nupdate()")
    else:
        # For Unix-like systems, copy the Python script or create it
        try:
            # Try to find update.py in the package
            import pkg_resources
            update_script_path = pkg_resources.resource_filename('dgupdater', '../update.py')
            copyfile(update_script_path, "update.py")
        except:
            # Fallback - create a minimal update.py
            with open("update.py", "w") as f:
                f.write("from dgupdater.cli_commands.update.update import update\nupdate()")

    
