from . import utils

class Client:
    def __init__(self, password: str):
        self.password = password
        
    def encrypt(self, string: str):
        return utils.encryptkit(string, self.password)
    
    def decrypt(self, string: str):
        return utils.decryptkit(string, self.password)