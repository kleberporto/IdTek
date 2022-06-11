import click
from flask.cli import FlaskGroup

from idtek.scrapper.scrapper import retrieve_contributors_data

from . import create_app_wsgi


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script for the idtek application."""
    
    retrieve_contributors_data()


if __name__ == "__main__":  # pragma: no cover
    main()
