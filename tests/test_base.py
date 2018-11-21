import os
import unittest
import json
from app import app
from config import TestConfig
from app.models import Database
from app import views
from app.dboperations import DbOperations
app.config.from_object(TestConfig)

database = Database()