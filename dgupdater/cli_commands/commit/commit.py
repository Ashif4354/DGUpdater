from click import command, option, prompt, echo

from .func.check_configuration_files_exists import check_configuration_files_exists
from .func.update_version import update_version
from .func.commit_changes import commit_changes
from ..publish.func.publish_changes import publish_changes
from .func.validate_version import validate_version

@command()
@option(
    '--version', '-v', 
    required = True, 
    prompt = 'New version number', 
    help='New version number of the application',
    callback=validate_version
)
def commit(version: str) -> None:   

    check_configuration_files_exists()
    
    if prompt("Are you sure you want to commit the changes? (y/n)").lower() in ["y", "yes"]:
        echo("Committing...")

        update_version(version)
        commit_changes()
        
        echo("Committed successfully.\nChanges are ready to be published.\n")    

        if prompt("Do you want to publish the changes now? (y/n)").lower() in ["y", "yes"]:
            publish_changes()
        else:
            echo("You can publish the changes later by running 'dgupdater publish' command.")
        return
    
    echo("Commit aborted.")

