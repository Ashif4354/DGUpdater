from os import getcwd
from os.path import join, exists
from json import load
from click import UsageError

from ...init.init import dgupdaterconf_json as template_dgupdaterconf_json

def check_release_files_exists() -> None:

    cwd = getcwd()

    if not exists(join(cwd, 'dgupdater_release')):
        raise UsageError('dgupdater_release directory not found. Commit the changes first.')
    
    if not exists(join(cwd, 'dgupdater_release', 'dgupdaterconf.json')):
        raise UsageError("'dgupdaterconf.json' file not found in the dgupdater_release directory. Commit the changes again.")
    
    if not exists(join(cwd, 'dgupdater_release', 'chunks')):
        raise UsageError('chunks directory not found in the dgupdater_release directory. Commit the changes again.')
    
    with open(join(cwd, 'dgupdater_release', 'dgupdaterconf.json')) as f:
        dgupdaterconf_json = load(f)

        
    if ('no_of_files' not in dgupdaterconf_json or 
        'update_ready' not in dgupdaterconf_json or
        'no_of_chunks' not in dgupdaterconf_json or
        check_keys(template_dgupdaterconf_json, dgupdaterconf_json) or
        not isinstance(dgupdaterconf_json['files_in_latest_version'], list)):  

        raise UsageError("'dgupdaterconf.json' file in the dgupdater_release directory seems to be corrupted. Commit the changes again.")
    
def check_keys(base_dict: dict, compare_dict: dict) -> bool:
    base_dict_keys, compare_dict_keys = set(base_dict.keys()), set(compare_dict.keys())

    for key in base_dict_keys:
        if key not in compare_dict_keys:
            return True
        
    return False  
