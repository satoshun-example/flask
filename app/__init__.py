from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # WWW
    from .www import www as www_blueprint
    app.register_blueprint(www_blueprint)

    return app
