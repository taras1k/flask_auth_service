from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    confirm_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                        server_default='0')

    def check_password(self, raw_password):
        pass

    def set_password(self, raw_password):
        pass

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
