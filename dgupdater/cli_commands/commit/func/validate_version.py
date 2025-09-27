from click import BadParameter
from json import load

def validate_version(ctx, param, value):

    try:
        new_version: list[int] = [int(x) for x in value.split(".")]

        if len(new_version) != 3:
            raise ValueError("Semantic Version should only have 3 parts")
        
    except ValueError as e:
        raise BadParameter("Enter a Valid Semantic Version") from e
    
    current_version: list[int] = get_version()

    if new_version <= current_version:
        raise BadParameter(f"New version should be greater than current version. Current Version: {current_version[0]}.{current_version[1]}.{current_version[2]}")    

    return value


def get_version() -> list[int]:    
    with open('dgupdaterconf.json', 'r') as f:
        version: str = load(f)['version']

        if version == "Version will be updated after publishing the changes.":
            return [0, 0, 0]

        try:
            version = [int(x) for x in version.split(".")]
        except ValueError:
            raise ValueError("dgupdaterconf.json file seems to be corrupted. Try 'dgupdater init' again.")

        if len(version) != 3:
            raise ValueError("dgupdaterconf.json file seems to be corrupted. Try 'dgupdater init' again.")

        return version