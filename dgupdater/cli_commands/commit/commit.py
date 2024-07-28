from click import command, option, prompt, echo

from .func.check_configuration_files_exists import check_configuration_files_exists
from .func.update_version import update_version
from .func.commit_changes import commit_changes

@command()
@option('--version', '-v', required = True, prompt = 'New version number', help='New version number of the application')
def commit(version: str) -> None:   

    check_configuration_files_exists()
    
    if prompt("Are you sure you want to commit the changes? (y/n): ").lower() in ["y", "yes"]:
        echo("Committing...")

        update_version(version)
        commit_changes()
        
        echo("Committed successfully.")    
        return
    
    echo("Commit aborted.")

