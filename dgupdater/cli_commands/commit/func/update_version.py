from json import load, dump

def update_version(version: str) -> None:
    with open('dgupdaterconf.json') as f:
        dgupdaterconf_json = load(f)
    
    dgupdaterconf_json['version'] = version

    with open('dgupdaterconf.json', 'w') as f:
        dump(dgupdaterconf_json, f, indent = 4)
