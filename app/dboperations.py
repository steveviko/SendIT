import os
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app
from app.models import Database

db = Database()
cursor =db.cur
dictcur=db.dict_cursor



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

    def check_username(self, account_username):
        command = "SELECT user_id,username,hash_password,role from users WHERE username= '{}'".format(account_username)
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    # def hash_password(self,hashed_password, login_password):
    #     return check_password_hash(hashed_password["hash_password"], login_password["hash_password"])

    # def fetch_user(self, username):
    #     query = self.query_user(username)
    #     return query.fetchone()

    def query_user(self, account):
        command = "SELECT * FROM users WHERE username= '{}'".format(account["username"])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

        