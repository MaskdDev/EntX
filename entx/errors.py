class InvalidPasswordException(Exception):
    """
    Exception raised if password provided is incorrect.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        
class UserAlreadyExists(Exception):
    """
    Exception raised if user already exists in directory.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        
class InvalidUser(Exception):
    """
    Exception raised if user does not exist in a directory.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)