class UserNameTakenException(Exception):
    def __init__(self, message='Username already taken'):
        self.message = message
