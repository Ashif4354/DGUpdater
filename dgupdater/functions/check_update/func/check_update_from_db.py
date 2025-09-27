from contextlib import suppress
from pymongo import MongoClient
from os.path import join
from json import load

def check_update_from_db(root_dir: str) -> bool:
    conf: dict = get_conf(root_dir)

    mongodbstrc: str = conf['mongodb_connection_string_client']
    app_name: str = conf['app_name']
    current_version: str = conf['version']


    with MongoClient(mongodbstrc) as client:
        db = client['DGUPDATER']
        collection = db[app_name]

        data = collection.find_one({'obj_type': 'config'})

        with suppress(KeyError):
            
            if (data is not None and 
                data['version'] != current_version and 
                data['update_ready']):
                return True
            
        return False



def get_conf(root: str) -> dict:
    conf_path = join(root, 'dgupdaterconf.json')

    with open(conf_path, 'r') as f:
        return load(f)
    

if __name__ == '__main__':
    from os import getcwd
    check_update_from_db(getcwd())