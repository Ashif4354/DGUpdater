from json import dump, load
from json.decoder import JSONDecodeError
from os import makedirs
from os.path import join, exists
from platformdirs import user_data_dir
from importlib.resources import path as package_path
from shutil import copyfile

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
        f.write('.dgupdaterignore\ndgupdaterupdate.exe')

    with package_path("dgupdater") as bin_path:
        copyfile(join(bin_path, "bin", "dgupdaterupdate.exe"), "dgupdaterupdate.exe")

    
