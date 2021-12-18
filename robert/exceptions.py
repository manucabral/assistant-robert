class RobertException(Exception):
    def __init__(self, message: str = None):
        message = 'An fatal error has occurred' if message is None else message
        super().__init__(message)

class LanguageNotSupported(RobertException):
    def __init__(self):
        super().__init__('That language is not supported')

class UnknownSafeSearchType(RobertException):
    def __init__(self, type):
        super().__init__(f'Safe search {type} does not exist')