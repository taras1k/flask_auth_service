import os
from flask import Flask
from extensions import db
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from apps.index_app.views import index_app

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_CONFIG_CLASS'))

db.init_app(app)
db.app = app
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

app.register_blueprint(index_app, url_prefix='/')


if __name__ == '__main__':
    manager.run()
