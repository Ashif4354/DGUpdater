from os.path import exists
from click import echo, UsageError
from json import load

from ...init.init import dgupdaterconf_json as template_dgupdaterconf_json

def check_configuration_files_exists() -> None:
    if not exists('dgupdaterconf.json'):
        raise UsageError("'dgupdaterconf.json' file not found. Run 'dgupdater init' first. Also check if you are in the correct directory.")
    
    with open('dgupdaterconf.json') as f:
        dgupdaterconf_json = load(f)

    # if (dgupdaterconf_json.keys() != template_dgupdaterconf_json.keys()):
    #     raise UsageError("'dgupdaterconf.json' file seems to be corrupted. Try 'dgupdater init' again.")

    for key in template_dgupdaterconf_json.keys():
        if key not in dgupdaterconf_json.keys():
            raise UsageError(f"'dgupdaterconf.json' file seems to be corrupted. Try 'dgupdater init' again. Missing key: {key}")
    




