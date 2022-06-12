from idtek.livefeed.livefeed import open_camera
from idtek.scrapper.scrapper import retrieve_contributors_data


def live_feed():
    """Open camera for inference"""
    open_camera()


def download_data():
    """Populate db with scrapped data"""
    retrieve_contributors_data()


def init_app(app):
    # add multiple commands in a bulk
    for command in [download_data, open_camera]:
        app.cli.add_command(app.cli.command()(command))
