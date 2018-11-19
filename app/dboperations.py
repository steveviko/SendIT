import os
from .models import Database
from app import create_app


class DbOperations:
    def __init__(self):
        self.connect=Database()
        

    def register_user(self, username,email, hash_password):
        """ insert a new user into the users table """

        sql = """INSERT INTO users(username,email, hash_password)
                VALUES(%s,%s, %s);"""
        return  self.connect.conn(sql, username, email, hash_password)