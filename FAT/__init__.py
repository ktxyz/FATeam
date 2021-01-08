import logging

from flask import Flask
from FAT.config import FATConfig
from FAT.database import db, migrate

from flask_sessions import Session

from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler


def create_app():
    app = Flask(__name__)
    app.config.from_object(FATConfig)

    # App Insight logging
    FlaskMiddleware(
        app,
        exporter=AzureExporter(connection_string=f'InstrumentationKey={app.config["APP_INSIGHT_KEY"]}'),
        sampler=ProbabilitySampler(rate=1.0)
    )
    logger = logging.getLogger(__name__)
    handler = AzureLogHandler(connection_string=f'InstrumentationKey={app.config["APP_INSIGHT_KEY"]}')
    logger.addHandler(handler)

    # Sessions for AD auth
    Session(app)
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Database
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        import FAT.auth
        import FAT.routes

    return app