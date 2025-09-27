from os import chmod
from os.path import join
from tempfile import gettempdir
from shutil import copyfile

def get_temp_file(root_dir: str, this_os: str) -> str:
    temp_dir: str = gettempdir()

    if this_os == 'Linux':
        temp_file = join(temp_dir, 'dgupdaterupdate_lin')
        copyfile(join(root_dir, 'dgupdaterupdate', 'dgupdaterupdate_lin'), temp_file)

    elif this_os == 'Darwin':
        temp_file = join(temp_dir, 'dgupdaterupdate_mac')
        copyfile(join(root_dir, 'dgupdaterupdate', 'dgupdaterupdate_mac'), temp_file)

    elif this_os == 'Windows':
        temp_file = join(temp_dir, 'dgupdaterupdate_win.exe')
        copyfile(join(root_dir, 'dgupdaterupdate', 'dgupdaterupdate_win.exe'), temp_file)

    else:
        raise OSError(f'Unsupported OS: {this_os}')
    
    chmod(temp_file, 0o755)

    return temp_file