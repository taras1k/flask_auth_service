from werkzeug.security import generate_password_hash, \
     check_password_hash, gen_salt
from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(150), nullable=False,
                                     server_default='')
    confirm_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                        server_default='0')

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)
        self.set_confirm_token()

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def set_reset_token(self):
        self.reset_password_token = '{0}${1}'.format(gen_salt(100), self.id)

    def set_confirm_token(self):
        self.confirm_token = '{0}'.format(gen_salt(100))

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
