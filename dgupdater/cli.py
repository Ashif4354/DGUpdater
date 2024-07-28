from click import group

from .cli_commands.init.init import init
from .cli_commands.commit.commit import commit
from .cli_commands.publish.publish import publish

@group()
def cli():
    pass

cli.add_command(init)
cli.add_command(commit)
cli.add_command(publish)

if __name__ == "__main__":
    cli()
