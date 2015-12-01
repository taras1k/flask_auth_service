from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    confirm_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                        server_default='0')


