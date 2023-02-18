class InvalidPasswordException(Exception):
    """
    Exception raised if password provided is incorrect.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)