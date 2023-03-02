from .storage import JSONClient
from .errors import InvalidPasswordException, UserAlreadyExists, InvalidUser
import os

class User:
    def __init__(self, username: str, password: str, user_dir: str = None):
        self.username = username
        self.password = password
        if user_dir != None:
            self.user_dir = f"{user_dir}/{username}.json"
        else:
            self.user_dir = f"{username}.json"
        self.client = JSONClient(password)
        self.obj = {}
    
    @classmethod
    def new_user(cls, username: str, password: str, user_dir: str = None):
        if f"{username}.json" not in os.listdir(user_dir):
            user = cls(username, password, user_dir)
            user_obj = {
                "username": user.username,
                "data": user.obj
            }
            with open(user.user_dir, "w") as user_file:
                user.client.dump(user_obj, user_file)
            return user
        else:
            raise UserAlreadyExists(f"A user named {username} already exists in this directory.")
    
    @classmethod   
    def login(cls, username: str, password: str, user_dir: str = None):
        if f"{username}.json" in os.listdir(user_dir):
            user = cls(username, password, user_dir)
            with open(user.user_dir, "r") as user_file:
                user_obj = user.client.load(user_file)
                if "username" not in user_obj:
                    raise InvalidPasswordException("Incorrect password provided.")
                elif user_obj["username"] == username:
                    user.obj = user_obj["data"]
                    return user
                else:
                    raise InvalidPasswordException("Incorrect password provided.")
        else:
            raise InvalidUser(f"A user named {username} does not exist in this directory.")
        
    def update(self):
        user_obj = {
            "username": self.username,
            "data": self.obj
        }
        with open(self.user_dir, "w") as user_file:
            self.client.dump(user_obj, user_file)
    
    