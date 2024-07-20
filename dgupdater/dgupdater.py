from click import group, command, echo

from .init.init import init

@group()
def cli():
    pass

cli.add_command(init)
# cli.add_command()
# cli.add_command()
# cli.add_command()
# cli.add_command()



if __name__ == "__main__":
    cli()
