from decouple import config

from utils.constants import DB_URI


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '.herokuapp.com']


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '.herokuapp.com']


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
