import os
from app.models import Database
db = Database()
cursor =db.cur
dictcur=db.dict_cursor
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app


class DbOperations:
    def __init__(self):
        self.connect=Database()
    
    def add_user(self,account):
        """ insert a new user into the users table """
        command = "INSERT INTO users(username, email,hash_password, role) VALUES(\
                '{}',  '{}', '{}', 'user')".format(account["username"],  account["email"]\
                , generate_password_hash(account["password"]))
        cursor.execute(command)
        return account