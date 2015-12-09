class UserInputError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super(UserInputError, self).__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict()
        rv['errors'] = dict(self.payload or ())
        rv['message'] = self.message
        return rv
