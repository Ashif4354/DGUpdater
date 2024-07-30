from os import remove
from os.path import join
from click import echo


def delete_deprecated_files(root: str, files_in_current_version: list[str], files_in_new_version: list[str]) -> None:
    """
    Deletes files of the current version that are not present in the new version.
    """  

    for file in files_in_current_version:
        if file not in files_in_new_version:
            remove(join(root, file.strip('\\')))
    echo("\nDeleted deprecated files")



if __name__ == '__main__':
    old = ['\\a', '\\b', '\\c', '\\b\\c\\d']
    new = ['\\a', '\\b', '\\c', '\\d']

    delete_deprecated_files('C:\\Users\\user\\Desktop\\test', old, new)