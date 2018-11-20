from flask import Flask
from config import DevelopmentConfig
from config import TestConfig


def create_app():    
    app = Flask(__name__, instance_relative_config=True) 
    app.config.from_object(DevelopmentConfig)  
    return app



from app.views import app
from app.models import Database
db=Database()
db.create_user_table()
db.create_parcels_table()