from os import makedirs
from os.path import join, exists
from json import dump, load
from json.decoder import JSONDecodeError
from contextlib import suppress
from importlib.resources import path as package_path
from shutil import copyfile

from platformdirs import user_data_dir

def create_configuration_files(data: dict, app_name: str, mongodbstrd: str) -> None:
    with open("dgupdaterconf.json", "w") as f:
        dump(data, f, indent = 4)

    dgupdater_dir: str = user_data_dir("dgupdater", "DarkGlance")
    makedirs(dgupdater_dir, exist_ok = True)

    dgupdaterconf_json: dict = {
        'mongodbstrds': {}
    }

    file: str = join(dgupdater_dir, "dgupdaterconf.json")

    with suppress(JSONDecodeError):
        if exists(file):
            with open(file, 'r') as f:
                dgupdaterconf_json = load(f)

    dgupdaterconf_json['mongodbstrds'][app_name] = mongodbstrd    

    with open(file, "w") as f:
        dump(dgupdaterconf_json, f, indent = 4)

    with open('.dgupdaterignore', 'w') as f:
        f.write('.dgupdaterignore\ndgupdaterupdate')

    makedirs("dgupdaterupdate", exist_ok = True)

    with package_path("dgupdater") as bin_path:
        copyfile(join(bin_path, "bin", "dgupdaterupdate_win.exe"), "dgupdaterupdate/dgupdaterupdate_win.exe")
        copyfile(join(bin_path, "bin", "dgupdaterupdate_lin"), "dgupdaterupdate/dgupdaterupdate_lin")
        copyfile(join(bin_path, "bin", "dgupdaterupdate_mac"), "dgupdaterupdate/dgupdaterupdate_mac")
    
 