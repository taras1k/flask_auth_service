from flask import Blueprint, request, jsonify
from flask.ext.login import login_user, login_required
from flask.ext.login import logout_user
from extensions import login_manager, db

from app_exceptions import UserInputError
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
        raise UserInputError('login error')
    return jsonify({'status': True})


@user_app.route('/register', methods=['POST'])
def reqister():
    email = request.form.get('email')
    password = request.form.get('password')
    #! TODO add password required and email validation
    password_confirm = request.form.get('password_confirm')
    if password != password_confirm:
        raise UserInputError('password_missmatch', payload={'password': 'mismatch'})
    user = User.query.filter_by(email=email).first()
    if user:
        raise UserInputError('email_exists ', payload={'email': 'email_exists'})
    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': True})
