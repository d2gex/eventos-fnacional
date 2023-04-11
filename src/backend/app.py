from flask import Flask
from src.backend import config


def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from src.backend.api import api
    app.register_blueprint(api, url_prefix='/api')
    return app
