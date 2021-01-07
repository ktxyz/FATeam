from flask import Flask
from FAT.config import FATConfig

from flask_sessions import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(FATConfig)

    # Sessions for AD auth
    Session(app)

    with app.app_context():
        import FAT.routes

    return app