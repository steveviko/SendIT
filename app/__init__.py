from flask import Flask



def create_app():    
    app = Flask(__name__, instance_relative_config=True)
         
    return app



from app.views import app
from app.database.models import Database
db=Database()
db.create_user_table()
db.create_parcels_table()