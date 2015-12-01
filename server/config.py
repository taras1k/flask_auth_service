import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    LOG_FILE = '%s/app.log' % BASEDIR
    WSGI_SCRIPT = '%s/app.sock' % BASEDIR
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
