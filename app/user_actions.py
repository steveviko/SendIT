# from app.views import app
from .user import User
from .dboperations import DbOperations
from .parcels import Parcels
from werkzeug.security import generate_password_hash, check_password_hash

user_Obj = User()
parcelObject = Parcels()

class UserActions:
    def __init__(self):
        self.db_Object = DbOperations()
        

    