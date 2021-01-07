from flask import Flask
from FAT.config import FATConfig

from flask_sessions import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(FATConfig)

    # Sessions for AD auth
    Session(app)
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    with app.app_context():
        import FAT.auth
        import FAT.routes

    return app