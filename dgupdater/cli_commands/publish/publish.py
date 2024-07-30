from click import command, echo, prompt

from .func.check_release_files_exists import check_release_files_exists
from .func.publish_changes import publish_changes


@command()
def publish() -> None:

    check_release_files_exists()

    if prompt("Are you sure you want to publish the changes? (y/n)").lower() in ["y", "yes"]:

        publish_changes()
        return
    
    echo("Aborted publishing changes.")


    



        
    