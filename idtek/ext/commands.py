import click

from idtek.ext.auth import create_user
from idtek.ext.database import db
from idtek.models import Product
from idtek.scrapper.scrapper import retrieve_contributors_data


def create_db():
    """Creates database"""
    #  db.create_all()
    pass


def drop_db():
    """Cleans database"""
    #  db.drop_all()
    pass


def populate_db():
    """Populate db with scrapped data"""
    retrieve_contributors_data()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
