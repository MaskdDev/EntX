import json
from .utils import apply_map
from .__init__ import Client

class JSONClient(Client):
    def __init__(self, password: str):
        super().__init__(password)
        
    def dumps(self, obj: dict):
        if isinstance(obj, dict):
            encrypted_obj = apply_map(dict(obj), self.encrypt)
            return json.dumps(obj = encrypted_obj)
        else:
            raise TypeError("obj must be an instance of dict.")
        
    def dump(self, obj: dict, fp):
        if isinstance(obj, dict):
            encrypted_obj = apply_map(dict(obj), self.encrypt)
            return json.dump(obj = encrypted_obj, fp = fp)
        else:
            raise TypeError("obj must be an instance of dict.")
        
    def loads(self, s: str | bytes | bytearray):
        if isinstance(s, str):
            obj = json.loads(s)
            decrypted_obj = apply_map(dict(obj), self.decrypt)
            return decrypted_obj
        else:
            raise TypeError("s must be an instance of str.")
        
    def load(self, fp):
        obj = json.load(fp)
        decrypted_obj = apply_map(dict(obj), self.decrypt)
        return decrypted_obj