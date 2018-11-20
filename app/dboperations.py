import os
from .models import Database
from app import create_app


class DbOperations:
    def __init__(self):
        self.connect=Database()
        