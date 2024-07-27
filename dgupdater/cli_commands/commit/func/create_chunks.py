from json import load, dump
from math import ceil


def create_chunks(release_json_str: str, app_name: str) -> int:
    
    max_chunk_size = 1000000 # 10 Lakh (or) 1 Million

    release_json_size = len(release_json_str)

    no_of_chunks = ceil(release_json_size / max_chunk_size)
    
    start = 0
    for i in range(no_of_chunks):
        chunk_part = i + 1
        chunk_name = f'{app_name}_part{chunk_part}'

        chunk = release_json_str[start:start + max_chunk_size]        
        chunk = {
            '_id': chunk_name,
            'chunk_data': chunk
        }

        with open(f'release/chunks/{chunk_name}.json', 'w') as f:
            dump(chunk, f, indent = 4)

        start += max_chunk_size

    return no_of_chunks


