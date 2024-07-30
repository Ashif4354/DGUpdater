from click import group

from .cli_commands.init.init import init
from .cli_commands.commit.commit import commit
from .cli_commands.publish.publish import publish
from .cli_commands.update.update import update

@group()
def cli() -> None:
    pass

cli.add_command(init)
cli.add_command(commit)
cli.add_command(publish)
cli.add_command(update)

if __name__ == "__main__":
    cli()
