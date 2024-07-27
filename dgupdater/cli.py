from click import group

from .cli_commands.init.init import init
from .cli_commands.commit.commit import commit

@group()
def cli():
    pass

cli.add_command(init)
cli.add_command(commit)
# cli.add_command()
# cli.add_command()
# cli.add_command()



if __name__ == "__main__":
    cli()
