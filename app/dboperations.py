import os
from .models import Database
from app import create_app


class DbOperations:
    def __init__(self):
        self.connect=Database()
    
    def register_user(self,email, hash_password):
        """ insert a new user into the users table """

        sql = """INSERT INTO users(email,  hash_password)
                VALUES(%s,%s, %s);"""
        return self.connect.connect(sql, email,hash_password)