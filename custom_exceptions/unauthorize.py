class UnauthorizedException(Exception):
    def __init__(self, message='Unauthorized'):
        self.message = message
