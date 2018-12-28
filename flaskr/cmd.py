import click
from flask.cli import with_appcontext


@click.command('init-cmd')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    click.echo('Initialized the command.')


def init_cmd(app):
    app.cli.add_command(init_db_command)
