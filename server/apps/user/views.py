from flask import Blueprint, request, abort, jsonify
from flask.ext.login import login_user, login_required
from flask.ext.login import logout_user
from extensions import login_manager
from .models import User


user_app = Blueprint('user_app', __name__)


@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()


@user_app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'status': True})


@user_app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '')
    password = request.form.get('pasword', '')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
    else:
        abort(400)
        return jsonify({'status': True})

