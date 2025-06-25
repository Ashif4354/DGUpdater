from json import dump
from math import ceil
from tqdm import tqdm
from os.path import join
from os import getcwd


def create_chunks(release_json_str: str, app_name: str) -> int:
    
    MAX_CHUNK_SIZE = 1_000_000 # 10 Lakh (or) 1 Million

    release_json_size = len(release_json_str)

    no_of_chunks = ceil(release_json_size / MAX_CHUNK_SIZE)
    
    start = 0
    
    with tqdm(total = no_of_chunks, desc = "Creating Chunks", ncols = 110, unit='chunks') as pbar: # progres bar
        
        for i in range(no_of_chunks):
            chunk_part = i + 1
            chunk_name = f'{app_name}_part{chunk_part}'

            chunk = release_json_str[start:start + MAX_CHUNK_SIZE]        
            chunk = {
                'obj_type': 'chunk',
                '_id': chunk_name,
                'chunk_data': chunk
            }

            with open(join(getcwd(), 'dgupdater_release', 'chunks', f'{chunk_name}.json'), 'w') as f:
                dump(chunk, f, indent = 4)

            start += MAX_CHUNK_SIZE
            pbar.update(1)

    return no_of_chunks




