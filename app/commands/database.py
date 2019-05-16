import click

from ..models import Base, engine
from ..models.user import User  # noqa: import


@click.command("initdb", short_help="Init App database.")
def create_db():
    Base.metadata.create_all(engine)
