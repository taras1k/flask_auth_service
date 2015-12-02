from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.oauthlib.provider import OAuth2Provider

db = SQLAlchemy()
oauth = OAuth2Provider()

