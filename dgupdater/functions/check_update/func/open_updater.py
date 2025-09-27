from subprocess import Popen

def open_updater(temp_file: str, root_dir: str, this_os: str) -> None:
    kwargs_for_popen: dict = {}

    if this_os in {'Darwin', 'Linux'}:
        kwargs_for_popen['start_new_session'] = True

    elif this_os == 'Windows':
        from subprocess import CREATE_NEW_CONSOLE
        kwargs_for_popen['creationflags'] = CREATE_NEW_CONSOLE

    else:
        raise OSError(f'Unsupported OS: {this_os}')
        
    Popen(
        [
            temp_file,
            '-r',
            root_dir,
        ],
        cwd=root_dir,
        **kwargs_for_popen
    )
