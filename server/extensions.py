from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.oauthlib.provider import OAuth2Provider
from flask.ext.login import LoginManager

db = SQLAlchemy()
oauth = OAuth2Provider()
login_manager = LoginManager()

