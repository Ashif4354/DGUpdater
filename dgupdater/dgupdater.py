import click

@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo("Initializing dgupdater...")

if __name__ == "__main__":
    cli()
