import json
from .utils import apply_map
from .__init__ import Client
from .errors import InvalidPasswordException

class JSONClient(Client):
    def __init__(self, password: str):
        super().__init__(password)
        
    def dumps(self, obj: dict, encrypt_output: bool = True):
        if isinstance(obj, dict):
            # Checks whether output string should be encrypted
            if encrypt_output:
                encrypted_obj = apply_map(dict(obj), self.encrypt)
                unencrypted_json = json.dumps(obj = encrypted_obj)
                return self.encrypt(unencrypted_json)
            else:
                encrypted_obj = apply_map(dict(obj), self.encrypt)
                return json.dumps(obj = encrypted_obj)
        else:
            raise TypeError("obj must be an instance of dict.")
        
    def dump(self, obj: dict, fp, encrypt_output: bool = True):
        if isinstance(obj, dict):
            # Checks whether output should be encrypted
            if encrypt_output:
                encrypted_json = self.dumps(obj)
                fp.write(encrypted_json)
            else:
                encrypted_obj = apply_map(dict(obj), self.encrypt)
                json.dump(obj = encrypted_obj, fp = fp)
        else:
            raise TypeError("obj must be an instance of dict.")
        
    def loads(self, s: str | bytes | bytearray, encrypted_input: bool = True):
        if isinstance(s, str):
            try:
                # Checks whether input has been encrypted
                if encrypted_input:
                    decrypted_string = self.decrypt(s)
                    obj = json.loads(decrypted_string)
                    decrypted_obj = apply_map(dict(obj), self.decrypt)
                    return decrypted_obj
                else:
                    obj = json.loads(s)
                    decrypted_obj = apply_map(dict(obj), self.decrypt)
                    return decrypted_obj
            except json.JSONDecodeError:
                raise InvalidPasswordException("Incorrect password provided.")
        else:
            raise TypeError("s must be an instance of str.")
        
    def load(self, fp, encrypted_input: bool = True):
        try:
            # Checks whether input has been encrypted
            if encrypted_input:
                encrypted_string = fp.read()
                return self.loads(encrypted_string)
            else:
                obj = json.load(fp)
                decrypted_obj = apply_map(dict(obj), self.decrypt)
                return decrypted_obj
        except json.JSONDecodeError:
            raise InvalidPasswordException("Incorrect password provided.")