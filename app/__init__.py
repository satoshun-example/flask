import os

from flask import Flask
from flask.ext.cache import Cache
from flask.ext.redis import FlaskRedis

from config import config, basedir

cache = Cache()
redis = FlaskRedis()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    cfg_path = os.path.join(basedir, 'application.cfg')
    if os.path.isfile(cfg_path) and config_name != 'testing':
        app.config.from_pyfile(cfg_path)
    config[config_name].init_app(app)

    cache.init_app(app)
    redis.init_app(app)

    # WWW
    from .www import www as www_blueprint
    app.register_blueprint(www_blueprint)

    return app
