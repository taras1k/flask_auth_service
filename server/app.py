import os
from flask import Flask, jsonify
from extensions import db, oauth, login_manager
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from apps.index_app.views import index_app
from apps.user.views import user_app
from apps.oauth.views import oauth_app

from app_exceptions import UserInputError

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_CONFIG_CLASS'))

@app.errorhandler(UserInputError)
def handle_user_input_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


db.init_app(app)
db.app = app
oauth.init_app(app)
login_manager.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(oauth_app, url_prefix='/oaut')


if __name__ == '__main__':
    manager.run()
