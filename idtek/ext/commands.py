from idtek.scrapper.scrapper import retrieve_contributors_data


def download_data():
    """Populate db with scrapped data"""
    retrieve_contributors_data()


def init_app(app):
    # add multiple commands in a bulk
    for command in [download_data]:
        app.cli.add_command(app.cli.command()(command))
