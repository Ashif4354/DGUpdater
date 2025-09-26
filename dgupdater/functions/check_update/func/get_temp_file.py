from os.path import join
from os import gettempdir
from shutil import copyfile

def get_temp_file(root_dir: str, this_os: str) -> str:
    temp_dir = gettempdir()


    if this_os in {'Linux', 'Darwin'}:
        temp_file = join(temp_dir, 'dgupdaterupdate')
        copyfile(join(root_dir, 'dgupdaterupdate'), temp_file)

    elif this_os == 'Windows':
        temp_file = join(temp_dir, 'dgupdaterupdate.exe')
        copyfile(join(root_dir, 'dgupdaterupdate.exe'), temp_file)

    return temp_file