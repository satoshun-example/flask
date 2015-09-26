import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hogehogehoge'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    CACHE_TYPE = 'memcached'
    CACHE_MEMCACHED_SERVERS = ('127.0.0.1:11211', )


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
