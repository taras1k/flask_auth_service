import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    LOG_FILE = '%s/app.log' % BASEDIR
    WSGI_SCRIPT = '%s/app.sock' % BASEDIR
    OAUTH_GRANT_EXPIRE = 100
    SQLALCHEMY_DATABASE_URI = 'postgresql://docker:docker@localhost:5432/flask_auth_service'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
