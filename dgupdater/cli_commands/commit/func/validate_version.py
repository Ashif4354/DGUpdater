from click import BadParameter
from json import load

def validate_version(ctx, param, value):
    current_version = get_version()
    if value == current_version:
        raise BadParameter(f"Version {value} is already the current version.")    

    return value


def get_version():    
    with open('dgupdaterconf.json', 'r') as f:
        return load(f)['version']