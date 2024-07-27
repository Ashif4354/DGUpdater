from os.path import exists
from click import echo
from json import load
from ...init.init import dgupdaterconf_json


def check_configuration_files_exists() -> bool:
    if not exists('dgupdaterconf.json'):
        echo("\ndgupdaterconf.json not found. Run 'dgupdater init' first. \nAlso check if you are in the correct directory.")
        return False
    
    with open('dgupdaterconf.json') as f:
        dgupdaterconf_json_ = load(f)

    if (dgupdaterconf_json_.keys() != dgupdaterconf_json.keys()):
        echo("dgupdaterconf.json is not valid. \nTry 'dgupdater init' again.")
        return False
    
    return True


