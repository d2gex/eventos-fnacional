from flask import Flask
from src import config


def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from src.backend.api import api

    app.register_blueprint(api)
    return app


if __name__ == '__main__':
    app = create_app(config.Config)
    app.run(host='0.0.0.0', debug=False)