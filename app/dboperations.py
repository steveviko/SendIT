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
    
    