import importlib

import click
from flask.cli import FlaskGroup

import app.commands


def make_app(info):
    """
        Create APP
    """
    from app import create_app

    return create_app()


@click.group(cls=FlaskGroup, create_app=make_app)
def my_app():
    """ app CLI """


# commands auto-discovery
#
for m in app.commands.__all__:
    module = importlib.import_module("app.commands.%s" % m)
    for func_name in dir(module):
        func = module.__dict__.get(func_name)
        if type(func) == click.core.Command:
            my_app.add_command(func)


if __name__ == "__main__":
    my_app()
